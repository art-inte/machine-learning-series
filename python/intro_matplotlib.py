import matplotlib.pyplot as pyplot
import numpy
import pandas

if __name__ == '__main__':
    gender_dataset = pandas.read_csv('res/gender_height_weight.csv')

    data = []
    y_trues = []
    for index, row in gender_dataset.iterrows():
        data.append(numpy.array([row['Height'], row['Weight']]))
        y_trues.append(1 if row['Gender'] == 'Male' else 0)

    # A scatter plot of y vs. x with varying marker size and/or color.
    pyplot.scatter(numpy.array(data)[:, 0], numpy.array(data)[:, 1], c=y_trues)
    pyplot.show()
