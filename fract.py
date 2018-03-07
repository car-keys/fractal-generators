from PIL import Image, ImageDraw
import random, math
import itertools
dim = (1000, 1000)
iters = 100000
WHITE = (255,255,255)
GREEN = (0,255,0)
a1 = (int(.5*dim[0]),int(0*dim[1]))
a2 = (int(0*dim[0]),int(1*dim[1]))
a3 = (int(1*dim[0]),int(1*dim[1]))

def distance(p1, p2):
    return math.sqrt((p1[0] + p2[0])**2 + (p1[1] + p2[1])**2)

def midpoint(p1, p2):
    return (int(p1[0] + p2[0]/2), int(p1[1] + p2[1]/2))
m12 = midpoint(a1, a2)
m13 = midpoint(a1, a3)
m23 = midpoint(a2, a3)

def draw_box_around(point, img_draw, radius, color):
    for x in range(point[0]-radius, point[0]+radius):
        for y in range(point[1]-radius, point[1]+radius):
            img_draw.point((x,y), color)

im= Image.new('RGB', dim)  
draw = ImageDraw.Draw(im)

pixel = [300, 300]
for x in range(1000):
    for i in range(iters/1000):
        choice = random.randint(1,3)
        if choice == 1:
            pixel[0] = (pixel[0]+a1[0])//2
            pixel[1] = (pixel[1]+a1[1])//2
        elif choice == 2:
            pixel[0] = (pixel[0]+a2[0])//2
            pixel[1] = (pixel[1]+a2[1])//2
        elif choice == 3:
            pixel[0] = (pixel[0]+a3[0])//2
            pixel[1] = (pixel[1]+a3[1])//2
        elif choice == 4:
            pixel[0] = (pixel[0]+a4[0])//2
            pixel[1] = (pixel[1]+a4[1])//2
        else:
            pixel[0] = (pixel[0]+a5[0])//2
            pixel[1] = (pixel[1]+a5[1])//2
        r = int(pixel[0]/float(dim[0])*255)
        b = int((dim[0] - pixel[0] + pixel[1])/2/float(dim[0]+dim[1]/2)*255)
        g = int((pixel[0] + pixel[1])/2/float(dim[0]+dim[1]/2)*255)
        draw.point(pixel, (r,g,b))
im.save('serpinski.png')
