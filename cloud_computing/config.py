import yaml

with open("./config.yaml", encoding="utf-8") as file:
    Config = yaml.full_load(file)
    MONGO = Config.get('Mongo')
    Kafka = Config.get('Kafka')
    Mysql = Config.get('Mysql')
