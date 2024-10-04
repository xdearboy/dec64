import base64


class Base64Decoder:
    @staticmethod
    def is_base64(s):
        try:
            return base64.b64decode(s, validate=True)
        except Exception:
            return False

    @staticmethod
    def decode_base64(data):
        try:
            return base64.b64decode(data).decode("utf-8")
        except (base64.binascii.Error, UnicodeDecodeError) as e:
            print(f"Error: {e}")
            return None

    @classmethod
    def decode_until_end(cls, encoded_str):
        decoded_str = encoded_str
        while cls.is_base64(decoded_str):
            decoded_str = cls.decode_base64(decoded_str)
            if decoded_str is None:
                break
        return decoded_str
