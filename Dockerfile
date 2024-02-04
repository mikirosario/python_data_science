# Imagen donde se va a ejecutar nuestro código
FROM python:3.10-alpine

# Directorio de vamos a almacenar nuestra app
WORKDIR /app

RUN apk update; \
    apk add \
    bash \
    git

COPY . .

CMD ["bash"]