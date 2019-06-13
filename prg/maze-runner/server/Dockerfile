FROM python:3-alpine

RUN apk add --no-cache socat

WORKDIR /usr/src/app

COPY . .

CMD [ "socat", "TCP4-LISTEN:8080,fork", "EXEC:./maze_game.py" ]

EXPOSE 8000

