FROM node:lts-alpine

ENV NODE_VERSION 24.7.0

RUN apk add --update nodejs npm

WORKDIR /

COPY package*.json ./

RUN npm install

COPY . . 

EXPOSE 3000

CMD ["npm", "run", "dev"]