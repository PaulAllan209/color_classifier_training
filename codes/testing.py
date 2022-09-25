from datetime import datetime
import os

global models_path
models_path = "./trained_models/model1/saved_per_train/train1"


trained_list = os.listdir(models_path)
trained_list.remove("logs.csv")
print(trained_list)
print(min(trained_list, key=lambda loss_val:loss_val[-4:-1]))
