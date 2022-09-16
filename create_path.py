from glob import glob

train_img_list = glob('C:/Users/PC/VSC/yolov7/car_dataset/train/images/*.jpg')
print(len(train_img_list))
valid_img_list = glob('C:/Users/PC/VSC/yolov7/car_dataset/valid/images/*.jpg')
print(len(valid_img_list))
test_img_list = glob('C:/Users/PC/VSC/yolov7/car_dataset/test/images/*.jpg')
print(len(test_img_list))

with open('C:/Users/PC/VSC/yolov7/car_dataset/train.txt', 'w') as f:
	f.write('\n'.join(train_img_list) + '\n')
    
with open('C:/Users/PC/VSC/yolov7/car_dataset/valid.txt', 'w') as f:
	f.write('\n'.join(valid_img_list) + '\n')
 
with open('C:/Users/PC/VSC/yolov7/car_dataset/test.txt', 'w') as f:
	f.write('\n'.join(test_img_list) + '\n')