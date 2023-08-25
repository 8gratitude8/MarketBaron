import unittest
from src.nft import NFT, validate_nft_data

class TestNFT(unittest.TestCase):

    def setUp(self):
        self.nft_data = {
            'nft_id': '1',
            'user_id': '1',
            'nft_name': 'Test NFT',
            'nft_description': 'This is a test NFT',
            'nft_image_url': 'http://test.com/nft.jpg'
        }
        self.nft = NFT(self.nft_data)

    def test_nft_creation(self):
        self.assertEqual(self.nft.nft_id, '1')
        self.assertEqual(self.nft.user_id, '1')
        self.assertEqual(self.nft.nft_name, 'Test NFT')
        self.assertEqual(self.nft.nft_description, 'This is a test NFT')
        self.assertEqual(self.nft.nft_image_url, 'http://test.com/nft.jpg')

    def test_validate_nft_data(self):
        self.assertTrue(validate_nft_data(self.nft_data))

        invalid_nft_data = self.nft_data.copy()
        invalid_nft_data['nft_name'] = ''
        self.assertFalse(validate_nft_data(invalid_nft_data))

if __name__ == '__main__':
    unittest.main()