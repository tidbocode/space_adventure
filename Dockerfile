# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the project files
COPY space_adventure/ ./space_adventure/

# Since there are no external dependencies, no pip install needed

# Command to run the game
CMD ["python", "-m", "space_adventure"]