import os

import cv2 as cv
import numpy as np
import PIL.Image
import tensorflow as tf
import tensorflow_hub as hub


class StyleTransfer:
    def __init__(self):
        os.environ["TFHUB_MODEL_LOAD_FORMAT"] = "COMPRESSED"
        self.model = hub.load("./paint_yourself_api/image_stylization_model/")

    def tensor_to_image(self, tensor):
        tensor = tensor * 255
        tensor = np.array(tensor, dtype=np.uint8)
        if np.ndim(tensor) > 3:
            assert tensor.shape[0] == 1
            tensor = tensor[0]
        return PIL.Image.fromarray(tensor)

    def load_img(self, path_to_img):
        max_dim = 512
        img = tf.io.read_file(path_to_img)
        img = tf.image.decode_image(img, channels=3)
        img = tf.image.convert_image_dtype(img, tf.float32)

        shape = tf.cast(tf.shape(img)[:-1], tf.float32)
        long_dim = max(shape)
        scale = max_dim / long_dim

        new_shape = tf.cast(shape * scale, tf.int32)

        img = tf.image.resize(img, new_shape)
        img = img[tf.newaxis, :]
        return img

    def paint_image(self, input_image_path, input_style_path):
        # Load an input image & style into a tensor
        input_image = self.load_img(input_image_path)
        input_style = self.load_img(input_style_path)

        # # Show the image and reference image
        # cv.imshow('image', cv.cvtColor(np.array(self.tensor_to_image(input_image)), cv.COLOR_BGR2RGB))
        # cv.imshow('reference', cv.cvtColor(np.array(self.tensor_to_image(input_style)), cv.COLOR_BGR2RGB))

        # Load the co
        stylized_image = self.model(tf.constant(input_image), tf.constant(input_style))[
            0
        ]
        stylized_image = np.array(self.tensor_to_image(stylized_image))

        # Adjust contrast
        hsvImg = cv.cvtColor(stylized_image, cv.COLOR_BGR2HSV)
        hsvImg[..., 1] = (hsvImg[..., 1] * 1.5).clip(0, 255)
        hsvImg[..., 2] = (hsvImg[..., 2] * 1.1).clip(0, 255)
        stylized_image = cv.cvtColor(hsvImg, cv.COLOR_HSV2BGR)
        stylized_image = cv.cvtColor(stylized_image, cv.COLOR_BGR2RGB)

        # cv.imshow('stylized_img', cv.cvtColor(stylized_image, cv.COLOR_BGR2RGB))
        # cv.waitKey(0)

        return stylized_image


if __name__ == "__main__":
    # Load the painting model
    s = StyleTransfer()

    image = s.paint_image("./samples/Daniel.png", "./styles/Cezanne/215466.jpg")

    cv.imshow("image", image)
    cv.waitKey(0)
