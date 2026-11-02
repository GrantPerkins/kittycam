docker build -t kittycam:latest ./cam
docker tag kittycam:latest grantperkins/kittycam:latest
docker push grantperkins/kittycam:latest