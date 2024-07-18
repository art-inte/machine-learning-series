
import mnist_parse
import math
import matplotlib.pyplot as pyplot
import random

def show_images(images, title_texts):
    """
    Helper function to show a list of images with their relating titles.
    """
    cols = 5
    rows = math.ceil(len(images) / cols)
    pyplot.figure(figsize=(10, 7))
    index = 1
    for x in zip(images, title_texts):
        image = x[0]
        title_text = x[1]
        pyplot.subplot(rows, cols, index)
        pyplot.imshow(image)
        if title_text != '':
            pyplot.title(title_text, fontsize=8)
        index += 1
    pyplot.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)
    pyplot.savefig('temp/mnist_dataset.png', dpi=300)
    pyplot.show()

if __name__ == '__main__':
    (x_train, y_train), (x_test, y_test) = mnist_parse.mnist_load()

    # Show some random training and test images.
    images_show = []
    titles_show = []
    for i in range(0, 10):
        r = random.randint(0, 60000)
        images_show.append(x_train[r])
        titles_show.append('train image [' + str(r) + '] = ' + str(y_train[r]))

    for i in range(0, 5):
        r = random.randint(0, 10000)
        images_show.append(x_test[r])
        titles_show.append('test images [' + str(r) + '] = ' + str(y_test[r]))


    show_images(images_show, titles_show)

