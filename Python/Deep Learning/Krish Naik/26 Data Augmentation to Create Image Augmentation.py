# todo: Methods for augmentation
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
datagen = ImageDataGenerator(             # for flipping the image
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')

# todo: loading dataset and converting to array
img = load_img('data/train/cats/cat.0.jpg')  # Loading the Image
x = img_to_array(img)  # Converting Image into Numpy array with shape (3, 150, 150)
x = x.reshape((1,) + x.shape)  # converting Numpy array into 4D array with shape (1, 3, 150, 150)

# todo: applying augmentation methods to image array
# the .flow() command below generates batches of randomly transformed images
# and saves the results to the `preview/` directory
i = 0
for batch in datagen.flow(x, batch_size=1,
                          save_to_dir='preview', save_prefix='cat', save_format='jpeg'):
    i += 1
    if i > 20:
        break  # otherwise the generator would loop indefinitely
