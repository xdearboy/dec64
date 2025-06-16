import unittest
from ..Base64Decoder import Base64Decoder, decode_base64, is_base64


class TestBase64Decoder(unittest.TestCase):
    def test_is_base64(self):
        self.assertTrue(is_base64("ZGVjNjQ="))
        self.assertFalse(is_base64("not base64"))

    def test_decode_base64(self):
        decoded_string = decode_base64("ZGVjNjQ=")
        print(f"Decoded string: {decoded_string}")
        self.assertEqual(decoded_string, "dec64")
        self.assertIsNone(decode_base64("not base64"))

    def test_decode_until_end(self):
        decoder = Base64Decoder()
        self.assertEqual(decoder.decode_until_end("ZGVjNjQ="), "dec64")