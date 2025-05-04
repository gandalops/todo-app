# 🏷️ Step 1: Use official Python image
FROM python:3.9-slim

# 🏷️ Step 2: Set workdir
WORKDIR /app

# 🏷️ Step 3: Copy local app files to container
COPY app.py .

# 🏷️ Step 4: Install Python dependencies
RUN pip install --no-cache-dir flask

# Expose the port your Flask app runs on
EXPOSE 8000

# 🏷️ Step 5: Set container entry point
CMD ["python", "app.py"]
