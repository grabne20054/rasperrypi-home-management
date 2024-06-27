# Base image
FROM node:14-alpine

WORKDIR /usr/app/wheaterapp

RUN npm install -g @vue/cli

# Copy package.json and package-lock.json
COPY package*.json ./usr/app/wheaterapp

# Install dependencies
RUN npm install

# Copy project files
COPY . .

# Build the Vue.js application
RUN npm run build

# Expose the application port
EXPOSE 8080

# Start the application
CMD [ "npm", "run", "serve" ]