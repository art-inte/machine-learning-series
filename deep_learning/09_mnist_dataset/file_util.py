import hashlib
import gzip
import os
import urllib
import urllib.error
import urllib.request
import shutil
import tarfile
import zipfile

# Set machine learning base dir path given MACHINE_LEARNING_HOME env variable, if applicable.
# Otherwise either ~/.machine_learning or /tmp.
if 'MACHINE_LEARNING_HOME' in os.environ:
    _MACHINE_LEARNING_DIR = os.environ.get('MACHINE_LEARNING_HOME')
else:
    _machine_learning_base_dir = os.path.expanduser('~')
    if not os.access(_machine_learning_base_dir, os.W_OK):
        _machine_learning_base_dir = '/tmp'
    _MACHINE_LEARNING_DIR = os.path.join(_machine_learning_base_dir, '.machine_learning')

def machine_learning_home():
    # Private accessor for the machine learning home location.
    return _MACHINE_LEARNING_DIR

def path_to_string(path):
    """
    Convert `PathLike` objects to their string representation. If given a non-string typed path
    pobject, converts it to its string representation.

    :param path: `PathLike` object that represents a path.
    :return: A string representation of the path argument, if Python support exists.
    """
    if isinstance(path, os.PathLike):
        return os.fspath(path)
    return path

def resolve_hasher(algorithm, file_hash=None):
    """
    Returns hash algorithms as hashlib function.
    """
    if algorithm == 'sha256':
        return hashlib.sha256()

    if algorithm == 'auto' and file_hash is not None and len(file_hash) == 64:
        return hashlib.sha256()
    
    return hashlib.md5()

def hash_file(file_path, algorithm, chunk_size=65535):
    """
    Calculates a file sha56 or md5 hash.

    Example: hash_file('/path/to/file.zip')
    Output: 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'

    :param file_path: Path to the file being validated.
    :param algorithm: Hash algorithm, one of `auto`, `sha256`, or `md5`.
                      The default `auto` detects the hash algorithm in use.
    :param chunk_size: Bytes to read at a time, important for large files.
    :return: The file hash.
    """
    if isinstance(algorithm, str):
        hasher = resolve_hasher(algorithm)
    else:
        hasher = algorithm
    
    with open(file_path, 'rb') as file:
        for chunk in iter(lambda: file.read(chunk_size), b''):
            hasher.update(chunk)
    
    return hasher.hexdigest()

def validate_file(file_path, file_hash, algorithm='auto', chunk_size=65535):
    """
    Validates a file against a sha256 or md5 hash.

    :param file_path: Path to the file being validated.
    :param file_hash: The expected hash string of the file. The sha256 and md5 hash
                      algorithms are both supported.
    :param algorithm: Hash algorithm, one of `auto`, `sha256`, or `md5`.
                      The default `auto` detects the hash algorithm in use.
    :param chunk_size: Bytes to read at a time, important for large files.
    :return: Boolean, whether the file is valid.
    """
    hasher = resolve_hasher(algorithm, file_hash)

    if str(hash_file(file_path, hasher, chunk_size)) == str(file_hash):
        return True
    else:
        return False
    
def extract_archive(file_path, path='.', archive_format='auto'):
    """
    Extracts an archive if it matches a support format.

    :param file_path: Path to the archive file.
    :param path: Where to extract the archive file.
    :param archive_format: Archive format to try for extracting the file.
    """
    if archive_format is None:
        return False, ''
    if archive_format == 'auto':
        archive_format = ['tar', 'zip', 'gz']
    if isinstance(archive_format, str):
        archive_format = [archive_format]

    file_path = path_to_string(file_path)
    path = path_to_string(path)

    open_fn = None
    for archive_type in archive_format:
        if archive_type == 'tar':
            open_fn = tarfile.open
        if archive_type == 'zip':
            open_fn = zipfile.ZipFile
        if archive_type == 'gz':
            open_fn = gzip.open

    with open_fn(file_path) as archive:
        try:
            if zipfile.is_zipfile(file_path):
                # Zip archive.
                archive.extractall(path)
                return True, path
            elif tarfile.is_tarfile(file_path):
                # Tar archive.
                archive.extractall(path)
                return True, path
            else:
                # GZ archive.
                obj_file_path = os.path.join(path, os.path.basename(file_path).removesuffix('.gz'))
                with open(obj_file_path, 'wb') as file:
                    shutil.copyfileobj(archive, file)
                return True, obj_file_path
        except (tarfile.TarError, RuntimeError, KeyboardInterrupt):
            if os.path.exists(path):
                if os.path.isfile(path):
                    os.remove(path)
                else:
                    shutil.rmtree(path)
            raise

