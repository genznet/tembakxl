# netlify/functions/api.py
import json
import main  # Ini akan mengimpor logika dari main.py kamu

def handler(event, context):
    # Panggil fungsi utama dari main.py di sini
    # Contoh: hasil = main.eksekusi_tembak()
    
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Script XL Berhasil Dijalankan!"})
    }
