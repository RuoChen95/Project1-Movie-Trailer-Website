import time
import webbrowser

print("this program started on"+time.ctime())
count = 0
while (count<3):
    time.sleep(10)
    webbrowser.open("http://www.baidu.com")
    count = count + 1
