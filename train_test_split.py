import os
import numpy as np
import shutil

# Path to your dir with images
# root_dir = 'D:/93/'
print('Enter path to your images:')
root_dir = str(input())

# Sample split as a percentage
val_ratio = 0.05 # val dataset
test_ratio = 0.35 # test dataset

src = root_dir
allFileNames = os.listdir(src)

# Make folders for train, test, val datasets
os.makedirs(root_dir + '/train/', exist_ok=True)
os.makedirs(root_dir + '/val/', exist_ok=True)
os.makedirs(root_dir + '/test/', exist_ok=True)

# Use random to mix images
np.random.shuffle(allFileNames)
train_FileNames, val_FileNames, test_FileNames = np.split(np.array(allFileNames),
                                                          [int(len(allFileNames) * (1 - (val_ratio + test_ratio))),
                                                           int(len(allFileNames) * (1 - test_ratio))])

train_FileNames = [src + '/' + name for name in train_FileNames.tolist()]
val_FileNames = [src + '/' + name for name in val_FileNames.tolist()]
test_FileNames = [src + '/' + name for name in test_FileNames.tolist()]

print('Total images: ', len(allFileNames))
print('Training: ', len(train_FileNames))
print('Validation: ', len(val_FileNames))
print('Testing: ', len(test_FileNames))

try:
    for name in train_FileNames:
        shutil.copyfile(name, os.path.join(root_dir, 'train', os.path.basename(name)))
    print('Train dataset is Done')
    for name in val_FileNames:
        shutil.copyfile(name, os.path.join(root_dir, 'val', os.path.basename(name)))
    print('Val dataset is Done')
    for name in test_FileNames:
        shutil.copyfile(name, os.path.join(root_dir, 'test', os.path.basename(name)))
    print('Test dataset is Done')
except FileExistsError:
    print('File already exists')

# Make train.txt, test.txt files for Darknet usage
with open(root_dir + 'train/train.txt', 'w') as file:
    for item in train_FileNames:
        item = item.replace(root_dir, 'train')
        item = root_dir + item
        file.write('%s\n' % item)
    print('Train txt is Done')

with open(root_dir + 'test/test.txt', 'w') as file:
    for item in test_FileNames:
        item = item.replace(root_dir, 'test')
        item = root_dir + item
        file.write('%s\n' % item)
    print('Test txt is Done')

with open(root_dir + 'val/val.txt', 'w') as file:
    for item in val_FileNames:
        item = item.replace(root_dir, 'val')
        item = root_dir + item
        file.write('%s\n' % item)
    print('Val txt is Done')