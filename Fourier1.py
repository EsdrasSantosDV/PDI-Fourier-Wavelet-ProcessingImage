import cv2
import numpy as np
from matplotlib import pyplot as plt

#SO TROCAR PRO DADO SEU
img = cv2.imread('dado2.jpg',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Imagem'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Espectro de magnitude'), plt.xticks([]), plt.yticks([])
plt.show()