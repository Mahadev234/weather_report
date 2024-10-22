# Use official Node.js image as the base image
FROM node:14-alpine

# Set working directory inside the container
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json ./
RUN npm install

# Copy the entire application to the working directory
COPY . .

# Expose the port the app runs on
EXPOSE 3000

# Command to start the app
CMD ["npm", "start"]
