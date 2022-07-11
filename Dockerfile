FROM python:3.6-slim
WORKDIR /usr/src/app
COPY src/ .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "app.py"]
EXPOSE 5000
