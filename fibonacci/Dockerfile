# Container image that runs your code
FROM debian:9.5-slim 

# Copies your code file from your action repository to the filesystem path `/` of the container
ADD entrypoint.sh /entrypoint.sh
ADD fibonacci.py /fibonacci.py

# Set execution permissions
RUN chmod +x /entrypoint.sh
RUN chmod +x /fibonacci.py
RUN apt-get update
RUN apt-get -y install python3

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["./entrypoint.sh"]
