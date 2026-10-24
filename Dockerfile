FROM python:3.14-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
COPY . .
CMD ["python", "-c", "print('📦 Bodhi Storage Vault is Active!')"]
