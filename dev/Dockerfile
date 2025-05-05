# 🏷️ Step 1: Use official Python base image
FROM python:3.11-slim

# 🏷️ Step 2: Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 🏷️ Step 3: Set workdir
WORKDIR /app

# 🏷️ Step 4.1: Copy dependency file first for better caching
COPY requirements.txt .

# 🏷️ Step 5:  Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 🏷️ Step 4.2: Copy the rest of the application
COPY . .               

#🏷️ Step 6: Expose the port your Flask app runs on
EXPOSE 8000

# 🏷️ Step 7: Default command to run the Flask app
CMD ["python", "app.py"]
