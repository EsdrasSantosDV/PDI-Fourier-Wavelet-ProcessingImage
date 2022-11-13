import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('dado2.jpg',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
rows,cols = img.shape
crow,ccol = (int)(rows/2),(int)(cols/2)
fshift[crow-30:crow+30, ccol-30:ccol+30] = 0
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)
plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Imagem'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(img_back, cmap = 'gray')
plt.title('Passa alta'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(img_back)
plt.title('Resultado'), plt.xticks([]), plt.yticks([])
plt.show()