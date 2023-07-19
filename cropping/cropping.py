import cv2

# mengambil gambar
image = cv2.imread('./photo.jpg')
print(image.shape)

# [start_y : end_y, start_x:enc_x]
crop = image[100:200, 200:300]

cv2.imshow("full", image)
cv2.imshow("crop",crop)
cv2.waitKey(0)
