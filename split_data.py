import os
import shutil
import tqdm
import random
from sklearn.model_selection import train_test_split

train_path = 'output/images'
anno_path = 'output/labels'
images = [os.path.join(train_path, x) for x in os.listdir(train_path)]
annotations = [os.path.join(anno_path, x) for x in os.listdir(anno_path) if x[-3:] == "txt"]

images.sort()
annotations.sort()

# Split the dataset into train-valid-test splits 
train_images, val_images, train_annotations, val_annotations = train_test_split(images, annotations, test_size = 0.1, random_state = 1)

def move_files_to_folder(list_of_files, destination_folder):
    for f in list_of_files:
        try:
            shutil.move(f, destination_folder)
        except:
            print(f)
            assert False
# os.makedirs('dataset', exist_ok = True)
forder_image_train = 'dataset/images/train'
forder_image_val = 'dataset/images/val'
forder_label_train = 'dataset/label/train'
forder_label_val = 'dataset/label/val'
os.makedirs(forder_image_train, exist_ok = True)
os.makedirs(forder_image_val, exist_ok = True)
os.makedirs(forder_label_train, exist_ok = True)
os.makedirs(forder_label_val, exist_ok = True)

# Move the splits into their folders
move_files_to_folder(train_images, forder_image_train)
move_files_to_folder(val_images, forder_image_val)
move_files_to_folder(train_annotations, forder_label_train)
move_files_to_folder(val_annotations, forder_label_val)