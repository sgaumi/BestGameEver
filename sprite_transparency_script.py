import matplotlib.pyplot as plt
from os import listdir

path="data"

sprite_path=listdir(path)
topop=[]
for i,f in enumerate(sprite_path):
    if f[:6]!="sprite" or f[-4:]!=".png":
        topop.append(i)
topop.reverse()
for t in topop:
    sprite_path.pop(t)

for im_path in sprite_path:
    if len(path)>0:
        im_path=path+"/"+im_path
    im = plt.imread(im_path)
    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            if im[i,j,0]+im[i,j,1]+im[i,j,2] == 3.:
                im[i,j,3]=0.
    plt.imsave(im_path,im)

print("Done")