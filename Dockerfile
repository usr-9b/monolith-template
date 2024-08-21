FROM python:bullseye

RUN apt-get update -y
RUN apt-get upgrade -y
RUN pip install pip -U

WORKDIR /src
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD alembic -c /src/alembic.ini upgrade head && python /src/main.py