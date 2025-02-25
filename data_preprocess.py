import numpy as np
from PIL import Image

train_path = "data/train_set/"
test_path = "data/test_set/"
data = np.load("full_numpy_bitmap_guitar.npy")
data = data[0:3000,:]

for i in range(0,3000):
    x=np.reshape(data[i],(64,64))  
    img = Image.fromarray(x)
    img = img.convert('L')
    if i<2400: img.save(train_path+"guitar/guitar"+str(i)+".png")
    else : img.save(test_path+"guitar/guitar"+str(i-2400)+".png")
    