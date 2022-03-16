import yaml

with open("config.yaml", encoding="utf-8") as file:
    Config = yaml.full_load(file)
    Mongo = Config.get('Mongo')
    Kafka = Config.get('Kafka')
    Statsd = Config.get('Statsd')
