FROM python:3.8 
LABEL Maintainer="Matthew Clarke" 
ENV SRC_DIR /usr/bin/src/webapp/src  
COPY src/* ${SRC_DIR}/
WORKDIR ${SRC_DIR}
ENV PYTHONUNBUFFERED=1
CMD ["python", "simple_server.py"]
