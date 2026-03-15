import os
import cv2
import torch
from torchvision import transforms

from backend.currency_classifier import CurrencyClassifier


currency_classes = ["CNY", "EUR", "GBP", "INR", "JPY", "USD"]


model = CurrencyClassifier(num_classes=6)
model.load_state_dict(torch.load("models/currency_classifier.pth"))
model.eval()


transform = transforms.Compose(
    [transforms.ToPILImage(), transforms.Resize((224, 224)), transforms.ToTensor()]
)


correct = 0
total = 0


dataset_path = "dataset"


for idx, currency in enumerate(currency_classes):

    currency_path = os.path.join(dataset_path, currency)

    for file in os.listdir(currency_path):

        path = os.path.join(currency_path, file)

        if os.path.isfile(path):

            image = cv2.imread(path)

            if image is None:
                continue

            image = transform(image)
            image = image.unsqueeze(0)

            with torch.no_grad():

                output = model(image)

                pred = torch.argmax(output, 1).item()

            if pred == idx:
                correct += 1

            total += 1


accuracy = (correct / total) * 100

print("Total images tested:", total)
print("Correct predictions:", correct)
print("Accuracy:", accuracy, "%")
