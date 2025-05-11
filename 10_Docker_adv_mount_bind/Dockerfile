FROM python

WORKDIR /application

COPY . .


RUN pip install  --no-cache-dir -r requirement.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
