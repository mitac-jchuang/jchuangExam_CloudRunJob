# Use the official Python base image
FROM python:3.11-slim

# Define a build-time argument. This can be set with --build-arg
ARG PROJECT_ID
ARG BRONZE_BUCKET

# Set the working directory inside the container
WORKDIR /app
RUN mkdir /env
# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the application code to the working directory
COPY . .

# Expose the port on which the application will run
EXPOSE 8080

# Define environment variable
ENV PROJECT_ID=$PROJECT_ID
ENV BRONZE_BUCKET=$BRONZE_BUCKET

# Run the FastAPI application using uvicorn server
#CMD ["python", "main.py"]
ENTRYPOINT ["python", "main.py"]