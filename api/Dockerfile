# Use the official Python image as a parent image
FROM python:3.8

# Set the working directory in the container to /api
WORKDIR /api

# Copy the requirements file into the container at /api
COPY ./requirements.txt /api/requirements.txt

# Install any dependencies
RUN pip install --no-cache-dir --upgrade -r /api/requirements.txt

# Copy the current directory contents into the container at /api
COPY . /api

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
