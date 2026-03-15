import torch
from backend.currency_classifier import CurrencyClassifier


model = CurrencyClassifier(num_classes=6)

x = torch.randn(1, 3, 224, 224)

output = model(x)

print(output.shape)