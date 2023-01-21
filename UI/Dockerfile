FROM node
WORKDIR /main
COPY package.json .
RUN npm install
COPY . .
#expose is more for documentation
EXPOSE 4200 
CMD ["npm","start"]