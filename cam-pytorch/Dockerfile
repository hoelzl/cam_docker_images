FROM pytorch/pytorch:2.1.0-cuda12.1-cudnn8-devel
LABEL authors="Matthias Hölzl <matthias.hoelzl@coding-academy.com>"

COPY requirements.txt /tmp
RUN apt-get update && apt-get upgrade -y && apt-get install -y git curl && apt-get clean
RUN pip install --upgrade pip && pip install -r /tmp/requirements.txt && pip cache purge

EXPOSE 7860
EXPOSE 8000
EXPOSE 8888

WORKDIR /workspace
CMD ["/bin/bash"]
