import os
from redis import StrictRedis
import config

from db import Mongo


conn = Mongo(config.Mongo["URL"]).get_session()

db = conn['datacenter']

paas_collect_event = db.paas_collect_event

paas_user_stream = db.paas_user_stream
paas_channel = db.paas_channel
paas_user = db.paas_user
paas_user_by_day = db.paas_user_by_day

tosee_user = db.tosee_userw
tosee_user_by_day = db.tosee_user_by_day
tosee_channel = db.tosee_channel

redis = StrictRedis(host=os.getenv("REDIS_HOST", "localhost"),
                    port=os.getenv("REDIS_PORT", 6379),
                    decode_responses=True)