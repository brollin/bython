import os, sys
from PIL import Image

size = (150, 150)

for infile in sys.argv[1:]:
    outfile = "processed/" + os.path.splitext(infile)[0].lower().replace('&','and') + ".png"
    if infile != outfile:
        try:
            im = Image.open(infile)
            im.thumbnail(size, Image.ANTIALIAS)
            im.save(outfile, "PNG")
        except IOError:
            print "cannot create thumbnail for '%s'" % infile
