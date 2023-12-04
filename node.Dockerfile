FROM node:20

# Note: this is the manual way to install node on a base image like debian
#RUN apt-get update \
#    && apt-get install -y ca-certificates curl gnupg \
#    && mkdir -p /etc/apt/keyrings \
#    && curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key \
#    | gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg
#
#ENV NODE_MAJOR=20
#RUN echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_$NODE_MAJOR.x nodistro main" \
#    | tee /etc/apt/sources.list.d/nodesource.list
#
#RUN apt-get update \
#    && apt-get install -y nodejs

RUN npm install -g npm

WORKDIR /code

COPY package.json package-lock.json /code/
RUN npm ci --force

COPY . /code/

ENTRYPOINT ["npm", "run", "dev"]
