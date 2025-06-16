import argparse
import base64
from .Base64Decoder import Base64Decoder


class File:
    pass


class Dec64App:
    def __init__(self):
        self.decoder = Base64Decoder()

    def decode_from_file(self, file_path):
        encoded_str = self.read_from_file(file_path)
        return self.decoder.decode_until_end(encoded_str)

    def decode_from_text(self, encoded_text):
        return self.decoder.decode_until_end(encoded_text)

    def read_from_file(self, file_path):
        with open(file_path, "r") as file:
            return file.read()

    def run(self):
        parser = argparse.ArgumentParser(description="Decode base64 encoded text.")
        parser.add_argument("-f", "--file")
        parser.add_argument("-t", "--text")
        args = parser.parse_args()

        if args.file:
            decoded_text = self.decode_from_file(args.file)
        elif args.text:
            decoded_text = self.decode_from_text(args.text)
        else:
            print("Error: No input file or text provided.")
            print("""
                  Usage: dec64.py [-h] [-f File.txt] [-t Text]


                  Recursively decode Base64 encoded strings.


                  Available options:
      -h Sends you this help.
      -f FILE, --file The path to the file
      -t TEXT, --text  Text to decode
            """)
            exit(1)

        print("Decoded text:", decoded_text)


def main():
    app = Dec64App()
    app.run()


if __name__ == "__main__":
    main()
