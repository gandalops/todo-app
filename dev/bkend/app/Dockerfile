# 🏷️ Step 1: Use official Python image
FROM python:3.10-alpine

# 🏷️ Step 2: Set workdir
WORKDIR /app

# 🏷️ Step 3: Copy local app files to container
COPY . .

# 🏷️ Step 4: Install Python dependencies
RUN pip install -r requirements.txt

# 🏷️ Step 5: Set container entry point
CMD ["python", "app.py"]
