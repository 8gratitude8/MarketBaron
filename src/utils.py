import os
from src.config import NFT_STORAGE_PATH
from src.nft import NFT

def validate_nft_data(nft_data):
    required_fields = ['nft_id', 'user_id', 'nft_name', 'nft_description', 'nft_image_url']
    return all(field in nft_data for field in required_fields)

def save_nft_image(nft_id, image_data):
    image_path = os.path.join(NFT_STORAGE_PATH, f'{nft_id}.png')
    with open(image_path, 'wb') as image_file:
        image_file.write(image_data)
    return image_path

def create_nft_object(nft_data):
    if not validate_nft_data(nft_data):
        raise ValueError("Invalid NFT data")
    nft_image_path = save_nft_image(nft_data['nft_id'], nft_data['nft_image_url'])
    return NFT(nft_data['nft_id'], nft_data['user_id'], nft_data['nft_name'], nft_data['nft_description'], nft_image_path)