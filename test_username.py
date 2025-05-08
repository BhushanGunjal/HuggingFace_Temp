import os
from dotenv import load_dotenv
import requests

load_dotenv()
token = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")

print("🔍 Token prefix in use:", token[:10] if token else "None")

# Who owns this token?
headers = {"Authorization": f"Bearer {token}"}
resp = requests.get("https://huggingface.co/api/whoami-v2", headers=headers)
if resp.ok:
    print("✅ This token belongs to:", resp.json()["name"])
else:
    print("❌ Invalid or unauthorized token")
    print("Response:", resp.text)
    exit(1)
