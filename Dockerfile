FROM python:3.10-slim
WORKDIR /app
COPY agent.py /app/agent.py
RUN pip install --no-cache-dir anthropic
CMD ["python", "agent.py"]
