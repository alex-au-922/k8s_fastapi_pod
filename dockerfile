FROM python:3.12-alpine as builder
COPY backend/requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

FROM python:3.12-alpine as runtime
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY backend/src /app
WORKDIR /app
RUN adduser -D myuser
USER myuser
ARG PORT=8080
EXPOSE ${PORT}
CMD uvicorn app:app --host 0.0.0.0 --port ${PORT}