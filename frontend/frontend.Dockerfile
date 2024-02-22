# frontend Dockerfile
FROM node:latest AS build

WORKDIR /app

COPY aid-vault/package.json ./
COPY aid-vault/package-lock.json ./
RUN npm install
COPY aid-vault/ ./
RUN npx vite build

FROM nginx:1.19-alpine
COPY nginx/ /etc/nginx/ssl/
COPY nginx/nginx.conf /etc/nginx/nginx.conf
#COPY nginx/nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/dist /usr/share/nginx/html
#COPY /usr/share/nginx/html/assets/* /usr/share/nginx/html
RUN cp /usr/share/nginx/html/assets/* /usr/share/nginx/html/
RUN sed -i 's/\/assets//g' /usr/share/nginx/html/index.html