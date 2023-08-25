import os
from flask import Flask, request, jsonify
from src.user_interface import upload_nft
from src.config import DATABASE_URI, NFT_STORAGE_PATH
from src.database import DATABASE
from src.nft import NFT

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    nft_data = request.get_json()
    response = upload_nft(nft_data)
    return jsonify(response)

@app.route('/nfts', methods=['GET'])
def get_nfts():
    nfts = DATABASE.get_all(NFT)
    return jsonify(nfts)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.getenv('PORT', 5000))