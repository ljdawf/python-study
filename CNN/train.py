import pandas as pd
import tensorflow as tf
import os
import math
Image_path = r"C:\2020人工神经网络\kaokore\images_256"
Label_path = r"C:\2020人工神经网络\kaokore\labels.csv"
csv_data = pd.read_csv(Label_path) 

#对训练集和验证集进行划分
train_image_path = [] 
train_label = []  
dev_image_path = [] 
dev_label = [] 
for p_image, p_label, p_set in zip(csv_data["image"],csv_data["gender"],csv_data["set"]):
    if p_set=="train":
        train_image_path.append(Image_path+"\\"+p_image)
        train_label.append(p_label)
    elif p_set=="dev":
        dev_image_path.append(Image_path+"\\"+p_image)
        dev_label.append(p_label)
print("训练集、验证集划分完成")

#构建数据通道
train_img_dataset = tf.data.Dataset.from_tensor_slices(train_image_path)
train_label_dataset = tf.data.Dataset.from_tensor_slices(train_label)
dev_img_dataset = tf.data.Dataset.from_tensor_slices(dev_image_path)
dev_label_dataset = tf.data.Dataset.from_tensor_slices(dev_label)

#图像预处理
def pre_image(img_path):
  img_tf = tf.io.read_file(img_path) 
  img_tensor = tf.image.decode_jpeg(img_tf,channels=3) 
  img_tensor = tf.image.resize(img_tensor,[224,224]) 
  img_tensor = tf.cast(img_tensor,tf.float32) 
  img = img_tensor/255 
  return img
train_img = train_img_dataset.map(pre_image)
train_data = tf.data.Dataset.zip((train_img,train_label_dataset)) 
dev_img = dev_img_dataset.map(pre_image) 
dev_data = tf.data.Dataset.zip((dev_img,dev_label_dataset))
BATCH_SIZE=16 
train_data = train_data.repeat().shuffle(len(train_image_path)).batch(BATCH_SIZE)
dev_data = dev_data.batch(BATCH_SIZE) 

#构建网络层
model = tf.keras.Sequential() 
model.add(tf.keras.layers.Conv2D(64,(3,3),input_shape=(224,224,3),activation = "relu",padding = "same"))
model.add(tf.keras.layers.Conv2D(64,(3,3),activation = "relu",padding = "same"))
model.add(tf.keras.layers.MaxPool2D()) 
model.add(tf.keras.layers.Dropout(0.3))
model.add(tf.keras.layers.Conv2D(128,(3,3),activation = "relu",padding = "same"))
model.add(tf.keras.layers.Conv2D(128,(3,3),activation = "relu",padding = "same"))
model.add(tf.keras.layers.MaxPool2D())
model.add(tf.keras.layers.Dropout(0.3))
model.add(tf.keras.layers.Conv2D(256,(3,3),activation = "relu",padding = "same"))
model.add(tf.keras.layers.Conv2D(256,(3,3),activation = "relu",padding = "same"))
model.add(tf.keras.layers.MaxPool2D())
model.add(tf.keras.layers.Dropout(0.3))
model.add(tf.keras.layers.GlobalAveragePooling2D()) 
model.add(tf.keras.layers.Dense(512,activation="relu"))
model.add(tf.keras.layers.Dense(1,activation="sigmoid")) 

#编译模型
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    loss='binary_crossentropy',
    metrics=['acc']
)

#开始训练
his = model.fit(train_data,epochs=10,steps_per_epoch=len(train_image_path)//BATCH_SIZE,
                validation_data=dev_data,validation_steps=len(dev_image_path)//BATCH_SIZE)
model.save(r"C:\2020人工神经网络\model1.h5") 





