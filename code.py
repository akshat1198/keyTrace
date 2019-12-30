import cv2
import matplotlib.pyplot as plt 

image = cv2.imread('key.jpg')
key = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#the following are filters, change the
#values to allow/block certain colors

min = (0, 0, 0)
max = (255,255,150)


filtered_key = cv2.inRange(key, min, max)


plt.subplot(1, 2, 1)
plt.imshow(key)
plt.subplot(1, 2, 2)
plt.imshow(filtered_key, cmap="gray")
plt.show()
