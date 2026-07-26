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
- [] establish github pull access
- [] create hello world flask app with docker compose
- [] push initial built containers to a dockerhub repo
- [] validate service startup on rpi
- [] see if helloworld app accessible on local network (optional)
- [] connect cloudtrail tunnel
- [] connect cloudtrail access with allowlist
- [] E2E helloworld validation
- [] design actual service w/mock camera
- [] finish off impl
- [] brag to kylee, bday present
