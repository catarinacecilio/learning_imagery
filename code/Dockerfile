FROM python:3.8.12-buster

WORKDIR /code

# libraries required by OpenCV
RUN apt-get update
RUN apt-get install \
  'ffmpeg'\
  'libsm6'\
  'libxext6'  -y

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# You can add --port $PORT if you need to set PORT as a specific env variable
CMD uvicorn backend/fast_api.api:app --host 0.0.0.0 --port 8000
