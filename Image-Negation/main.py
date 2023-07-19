import cv2

# membaca img
img = cv2.imread('./gambar2.jpg')
gray = cv2.imread('./gambar3.jpg',0)

row = gray.shape[0]
col = gray.shape[1]
negative = gray.copy()
# convert format img
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# perhitungan colored
colored_negative = abs(255-img)

# perhitungan gray_negative
for i in range (row):
    for j in range(col):
        negative[i][j] = 255 - negative[i][j]

# simpan gambar
cv2.imwrite('newimg2.jpg', img)
cv2.imwrite('newimg3.jpg', negative)