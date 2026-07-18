from skimage import io
import numpy as np
from matplotlib import pyplot as plt
from skimage import img_as_float

my_image = io.imread("myimage.jpg")
print(my_image.min(),my_image.max())
plt.imshow(my_image)


my_float_image = img_as_float(my_image)
print(my_float_image.min(),my_float_image.max())
plt.imshow(my_float_image)

'''
random_image = np.random.random([500,500])
plt.imshow(random_image)
print(random_image.max(),random_image.min())
'''

'''
dtypes...
uint8 - Ø to 255
uint16 = 0 to 65535
uint 32 = 0 to ((2**32) - 1)
float = -1 to 1 or Ø to 1
int8 = -128 to 127
int16 = -32768 to 32767
int32 = -2**31 to 2**31 - 1
Functions that convert images to desired dtype and properly rescale their values img_as_float - Convert to 64-bit floating point. img_as_ubyte - Convert to 8-bit uint. img_as_uint - Convert to 16-bit uint. img_as_int - Convert to 16-bit int.
'''