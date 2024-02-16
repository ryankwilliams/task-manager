FROM registry.access.redhat.com/ubi9/python-311:latest
ARG APP_DIR=/opt/app-root/src
COPY . ${APP_DIR}
RUN pip install --no-cache-dir .
WORKDIR $APP_DIR
CMD  uvicorn app.main:app --host 0.0.0.0 --port 8080 --workers 1
