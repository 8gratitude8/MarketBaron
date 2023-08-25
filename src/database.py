```python
import sqlite3
from src.config import DATABASE_URI
from src.nft import NFT

class Database:
    def __init__(self):
        self.connection = sqlite3.connect(DATABASE_URI)
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS nfts (
                nft_id INTEGER PRIMARY KEY,
                user_id INTEGER,
                nft_name TEXT,
                nft_description TEXT,
                nft_image_url TEXT
            )
        """)
        self.connection.commit()

    def add_nft(self, nft: NFT):
        self.cursor.execute("""
            INSERT INTO nfts (user_id, nft_name, nft_description, nft_image_url)
            VALUES (?, ?, ?, ?)
        """, (nft.user_id, nft.nft_name, nft.nft_description, nft.nft_image_url))
        self.connection.commit()

    def get_nft(self, nft_id: int):
        self.cursor.execute("""
            SELECT * FROM nfts WHERE nft_id = ?
        """, (nft_id,))
        return self.cursor.fetchone()

DATABASE = Database()
```