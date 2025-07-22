FROM python:3.9-slim

WORKDIR /app
COPY . /app

RUN pip install PyPDF2 requests beautifulsoup4

CMD ["python", "file_organizer.py"]