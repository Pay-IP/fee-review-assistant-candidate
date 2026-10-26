FROM node:22.23.4-alpine@sha256:fe4f6d74e20370acb04ad889077d14d0f64a9c8ea6a42bc60cddf1e844699914

WORKDIR /app

COPY frontend/package*.json ./
RUN npm ci

COPY frontend/ .

EXPOSE 5173

CMD ["npm", "run", "dev"]
