FROM python:3.11-alpine3.18
WORKDIR /app
COPY requirements.txt requirements.txt
# RUN pip install -r requirements.txt
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt

COPY . /app
# CMD python ./app.py
ENV FLASK_APP=wsgi.py
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]
# CMD ["waitress-serve","--host=0.0.0.0", "--port=5050", "--call" "app:create_app"]


# FROM python:3-alpine3.15
# WORKDIR /app
# COPY requirements.txt requirements.txt
# RUN pip install -r requirements.txt
# COPY . /app
# # Set the WSGI entry point
# ENV FLASK_APP=wsgi.py
# # Expose the port on which your Flask app runs
# EXPOSE 5000
# Command to run the application using gunicorn (replace "your_app_module" with the actual module containing your app)
# CMD ["waitress-serve", "--host=0.0.0.0", "--port=5000", "your_app_module:app"]
# CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]



FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /app
ENV FLASK_APP=wsgi.py
EXPOSE 5000
CMD ["waitress-serve","--host=0.0.0.0", "--port=5000", "--call" "app:create_app"]

