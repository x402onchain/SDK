# X402 SDK for Python

Official Python SDK for integrating with the X402 autonomous payment protocol on Solana.

## Installation

```bash
pip install x402-sdk
```

With Flask middleware support:
```bash
pip install x402-sdk[flask]
```

With Solana wallet support:
```bash
pip install x402-sdk[solana]
```

## Quick Start

```python
from x402_sdk import X402Client

client = X402Client(
    api_key='x402_your_api_key',
    base_url='https://api.x402agent.tech',
    max_payment_per_request=0.1  # Max SOL per request
)

# Make a payment-enabled request
response = client.request('https://api.example.com/premium-data')
print(response.data)

# If payment was made automatically:
if response.payment_made:
    print(f"Paid {response.payment_made['amount']} {response.payment_made['currency']}")
```

## Flask Middleware

```python
from flask import Flask
from x402_sdk import create_x402_middleware

app = Flask(__name__)
x402 = create_x402_middleware(
    api_key='x402_your_api_key',
    recipient='YOUR_SOLANA_WALLET_ADDRESS'
)

@app.route('/api/premium')
@x402.require_payment(0.001)  # 0.001 SOL
def premium_endpoint():
    return {'data': 'Premium content!'}
```

## Documentation

Full documentation: https://x402agent.tech/docs

## Support

- GitHub: https://github.com/x402onchain/sdk
- Email: support@x402agent.tech

## License

MIT
