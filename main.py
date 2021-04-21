import numpy as np
import matplotlib.pyplot as plt

"""
here e going to take a photo and after running the code the outlinne of the object(s) 
in the photo will apprear in a new image!
"""
def change_image(im):
    im2 = im
    blckfactor = [0.1,0.2,0.3] #these are the factors
    for factor in blckfactor:
        for i in range(1, np.shape(im)[0]-1):
            for j in range(1, np.shape(im)[1]-1):
                im2[i, j] = is_outline(im, i, j, factor)

        #following lines making the outline black insted of white essentally toggling 0 to 1 and vice versa
        for i in range(0, np.shape(im2)[0] - 1):
            for j in range(1, np.shape(im2)[1] - 1):
                x1 = im2[i, j]
                if x1 == 0:
                    im2[i, j] = 1
                else:
                    im2[i, j] = 0

        #showing images:
        plt.imshow(im2, cmap="gray")
        plt.show()




def is_outline(im1, i, j, blackfactor):
    count = 0
    the_pixsle = im[i,j]
    c_0 = im1[i-1, j-1]
    c_1 = im1[i-1, j]
    c_2 = im1[i-1, j+1]
    c_3 = im1[i, j-1]
    c_5 = im1[i, j+1]
    c_6 = im1[i+1, j-1]
    c_7 = im1[i+1, j]
    c_8 = im1[i+1, j+1]
    around_pixel = [c_0,c_1,c_2,c_3,c_5,c_6,c_7,c_8]
    for cell in around_pixel:
        if (cell + blackfactor > the_pixsle):
            count = count + 1
    if count > 3:
        return 0
    return 1


input_file = r"C:\Users\malic\PycharmProjects\imageProcessing\imageProcessimng\images\stinkbug.png"
plt.figure()
im = plt.imread(input_file)
plt.imshow(im, cmap="gray")
plt.show()
change_image(im)
#cheakk
