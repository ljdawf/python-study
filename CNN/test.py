import tensorflow as tf
import pandas as pd
Image_path = r"C:\2020人工神经网络\kaokore\images_256"
Label_path = r"C:\2020人工神经网络\kaokore\labels.csv"
csv_data = pd.read_csv(Label_path) 

#对训练集和验证集进行划分
test_image_path = []
test_label = []
for p_image, p_label, p_set in zip(csv_data["image"],csv_data["gender"],csv_data["set"]):
    if p_set=="test":
        test_image_path.append(Image_path+"\\"+p_image)
        test_label.append(p_label)

#构建数据通道
test_img_dataset = tf.data.Dataset.from_tensor_slices(test_image_path) 

#图像预处理
def pre_image(img_path):  
  img_tf = tf.io.read_file(img_path) 
  img_tensor = tf.image.decode_jpeg(img_tf,channels=3) 
  img_tensor = tf.image.resize(img_tensor,[224,224])  
  img_tensor = tf.cast(img_tensor,tf.float32)
  img = img_tensor/255
  return img

test_data = test_img_dataset.map(pre_image) 

BATCH_SIZE=16
test_data= test_data.batch(BATCH_SIZE) 

#加载模型
model = tf.keras.models.load_model(r"C:\2020人工神经网络\model.h5") 
pre_label = model.predict(test_data)

label = (pre_label>0.5).astype("int32") 

print(label) 


