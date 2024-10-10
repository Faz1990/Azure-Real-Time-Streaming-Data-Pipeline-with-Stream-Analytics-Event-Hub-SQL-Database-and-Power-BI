import json
import time
import csv
import os
import logging
from azure.eventhub import EventHubProducerClient, EventData

# Logging Configuration
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Azure Event Hub Configuration with environment variables for added security
connection_str = os.getenv('EVENT_HUB_CONNECTION_STRING')
event_hub_name = os.getenv('EVENT_HUB_NAME')

# Function to send data to Azure Event Hub
def send_data(client, events):
    try:
        event_data_batch = client.create_batch()
        for event in events:
            event_data_batch.add(EventData(json.dumps(event)))
        client.send_batch(event_data_batch)
        logger.info(f'Sent batch of {len(events)} events')
    except Exception as e:
        logger.error(f'Failed to send events: {e}')

# Function to read CSV files
def read_csv(file_path):
    try:
        with open(file_path, 'r', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                yield row
    except Exception as e:
        logger.error(f'Failed to read CSV file: {e}')
        raise

def main():

    # Checks if connection string and event hub name provided
    if not connection_str or not event_hub_name:
        logger.error('Azure Event Hub connection string and name must be set')
        return

    # CSV File path
    file_path = 'transportation.csv'

    try:
        # Client creation
        with EventHubProducerClient.from_connection_string(
            conn_str=connection_str,
            eventhub_name=event_hub_name
        ) as client:

            events_batch = []
            batch_size = 5

            for row in read_csv(file_path):
                events_batch.append(row)

                # Events sent in batches
                if len(events_batch) == batch_size:
                    send_data(client, events_batch)
                    events_batch = []
                    time.sleep(0.4)
            # Remaining events sent
            if events_batch:
                send_data(client, events_batch)

    except Exception as e:
        logger.error(f'An error has occurred: {e}')

if __name__ == '__main__':
    main()
