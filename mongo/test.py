import json

import requests
import unittest
from client import conn


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

    def test_mongo(self):
        col = conn["test"]["duobei"]
        # data = {
        #    "author": "abc123",
        #    "title": "zzz",
        #    "tags": ["programming", "database", "mongodb", "dada" ]
        # }
        # col.save(data)
        res = col.aggregate([
            {
                "$group": {
                    "_id": "$author",
                    "tags": {
                        "$push": "$tags"
                    }
                },
            },
            {"$addFields": {
                "tags": {
                    "$reduce": {
                        "input": "$tags",
                        "initialValue": [],
                        "in": {"$concatArrays": ["$$value", "$$this"]}
                    }
                }
            }},
            {
                "$project": {
                    "_id": 0,
                    "tags": 1,
                }
            }]
        )
        for i in res:
            print(i)

    def test_mongo2(self):
        col = conn["test"]["duobei"]
        res = col.aggregate([
            {
                "$group": {
                    "_id": "$author",
                    "title": {
                        "$push": "$title"
                    }
                },
            },
        ])

        for i in res:
            print(i)

    def test_gmsConnectChanged(self):
        log = {
            "Geo": {
                "Isp": "中国联通",
                "Province": "北京市",
                "Ip": "222.128.2.34",
                "Country": "中国",
                "City": "北京市"
            },
            "UserInfo": {
                "enterpriseName": "",
                "userId": 0,
                "username": "",
                "mobile": "",
                "nickname": "",
                "enterpriseID": 0
            },
            "state": "已连接",
            "deviceId": "3f426330-9d97-11eb-8d1e-f18510275be1",
            "gmsuid": "rrjD6m8PQg2wPTx5Bwx1Vj7N10",
            "uid": "rrjD6m8PQg2wPTx5Bwx1Vj7N10",
            "osVersion": "10",
            "timestamp": 1630637902975,
            "serverAddr": "",
            "companyName": "北京沃龙科技发展有限公司",
            "appPack": "tongshi-pc",
            "appVersion": "2.5.7",
            "platform": "Windows",
            "mobile": "18838980951",
            "UserAgent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) tosee-web-client/2.5.7 Chrome/91.0.4472.69 Electron/13.0.1 Safari/537.36",
            "reason": "登录成功",
            "nickname": "【乐高】小北",
            "type": "GMSConnectStateChanged"
        }
        url = "http://localhost:8889/tosee/collect-event"

        res = requests.post(url=url, data=json.dumps(log))
        print(res)

    def test_update(self):
        col = conn["test"]["duobei"]
        res = col.update_many({"_id": 1}, {"$set": {
            'dad': "da"
        }})
        # {'n': 0, 'nModified': 0, 'ok': 1.0, 'updatedExisting': False}
        print(res.modified_count)
