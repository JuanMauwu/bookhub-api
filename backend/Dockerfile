#dockerfile

FROM python:3.12-slim

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1



# install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        binutils \
        gdal-bin \
        gcc \
        g++ \
        libssl-dev \
        libgdal-dev \
        libproj-dev \
        libkrb5-dev \
        jq \
        tk \
        postgresql-client && \
    apt-get clean && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

# upgrade pip
RUN pip install --no-cache-dir --upgrade pip

# install Python dependencies
COPY requirements.txt /usr/src/app/

# install requirements from pip
RUN pip install --no-cache-dir -r requirements.txt

# install arcgis
# RUN pip install --no-cache-dir -vvv arcgis

# Install GDAL Python bindings matching the system version
#ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
#ENV C_INCLUDE_PATH=/usr/include/gdal

#RUN gdal-config --version
#RUN pip install --no-cache-dir GDAL==$(gdal-config --version)

# expose port
EXPOSE 8000

# create a non-root user
# RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /usr/src/app
# USER appuser

# set entrypoint
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]