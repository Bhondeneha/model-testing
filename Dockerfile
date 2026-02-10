FROM python:3.11-slim
RUN pip install --no-cache-dir fastapi uvicorn
COPY ./main.py /usr/local/src/
WORKDIR /usr/local/src
ENTRYPOINT ["python", "./main.py"]