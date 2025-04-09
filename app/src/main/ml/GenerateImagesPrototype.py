import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import save_img
import matplotlib.pyplot as plt
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_dir, 'models', 'VAST_CNN_Main_Model.h5')
output_image_path = os.path.join(script_dir, '..', 'data', 'generated_image.png')

model = load_model(model_path); print("Model loaded for image generation.")

# initialize a random noise image (starting point)
def generate_random_image(seed=None):
    size = (32, 32, 3)
    if seed is not None: np.random.seed(seed)  # rand seed by default
    # return quantize_colors(np.random.uniform(0, 1, size=size).astype("float32"))
    return np.random.uniform(0, 1, size=size).astype("float32")



def quantize_colors(image, num_colors=3):
    # palette = np.array([0.0, 0.5, 1.0])  # 3-color palette
    # quantized_image = np.empty_like(image)
    # for channel in range(image.shape[-1]):  # each channel calculated independently
    #     quantized_image[..., channel] = palette[np.abs(palette - image[..., channel]).argmin(axis=0)]
    # return quantized_image
    
    
    
    
    h, w, c = image.shape; image_flat = image.reshape((-1, c))
    
    palette = np.linspace(0, 1, num_colors) # make our palette of colors evenly distributed in the range [0, 1]
    
    quantized = np.zeros_like(image_flat)
    for channel in range(c):# each chanel
        quantized[:, channel] = np.array([
            palette[np.abs(palette - pixel).argmin()] for pixel in image_flat[:, channel]
        ])
    
    quantized_image = quantized.reshape((h, w, c));  # back to the original shape before retrun
    
    quantized_image = np.mean(quantized_image, axis=-1, keepdims=True)  # average RGB values
    quantized_image = np.repeat(quantized_image, 3, axis=-1)
    return quantized_image

# gradient ascent to improve the aesthetic score
def optimize_image(model, initial_image, steps=200, learning_rate=0.05):
    image = tf.Variable(initial_image)  # converts image to a TensorFlow variable for gradient updates

    for step in range(steps):
        with tf.GradientTape() as tape:
            tape.watch(image)
            prediction = model(tf.expand_dims(image, axis=0))  # predict aesthetics
            loss = prediction[0][0]  # the aesthetic score is the target to maximize

        # gradients for grad ascent
        gradients = tape.gradient(loss, image)
        gradients = tf.math.l2_normalize(gradients)  # Normalize gradients for stability
        image.assign_add(learning_rate * gradients)  # update img

        # clip image values to valid range [0, 1]
        image.assign(tf.clip_by_value(image, 0.0, 1.0))
        
        # 3 colour maping
        image.assign(tf.convert_to_tensor(quantize_colors(image.numpy())))

        # prin prog
        if (step + 1) % 10 == 0:
            print(f"Step {step + 1}/{steps}, Aesthetic Score: {loss.numpy():.4f}")

    return image.numpy()

# generate & optimize the image
def generate_New_Image(seed=None):
    initial_image = generate_random_image(seed); optimized_image = optimize_image(model, initial_image, steps=500, learning_rate=8); return optimized_image



# # save & print the new img
# save_img(output_image_path, optimized_image); print(f"Generated image saved to {output_image_path}")

# MPL stuff to show img

# # uncomment to run:
# optimized_image = generate_New_Image(100)
# plt.imshow(optimized_image); plt.axis('off'); plt.title("Generated Image"); plt.show()
