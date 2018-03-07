from PIL import Image, ImageDraw

iters = 9
bg = (50, 50, 50)
dim = (1920, 1080)
line_len_x = float(dim[0])/float(2**iters+1)
line_len_y = float(dim[1])/float(2**iters+1)

def rot_cw_rev(dirs):
    output = []
    for dir in dirs:
        if    dir == 'L':
            output.append('U')
        elif  dir == 'U':
            output.append('R')
        elif  dir == 'R':
            output.append('D')
        else:#dir == 'D'
            output.append('L')
    return list(reversed(output))


	
def rot_cc_rev(dirs):
    output = []
    for dir in dirs:
        if    dir == 'L':
            output.append('D')
        elif  dir == 'U':
            output.append('L')
        elif  dir == 'R':
            output.append('U')
        else:#dir == 'D'
            output.append('R')
    return list(reversed(output))



def level_up(reps):
    if reps==1:
        return ['U', 'R', 'D']
    else:
        prev_seq = level_up(reps-1)
        next_seq = []
        next_seq.extend(rot_cc_rev(prev_seq))
        next_seq.append('U')
        next_seq.extend(prev_seq)
        next_seq.append('R')
        next_seq.extend(prev_seq)
        next_seq.append('D')
        next_seq.extend(rot_cw_rev(prev_seq))
        return next_seq

img= Image.new('HSV', dim, color=bg)
draw = ImageDraw.Draw(img)

#set start pos to lower left coner, spaced one unit away
px = (0+line_len_x, dim[1]-line_len_y)
new_px = 0
sequence = level_up(iters)
length = len(sequence)
for number,move in enumerate(sequence):
    if move==('L'):
        new_px = (px[0]-line_len_x,px[1])
    if move==('R'):
        new_px = (px[0]+line_len_x,px[1])
    if move==('U'):
        new_px = (px[0],px[1]-line_len_y)
    if move==('D'):
        new_px = (px[0],px[1]+line_len_y)
    draw.line([px, new_px], fill=((number+0.0)/length*255, 255, 255))
    px = new_px
img.convert('RGB').save('mandel_bg.png')
