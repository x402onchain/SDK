# X402 SDK

Official SDK for integrating with the X402 autonomous payment protocol on Solana.

## Installation

### TypeScript/JavaScript
```bash
npm install @x402/sdk
# or
yarn add @x402/sdk
```

### Python
```bash
pip install x402-sdk
```

## Quick Start

### TypeScript
```typescript
import { X402Client } from '@x402/sdk';

const client = new X402Client({
  apiKey: 'x402_your_api_key',
  baseUrl: 'https://api.x402agent.tech'
});

// Verify a payment
const result = await client.verify({
  payment: {
    amount: 0.001,
    recipient: 'YOUR_WALLET_ADDRESS',
    memo: 'API call payment'
  }
});
```

### Python
```python
from x402_sdk import X402Client

client = X402Client(
    api_key='x402_your_api_key',
    base_url='https://api.x402agent.tech'
)

# Verify a payment
result = client.verify(
    payment={
        'amount': 0.001,
        'recipient': 'YOUR_WALLET_ADDRESS',
        'memo': 'API call payment'
    }
)
```

## API Reference

### Base URL
```
https://api.x402agent.tech/api
```

### Authentication
All requests require a Bearer token:
```
Authorization: Bearer x402_your_api_key
```

### Endpoints

#### POST /api/verify
Verify a payment transaction.

**Request:**
```json
{
  "payment": {
    "amount": 0.001,
    "recipient": "RECIPIENT_WALLET",
    "memo": "optional memo"
  }
}
```

**Response:**
```json
{
  "verified": true,
  "timestamp": "2026-01-04T12:00:00.000Z",
  "payment": {
    "amount": 0.001,
    "recipient": "RECIPIENT_WALLET",
    "memo": "optional memo"
  }
}
```

## Features

- Automatic 402 response handling
- Solana transaction signing
- Request retry logic
- Usage tracking
- Rate limiting support

## Getting an API Key

1. Sign up at https://x402agent.tech
2. Navigate to Dashboard > API Keys
3. Create a new API key
4. Contact support@x402agent.tech for activation

## Repository Structure

```
sdk/
├── README.md    # This file
├── ts/          # TypeScript SDK
└── python/      # Python SDK
```

## Support

- Documentation: https://x402agent.tech/docs
- GitHub: https://github.com/x402onchain/sdk
- Twitter: https://x.com/terminagent
- Email: support@x402agent.tech

## License

MIT
