"""
Unit tests for developer utilities.
"""

import unittest
from dev_toolkit.string_utils import slugify, camel_to_snake, snake_to_camel
from dev_toolkit.crypto_helpers import compute_sha256, secure_compare, generate_secure_token
from dev_toolkit.rate_limiter import TokenBucket

class TestDevToolkit(unittest.TestCase):
    def test_strings(self):
        self.assertEqual(slugify("Hello World! 2026"), "hello-world-2026")
        self.assertEqual(camel_to_snake("userDataPayload"), "user_data_payload")
        self.assertEqual(snake_to_camel("user_data_payload"), "userDataPayload")

    def test_crypto(self):
        token = generate_secure_token(16)
        self.assertEqual(len(token), 32)
        digest = compute_sha256("test")
        self.assertTrue(secure_compare(digest, compute_sha256("test")))

    def test_rate_limiter(self):
        bucket = TokenBucket(capacity=2, refill_rate=1.0)
        self.assertTrue(bucket.consume(1))
        self.assertTrue(bucket.consume(1))
        self.assertFalse(bucket.consume(1))

if __name__ == '__main__':
    unittest.main()
