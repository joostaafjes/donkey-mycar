# Connect to my donkey

- ssh pi@knoestpi.local
- cd mycar

## Training

python train.py --tubs data/ --model ./models/myfirstpilot.h5

## Driving

python manage.py drive --model ./models/01-track-with-dashed/clock/data-01-and-02.h5

In your local browser goto `http://knoestpi.local:8887/drive`
- Control mode: gamepad = Logitech steering wheel
- Mode & Pilot:
    - User: both steering and throttle with steering wheel
    - Local pilot: throttle with steering wheel and steering automatically(=NN)
    - Local angle:

## Driving with simulator

copy symconfig.cp to myconfig.py and do `python manage.py drive`