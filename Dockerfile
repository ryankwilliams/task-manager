FROM registry.access.redhat.com/ubi9/python-311:latest
ARG APP_DIR=/opt/app-root/src
ARG APP_PORT=9090
ENV APP_PORT=$APP_PORT
COPY . $APP_DIR
RUN pip install --no-cache-dir .
WORKDIR $APP_DIR
CMD  uvicorn app.main:app --host 0.0.0.0 --port $APP_PORT --workers 1
