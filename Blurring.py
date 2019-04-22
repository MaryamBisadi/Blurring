from Tkinter import Tk
from tkinter.filedialog import askopenfilename
import cv2
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def blur(ks):
    average = cv2.blur(im, (ks,ks))
    gaussian = cv2.GaussianBlur(im, (ks,ks), 0)
    median = cv2.medianBlur(im, ks)

    cv2.imwrite('AverageBlur.jpg', average)
    cv2.imwrite('GaussianBlur.jpg', gaussian)
    cv2.imwrite('MedianBlur.jpg', median)
 
    plt.subplot(221), plt.imshow(im), plt.title('Original Image')
    plt.xticks([]), plt.yticks([])
    plt.subplot(222), plt.imshow(average), plt.title('Average Blur')
    plt.xticks([]), plt.yticks([])
    plt.subplot(223), plt.imshow(gaussian), plt.title('Gaussian Blur')
    plt.xticks([]), plt.yticks([])
    plt.subplot(224), plt.imshow(median), plt.title('Median Blur')
    plt.xticks([]), plt.yticks([])

def update(val):
    blur(int(val))
    fig.canvas.draw_idle()

root = Tk()
root.withdraw()
filename = askopenfilename()
im = cv2.imread(filename)

fig, ax = plt.subplots()

blur(5)
axks = plt.axes([0.2, 0.05, 0.65, 0.03], facecolor='lightgoldenrodyellow')
kernelSizes = Slider(axks, 'Kernel Sizes', 1, 20, valinit=5, valfmt='%0.0f',valstep=2)

kernelSizes.on_changed(update)
plt.show()

