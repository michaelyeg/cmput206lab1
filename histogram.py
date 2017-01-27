import cv2, numpy as np
from matplotlib import pyplot as plt

def createhist(img):
    # Create 1D array of size 256
    H = np.zeros(256)
    # Iterate over image pixels
    for i in img:
        for j in i:
            H[j] += 1
    return H

# Create histogram by opencv builtin function
def createhistbycv(img):
    histr = cv2.calcHist([img], [0], None, [256], [0, 256])
    return histr

# Compute cumulative histogram
def cumulatehist(hist):
    newhist = []
    for i in range(0, len(hist)):
        if i == 0:
            newhist.append(hist[i])
        else:
            newhist.append(newhist[i-1] + hist[i])
    return newhist

# Histogram equalization
def equahis(hist, originimg):
    cumhist = cumulatehist(hist)
    dimension=list(originimg.shape)
    M = dimension[0]
    N = dimension[1]
    newimg = originimg.copy()
    for m in range(0, M):
        for n in range(0, N):
            newimg[m,n] = int(255*cumhist[int(newimg[m,n])]/int(M*N)+0.5)
    newhist = createhist(newimg)
    cursor=plt.subplot(221)
    cursor.set_title('Original Image')
    plt.imshow(originimg,'gray')
    cursor=plt.subplot(222)
    cursor.set_title('Histogram')
    plt.plot(hist)
    cursor=plt.subplot(223)
    cursor.set_title('New Image')
    plt.imshow(newimg, 'gray')
    cursor=plt.subplot(224)
    cursor.set_title('Histogram After Equalization')
    plt.plot(newhist)
    plt.show()
    return

# Input a list of plots and display in one
def plotmulti(imglist):
    cmdstr = ""
    if len(imglist) == 4:
        cmdstr = "22"
        for i in range(0, 4):
            cmdstr += str(i+1)
            plt.subplot(int(cmdstr))
            plt.plot(imglist[i])
            cmdstr = "22"
        plt.show()
    elif len(imglist) == 2:
        cursor=plt.subplot(121)
        cursor.set_title('Histogram by OpenCV')
        plt.plot(imglist[0])
        cursor=plt.subplot(122)
        cursor.set_title('Our Own Histogram')
        plt.plot(imglist[1])
        plt.show()
    return

def main():
    img = cv2.imread('test.jpg',0)
    hist = createhist(img)
    histbycv = createhistbycv(img)
    plotmulti([histbycv, hist])
    equahis(hist, img)

if __name__ == "__main__":
    main()