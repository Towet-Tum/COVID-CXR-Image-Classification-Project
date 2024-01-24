import os
import tensorflow as tf
from tensorflow.keras.preprocessing_image import ImageDataGenerator
from cnnClassifier.entity.config_entity import TrainingConfig


class Training:
    def __init__(self, config: TrainingConfig):
        self.config = config 

    def train_val_gen(self):
        # Set your dataset directory
        train_dir = os.path.join("artifacts", "data_preprocessing", "split_dataset", "train")
        val_dir = os.path.join("artifacts", "data_preprocessing", "split_dataset", "val")
        

        # Use ImageDataGenerator for data augmentation and normalization
        train_datagen = ImageDataGenerator(rescale=1./255, shear_range=0.2, 
                                           zoom_range=0.2, horizontal_flip=True)
        val_datagen = ImageDataGenerator(rescale=1./255)

        # Create data generators
        train_generator = train_datagen.flow_from_directory(train_dir, target_size=(self.config.imgsz, 
                                                                                    self.config.imgsz),
                                                            batch_size=self.config.batch_size, 
                                                            class_mode='categorical')

        val_generator = val_datagen.flow_from_directory(val_dir, target_size=(self.config.imgsz, 
                                                                              self.config.imgsz),
                                                        batch_size=self.config.batch_size,
                                                          class_mode='categorical')

        # Set the number of training steps
        return train_generator, val_generator
    
    def train(self):
        pretrained_model = tf.keras.applications.VGG16(weights=self.config.weights, 
                                                       include_top=self.config.include_top, 
                                                       input_shape=[self.config.imgsz
                                                                    , self.config.imgsz, 3])
        pretrained_model.trainable=False
        vgg16_model = tf.keras.Sequential([
            pretrained_model,
            tf.keras.layers.GlobalAveragePooling2D(),
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dense(3, activation='softmax')
        ])

        train_generator, val_generator = self.train_val_gen()
    
        steps_per_epoch = train_generator.samples // self.config.batch_size
        validation_steps = val_generator.samples // self.config.batch_size

        checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(self.config.model_path, save_best_only=True)

        early_stopping_callback = tf.keras.callbacks.EarlyStopping(
            monitor="val_accuracy",patience=5, restore_best_weights=True
        )

        vgg16_model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
        history = vgg16_model.fit(train_generator, steps_per_epoch=steps_per_epoch, 
                                  epochs=self.config.epochs,
                            validation_data=val_generator, 
                            validation_steps=validation_steps,
                            callbacks=[checkpoint_callback,early_stopping_callback])