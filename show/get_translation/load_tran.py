from . import load_model
class Translation:
    def __init__(self,data_path,model_path):
        self.pe=load_model.load_model()
    def get_trans(self,inputs):
        return load_model.translation(*self.pe,inputs)