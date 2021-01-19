# app-compose

A project to deploy a flask app connected with Redis using docker-compose. It will count the number of time user visits the website. Click on either will increase the count and add it in redis .
If use the existing images that are avaiable in public registry or build your own images ans use those instead, by uncommenting "build" and commenting "image" line docker-compose

To deploy it use the below command

`docker-compose up`
