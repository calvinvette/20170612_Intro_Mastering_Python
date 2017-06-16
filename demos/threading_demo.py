import threading
import time
import random

done = [

]


def my_thread(*url_to_download):
    time.sleep(random.randint(1, 10))
    done.append(url_to_download)

urls = [
    r'http://google.com',
    r'http://google.com/logo.png',
    r'http://google.com/main.js',
    r'http://google.com/site.css'
]

for url in urls:
    t = threading.Thread(target=my_thread, args=(url))
    t.daemon = True
    t.start()

done_len = len(done)
url_len = len(urls)
print(url_len)
while done_len <= url_len:
    # print('-' * 40)
    print("%d: %s" % (len(done), done), end='\r')
    time.sleep(1)
    done_len = len(done)


print("Done!")




