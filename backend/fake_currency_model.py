import torch
import torch.nn as nn
import torchvision.models as models


class FakeCurrencyDetector(nn.Module):

    def __init__(self):

        super(FakeCurrencyDetector, self).__init__()

        self.model = models.mobilenet_v2(weights="DEFAULT")

        self.model.classifier[1] = nn.Linear(self.model.last_channel, 2)

    def forward(self, x):

        return self.model(x)


classes = ["Real", "Fake"]
