import paho.mqtt.client as mqtt
from image_processor import process_and_save_image
from database import image_collection
from config import MQTT_BROKER, MQTT_PORT, MQTT_TOPIC

def on_message(client, userdata, msg):
    image_data = msg.payload.decode()
    image_id = process_and_save_image(image_data)
    
    # Salvează metadatele în MongoDB
    image_collection.insert_one({"image_id": image_id, "url": f"http://localhost:9000/images/{image_id}"})
    print(f"Saved image: {image_id}")

mqtt_client = mqtt.Client()
mqtt_client.on_message = on_message
mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
mqtt_client.subscribe(MQTT_TOPIC)
mqtt_client.loop_start()
