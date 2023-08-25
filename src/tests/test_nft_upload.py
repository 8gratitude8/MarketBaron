import unittest
from src.nft_upload import upload_nft, validate_nft_data
from src.nft import NFT

class TestNFTUpload(unittest.TestCase):

    def setUp(self):
        self.valid_nft_data = {
            'nft_id': '1',
            'user_id': '1',
            'nft_name': 'Test NFT',
            'nft_description': 'This is a test NFT',
            'nft_image_url': 'http://test.com/test.jpg'
        }
        self.invalid_nft_data = {
            'nft_id': '1',
            'user_id': '1',
            'nft_name': '',
            'nft_description': 'This is a test NFT',
            'nft_image_url': 'http://test.com/test.jpg'
        }

    def test_validate_nft_data(self):
        self.assertTrue(validate_nft_data(self.valid_nft_data))
        self.assertFalse(validate_nft_data(self.invalid_nft_data))

    def test_upload_nft(self):
        self.assertEqual(upload_nft(self.valid_nft_data), "upload-success")
        self.assertEqual(upload_nft(self.invalid_nft_data), "invalid-nft-data")

if __name__ == '__main__':
    unittest.main()