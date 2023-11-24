from Crypto.PublicKey import ECC
from Crypto.Hash import TupleHash128
from Crypto.Random import get_random_bytes
from Crypto.Protocol.DH import key_agreement

SESSION_SALT = get_random_bytes(16)

# Alice
alice_id = get_random_bytes(16)
alice_private_key = ECC.generate(curve='p256')
alice_ephemeral_private_key = ECC.generate(curve='p256')

# Bob
bob_id = get_random_bytes(16)
bob_public_key = ECC.generate(curve='p256').public_key()
bob_ephemeral_public_key = ECC.generate(curve='p256').public_key()

# Key derivation function
def kdf(x):
  h = TupleHash128.new(digest_bytes=32)
  h.update(
    x,
    SESSION_SALT,
    alice_id,
    bob_id,
    b'Generic encryption',
    b'TupleHash128',
    b'AES256'
  )
  return h.digest()

# Generazione chiave di sessione (AES-256)
session_key = key_agreement(
  static_priv=alice_private_key,
  static_pub=bob_public_key,
  eph_priv=alice_ephemeral_private_key,
  eph_pub=bob_ephemeral_public_key,
  kdf=kdf
)

print(session_key)
