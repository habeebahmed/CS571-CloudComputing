# Use an official Python image as the base image
FROM python:3.8-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the contents of the local directory to the container's /app directory
COPY . /app

# Install required packages from requirements.txt file
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for the application to listen on
EXPOSE 9000

ENTRYPOINT ["python"]

CMD ["ZipCodeService.py"]

# Run the command to start the application
# CMD ["python", "ServerOne.py"]