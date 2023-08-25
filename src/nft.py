```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class NFT(Base):
    __tablename__ = 'nfts'

    nft_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    nft_name = Column(String(100), nullable=False)
    nft_description = Column(String(500), nullable=True)
    nft_image_url = Column(String(500), nullable=False)

    def __init__(self, user_id, nft_name, nft_description, nft_image_url):
        self.user_id = user_id
        self.nft_name = nft_name
        self.nft_description = nft_description
        self.nft_image_url = nft_image_url
```