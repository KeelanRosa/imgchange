from PIL import Image
from PIL import ImageFilter
import glob, os, sys

size = 100, 100

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python imgchange.py folder")
    folder = glob.glob(sys.argv[1] + "/*.jpg")

    for infile in folder:
    # for infile in glob.glob("*.jpg"):
        file, ext = os.path.splitext(infile)
        im = Image.open(infile)
        im.filter(ImageFilter.SHARPEN).resize((100, 100)).save(infile[:-4] + ".PNG")

if __name__ == "__main__":
    main()
