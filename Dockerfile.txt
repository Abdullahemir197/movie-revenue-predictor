FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all project files into the container
COPY . .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install -r movie_api/requirements.txt

# Expose FastAPI and Streamlit ports
EXPOSE 8000
EXPOSE 8501

# Default command (runs FastAPI)
CMD ["uvicorn", "movie_api.main:app", "--host", "0.0.0.0", "--port", "8000"]
