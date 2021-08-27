import requests
import time

urls = [
     'https://images.pexels.com/photos/305821/pexels-photo-305821.jpeg',
     'https://images.pexels.com/photos/509922/pexels-photo-509922.jpeg',
     'https://images.pexels.com/photos/325812/pexels-photo-325812.jpeg',
     'https://images.pexels.com/photos/1252814/pexels-photo-1252814.jpeg',
     'https://images.pexels.com/photos/1420709/pexels-photo-1420709.jpeg',
 ]

def download(url):
     img_data = requests.get(url).content
     img_name = url.split('/')[4]
     img_name = f'{img_name}.jpg'
     with open(img_name, 'wb') as img_file:
         img_file.write(img_data)
         print(f'downloading {img_name}')

t1 = time.perf_counter()
for i in urls:
     download(i)
t2 = time.perf_counter()

print(f'Finished in {t2-t1} seconds') 
