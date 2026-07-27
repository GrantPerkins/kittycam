# kittycam

i want to watch my cats from work, on vaca, etc. especially since Kylee is flying home soon.

## Requirements
1. live web stream from raspberry pi to personal device
2. allowlist auth to prevent 3rd parties from seeing inside my house
3. mobile-friendly for Kylee

## Design
- a camera stream will be available via http endpoint
### Hardware
- raspberry pi 3 (cheap) with 32gb sd card
- logitech usb webcam
### Service
- fastapi, possibly running with nginx (TBD)
- opencv service for pulling frames and created h264 stream
- 

## Implementation
- [X] image the sd card
- [X] confirm ssh access
- [X] create non-root user and ensure ssh access
- [X] install git, docker
- [X] establish github pull access
- [X] create hello world flask app with docker compose
- [X] validate service startup on pi
- [X] see if helloworld app accessible on local network (optional)
- [X] connect cloudtrail tunnel
- [X] connect cloudtrail access with allowlist
- [X] E2E helloworld validation
- [X] design actual service w/mock camera
- [X] finish off impl
- [X] brag to kylee, bday present
- [X] enable jwt auth on all endpoints
