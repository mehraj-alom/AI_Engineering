FROM python

WORKDIR /app

COPY . .

RUN pip install  --no-cache-dir -r requirement.txt

RUN  mkdir -p logs

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
