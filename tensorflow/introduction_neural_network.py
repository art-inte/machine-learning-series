import numpy
import pandas

# Gender: male/female
# Height: number (cm)
# Weight: number (kg)
# Index: 0 - extremely weak, 1 - weak, 2 - normal, 3 - overweight, 4 - obesity, 5 - extreme obesity.

def sigmoid(x):
    # Sigmoid activation function: f(x) = 1 / (1 + e^(-x)).
    return 1 / (1 + numpy.exp(-x))

def derivative_sigmoid(x):
    # Derivative of sigmoid: f'(x) = f(x) * (1 - f(x)).
    fx = sigmoid(x)
    return fx * (1 - fx)

def mse_loss(y_true, y_pred):
    # Mean Squared Error loss function.
    return ((y_true - y_pred) ** 2).mean()

learn_rate = 0.01
epochs = 5

class SimpleNeuralNetwork:
    # A neural network with:
    #  - 2 inputs
    #  - 1 hidden layer with 2 neurons (h1, h2)
    #  - 1 output layer with 1 neuron (o1)
    def __init__(self):
        # weights
        numpy.random.seed(0)
        self.w1 = numpy.random.normal()
        self.w2 = numpy.random.normal()
        self.w3 = numpy.random.normal()
        self.w4 = numpy.random.normal()
        self.w5 = numpy.random.normal()
        self.w6 = numpy.random.normal()

        # biases
        self.b1 = numpy.random.normal()
        self.b2 = numpy.random.normal()
        self.b3 = numpy.random.normal()

    def forward(self, input):
        # input is a numpy array with 2 elements.
        h1 = sigmoid(self.w1 * input[0] + self.w2 * input[1] + self.b1)
        h2 = sigmoid(self.w3 * input[0] + self.w4 * input[1] + self.b2)
        o1 = sigmoid(self.w5 * h1 + self.w6 * h2 + self.b3)
        return o1

    def train(self, data, labels):
        for epoch in range(epochs):
            for x, y_true in zip(data, labels):
                # Do a feedforward.
                sum_h1 = self.w1 * x[0] + self.w2 * x[1] + self.b1
                h1 = sigmoid(sum_h1)
                sum_h2 = self.w3 * x[0] + self.w4 * x[1] + self.b2
                h2 = sigmoid(sum_h2)
                sum_o1 = self.w5 * h1 + self.w6 * h2 + self.b3
                o1 = sigmoid(sum_o1)
                ypred = o1

                d_loss_d_ypred = -2 * (y_true - ypred)

                # neuron o1
                d_ypred_d_w5 = h1 * derivative_sigmoid(sum_o1)
                d_ypred_d_w6 = h2 * derivative_sigmoid(sum_o1)
                d_ypred_d_b3 = derivative_sigmoid(sum_o1)
                d_ypred_d_h1 = self.w5 * derivative_sigmoid(sum_o1)
                d_ypred_d_h2 = self.w6 * derivative_sigmoid(sum_o1)

                # neuron h1
                d_h1_d_w1 = x[0] * derivative_sigmoid(sum_h1)
                d_h1_d_w2 = x[1] * derivative_sigmoid(sum_h1)
                d_h1_d_b1 = derivative_sigmoid(sum_h1)

                # neuron h2
                d_h2_d_w3 = x[0] * derivative_sigmoid(sum_h2)
                d_h2_d_w4 = x[1] * derivative_sigmoid(sum_h2)
                d_h2_d_b2 = derivative_sigmoid(sum_h2)

                # Update weights and biases.
                self.w1 -= learn_rate * d_loss_d_ypred * d_ypred_d_h1 * d_h1_d_w1
                self.w2 -= learn_rate * d_loss_d_ypred * d_ypred_d_h1 * d_h1_d_w2
                self.b1 -= learn_rate * d_loss_d_ypred * d_ypred_d_h1 * d_h1_d_b1

                self.w3 -= learn_rate * d_loss_d_ypred * d_ypred_d_h2 * d_h2_d_w3
                self.w4 -= learn_rate * d_loss_d_ypred * d_ypred_d_h2 * d_h2_d_w4
                self.b2 -= learn_rate * d_loss_d_ypred * d_ypred_d_h2 * d_h2_d_b2

                self.w5 -= learn_rate * d_loss_d_ypred * d_ypred_d_w5
                self.w6 -= learn_rate * d_loss_d_ypred * d_ypred_d_w6
                self.b3 -= learn_rate * d_loss_d_ypred * d_ypred_d_b3

            # Calcuate total loss at the end of each epoch.
            y_preds = numpy.apply_along_axis(self.forward, 1, data)
            loss = mse_loss(labels, y_preds)
            print('Epoch %d loss: %.3f' % (epoch, loss))

if __name__ == '__main__':
    gender_dataset = pandas.read_csv('res/gender_height_weight.csv')

    data = []
    y_trues = []
    for index, row in gender_dataset.iterrows():
        data.append(numpy.array([row['Height'], row['Weight']]))
        y_trues.append(1 if row['Gender'] == 'male' else 0)

    network = SimpleNeuralNetwork()
    network.train(data, y_trues)
