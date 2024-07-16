
class Neuron:
    def __init__(self):
        self.w1 = 0
        self.w2 = 0
        self.b = 0

    def forward(self, x1, x2):
        return self.w1 * x1 + self.w2 * x2 + self.b

    def __call__(self, x1, x2):
        return self.forward(x1, x2)

if __name__ == '__main__':
    n = Neuron()
    print(n(1, 2))

