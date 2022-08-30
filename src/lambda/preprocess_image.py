from pathlib import Path
from pprint import pprint
import cv2
import numpy as np

from PIL import Image

#AWS Specific
import boto3

def lambda_handler(event, context):
    # String value of the S3 Object name passed
    #  to get_image_from_s3 function returning an Image object
    s3Object =  Image(get_image_from_s3(event['s3Object'].value))

    img_arr = np.asarray(s3Object) #convert image to matrix
    img_arr = cv2.cvtColor(img_arr, cv2.COLOR_BGR2GRAY) #convert to grayscale before binarzation
    ret, imgf = cv2.threshold(img_arr, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) #binarize using Otsu's algorithm
    img = Image.fromarray(imgf)
    return img

def get_image_from_s3(s3ObjectName):

    s3Resource = boto3.resource('s3', region_name='us-east-1')
    s3Bucket = s3Resource.Bucket('sampleUploads123')
    

    x = undefined
    return Image(x)