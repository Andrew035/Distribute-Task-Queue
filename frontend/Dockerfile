# Use Node.js LTS version
From node:20-slim

WORKDIR /app

# Copy package files first for better caching
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the code
COPY . .

# Vite's default dev port
EXPOSE 5173

# Start the dev server with host binding
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
