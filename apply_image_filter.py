#!/usr/bin/python

import sys
import os
import PIL.Image as Image
#import logging
#logging.basicConfig(filename="image_filter.log", level=logging.INFO)
#logger = logging.getLogger(__name__)
import logging
logger = logging.getLogger('root')
FILE = "my_log_file.log"
FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
logging.basicConfig(format=FORMAT, filename=FILE)
logger.setLevel(logging.DEBUG)



def ApplyFilter(bg_image , fg_image):
        logger.info("the bg_image %s",bg_image) 

	filtered_name =  bg_image.split('.')[0]+ fg_image.split('.')[0]+ ".png"
	logger.info("the filtered name is  %s",filtered_name)
	bg =  Image.open(bg_image)

	fg = Image.open(fg_image + ".png")

	bg = bg.convert('RGBA')
	fg = fg.convert('RGBA')

	bg =  bg.resize((1000,1000), Image.ANTIALIAS)

	Image.alpha_composite(bg, fg).save(filtered_name)

if __name__=='__main__':
        print(os.path.basename("."))
	bg_name = sys.argv[1]
	fg_name = sys.argv[2]
	ApplyFilter(bg_name , fg_name)
