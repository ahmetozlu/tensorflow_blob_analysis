# Training Layer

It performs transfer learning to train just for heads of pre-trained Mask R-CNN model to fine tune the model for our custom cases. We specify our custom cases with our own training data.

## Training steps

1. Annotate your data using the [VGG Image Annotator Tool](http://www.robots.ox.ac.uk/~vgg/software/via/via-1.0.6.html). You can find sample annotated data in [here](https://github.com/ahmetozlu/tensorflow_blob_analysis/tree/main/training_layer/data).

2. Seperate your annotated training images under the [val](https://github.com/ahmetozlu/tensorflow_blob_analysis/tree/main/training_layer/data/val) and [train](https://github.com/ahmetozlu/tensorflow_blob_analysis/tree/main/training_layer/data/train) folders with 30 percentage for val and 70 percentage for train.

3. To set the detection minimum confidence value, please update [this line](https://github.com/ahmetozlu/tensorflow_blob_analysis/blob/main/training_layer/training_main.py#L57).

4. Run the command to start to training:

       python3 custom.py train --dataset=./data --weights=coco

5. The frozen inference graph (.h5) will be saved after each epoch under the log directory that is given on the console at the beginning of the training process.

