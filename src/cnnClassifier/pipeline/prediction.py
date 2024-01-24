import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os



class PredictionPipeline:
    def __init__(self,filename):
        self.filename =filename


    
    def predict(self):
        ## load model
        
        #model = load_model(os.path.join("artifacts","training", "model.h5"))
        model = load_model("/home/towet/Desktop/Visions/OpenProjects/COVID-CXR-Image-Classification-Project/artifacts/training/vgg16_model.h5")

        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (224,224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = np.argmax(model.predict(test_image), axis=1)
        class_names = ['covid', 'normal', 'virus']
        print(f"this is the >>>>>>>>>>>>>>>>>> {class_names[int(result)]} >>> output")

        return class_names[int(result)]