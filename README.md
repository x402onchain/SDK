# X402 SDK

Official SDK for integrating with the X402 autonomous payment protocol on Solana.

**GitHub:** https://github.com/x402onchain/sdk

## Repository Structure

```
sdk/
├── README.md           # This file
├── ts/                 # TypeScript SDK
│   ├── index.ts        # Main exports
│   ├── client.ts       # X402Client class
│   ├── types.ts        # Type definitions
│   ├── errors.ts       # Error classes
│   ├── middleware.ts   # Express middleware
│   └── wallet.ts       # Wallet utilities
└── python/             # Python SDK
    └── x402_sdk/
        ├── __init__.py # Package exports
        ├── client.py   # X402Client class
        ├── types.py    # Type definitions
        ├── errors.py   # Error classes
        ├── middleware.py # Flask middleware
        └── wallet.py   # Wallet utilities
```

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
  baseUrl: 'https://api.x402agent.tech',
  maxPaymentPerRequest: 0.1, // Max SOL per request
});

// Make a payment-enabled request
const response = await client.request('https://api.example.com/premium-data');
console.log(response.data);

// If payment was made automatically:
if (response.paymentMade) {
  console.log(`Paid ${response.paymentMade.amount} ${response.paymentMade.currency}`);
}
```

### Python
```python
from x402_sdk import X402Client

client = X402Client(
    api_key='x402_your_api_key',
    base_url='https://api.x402agent.tech',
    max_payment_per_request=0.1
)

# Make a payment-enabled request
response = client.request('https://api.example.com/premium-data')
print(response.data)

# If payment was made automatically:
if response.payment_made:
    print(f"Paid {response.payment_made['amount']} {response.payment_made['currency']}")
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

### Client Methods

| Method | Description |
|--------|-------------|
| `request(url, options)` | Make HTTP request with automatic 402 handling |
| `verify(request)` | Verify a payment transaction |
| `createPaymentRequest(request)` | Create a new payment request |
| `getBalance(address)` | Get wallet balance |
| `getTransaction(signature)` | Get transaction details |
| `getTransactionHistory(request)` | Get transaction history |

### Error Classes

| Error | Description |
|-------|-------------|
| `X402Error` | Base error class |
| `InsufficientBalanceError` | Wallet balance too low |
| `PaymentExpiredError` | Payment window expired |
| `PaymentRejectedError` | Payment rejected by server |
| `TransactionFailedError` | Blockchain transaction failed |
| `RateLimitError` | Rate limit exceeded |
| `MaxPaymentExceededError` | Payment exceeds max allowed |

## Server Middleware

### Express (TypeScript)
```typescript
import express from 'express';
import { createX402Middleware } from '@x402/sdk';

const app = express();
const x402 = createX402Middleware({
  apiKey: process.env.X402_API_KEY,
  recipient: 'YOUR_WALLET_ADDRESS',
});

// Protect an endpoint with payment
app.get('/api/premium', x402.requirePayment(0.001), (req, res) => {
  res.json({ data: 'Premium content!' });
});
```

### Flask (Python)
```python
from flask import Flask
from x402_sdk import create_x402_middleware

app = Flask(__name__)
x402 = create_x402_middleware(
    api_key=os.environ['X402_API_KEY'],
    recipient='YOUR_WALLET_ADDRESS'
)

@app.route('/api/premium')
@x402.require_payment(0.001)
def premium_endpoint():
    return {'data': 'Premium content!'}
```

## Wallet Utilities

### TypeScript
```typescript
import { X402Wallet, isValidSolanaAddress, lamportsToSol } from '@x402/sdk';

// Create wallet from secret key
const wallet = X402Wallet.fromSecretKey(secretKeyBytes);

// Generate new wallet
const newWallet = X402Wallet.generate();

// Validate address
if (isValidSolanaAddress('7xKXtg...')) {
  console.log('Valid address');
}

// Convert units
const sol = lamportsToSol(1000000000); // 1 SOL
```

### Python
```python
from x402_sdk import X402Wallet, is_valid_solana_address, lamports_to_sol

# Create wallet from secret key
wallet = X402Wallet.from_secret_key(secret_key_bytes)

# Generate new wallet
new_wallet = X402Wallet.generate()

# Validate address
if is_valid_solana_address('7xKXtg...'):
    print('Valid address')

# Convert units
sol = lamports_to_sol(1000000000)  # 1 SOL
```

## Configuration Options

### TypeScript
```typescript
interface X402Config {
  apiKey: string;                    // Required: Your API key
  baseUrl?: string;                  // Default: 'https://api.x402agent.tech'
  network?: 'mainnet-beta' | 'devnet' | 'testnet';
  rpcUrl?: string;                   // Custom Solana RPC
  maxPaymentPerRequest?: number;     // Default: 0.1 SOL
  commitment?: 'processed' | 'confirmed' | 'finalized';
  timeout?: number;                  // Default: 30000ms
  retryAttempts?: number;            // Default: 3
  retryDelay?: number;               // Default: 1000ms
}
```

### Python
```python
X402Config(
    api_key: str,                    # Required: Your API key
    base_url: str = "https://api.x402agent.tech",
    network: str = "mainnet-beta",
    rpc_url: Optional[str] = None,
    max_payment_per_request: float = 0.1,
    commitment: str = "confirmed",
    timeout: int = 30,
    retry_attempts: int = 3,
    retry_delay: float = 1.0,
)
```

## Getting an API Key

1. Sign up at https://x402agent.tech
2. Navigate to Dashboard > API Keys
3. Create a new API key
4. Contact support@x402agent.tech for activation

## Support

- Documentation: https://x402agent.tech/docs
- GitHub: https://github.com/x402onchain/sdk
- Twitter: https://x.com/terminagent
- Email: support@x402agent.tech

## License

MIT
