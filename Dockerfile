# syntax=docker/dockerfile:1
FROM python:3.9.10
WORKDIR /app
COPY requirements.txt .
COPY tests/ ./tests
RUN ls | grep "tests"
RUN echo "hello there"
RUN pip3 install --no-cache-dir -r requirements.txt
CMD ["pytest -s tests"]
