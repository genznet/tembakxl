import json
import os
import sys

# Tambahkan path agar bisa akses folder app/
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.service.auth import AuthInstance
from app.client.engsel import get_balance

def handler(event, context):
    # Cek jika ada parameter pilihan menu (query string)
    params = event.get("queryStringParameters", {})
    choice = params.get("choice")

    try:
        active_user = AuthInstance.get_active_user()
        
        if not active_user:
            return {"statusCode": 401, "body": json.dumps({"message": "Harap Login Terlebih Dahulu"})}

        # Contoh Logika: Jika user pilih '2' (Lihat Paket)
        if choice == "2":
            # Karena fetch_my_packages() aslinya nge-print ke terminal, 
            # kamu mungkin perlu mengubah fungsi tersebut agar me-return data JSON.
            from app.menus.package import fetch_my_packages
            data = fetch_my_packages() 
            return {
                "statusCode": 200,
                "body": json.dumps({"status": "success", "data": data})
            }

        # Default respon jika hanya ingin cek profil
        balance = get_balance(AuthInstance.api_key, active_user["tokens"]["id_token"])
        return {
            "statusCode": 200,
            "body": json.dumps({
                "number": active_user["number"],
                "balance": balance.get("remaining")
            })
        }

    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
