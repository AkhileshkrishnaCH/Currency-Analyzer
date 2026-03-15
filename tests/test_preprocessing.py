from utils.preprocessing import preprocess_image
import matplotlib.pyplot as plt

img=preprocess_image("dataset/INR/real/sample.jpg")
plt.imshow(img,cmap="gray")
plt.show()