import numpy as np
import cv2
import matplotlib.pyplot as plt
from steganography import Steganography

steg_var=Steganography()

mask_img=cv2.imread("./Resources/sherlock.jpg")
secret_message_img=cv2.imread("./Resources/message.jpg")
cypher=steg_var.embed_a_in_b(secret_message_img,mask_img)
cv2.imshow('mask',mask_img)
cv2.imshow('secret message',secret_message_img)
cv2.imshow('cypher image',cypher)
cv2.waitKey()

decyphered_image=steg_var.decrypt_image(cypher)
cv2.imshow('Decrypted image',decyphered_image)
cv2.waitKey()
