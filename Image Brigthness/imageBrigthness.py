import cv2
import matplotlib.pyplot as plt


image = cv2.imread('./imagebrightness/tes.jpg')

alpha = 1.5
beta = 10  
adjusted = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(1, 2, 2)
plt.imshow(adjusted)
plt.title('Adjusted')
plt.xticks([]), plt.yticks([])

plt.show()