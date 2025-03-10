from PIL import Image
import io
import base64
import uuid
from minio import Minio
from config import MINIO_ENDPOINT, MINIO_ACCESS_KEY, MINIO_SECRET_KEY, MINIO_BUCKET

# Conectare la MinIO
minio_client = Minio(
    MINIO_ENDPOINT,
    access_key=MINIO_ACCESS_KEY,
    secret_key=MINIO_SECRET_KEY,
    secure=False
)

# Asigură existența bucket-ului
if not minio_client.bucket_exists(MINIO_BUCKET):
    minio_client.make_bucket(MINIO_BUCKET)

def process_and_save_image(image_data):
    """Procesează și salvează imaginea"""
    image = Image.open(io.BytesIO(base64.b64decode(image_data)))
    image = image.resize((300, 300))  # Redimensionare
    buffer = io.BytesIO()
    image.save(buffer, format="JPEG")
    buffer.seek(0)

    image_id = f"{uuid.uuid4()}.jpg"
    minio_client.put_object(MINIO_BUCKET, image_id, buffer, len(buffer.getvalue()), content_type="image/jpeg")
    
    return image_id