def get_file(file_name=None,
             origin_url=None,
             file_hash=None,
             cache_dir=None,
             cache_subdir='dataset',
             hash_algorithm='auto',
             extract=False,
             archive_format='auto',
             force_download=False):
    """
    Downloads a file from a URL if it not already in the cache.

    By default, the file at the url `origin` is downloaded to the cache_dir `~/.machine_learning`,
    placed in the cache_subdir `dataset`, and given the filename `file_name`. The final location
    of a file `example.txt` would therefore be `~/.machine_learning/dataset/example.txt`.

    Files in `.tar`, `.tar.gz`, `.tar.bz`, and `.zip` formats can also be extracted.

    Passing a hash will verify the file after download. The command line programs `shasum` and
    `sha256sum` can compute the hash.

    Example: path_to_downloaded_file = get_file(origin = '...', extract=True)

    Args:

    file_name: Name of the file. If an absolute path, e.g. `/path/to/file.txt` is specified,
               the file will be saved at that location. If `None`, the name of the file at
               `origin` will be used.
    origin_url: Original URL of the file.
    file_hash: The expected hash string of the file after download. The sha256 and md5 hash
               algorithms are both supported.
    cache_dir: Location to store cached files, when None it defaults `~/.machine_learning`.
    cache_subdir: Subdirectory under the cache dir where the file is saved. If an absolute
                  path, e.g. `/path/to/folder` is specified, the file will be saved at that
                  location.
    hash_algorithm: Select the hash algorithm to verify the file. options are `md5`,
                    `sha256`, and `auto`. The default `auto` detects the hash algorithm in use.
    extract: True tries extracting the file as an Archive, like tar or zip.
    archive_format: Archive format to try for extracting the file. Options are `auto`, `tar`,
                    `gz`, `zip`.
    force_download: if `True`, the file will always be re-downloaded regardless of the cache
                    state.

    Returns:

        Path to the downloaded file.
    """
    if origin_url is None:
        raise ValueError('Please specify the `origin_url` argument (URL of the file to download).')
    
    if cache_dir is None:
        cache_dir = machine_learning_home()

    datadir_base = os.path.expanduser(cache_dir)
    if not os.access(datadir_base, os.W_OK):
        datadir_base = machine_learning_home()

    datadir = os.path.join(datadir_base, cache_subdir)
    # Create dataset dir.
    os.makedirs(datadir, exist_ok=True)

    file_name = path_to_string(file_name)
    if not file_name:
        file_name = os.path.basename(origin_url)
        if not file_name:
            raise ValueError("Can't parse the file name from the origin provided."
                             "Please specify the `file_name` as the input param.")
    
    file_path = os.path.join(datadir, file_name)

    if force_download:
        download = True
    elif os.path.exists(file_path):
        # File found in cache.
        download = False
        # Verify integrity if a hash was provided.
        if file_hash is not None:
            if not validate_file(file_path, file_hash, algorithm=hash_algorithm):
                print('A local file was found, but it seems to be incomplete '
                      'or outdated, so we will re-download the data.')
                download = True
    else:
        download = True
    
    if download:
        try:
            urllib.request.urlretrieve(origin_url, file_path)
        except urllib.error.HTTPError as e:
            raise Exception(e.name)
        except urllib.error.URLError as e:
            return Exception(e.reason)
        except (Exception, KeyboardInterrupt):
            if os.path.exists(file_path):
                os.remove(file_path)
            raise

        # Validate download if succeeded and user provided an expected hash
        # security conscious users would get the hash of the file.
        if os.path.exists(file_path) and file_hash is not None:
            if not validate_file(file_path, file_hash, algorithm=hash_algorithm):
                raise ValueError('Incomplete or corrupted file detected.')

    dest_file_path = ''
    if extract:
        status, dest_file_path = extract_archive(file_path, datadir, archive_format)
        if not status:
            print('Could not extract archive.')

    # Return extracted file_path if we extracted an archive.
    return dest_file_path
