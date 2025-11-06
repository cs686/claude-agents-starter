# claude-agents-starter

Starter repository for building Claude agents with a minimal agent script and Dockerfile.

## Overview

This repository contains a minimal example of how to call Anthropic’s Claude models via the Python SDK. The `agent.py` script loads your API key from the `ANTHROPIC_API_KEY` environment variable and sends a simple greeting to Claude. A lightweight Dockerfile is included to containerize the agent and make it easy to run in isolated environments.

## Prerequisites

- Python 3.10+ (only needed when running directly without Docker)
- An Anthropic API key (set it in your shell as `ANTHROPIC_API_KEY`)
- Docker (optional) if you prefer to run the agent in a container

## Running the agent locally

1. Clone this repository and install dependencies:

   ```bash
   git clone https://github.com/cs686/claude-agents-starter.git
   cd claude-agents-starter
   pip install anthropic
   ```

2. Export your API key:

   ```bash
   export ANTHROPIC_API_KEY=sk-your-key
   ```

3. Run the agent script:

   ```bash
   python agent.py
   ```

The script will call Claude and print the response.

## Running with Docker

To run the agent inside a container, build the image and pass your API key as an environment variable:

```bash
docker build -t claude-agent .
docker run --rm -e ANTHROPIC_API_KEY=sk-your-key claude-agent
```

The Dockerfile uses a slim Python base image and installs the required SDK.

## Extending the agent

Anthropic’s agent skills are folders with instructions, scripts, and resources that teach Claude to perform specialized tasks. Skills are designed to be composable and portable, making it easy to build more sophisticated agents. To extend this starter project, create your own skill modules and modify `agent.py` to load and use them.
