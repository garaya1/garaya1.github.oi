import json
from jwcrypto import jwk

# Generate RSA keypair
key = jwk.JWK.generate(kty='RSA', size=2048)

# Give the key a key ID
kid = "my-smart-key-1"
key.update(kid=kid, use="sig", alg="RS384")

# Export private key JWK if you want to store it as JWK JSON
private_jwk = key.export(private_key=True)

# Export public key JWK
public_jwk = key.export(private_key=False)

# Build JWKS
jwks = {"keys": [json.loads(public_jwk)]}

with open("private.jwk.json", "w") as f:
    f.write(private_jwk)

with open("jwks.json", "w") as f:
    json.dump(jwks, f, indent=2)

print("Created private.jwk.json and jwks.json")