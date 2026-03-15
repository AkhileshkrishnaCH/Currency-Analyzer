import torch
import cv2
from torchvision import transforms

from backend.currency_classifier import CurrencyClassifier, currency_classes


model = CurrencyClassifier(num_classes=6)
model.load_state_dict(torch.load("models/currency_classifier.pth"))
model.eval()


transform = transforms.Compose(
    [transforms.ToPILImage(), transforms.Resize((224, 224)), transforms.ToTensor()]
)


def predict_currency(image_path):

    image = cv2.imread(image_path)

    image = transform(image)

    image = image.unsqueeze(0)

    with torch.no_grad():

        outputs = model(image)

        predicted = torch.argmax(outputs, 1)

    return currency_classes[predicted.item()]


if __name__ == "__main__":

    result = predict_currency("backend/test_image.jpg")

    print("Detected Currency:", result)
