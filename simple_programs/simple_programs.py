from PIL import Image, ImageDraw
import random, math
import itertools
dimentions = (750, 300)
iters = 100000
WHITE = (255,255,255)
BLACK = (0,0,0)
decay = 20
def is_white(col):
    if col==WHITE:
        return 0
    else:
        return 1
        
def get_cases():
    print('assembling cases...')
    return list(itertools.product(range(2), repeat=5))

def get_rules():
    print('assembling rules...')
    return list(itertools.product(range(2), repeat=32))

def makepic(dim, rule):
    im= Image.new('RGB', dim)  
    draw = ImageDraw.Draw(im)
    code= ''
    for r in rule:
        code += str(r)
    cases = get_cases()
    print('working on ' + code)
    for x in xrange(0, dim[0]):
        if x == dim[0]//2:
            draw.point((x, 0),WHITE)
        else:
            draw.point((x, 0),BLACK)
            
    for y in xrange(1, dim[1]):
        for x in xrange(dim[0]-2):
            if x > 1:
                mom =   im.getpixel((x-1, y-1))
                bro =   im.getpixel((x,   y-1))
                dad =   im.getpixel((x+1, y-1))
                aunt =  im.getpixel((x+2, y-1))
                uncle = im.getpixel((x-2, y-1))
                for c,case in enumerate(cases):
                    if is_white(mom)==case[0] and is_white(bro) == case[1] and is_white(dad)==case[2] and is_white(aunt)==case[3] and is_white(uncle)==case[4]:
                        if rule[c] == 0:
                            draw.point((x, y),BLACK)
                        else:
                            draw.point((x, y),WHITE)
    code= ''
    for r in rule:
        code += str(r)
    #str(dim[0])+'x'+str(dim[1])
    im.save('sprogram'+code+'.png')

rules = get_rules()
print('Got rules')
for rule in rules:
    makepic(dimentions, rule)
