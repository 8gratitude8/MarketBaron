import os
from src.nft import NFT
from src.database import DATABASE
from src.config import NFT_STORAGE_PATH
from src.utils import validate_nft_data

def upload_nft(user_id, nft_name, nft_description, nft_image):
    # Validate NFT data
    if not validate_nft_data(nft_name, nft_description, nft_image):
        return {"status": "error", "message": "invalid-nft-data"}

    # Create NFT instance
    nft = NFT(user_id, nft_name, nft_description, nft_image)

    # Save NFT image to storage
    nft_image_path = os.path.join(NFT_STORAGE_PATH, f"{nft.nft_id}.png")
    with open(nft_image_path, "wb") as f:
        f.write(nft_image)

    # Update NFT image URL
    nft.nft_image_url = nft_image_path

    # Add NFT to database
    DATABASE.add_nft(nft)

    return {"status": "success", "message": "upload-success", "nft_id": nft.nft_id}