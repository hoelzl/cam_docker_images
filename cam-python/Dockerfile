FROM python:3.11
LABEL authors="Matthias Hölzl <matthias.hoelzl@coding-academy.com>"

COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt && pip cache purge

EXPOSE 8000
EXPOSE 8888

WORKDIR /workspace
CMD ["/bin/bash"]
