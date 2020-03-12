FROM mtgupf/essentia

MAINTAINER ykhorizon "ykhorizon.light@gmail.com"

# update system package
RUN apt-get update -y && apt-get -y install python3-pip ffmpeg
COPY . /solola
COPY requirements.txt /solola/requirements.txt

WORKDIR /solola
# RUN pip3 install -r requirements.txt

COPY prerequisites.sh /solola/prerequisites.sh
RUN sh prerequisites.sh

# run server
EXPOSE 5000
# CMD ["python3", "service/service.py"]