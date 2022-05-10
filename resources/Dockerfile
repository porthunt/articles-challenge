FROM mongo:latest

ARG DB_HOST
ARG DB_NAME
ARG COLLECTION

ENV DB_HOST ${DB_HOST}
ENV DB_NAME ${DB_NAME}
ENV COLLECTION ${COLLECTION}

COPY metadata.csv /metadata.csv

CMD mongoimport --uri ${DB_HOST} -d ${DB_NAME} -c ${COLLECTION} --file /metadata.csv --headerline --type csv
