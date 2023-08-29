FROM node:latest AS build

WORKDIR /app

COPY frontend/aid-vault/package.json ./
COPY frontend/aid-vault/package-lock.json ./
RUN npm install
COPY frontend/aid-vault/ ./
RUN npx vite build

FROM nginx:1.19-alpine
COPY --from=build /app/dist /usr/share/nginx/html
