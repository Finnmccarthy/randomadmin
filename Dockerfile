FROM arm64v8/python:3.9.10-slim-buster

WORKDIR /app

COPY requirments.txt requirments.txt
RUN pip3 install -r requirments.txt

COPY . .

CMD ["python3", "bot.py"]