# if not requests pip install requests
import thread
import threading
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

start = time.perf_counter()
threads = []
for i in urls:
    t = threading.Thread(target=download, args=[i])
    t.start()
    threads.append(t)
for thread in threads:
    thread.join()
finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} seconds')
