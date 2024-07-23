import jax.numpy as jnp

def selu(x, alpha=1.67, lmbda=1.05):
    return lmbda * jnp.where(x > 0, x, alpha * jnp.exp(x) - alpha)

if __name__ == '__main__':
    a = jnp.arange(5.0)
    print(selu(a))
