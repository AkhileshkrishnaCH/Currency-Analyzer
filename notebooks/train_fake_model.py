import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import transforms

from backend.fake_currency_model import FakeCurrencyDetector
from utils.fake_dataset_loader import FakeCurrencyDataset


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


dataset = FakeCurrencyDataset("dataset", transform=transform)

loader = DataLoader(dataset, batch_size=8, shuffle=True)


model = FakeCurrencyDetector()

criterion = nn.CrossEntropyLoss()

optimizer = optim.Adam(model.parameters(), lr=0.0005)


epochs = 10


for epoch in range(epochs):

    total_loss = 0

    for images, labels in loader:

        optimizer.zero_grad()

        outputs = model(images)

        loss = criterion(outputs, labels)

        loss.backward()

        optimizer.step()

        total_loss += loss.item()

    print(f"Epoch {epoch+1}/{epochs} Loss: {total_loss}")


torch.save(model.state_dict(), "models/fake_currency_model.pth")

print("Fake currency model saved")
