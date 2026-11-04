docker build -t kittycam:latest --platform linux/arm64/v8 ./cam
docker tag kittycam:latest grantperkins/kittycam:latest
docker push grantperkins/kittycam:latest
