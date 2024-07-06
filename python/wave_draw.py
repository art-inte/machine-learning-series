import matplotlib.pyplot  as pyplot
import numpy
import os
import requests
import wave

wave_file_url = 'https://freewavesamples.com/files/Alesis-Fusion-Nylon-String-Guitar-C4.wav'

if __name__ == '__main__':
    filename = wave_file_url.split('/')[-1]
    response = requests.get(wave_file_url)
    if response.status_code == 200:
        with open(os.path.join('temp', filename), 'wb') as fp:
            fp.write(response.content)
    else:
        print('Failed to download file, status code:', response.status_code)

    # 1. Use python wave module to decode wave file.
    with wave.open(os.path.join('temp', filename)) as wave_file:
        metadata = wave_file.getparams()
        print(metadata)
        samplerate = wave_file.getframerate()
        num_channel = wave_file.getnchannels()
        frames = wave_file.readframes(metadata.nframes)
        # only draw single channel
        frames = numpy.frombuffer(frames, dtype='int16')[::num_channel]
        time = numpy.linspace(0, len(frames) / samplerate, num = len(frames))

        # create a new figure
        pyplot.figure()
        pyplot.title('Sound Wave')
        pyplot.xlabel('Time')
        pyplot.plot(time, frames)
        pyplot.subplots_adjust(left=0.12, right=0.98, top=0.94, bottom=0.06)
        pyplot.savefig('image.png', dpi=300)
        pyplot.show()

    # 2. Hard-code wave decoder.
    # with open(os.path.join('temp', filename)) as fp:
  