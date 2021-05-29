# Tensorflow Blob Analysis
A sample project to perform blob analysis on images to detect blobs and analyze their shape features such as the presence, number, area, position, length, and direction of lumps.

## Quick Demo

Here is a demonstration of input and output image. Output image has maskings and bounding boxes around the blobs. Blob shape features are predicted and calculated using the masked area and all these information are stored in proper csv files.

<p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/119240817-02e65680-bb5b-11eb-885f-f4158204a3cc.gif" | width=480>
</p>

The output csv file has these headers to store blob shape properties: Blob Number, Blob Area (pixel), Blob Area (mm2), Blob Perimeter (pixel), Blob Perimeter (mm).

## Theory

This project has 2 main components:

- **[training_layer](https://github.com/ahmetozlu/tensorflow_blob_analysis/tree/main/training_layer):** This layer provides performing transfer learning on pre-trained deep learning models using TensorFlow and Keras API. Basically, transfer learning is performed on the model to fine tune it for our custom cases. We specify our custom cases with our training data. The output of this layer is used in processing_layer to process the images using our own trained deep learning model. The implementation and more detailed information for training_layer can be found in [here](https://github.com/ahmetozlu/tensorflow_blob_analysis/tree/main/training_layer).

<p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/119240192-cd3f6e80-bb56-11eb-9662-b201df5ff869.png" | width=800>
</p>

- **[processing_layer](https://github.com/ahmetozlu/tensorflow_blob_analysis/tree/main/processing_layer):** This layer provides to process images using our own trained model, which is an output of training_layer, to produces output images contain bounding boxes and maskings. This also provides csv file, which stores blob shapes' information, as an output. The implementation and more detailed information for processing_layer can be found in [here](https://github.com/ahmetozlu/tensorflow_blob_analysis/tree/main/processing_layer).

<p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/119240475-68851380-bb58-11eb-81d9-691b36b4c69e.png" | width=800>
</p>


## Installation

1. Clone this repository
2. Install dependencies
   ```bash
   pip3 install -r requirements.txt
   ```
3. Run setup from the repository root directory
    ```bash
    python3 setup.py install
    ``` 
4. Install `pycocotools` from one of these repos. Here are listed the necessary commands:
    ```bash
    pip3 install Cython
    git clone https://github.com/pdollar/coco.git  
    cd coco/PythonAPI
    make
    sudo make install
    sudo python3 setup.py install
    ``` 

## Citation
If you use this code for your publications, please cite it as:

    @ONLINE{
        author = "Ahmet Özlü",
        title  = "TensorFlow Blob Analysis",
        year   = "2021",
        url    = "https://github.com/ahmetozlu/tensorflow_blob_analysis"
    }

## Author
Ahmet Özlü

## License
This system is available under the MIT license. See the LICENSE file for more info.

