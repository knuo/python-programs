import os
import time
from TwitterAPI import TwitterAPI
from gpiozero import MotionSensor

pir = MotionSensor(4)
b=1
CONSUMER_KEY = 'ow73OQnCfioXm5yXNsQHXW2K7'
CONSUMER_SECRET = 'f2vXDmGsT6ziOHjrpNhqsMYJYmC8JOorpoRogGjbYC2OxqVfam'
ACCESS_TOKEN_KEY = '4100867894-bN3LXrdd6xhipQejjh4YOYK4r3wR3pQVUUf118h'
ACCESS_TOKEN_SECRET = 'VQNFzY8ODVTfPpaRSvhpSUZiisTlvhy3L3SWB2HHur1qw'
api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

while True:
    if pir.motion_detected:
        img="/home/pi/cam/"+str(b)+".jpg"
        cmd= "fswebcam -F 5 --fps 20 -r \"1200x800\" "+img
        os.system(cmd)
        print("pic taken")
        file = open(img, 'rb')
        data = file.read()
        r = api.request('statuses/update_with_media', {'status':'#pyTweetCMR'}, {'media[]':data})
        print(r.status_code)
        b=b+1

