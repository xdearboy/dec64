import base64
import binascii


def is_base64(s):
    try:
        base64.b64decode(s, validate=True)
        return True
    except (ValueError, binascii.Error):
        return False


def decode_base64(data):
    try:
        decoded = base64.b64decode(data).decode("utf-8")
        return decoded
    except (binascii.Error, UnicodeDecodeError):
        return None

class Base64Decoder:
    @classmethod
    def decode_until_end(cls, encoded_str):
        decoded_str = encoded_str
        last_decoded = ""
        while is_base64(decoded_str) and decoded_str != last_decoded:
            last_decoded = decoded_str
            decoded_str = decode_base64(decoded_str)
            if decoded_str is None:
                return last_decoded
        return decoded_str
