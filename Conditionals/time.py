import datetime
import time

now = datetime.datetime.now().hour
now_tm = time.localtime()
hour = now_tm.tm_hour
print(now)

if hour <= 12:
    print("Good Morning!")
elif hour <= 18:
    print("Good Afternoon!")
elif hour <= 20:
    print("Good Evening!")
else:
    print("Good NIGHT!\n Go to bed!")

