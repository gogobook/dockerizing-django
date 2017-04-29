FROM nginx:alpine
RUN apk add --update --no-cache nginx
RUN rm /etc/nginx/conf.d/default.conf
ADD conf.d/ /etc/nginx/conf.d
