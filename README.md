# Tensorflow Blob Analysis
A sample project to perform blob analysis on images to detect blobs and analyze their shape features such as the presence, number, area, position, length, and direction of lumps.

## Quick Demo

Here is a demonstration of input and output image. Output image has maskings and bounding boxes around the blobs. The accuracy is perfect and blob shape features are predicted and calculated using the masked area and all these information are stored in proper csv files.

<p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/119240817-02e65680-bb5b-11eb-885f-f4158204a3cc.gif" | width=480>
</p>

The output csv file has the headers:

Blob Number | Blob Area (pixel) | Blob Area (mm2) | Blob Perimeter (pixel) | Blob Perimeter (mm)
--- | --- |--- | --- | --- |

## Theory

This project has 2 main components:

- **training_layer:** This layer provides to perform transfer learning on trained deep learning models using TensorFlow and Keras API. Annotated data (metal blobs for this project) is required to be able to perform training. [VGG annotation tool](https://www.robots.ox.ac.uk/~vgg/software/via/via_demo.html) should be used to annotated the images. In this project, transfer learning is performed on coc trained model but this project provides transfer learning on ImageNet trained model as well. This project basically takes annotated images as input and produces trained model in .h5 format as an output. The output of this layer is used in processing_layer to process the images. The implementation and more detailed information for training_layer can be found in [here](https://github.com/ahmetozlu/tensorflow_blob_analysis/tree/main/training_layer).

<p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/119240192-cd3f6e80-bb56-11eb-9662-b201df5ff869.png" | width=800>
</p>

- **processing_layer:** This layer provides to process images using our own trained model, which is output of training_layer, to produces output images with bounding boxes and maskings. This also provides csv file, which stores blob shapes' information, as an output. It has batch image processing feature so large amount of input images can be processed one by pne automatically using this feature. The implementation and more detailed information for processing_layer can be found in [here](https://github.com/ahmetozlu/tensorflow_blob_analysis/tree/main/processing_layer).

<p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/119240475-68851380-bb58-11eb-81d9-691b36b4c69e.png" | width=800>
</p>


## Application Software Architecture

## Installation

### Setup

### Commands

## Citation
If you use this code for your publications, please cite it as:

    @ONLINE{vdtct,
        author = "Ahmet Özlü",
        title  = "TensorFlow Blob Analysis",
        year   = "2021",
        url    = "https://github.com/ahmetozlu/tensorflow_blob_analysis"
    }

## Author
Ahmet Özlü

## License
This system is available under the MIT license. See the LICENSE file for more info.


