import torch
import torch.nn as nn
import torchvision.models as models


class CurrencyClassifier(nn.Module):

    def __init__(self, num_classes):
        super(CurrencyClassifier, self).__init__()

        self.model = models.mobilenet_v2(weights="DEFAULT")
        self.model.classifier[1] = nn.Linear(self.model.last_channel, num_classes)

    def forward(self, x):
        return self.model(x)


currency_classes = ["CNY", "EUR", "GBP", "INR", "JPY", "USD"]
