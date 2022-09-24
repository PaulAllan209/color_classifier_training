from datetime import datetime
import os

# global models_path
# models_path = "./trained_models"


# if os.listdir(f"{models_path}"):
#     last_model_num = os.listdir(f"{models_path}")[-1][-1]
#     os.mkdir(f"{models_path}/model{int(last_model_num) + 1}")
    
#     # Makes a readme file that contains information on when was this created
#     last_model = os.listdir(f"{models_path}")[-1]
#     with open(f"{models_path}/{last_model}/readme.txt", "w+") as f:
#         f.write(f"Model created on: {str(datetime.now())}")

# elif not os.listdir(f"{models_path}"):
#     os.mkdir(f"{models_path}/model1")

#     # Makes a readme file that contains information on when was this created
#     with open(f"{models_path}/model1/readme.txt", "w+") as f:
#         f.write(f"Model created on: {str(datetime.now())}")

print(datetime.now())