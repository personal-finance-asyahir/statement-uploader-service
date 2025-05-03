import logging
import json
from dataclasses import asdict, is_dataclass

from kafka import KafkaProducer
from datetime import datetime

from app.model.settings import Settings

class KafkaProducerService:
    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers=Settings().kafka_brokers,
            key_serializer=str.encode)

        # value_serializer = lambda v: json.dumps(asdict(v) if is_dataclass(v) else v).encode("utf-8")

        logging.info("Kafka Producer Service Initialized")


    def send_event(self, topic:str, key:str, message):
        self.producer.send(topic=topic,
                               key=key,
                               value=message,
                               headers=[("created-at", datetime.now().isoformat().encode('utf-8'))])
        self.producer.flush()