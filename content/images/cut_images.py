from PIL import Image, ImageOps, ImageDraw
import glob, os, math, sys

folder = "*"
print(sys.argv[0])
if len(sys.argv[1:]) == 1:
    folder = sys.argv[1].strip()
print("Getting images from " + folder+".")

def resize(size, img, filename):
    img.thumbnail(size, resample=Image.ANTIALIAS)
    background = Image.new('RGBA', size, (255, 255, 255))
    background.paste(
        img, (int((size[0] - img.size[0]) / 2), int((size[1] - img.size[1]) / 2))
    )
    background.save(filename)

for infile in glob.glob(folder + "/destaque.png"):
    file, ext = os.path.splitext(infile)
    img = Image.open(infile)

    img.thumbnail((1024, 768), resample=Image.BICUBIC)
    img.save(file + '-1024x768.png')
    resize((1024,768), img, file + "-1024x768.png")
    resize((600,315), img, file + "-600x315.png")
    resize((300,225), img, file + "-300x225.png")
    resize((305,175), img, file + "-305x175.png")
    resize((270,270), img, file + "-270x270.png")
    resize((207,207), img, file + "-207x207.png")
    resize((150,150), img, file + "-150x150.png")
    resize((75,75), img, file + "-75x75.png")
    
    
    print('Cut image - ' + file)
