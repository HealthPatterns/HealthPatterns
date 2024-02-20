# frontend Dockerfile
FROM node:latest AS build

WORKDIR /app

COPY health-patterns/package.json ./
COPY health-patterns/package-lock.json ./
RUN npm install
COPY health-patterns/ ./
RUN npx vite build

FROM nginx:1.19-alpine
COPY --from=build /app/dist /usr/share/nginx/html
