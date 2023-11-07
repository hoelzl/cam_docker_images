FROM condaforge/mambaforge:latest
LABEL authors="Matthias Hölzl <matthias.hoelzl@coding-academy.com>"

COPY requirements.txt /tmp
RUN apt-get update &&\
    apt-get upgrade -y &&\
    apt-get install -y build-essential ca-certificates sshd git curl &&\
    apt-get clean
RUN pip install --upgrade pip && pip install -r /tmp/requirements.txt && pip cache purge

EXPOSE 8000
EXPOSE 8888

WORKDIR /workspace
CMD ["/bin/bash"]
