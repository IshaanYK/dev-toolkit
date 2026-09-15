"""
Secure hashing, token generation, and constant-time comparison helpers.
"""

import hashlib
import secrets
import hmac

def generate_secure_token(nbytes: int = 32) -> str:
    """Generates a cryptographically secure random hexadecimal token."""
    return secrets.token_hex(nbytes)

def compute_sha256(data: str) -> str:
    """Computes hex SHA-256 digest of input UTF-8 string."""
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def secure_compare(val_a: str, val_b: str) -> bool:
    """Constant-time string comparison to mitigate timing side-channel attacks."""
    return hmac.compare_digest(val_a.encode('utf-8'), val_b.encode('utf-8'))
