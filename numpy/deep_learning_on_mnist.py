import os
import requests

data_sources = {
    'training_images': 'train-images-idx3-ubyte.gz',    # 60,000 training images
    'test_images': 't10k-images-idx3-ubyte.gz',         # 10,000 test images
    'training_labels': 'train-labels-idx1-ubyte.gz',    # 60,000 training labels
    'test_labels': 't10k-labels-idx1-ubyte.gz',         # 10,000 test labels
}

# base_url = 'http://yann.lecun.com/exdb/mnist/'
base_url = "https://github.com/rossbar/numpy-tutorial-data-mirror/blob/main/"
data_dir = 'temp/mnist/'

if __name__ == '__main__':
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    for filename in data_sources.values():
        file_path = os.path.join(data_dir, filename)
        if not os.path.exists(file_path):
            print('Downloading file: ' + filename)
            resp = requests.get(base_url + filename, stream=True)
            resp.raise_for_status() # ensure download was successful
            with open(file_path, 'wb') as fp:
                for chunk in resp.iter_content(chunk_size=128):
                    fp.write(chunk)
