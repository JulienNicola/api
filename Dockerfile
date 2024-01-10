FROM python:3.10

EXPOSE 8000

WORKDIR /code

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

#local running
#CMD ["uvicorn", "fast_api:app", "--host", "0.0.0.0", "--port", "8000"]

#runnning on azure
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "fast_api:app", "--worker-class", "uvicorn.workers.UvicornWorker"]