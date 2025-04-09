RunSuccess = 0

import os
import GenerateImagesPrototype

image = GenerateImagesPrototype.generate_New_Image(22)

print(image.__class__)


import os
from GenerateImage import *

# First we defome our output directory
script_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(script_dir, "public", "data", "temp")
os.makedirs(output_dir, exist_ok=True)

# then we generate an image with a specific seed
seed = 12345
generated_image = generateQuality(seed, output_dir, n=72)

print(f"Generated and saved image for seed {seed} in {output_dir}")

RunSuccess = 1
print("run successful ", RunSuccess)

