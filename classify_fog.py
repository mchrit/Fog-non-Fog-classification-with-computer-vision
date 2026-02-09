from PIL import Image
import glob

def slow_horizontal_variance(im):
    '''Return average variance of horizontal lines of a grayscale image'''
    width, height = im.size
    if not width or not height: return 0
    vars = []
    pix = im.load()
    for y in range(height):
        row = [pix[x,y] for x in range(width)]
        mean = sum(row)/width
        variance = sum([(x-mean)**2 for x in row])/width
        vars.append(variance)
    return sum(vars)/height

for fn in glob.glob('*.png'):
    im = Image.open(fn).convert('L')
    var = slow_horizontal_variance(im)
    fog = var < 200    # FOG THRESHOLD
    print ('%5.0f - %5s - %s' % (var, fog and 'FOGGY' or 'NOT FOGGY', fn))
