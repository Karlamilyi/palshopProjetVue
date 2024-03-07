FROM python:3.8-alpine

# Set the working directory in the container
WORKDIR /backend

# Copy the current directory contents into the container at /backend
COPY . /backend

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Start the application
CMD ["python", "app.py"]
