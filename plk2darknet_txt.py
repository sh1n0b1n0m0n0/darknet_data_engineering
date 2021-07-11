import pickle
import cv2
from train_test_split import root_dir

print('Enter path to .pkl file:')
path_to_plk1 = str(input())

#path_to_plk1 = root_dir + '93.a.cache.pkl'
#path_to_plk2 = root_dir + '93.b.cache.pkl'

data = pickle.load(open(path_to_plk1, "rb"))

with open(root_dir + 'train/train.txt') as f:
    contents = f.readlines()


# pulling coordinates from data
# and align them
def take_cords(data):
    cords = []
    for crds in data:
        for i in crds['coordinates']:
            cords.append(i['x'])
            cords.append(i['y'])

    x1 = max(cords[0], cords[6])
    y1 = max(cords[1], cords[3])
    x2 = max(cords[2], cords[4])
    y2 = max(cords[5], cords[7])

    return x1, y1, x2, y2


for img_name in contents:
    try:
        img_name = img_name.replace(root_dir + 'train/','')
        img_name = img_name.replace('\n','')
        data_name = data[img_name]

        path = root_dir + img_name

        img = cv2.imread(path)
        h, w, d = img.shape

        x1, y1, x2, y2 = take_cords(data_name)


        x_cent = ((x2 + x1)/2)/w
        y_cent = ((y2 + y1)/2)/h
        W = (x2-x1)/w
        H = (y2-y1)/h
        # 0 - index if you have 1 label to detect
        indx = '0'
        darknet_ann = indx+' '+str(x_cent)+' '+str(y_cent)+' '+str(W)+' '+str(H)
        with open(root_dir + 'train/' + img_name.replace('.jpg','') + '.txt', 'w') as file:
            file.write('%s\n' % darknet_ann)
    except(KeyError):
        print('Image not found')
        pass


print('All is DONE!')
