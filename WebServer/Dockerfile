FROM alpine:latest

RUN apk --update add nginx && \
      ln -sf /dev/stdout /var/log/nginx/access.log && \
      ln -sf /dev/stderr /var/log/nginx/error.log && \
      mkdir -p /run/nginx && \
      mkdir -p /var/cache/apk/*
COPY conf.d/app.conf /etc/nginx/conf.d/app.conf

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]

