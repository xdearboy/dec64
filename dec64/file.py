import base64
import argparse
import sys
from .Base64Decoder import Base64Decoder


class File:
    def read_from_file(self, file_path):
        with open(file_path, "r") as file:
            return file.read()


class DecoderApp:
    def __init__(self):
        self.decoder = Base64Decoder()
        self.file_work = File()

    def decode_from_file(self, file_path):
        encoded_str = self.file_work.read_from_file(file_path)
        return self.decoder.decode_until_end(encoded_str)

    def decode_from_text(self, encoded_text):
        return self.decoder.decode_until_end(encoded_text)

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
                  Usage: dec64.py [-h] [-f File.txt] [-t Text] [-o Output.txt]


                  Recursively decode Base64 encoded strings.


                  Available options:
      -h Sends you this help.
      -f FILE, --file The path to the file
      -t ТЕКСТ, --text  Text to decode
      -o РЕЗУЛЬТАТ, --output  The path to the result file.
            """)
            sys.exit(1)

        print("Decoded text:", decoded_text)


def main():
    app = DecoderApp()
    app.run()


if __name__ == "__main__":
    main()
