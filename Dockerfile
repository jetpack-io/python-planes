
# app build
FROM --platform=amd64 node:alpine as build-app

# cache dependencies
WORKDIR /src
COPY app/package.json .
RUN npm install --legacy-peer-deps

# build vue app
WORKDIR /src/app

COPY app .
RUN npm run build


# production container
FROM --platform=amd64 python:3.9-slim

WORKDIR /app

# cache dependencies
COPY ./api/requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# build api
COPY ./api .
COPY --from=build-app /src/api/public ./public/.

ENV PORT 8080
EXPOSE 8080

CMD ["python", "main.py"]
