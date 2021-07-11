# darknet_data_engineering

Hello stranger!

This is a project that converts data for Darknet!

1.Run run.bat;

2.Enter path to your image folder;

![run.bat](run1.jpg)

3.Enter path to your Pickle file(.pkl);

![run.bat2](run2.jpg)

4.It's alright then you see "Image not found", script can't find image_name from your dataset with images in .pkl file!

![run.bat2](run3.jpg)

5.Download custom_data folder if you need.

6.Edit file obj.names in the directory darknet\, with objects names - each in new line:

![edit_custom](obj_names.jpg)

7.Edit file obj.data in the directory darknet\, containing (where classes = number of objects):

classes = 2
train  = data/train.txt
valid  = data/test.txt
names = data/obj.names
backup = backup/ 

![edit_custom](obj_data.jpg)
