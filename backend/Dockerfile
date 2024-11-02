# Use the official Python image from the DockerHub
FROM python:3.11-slim

# Set working directory
WORKDIR /backend

# Copy project descriptor files
COPY pyproject.toml poetry.lock /backend/

# Install Poetry
RUN pip install poetry

# Install dependencies
RUN poetry config virtualenvs.in-project true && poetry install --no-root

# Copy the entire application
COPY . /backend

# Command to run the application
CMD ["poetry", "run", "start"]
