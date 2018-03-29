from PIL import Image, ImageDraw
import random, math
import itertools
dimentions = (10, 100)
iters = 100000
WHITE = (255,255,255)
BLACK = (0,0,0)
decay = 20
def issame(p1, p2):
    return (p1==BLACK) == (p2==BLACK)

def makepic(dim, jump):
    im= Image.new('RGB', dim)  
    draw = ImageDraw.Draw(im)
    for x in xrange(0, dim[0]):
        #if random.randint(0,200) == 1:
        if x == dim[0]//2:
            draw.point((x, 0),WHITE)
        else:
            draw.point((x, 0),BLACK)
    for y in xrange(1, dim[1]):
        for x in xrange(dim[0]):
            if x <= jump-1:
                draw.point((x, y),im.getpixel((x+jump, y-1)))
            elif x >= dim[0]-jump:
                draw.point((x, y),im.getpixel((x-jump, y-1)))
            elif issame(im.getpixel((x+jump, y-1)), im.getpixel((x-jump, y-1))):
                    draw.point((x, y),WHITE)
            else:
                draw.point((x, y),BLACK)
        if y%100 == 0:
            print(y)
    im.save('noise'+str(dim[0])+'x'+str(dim[1])+'j'+str(jump)+'.png')
makepic(dimentions, 1)
