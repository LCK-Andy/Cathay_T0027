import cv2
import numpy as np
import json
import TestImages
import matplotlib.pyplot as plt
from Models import LuggageProcessor as lp
model = lp.LuggageProcessor()
path = r"TestImages\OIP.jpeg"
model.depth_test(image_path = path)