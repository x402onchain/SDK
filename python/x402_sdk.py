"""
X402 SDK for Python
Autonomous payment protocol integration for AI agents.
"""

import requests
from typing import Optional, Dict, Any


class X402Client:
    """Client for interacting with the X402 payment protocol API."""
    
    def __init__(self, api_key: str, base_url: str = "https://api.x402agent.tech"):
        """
        Initialize the X402 client.
        
        Args:
            api_key: Your X402 API key (starts with x402_)
            base_url: Base URL for the API (default: https://api.x402agent.tech)
        """
        self.api_key = api_key
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        })
    
    def verify(self, payment: Dict[str, Any]) -> Dict[str, Any]:
        """
        Verify a payment transaction.
        
        Args:
            payment: Payment details including amount, recipient, and optional memo
            
        Returns:
            Verification response with status and timestamp
            
        Example:
            result = client.verify({
                'amount': 0.001,
                'recipient': 'WALLET_ADDRESS',
                'memo': 'API payment'
            })
        """
        response = self.session.post(
            f'{self.base_url}/api/verify',
            json={'payment': payment}
        )
        
        if not response.ok:
            error = response.json()
            raise Exception(error.get('error', 'Request failed'))
        
        return response.json()
    
    def handle_402(self, response: requests.Response) -> Dict[str, Any]:
        """
        Parse a 402 Payment Required response.
        
        Args:
            response: The HTTP response with 402 status
            
        Returns:
            Payment requirements (amount, recipient)
        """
        if response.status_code != 402:
            raise ValueError('Response is not a 402 Payment Required')
        
        amount = float(response.headers.get('X-402-Amount', 0))
        recipient = response.headers.get('X-402-Recipient', '')
        
        if not amount or not recipient:
            raise ValueError('Invalid 402 response headers')
        
        return {
            'amount': amount,
            'recipient': recipient
        }


def create_client(api_key: str, base_url: Optional[str] = None) -> X402Client:
    """
    Factory function to create an X402 client.
    
    Args:
        api_key: Your X402 API key
        base_url: Optional custom base URL
        
    Returns:
        Configured X402Client instance
    """
    return X402Client(
        api_key=api_key,
        base_url=base_url or "https://api.x402agent.tech"
    )
