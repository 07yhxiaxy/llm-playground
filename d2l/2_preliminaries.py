import torch
import torch.nn as nn

x = torch.arange(12, dtype=torch.float32)

print(x)
print(x.numel())
print(x.size())
print(x.shape)

X = x.reshape(3,4)
print(X)

print(torch.zeros(2,3,4))
print(torch.ones(2,3,4))
print(torch.randn(3,4))
print(torch.tensor([[2,1,3,4],[1,2,3,4],[4,3,2,1]]))

print(X[1:3]) # we can access whole ranges of indices via slicing (e.g., X[start:stop]), where the returned value includes the first index (start) but not the last (stop).
print(X[-1])

X[1,2] = 17
print(X)

X[:2, :] = 12
print(X)

X = torch.exp(X)
print(X)

x = torch.tensor([1.0, 2, 4, 8])
y = torch.tensor([2, 2, 2, 2])
print(x + y, x - y, x * y, x / y, x ** y)