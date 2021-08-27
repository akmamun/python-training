# import time
# from PIL import Image, ImageFilter

# #pillow #opencv

# file_names = ['1.png', '2.png','3.png','4.png','5.png','6.png','7.png']
# start = time.perf_counter()

# size = (1200, 1200)
# def augment_image(img_name):
#      img = Image.open(f"images/{img_name}")
#      img = img.filter(ImageFilter.GaussianBlur(15))
#      img.thumbnail(size)
#      img.save(f'aug/{img_name}')
#      print(f'{img_name} was augmented...')
     
# for f in file_names:
#      augment_image(f)
# end = time.perf_counter()

# print(f'Finished in {round(end-start, 2)} seconds') 

#pip install pillow
#multi process

import time
import concurrent.futures

from PIL import Image, ImageFilter

#make sure those picture in disk
file_names = ['1.png', '2.png','3.png','4.png','5.png','6.png','7.png']

size = (1200, 1200)
def augment_image(img_name):
     img = Image.open(f"images/{img_name}")
     img = img.filter(ImageFilter.GaussianBlur(15))
     img.thumbnail(size)
     img.save(f'aug/{img_name}')
     print(f'{img_name} was augmented...')

start = time.perf_counter()

with concurrent.futures.ProcessPoolExecutor() as executor:
     executor.map(augment_image, file_names)

end = time.perf_counter()
print(f'Finished in {round(end-start, 2)} seconds') 
