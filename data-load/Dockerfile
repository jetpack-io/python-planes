# production container
FROM --platform=amd64 python:3.9-slim

WORKDIR /app

# cache dependencies
COPY ./requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# build api
COPY . .

ENV PORT 8080
EXPOSE 8080

CMD ["python", "main.py"]
