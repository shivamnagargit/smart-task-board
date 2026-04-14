# Use official Node.js image
FROM node:20-alpine

# Set the working directory inside the box
WORKDIR /app

# Copy the package lists and install them
COPY package*.json ./
RUN npm install

# Copy your Next.js code
COPY . .

# Build the project for production (Makes it super fast)
RUN npm run build

# Open port 3000
EXPOSE 3000

# The command to turn on the Waiter
CMD ["npm", "start"]
