FROM ubuntu

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y python3 python3-pip unzip python3-opencv
RUN pip3 install scikit-learn numpy tqdm tensorflow keras matplotlib opencv-python pandas

# Set the working directory
WORKDIR /work

# Add the data
ADD https://www.itec.aau.at/~narges/data.zip /work
RUN unzip data.zip

# Add python-script
COPY Traffic_sign_classification-checkpoint-lowaccuracy.py /work

ENTRYPOINT ["python3", "Traffic_sign_classification-checkpoint-lowaccuracy.py"]
