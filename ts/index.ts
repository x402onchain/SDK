interface X402Config {
  apiKey: string;
  baseUrl?: string;
}

interface PaymentRequest {
  payment: {
    amount: number;
    recipient: string;
    memo?: string;
  };
}

interface VerifyResponse {
  verified: boolean;
  timestamp: string;
  payment: {
    amount: number;
    recipient: string;
    memo?: string;
  };
}

export class X402Client {
  private apiKey: string;
  private baseUrl: string;

  constructor(config: X402Config) {
    this.apiKey = config.apiKey;
    this.baseUrl = config.baseUrl || 'https://api.x402agent.tech';
  }

  async verify(request: PaymentRequest): Promise<VerifyResponse> {
    const response = await fetch(`${this.baseUrl}/api/verify`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${this.apiKey}`,
      },
      body: JSON.stringify(request),
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.error || 'Request failed');
    }

    return response.json();
  }

  async handle402(response: Response): Promise<{ amount: number; recipient: string }> {
    if (response.status !== 402) {
      throw new Error('Response is not a 402 Payment Required');
    }

    const amount = parseFloat(response.headers.get('X-402-Amount') || '0');
    const recipient = response.headers.get('X-402-Recipient') || '';

    if (!amount || !recipient) {
      throw new Error('Invalid 402 response headers');
    }

    return { amount, recipient };
  }
}

export default X402Client;
