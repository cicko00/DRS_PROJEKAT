FROM node:18.13.0
RUN mkdir /app
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
#expose is more for documentation
EXPOSE 4200 
CMD ["npm","start"]