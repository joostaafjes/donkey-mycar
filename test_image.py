#!/usr/bin/env python3
"""
Scripts to test 1 image

Usage:
    manage.py drive [--model=<model>] [--type=(linear|categorical|tflite_linear)]

Options:
    -h --help          Show this screen.
"""

from docopt import docopt

import donkeycar as dk
from donkeycar.parts.tub_v2 import TubWriter
from donkeycar.parts.datastore import TubHandler
from donkeycar.parts.controller import LocalWebController
from donkeycar.parts.actuator import PCA9685, PWMSteering, PWMThrottle

from PIL import Image

cfg = dk.load_config()
model_type = cfg.DEFAULT_MODEL_TYPE
model_path = './models/01-track-with-dashed/clock/data-01.h5'

kl = dk.utils.get_model_by_type(model_type, cfg)
kl.load(model_path=model_path)

image = './data/01-track-with-dashed/clock/data-01/images/9_cam_image_array_.jpg'
# img = Image.open(image).resize((width, height))
img = Image.open(image)

print(kl.inference(image))
