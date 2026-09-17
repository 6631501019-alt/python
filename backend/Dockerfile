FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y openssh-client && rm -rf /var/lib/apt/lists/*
RUN mkdir -p /root/.ssh && printf "Host *\n   KexAlgorithms +diffie-hellman-group14-sha1,diffie-hellman-group1-sha1\n   HostkeyAlgorithms +ssh-rsa\n   Ciphers +aes128-cbc,3des-cbc\n   StrictHostKeyChecking no\n" > /root/.ssh/config

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]
