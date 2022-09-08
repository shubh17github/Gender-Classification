from array import array
import numpy as np
import pickle
import json
import config
class gender_class():

    def __init__(self,long_hair,forehead_width,forehead_height,nose_wide,nose_long,lips_thin,distance_nose_to_lip_long):
        self.longHair=long_hair
        self.FOrheadwdth=forehead_width
        self.FOrheadHeight=forehead_height
        self.NoseWide=nose_wide
        self.NoseLong=nose_long
        self.LipThin=lips_thin
        self.Distance_NoseLip=distance_nose_to_lip_long


    def load_model(self):
        with open(config.model_file_path,'rb') as file:
            self.model=pickle.load(file)

        with open(config.col_dict_path,'r') as file:
            self.col_dict=json.load(file)



    def predict(self):
        self.load_model()

        array=np.zeros(len(self.col_dict['column']))
        array[0]=self.longHair
        array[1]=self.FOrheadwdth
        array[2]=self.FOrheadwdth
        array[3]=self.NoseWide
        array[4]=self.NoseLong
        array[5]=self.LipThin
        array[6]=self.Distance_NoseLip

        result=self.model.predict([array])

        return result[0]
        



