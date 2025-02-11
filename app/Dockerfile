FROM tiangolo/uvicorn-gunicorn:python3.11

# Set the working directory in the container
WORKDIR /app

LABEL maintainer="Sebastian Ramirez <tiangolo@gmail.com>"

# Copy the application files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Start FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
