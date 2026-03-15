import os
import cv2
import torch
from torch.utils.data import Dataset


class FakeCurrencyDataset(Dataset):

    def __init__(self, root_dir, transform=None):

        self.images = []
        self.labels = []
        self.transform = transform

        for currency in os.listdir(root_dir):

            currency_path = os.path.join(root_dir, currency)

            real_path = os.path.join(currency_path, "real")
            fake_path = os.path.join(currency_path, "fake")

            if os.path.exists(real_path):
                for img in os.listdir(real_path):
                    self.images.append(os.path.join(real_path, img))
                    self.labels.append(0)

            if os.path.exists(fake_path):
                for img in os.listdir(fake_path):
                    self.images.append(os.path.join(fake_path, img))
                    self.labels.append(1)

    def __len__(self):

        return len(self.images)

    def __getitem__(self, idx):

        image = cv2.imread(self.images[idx])
        image = cv2.resize(image, (224, 224))

        if self.transform:
            image = self.transform(image)

        label = torch.tensor(self.labels[idx])

        return image, label
