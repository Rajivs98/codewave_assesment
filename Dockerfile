FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /app
ENV FLASK_APP=wsgi.py
EXPOSE 5000
CMD ["waitress-serve","--host=0.0.0.0", "--port=5000", "--call" "app:create_app"]

