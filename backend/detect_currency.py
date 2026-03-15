import torch
import cv2
from torchvision import transforms

from backend.currency_classifier import CurrencyClassifier, currency_classes
from backend.fake_currency_model import FakeCurrencyDetector, classes
from backend.currency_converter import convert_to_inr


currency_model = CurrencyClassifier(num_classes=6)
currency_model.load_state_dict(torch.load("models/currency_classifier.pth"))
currency_model.eval()


fake_model = FakeCurrencyDetector()
fake_model.load_state_dict(torch.load("models/fake_currency_model.pth"))
fake_model.eval()


transform = transforms.Compose(
    [
        transforms.ToPILImage(),
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
    ]
)


def detect(image_path):

    image = cv2.imread(image_path)

    img = transform(image)
    img = img.unsqueeze(0)

    with torch.no_grad():

        currency_output = currency_model(img)
        currency_pred = torch.argmax(currency_output, 1)

        fake_output = fake_model(img)
        fake_pred = torch.argmax(fake_output, 1)

    currency = currency_classes[currency_pred.item()]
    status = classes[fake_pred.item()]

    rate = convert_to_inr(currency)

    return currency, status, rate


if __name__ == "__main__":

    currency, status, rate = detect("backend/inrtest.jpg")

    print("Currency:", currency)
    print("Status:", status)

    if currency != "INR":
        print(f"1 {currency} ≈ {round(rate,2)} INR")
