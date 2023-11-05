FROM python:3.11-slim-bookworm
LABEL authors="Matthias Hölzl <matthias.hoelzl@coding-academy.com>"

COPY requirements.txt /tmp
RUN apt-get update && apt-get upgrade -y && apt-get install -y git && apt-get clean
RUN pip install -r /tmp/requirements.txt && pip cache purge

EXPOSE 8000
EXPOSE 8888

WORKDIR /workspace
CMD ["/bin/bash"]
