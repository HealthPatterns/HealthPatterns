# frontend Dockerfile
FROM node:latest AS build

WORKDIR /app

COPY aid-vault/package.json ./
COPY aid-vault/package-lock.json ./
RUN npm install
COPY aid-vault/ ./
RUN npx vite build

FROM nginx:1.19-alpine
COPY --from=build /app/dist /usr/share/nginx/html
