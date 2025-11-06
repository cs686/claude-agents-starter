#!/usr/bin/env python3

import os
import anthropic

def main():
    """
    Minimal Claude agent using the Anthropic Python SDK.
    Retrieves the API key from the ANTHROPIC_API_KEY environment variable and
    sends a simple greeting message to Claude.
    """
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("Please set the ANTHROPIC_API_KEY environment variable")

    client = anthropic.Anthropic(api_key=api_key)
    response = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=128,
        messages=[{"role": "user", "content": "Hello, Claude!"}],
    )
    print(response.content)

if __name__ == "__main__":
    main()
