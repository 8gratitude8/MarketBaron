import unittest
from src.database import DATABASE, add_nft_to_database
from src.nft import NFT

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.nft = NFT(nft_id=1, user_id=1, nft_name="Test NFT", nft_description="This is a test NFT", nft_image_url="http://test.com/nft.jpg")
        self.database = DATABASE

    def test_add_nft_to_database(self):
        initial_count = len(self.database)
        add_nft_to_database(self.nft)
        self.assertEqual(len(self.database), initial_count + 1)

    def test_database_contains_added_nft(self):
        add_nft_to_database(self.nft)
        self.assertIn(self.nft, self.database)

if __name__ == '__main__':
    unittest.main()