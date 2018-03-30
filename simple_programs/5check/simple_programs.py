from PIL import Image, ImageDraw
import random, math
import itertools
from random import getrandbits 
dimentions = (750, 300)
iters = 100000
WHITE = (255,255,255)
BLACK = (0,0,0)
decay = 20
used_rules = []
def is_white(col):
    if col==WHITE:
        return 0
    else:
        return 1
        
def get_next_rule(old):
    new = old[:]
    new[0] = (new[0]+1) % 2   #mod it cause binary
    i = 0  
    #if this causes a carry, keep carrying as it needs
    while new[i] == 0:
        i += 1
        new[i] = (new[i] + 1) % 2
    return new
def get_rand_rule(size):
    output = []
    for _ in xrange(size):
        output.append(int(getrandbits(1)))
    if output in used_rules:
        output = get_rand_rule(size)
    return output
def makepic(dim, rule):
    im= Image.new('RGB', dim)  
    draw = ImageDraw.Draw(im)
    code= ''
    for r in rule:
        code += str(r)
    
    print('working on ' + code)
    #init first row
    for x in xrange(0, dim[0]):
        if x == dim[0]//2:
            draw.point((x, 0),WHITE)
        else:
            draw.point((x, 0),BLACK)
    
    #cycle through rows, applying the rule to each pixel
    for y in xrange(1, dim[1]):
        for x in xrange(dim[0]-2):
            if x > 1:
                mom =   im.getpixel((x-1, y-1))
                bro =   im.getpixel((x,   y-1))
                dad =   im.getpixel((x+1, y-1))
                aunt =  im.getpixel((x+2, y-1))
                uncle = im.getpixel((x-2, y-1))
                
                case = 16*is_white(mom) + 8*is_white(bro) + 4*is_white(dad) + 2*is_white(aunt) + is_white(uncle)
                if rule[case] == 0:
                    draw.point((x, y),BLACK)
                else:
                    draw.point((x, y),WHITE)
    im.save('sprogram'+code+'.png')
while True:
    rule = get_rand_rule(32)
    makepic(dimentions, rule)
    
