import time
count = 0
while(True):
    print count
    count += 1
    exec(open("./monitor.py").read())
    time.sleep(1)
