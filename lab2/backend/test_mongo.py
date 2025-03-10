from pymongo import MongoClient

# Replace with your actual connection string
MONGO_URI = "mongodb+srv://emiliabiancaserban:XpChUCifAGBwkpjZ@cluster0.6a0xw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DATABASE_NAME = "clusters"

try:
    client = MongoClient(MONGO_URI)
    db = client[DATABASE_NAME]

    # Check server info
    server_info = client.server_info()
    print(f"✅ Successfully connected to MongoDB: {server_info['version']}")

    # List databases (to verify connection)
    print("📂 Databases:", client.list_database_names())

except Exception as e:
    print(f"❌ Connection failed: {e}")
