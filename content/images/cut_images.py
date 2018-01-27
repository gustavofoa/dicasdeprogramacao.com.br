from PIL import Image, ImageOps, ImageDraw
import glob, os, math, sys

folder = "*"
print(sys.argv[0])
if len(sys.argv[1:]) == 1:
    folder = sys.argv[1].strip()
print("Getting images from " + folder+".")

for infile in glob.glob(folder + "/destaque.png"):
    file, ext = os.path.splitext(infile)
    img = Image.open(infile)

    ImageOps.fit(img, (75, 75), method=Image.BICUBIC, centering=(0.5, 0.5)).save(file + '-75x75.png')
    ImageOps.fit(img, (150, 150), method=Image.BICUBIC, centering=(0.5, 0.5)).save(file + '-150x150.png')
    ImageOps.fit(img, (207, 207), method=Image.BICUBIC, centering=(0.5, 0.5)).save(file + '-207x207.png')
    ImageOps.fit(img, (270, 270), method=Image.BICUBIC, centering=(0.5, 0.5)).save(file + '-270x270.png')
    ImageOps.fit(img, (305, 175), method=Image.BICUBIC, centering=(0.5, 0.5)).save(file + '-305x175.png')
    ImageOps.fit(img, (300, 225), method=Image.BICUBIC, centering=(0.5, 0.5)).save(file + '-300x225.png')
    ImageOps.fit(img, (600, 315), method=Image.BICUBIC, centering=(0.5, 0.5)).save(file + '-600x315.png')
    ImageOps.fit(img, (1024, 768), method=Image.BICUBIC, centering=(0.5, 0.5)).save(file + '-1024x768.png')
    print('Cut image - ' + file)
