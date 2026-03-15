import os
import cv2
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms

from backend.currency_classifier import CurrencyClassifier


currency_classes = ["CNY", "EUR", "GBP", "INR", "JPY", "USD"]


class CurrencyDataset(Dataset):

    def __init__(self, root_dir, transform=None):

        self.images = []
        self.labels = []
        self.transform = transform

        for idx, currency in enumerate(currency_classes):

            currency_path = os.path.join(root_dir, currency)

            for file in os.listdir(currency_path):

                path = os.path.join(currency_path, file)

                if os.path.isfile(path):

                    self.images.append(path)
                    self.labels.append(idx)

    def __len__(self):
        return len(self.images)

    def __getitem__(self, idx):

        image = cv2.imread(self.images[idx])
        image = cv2.resize(image, (224, 224))

        if self.transform:
            image = self.transform(image)

        label = torch.tensor(self.labels[idx])

        return image, label


transform = transforms.Compose(
    [
        transforms.ToPILImage(),
        transforms.RandomHorizontalFlip(),
        transforms.RandomRotation(15),
        transforms.RandomResizedCrop(224),
        transforms.ColorJitter(brightness=0.3, contrast=0.3),
        transforms.ToTensor(),
    ]
)


dataset = CurrencyDataset("dataset", transform)

loader = DataLoader(dataset, batch_size=8, shuffle=True)


model = CurrencyClassifier(num_classes=6)

criterion = nn.CrossEntropyLoss()

optimizer = optim.Adam(model.parameters(), lr=0.0001)


epochs = 15


for epoch in range(epochs):

    total_loss = 0

    for images, labels in loader:

        optimizer.zero_grad()

        outputs = model(images)

        loss = criterion(outputs, labels)

        loss.backward()

        optimizer.step()

        total_loss += loss.item()

    avg_loss = total_loss / len(loader)

    print(f"Epoch {epoch+1}/{epochs} Loss: {avg_loss}")


torch.save(model.state_dict(), "models/currency_classifier.pth")

print("Currency classifier retrained successfully")
