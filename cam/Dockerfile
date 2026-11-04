FROM python:3.15.2-trixie

WORKDIR /kittycam

# System dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    v4l-utils \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    && rm -rf /var/lib/apt/lists/*

COPY torch-requirements.txt torch-requirements.txt 

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r torch-requirements.txt --index-url https://download.pytorch.org/whl/cpu

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]
