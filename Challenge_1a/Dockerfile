FROM --platform=linux/amd64 python:3.10-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src
COPY sample_dataset/ ./sample_dataset
COPY process_pdfs.py ./process_pdfs.py

CMD ["python", "src/main.py"]
