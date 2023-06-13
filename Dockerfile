# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the source code to the working directory
COPY . .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the environment variable
ENV OPENAI_API_KEY sk-your-openai-api-key

# Run the command to start the Streamlit application
CMD ["streamlit", "run", "app.py"]
