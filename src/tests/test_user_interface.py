import unittest
from unittest.mock import patch
from src import user_interface

class TestUserInterface(unittest.TestCase):

    @patch('src.user_interface.upload_nft')
    def test_upload_button_click(self, mock_upload):
        user_interface.upload_button_click()
        mock_upload.assert_called_once()

    @patch('src.user_interface.validate_nft_data')
    def test_validate_nft_data(self, mock_validate):
        test_data = {
            "nft_name": "Test NFT",
            "nft_description": "This is a test NFT",
            "nft_image": "test_image.png"
        }
        user_interface.validate_nft_data(test_data)
        mock_validate.assert_called_once_with(test_data)

    @patch('src.user_interface.show_message')
    def test_show_message(self, mock_show_message):
        user_interface.show_message("upload-success")
        mock_show_message.assert_called_once_with("upload-success")

if __name__ == '__main__':
    unittest.main()