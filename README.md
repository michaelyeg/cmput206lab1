# cmput206lab1
Image Basics: know how to access pixels from an image matrix, compute a gray scale histogram and learn to equalize and compare histograms. This lab assignment is worth 5% of overall weight.  
Parts I and II have to be shown to the TA in the lab and part III has to be submitted online.  
Part I (40%): Write an OpenCV program to accomplish the following:  
1. Open the gray scale image called test.jpg  
2. Write your own code to compute a 256-bin gray scale histogram of the image.  
3. Plot the histogram.  
4. Also call OpenCV histogram function to compute a 256-bin histogram for the same gray scale image. Show the TA that your histogram and OpenCV histogram are same/similar.

Part II (40%): Histogram equalization:  
Write your own program to perform histogram equalization on the same test.jpg image used in the last part. You need to plot the original image, its histogram, the image after histogram equalization and its histogram. You are not allowed to use the OpenCV function cv2.equalizeHist() for this part.  
Tutorials on histogram equalization:  
• OpenCV Tutorials - Histogram Equalization  
• Wikipedia - Histogram equalization
  
Part III (20%): Histogram matching:  
Write an OpenCV program to compare histograms of two images - day.jpg and night.jpg. You will need to read both images, convert them to gray scale, compute their histograms and print the Bhattacharyya Coefficient of the two histograms. You can use OpenCV histogram function to compute the histograms. The solution to this part has to be submitted as a single Python source file named part3.py.