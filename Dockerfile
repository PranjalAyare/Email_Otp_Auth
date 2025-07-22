FROM python:3.10
# Set work directory in container
WORKDIR /app
# Copy project files
COPY . /app
# Upgrade pip and install requirements
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# Run Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
