import cv2
import torch
import numpy as np
from torchvision import transforms as T
from PIL import Image

def annotate_img(img_np_array, threshold):

    transform = T.ToTensor()
    img = transform(img_np_array)
    model = torch.load('model_prod.pt')
    model.eval()
    
    with torch.no_grad():
      pred = model([img])
      
    bboxes, scores = pred[0]['boxes'], pred[0]['scores']
    num = torch.argwhere(scores > threshold).shape[0]
    font = cv2.FONT_HERSHEY_SIMPLEX
    for i in range(num) :
        x1, y1, x2, y2 = bboxes[i].numpy().astype('int')
        class_name =  'penguin'
        img_np_array = cv2.rectangle(img_np_array, (x1, y1), (x2, y2), (0, 255, 0), 1)
        img_np_array = cv2.putText(img_np_array, class_name, (x1, y1-10), font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
    
  return img_np_array
