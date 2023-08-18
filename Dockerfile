# Use the nemo base image
FROM nvcr.io/nvidia/nemo:23.06
LABEL Name=cognosis Version=0.0.1
# docker run --runtime=nvidia -it --rm \
#   -v \
#   --shm-size=16g \
#   -p 8888:8888 \
#   -p 6006:6006 \
#   --ulimit memlock=-1 \
#   --ulimit stack=67108864 \
#   nvcr.io/nvidia/nemo:23.06 
# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .
# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Copy the Python code to the container
COPY . .
# Set the environment variable
# ARG LANGCHAIN_API_KEY
# ENV LANGCHAIN_API_KEY=$LANGCHAIN_API_KEY
# Expose the desired ports
# Copy the .env file to the container instead of ^^^
# COPY .env /app/.env
EXPOSE 8888 6006
# Set the ulimit options
CMD ["bash", "-c", "ulimit -l unlimited && ulimit -s 65536 && python /app/langsmith.py"]
# debug:
# docker run -it --rm --gpus all --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 -v .:/app cognosis /bin/bash
# run:
# docker run -it --rm --gpus all --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 -v C:\Users\deV\Documents\source\cognosis:/app cognosis python /app/app/langsmith.py