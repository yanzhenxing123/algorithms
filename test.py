import requests
import unittest



class Test(unittest.TestCase):

    def testGms(self):
        url = "http://localhost:8889/gms/v1/collect-event/"
        log = {
            "platform": "native",
            "UserAgent": "okhttp/4.9.0",
            "result": 1,
            "sdkVer": "1.5.0",
            "uid": "gms1402205437565136897",
            "channelId": "",
            "os": "Android/8.1.0",
            "type": "LeaveChannel",
            "timestamp": 1629163654339,
            "elapsed": 74,
            "deviceId": "e7a39215dcd92061",
            "channelSessionId": "",
            "appId": "GaLknQbqNqe9p23z",
            "errorCode": 0,
            "appIdEncrypt": False,
            "clientSessionId": "c926bb0d-af4e-4dff-b9b5-8624e4bfeaa7",
            "Geo": {
                "Isp": "中国联通",
                "City": "北京市",
                "Ip": "111.206.85.4",
                "Country": "中国",
                "Province": "北京市"
            }
        }
        res = requests.post(url=url, data=log)
        print(res)
