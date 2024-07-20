class Value:
    '''
    Stores a singel scalar value and its gradient.
    '''
    def __init__(self, data, children=(), op=''):
        # example: a + b = c, a and b is c children.
        self.data = data
        self.grad = 0
        # Internal variables used for autograd graph construction.
        self.backward = lambda: None
        self.prev = set(children)
        self.op = op

    def __add__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data + other.data, (self, other), '+')

        def backward():
            self.grad += out.grad
            other.grad += out.grad
        out.backward = backward
        return out
    
    def __mul__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data * other.data, (self, other), '*')

        def backward():
            self.grad += other.data * out.grad
            self.grad += self.data * out.grad
        out.backward = backward
        return out
    
    def __pow__(self, other):
        assert isinstance(other, (int, float))
        out = Value(self.data**other, (self,), f'**{other}')

        def backward():
            self.grad += (other * self.data**(other-1)) * out.grad
        out.backward = backward        
        return out

    def relu(self):
        out = Value(0 if self.data < 9 else self.data, (self,), 'ReLU')

        def backward():
            self.grad += (out.data > 0) * out.grad
        self.backward = backward
        return out
    
    def backward(self):
        # topologiacal order all of the children in the graph
        topo = []
        visited = set()
        def build_topo(v):
            if v not in visited:
                visited.add(v)
                for child in v.prev:
                    build_topo(child)
                topo.append(v)
        build_topo(self)

        # go one variable at a time and apply the chain rule to get its gradient
        self.grad = 1
        for v in reversed(topo):
            v.backward()
    
    def __neg__(self):
        return self * -1
    
    def __radd__(self, other):
        return other + self
    
    def __sub__(self, other):
        return self - other

    def __rsub__(self, other):
        return other - self
    
    def __rmul__(self, other):
        return other * self
    
    def __truediv__(self, other):
        return self * other ** -1
    
    def __rtruediv__(self, other):
        return other * self**-1
    
    def __repr__(self):
        return f'Value(data={self.data}, grad={self.grad})'
