import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator


model = load_model(r"bovine_breed_classifier_final.keras")


dataset_path = r"indian_bovine_breeds"
datagen = ImageDataGenerator(rescale=1.0/255)
train_generator = datagen.flow_from_directory(
    dataset_path,
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical',
    shuffle=False
)


class_indices = train_generator.class_indices
breed_labels = {v: k for k, v in class_indices.items()}


def predict_breed(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)


    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions)


    return breed_labels[predicted_class]
