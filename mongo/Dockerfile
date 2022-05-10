FROM mongo:latest

ARG DB_HOST
ARG DB_NAME
ARG COLLECTION

ENV DB_HOST ${DB_HOST}
ENV DB_NAME ${DB_NAME}
ENV COLLECTION ${COLLECTION}

CMD apt-get -qq -y update && apt-get -qq -y install curl && \
    curl https://ai2-semanticscholar-cord-19.s3-us-west-2.amazonaws.com/2020-04-03/metadata.csv --output metadata.csv && \
    mongoimport --uri ${DB_HOST} -d ${DB_NAME} -c ${COLLECTION} --file /metadata.csv --headerline --type csv --quiet
