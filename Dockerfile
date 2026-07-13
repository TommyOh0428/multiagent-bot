FROM cgr.dev/chainguard/python:latest-dev AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN python -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


FROM cgr.dev/chainguard/python:latest

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/app/venv/bin:$PATH" \
    PORT=8080

WORKDIR /app

COPY --from=builder /app/venv /app/venv
COPY agents ./agents
COPY main.py .

EXPOSE 8080

ENTRYPOINT ["/app/venv/bin/python", "-m", "uvicorn"]
CMD ["main:app", "--host", "0.0.0.0", "--port", "8080"]
