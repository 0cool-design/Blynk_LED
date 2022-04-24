
import requests
import json

def SendRQ(value, PinNM):
    BLYNK_AUTH = 'api auth'
    BLYNK_URL = 'http://188.166.206.43/'
    put_header={"Content-Type": "application/json"}
    put_body = json.dumps([value])

    r = requests.put(BLYNK_URL+BLYNK_AUTH+'/update/'+PinNM, data=put_body, headers=put_header)
    print(r)

while True:
    S = int(input(">>>"))
    if S == 0:
        SendRQ(0, "V2")
    elif  S == 1:
        SendRQ(1, "V2")
    else:
        print("wrong")
