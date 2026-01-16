# Build Stage
FROM node:20-alpine AS builder
WORKDIR /app

# Copy package info
COPY package.json ./

# Install dependencies (including devDependencies for build)
RUN npm install

# Copy source
COPY . .

# Build
RUN npm run build

# runtime Stage
FROM nginx:alpine AS runtime
COPY ./nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /app/dist /usr/share/nginx/html

EXPOSE 80
