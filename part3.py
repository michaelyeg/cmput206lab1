import cv2, numpy as np
# from matplotlib import pyplot as plt


class image:
    def __init__(self):
        self.image = []
        self.histogram = []

    def loadgrayscale(self, filename):
        self.image = cv2.imread(filename, 0)

    def createhist(self):
        if len(self.image) != 0:
            self.histogram = cv2.calcHist([self.image], [0], None, [256], [0, 256])

    def normalizehist(self):
        self.histogram = self.histogram / sum(self.histogram)

    def gethistogram(self):
        return self.histogram


def calculatebc(imageA, imageB):
    # First normalize histograms
    imageA.normalizehist()
    imageB.normalizehist()
    BC = sum(np.sqrt(np.multiply(imageA.gethistogram(), imageB.gethistogram())))
    print "The Bhattacharyya Coefficient of the two histograms is " + str(BC[0])+".\r\n"
    return


def main():
    imgA = image()
    imgA.loadgrayscale('day.jpg')
    imgA.createhist()
    imgB = image()
    imgB.loadgrayscale('night.jpg')
    imgB.createhist()
    calculatebc(imgA, imgB)

if __name__ == "__main__":
    main()