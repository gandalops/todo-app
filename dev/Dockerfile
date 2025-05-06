# 🏷️ Step 1: Use official Python base image
FROM python:3.11-slim

# 🏷️ Step 2: Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 🏷️ Step 3: Set working directory inside container
WORKDIR /app

# 🏷️ Step 4: Copy dependency file separately for caching
COPY requirements.txt .

# 🏷️ Step 5: Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 🏷️ Step 6: Copy application code and required folders
COPY app.py .
COPY bkend/ bkend/
COPY ftend/templates/ templates/
COPY ftend/static/ static/

# 🏷️ Step 7: Expose the port your Flask app uses
EXPOSE 8000

# 🏷️ Step 8: Run the app
CMD ["python", "app.py"]
