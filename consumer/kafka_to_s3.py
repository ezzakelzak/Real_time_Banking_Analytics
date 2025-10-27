import boto3
from kafka import KafkaConsumer
import json
import pandas as pd
from datetime import datetime
import os
from dotenv import load_dotenv


load_dotenv()

# Kafka consumer settings
consumer = KafkaConsumer(
    'banking_server.public.customers',
    'banking_server.public.accounts',
    'banking_server.public.transactions',
    bootstrap_servers=os.getenv("KAFKA_BOOTSTRAP"),
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id=os.getenv("KAFKA_GROUP"),
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# AWS S3 client
s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
)

bucket = os.getenv("S3_BUCKET_NAME")

# Upload function
def write_to_s3(table_name, records):
    if not records:
        return
    df = pd.DataFrame(records)
    file_path = f'{table_name}.parquet'
    df.to_parquet(file_path, engine='fastparquet', index=False)

    
    s3_key = f'{table_name}/{table_name}_{datetime.now().strftime("%Y%m%d_%H%M%S%f")}.parquet'
    s3.upload_file(file_path, bucket, s3_key)
    os.remove(file_path)
    print(f'Uploaded {len(records)} records to s3://{bucket}/{s3_key}')

# Consume and buffer messages
batch_size = 50
buffer = {
    'banking_server.public.customers': [],
    'banking_server.public.accounts': [],
    'banking_server.public.transactions': []
}

print("✅ Connected to Kafka. Listening for messages...")
print("📡 Subscribed topics:", consumer.subscription())

for message in consumer:
    topic = message.topic
    event = message.value
    payload = event.get("payload")

    if not payload:
        continue  

    record = payload.get("after")
    if record:
        buffer[topic].append(record)
        print(f"[{topic}] +1 record")

    if len(buffer[topic]) >= batch_size:
        write_to_s3(topic.split('.')[-1], buffer[topic])
        buffer[topic] = []
