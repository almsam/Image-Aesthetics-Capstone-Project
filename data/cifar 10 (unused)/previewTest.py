import unittest
import numpy as np
from preview import load_cifar_batch, reshape_images

class TestCifarFunctions(unittest.TestCase):

    def test_load_cifar_batch(self):
        images, labels = load_cifar_batch('C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/data/cifar-10-batches-py/data_batch_1')
        
        # test 1: make sure our images & labels have been loaded
        self.assertIsInstance(images, np.ndarray, "Images should be a NumPy array")
        self.assertIsInstance(labels, list, "Labels should be a list")

        # test 2: is the length of labels 10000 as expected for CIFAR-10 styff
        self.assertEqual(len(labels), 10000, "There should be 10000 labels in the batch")
    
    def test_reshape_images(self):
        
        # test set of images # 10 images, 32x32 pixels, 3 color channels
        dummy_images = np.random.randint(255, size=(10, 3 * 32 * 32))  # 10 images flattened
        reshaped_images = reshape_images(dummy_images)
        
        # test 3: correct shape # (batch_size, 32, 32, 3)
        self.assertEqual(reshaped_images.shape, (10, 32, 32, 3), "Images should be reshaped to (10, 32, 32, 3)")

if __name__ == '__main__':
    unittest.main()
