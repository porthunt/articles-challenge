FROM node:alpine

ARG API_URL
ENV REACT_APP_API_URL ${API_URL}

COPY ./ /app
WORKDIR /app

RUN npm install

CMD ["npm", "start"]
