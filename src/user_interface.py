import tkinter as tk
from tkinter import filedialog
from src.nft_upload import upload_nft

class UserInterface:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("NFT Upload Platform")

        self.nft_name_input = tk.Entry(self.window)
        self.nft_name_input.pack()

        self.nft_description_input = tk.Entry(self.window)
        self.nft_description_input.pack()

        self.upload_button = tk.Button(self.window, text="Upload NFT", command=self.upload_nft)
        self.upload_button.pack()

    def upload_nft(self):
        nft_name = self.nft_name_input.get()
        nft_description = self.nft_description_input.get()

        nft_image_path = filedialog.askopenfilename()

        if not nft_name or not nft_description or not nft_image_path:
            self.show_message("invalid-nft-data")
            return

        success = upload_nft(nft_name, nft_description, nft_image_path)

        if success:
            self.show_message("upload-success")
        else:
            self.show_message("upload-failure")

    def show_message(self, message_name):
        message = tk.Label(self.window, text=message_name)
        message.pack()

if __name__ == "__main__":
    ui = UserInterface()
    ui.window.mainloop()