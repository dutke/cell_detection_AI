# cell_detection_AI

# **USER GUIDE**
## Setup the environment
    
1. Open a command prompt 

With the `cd` command, navigate to the directory where you want to download that git.
```
    git clone https://github.com/dutke/cell_detection_AI.git
```

Download the files from the *doc_data* directory with the link : [***doc_data***](https://drive.google.com/drive/folders/1CN0wtB8tAOkvwMoFn3bnV_cpa7my7MFb?usp=sharing) \
Put the files in a folder placed in the darknet root directory as the following structure :
```
darknet
└───3rdparty
└───backup  
└───build
└───cfg
└───cmake
└───data
└───doc_data
    └───doc_images
        │   (1).jpg
        │   (1).txt
        │   ...
    └───test
        └───video_test
        |   (1).jpg
        |   (2).jpg
        |   ...
        |   FDG82336....
    |   document.data
    |   document.names
    |   document_test.txt
    |   document_training.txt
    |   yolov4.conv.137
    |   yolov4.weights
    |   yolov4_custom.cfg
    |   yolov4_custom_best.weights
│   
└───include
└───obj
└───results
└───scripts
└───src
|CMakeLists.txt
|DarknetConfig.cmake.in
|...

```

Put the ***darknet*** root directory win this git folder such as : 
```
cell_detection_ai
|
└───darknet
    └───3rdparty
    |...
|   custom_network.ipynb
|   image_yolo.ipynb
|   multiple_frame_yolo.ipynb
|   file_renamer_jpg.py
|   file_renamer_txt.py
|   README.md

```

Finally, upload on your Google Drive the *cell_detection _ai* folder such as :

```
drive
└───MyDrive
    └───Colab Notebook
        └───darknet
        |
        |   custom_network.ipynb
        |   ...

```


## Dependencies

The scipts use the following dependencies : 
- numpy 
- opencv==3.4.13.47
- google.colab.patches
- glob
- os

## Highlevel overview of source files

**CARE:** OUR DETECTION ALGORITHMS ONLY SUPPORT *.JPG* OR *.PNG* FILES.

In the top-level directory are executable scripts to train, execute and evaluate the neural network. \
In package `cell_detection_ai` is the main code : 

- `multiple_frame_yolo.ipynb`: Main notebook that applies the YOLO detection algorithm using the **.weights** file of your choice. By default, it uses the *yolov4_custom_best.weights* file. Don't forget to modify the path of the different 
- `image_yolo.ipynb`: A notebook used for debug. It applies the detection algorithm to a single frame. 
- `custom_network.ipynb`: Train the CNN on any set of data you want. All the explanation about the configuration is already in the notebook.
- `file_renamer_jpg.py`: A script to rename all the elements of a folder that end with the extension *.jpg* as *(1).jpg, (2).jpg,...*
- `file_renamer_txt.py`: A script to rename all the elements of a folder that end with the extension *.txt* as *(1).txt, (2).txt.* except the *classes.txt* file. Pay attention that if frame(.jpg file) has an annotation (.txt file) linked to it in the same folder, the frame number and the annotation number will match.


## The doc_data directory

In this directory are all the files I needed for the training and the evaluation of the CNN.

- `./doc_images`: This folder contains the dataset used for the training of the CNN. It needs to contain the pictures and their corresponding annotations from labelImg, plus the `classes.txt` file. The *classes.txt* file corresponds to the labels that were annoted in the pictures.
- `test`: This folder contains an image that was used to evaluate the performance of the training with the `image_yolo.ipynb` scriptn and a folder containing all the frames of a video that was used in the `multiple_frame_yolo.ipynb`.
- `document_test.txt`: A map of the data used for the test.
- `document_training.txt`: A map of the data used for the training.
- `document.data`: A configuration map of the other maps.
- `document.names`: A map of the label for detection.
- `yolov4_custom.cfg`: A configuration file for the trining of the CNN.
- `yolov4.weights`: A file containing the weights obtained after a training on a the COCO dataset.
- `yolov4_custom_best.weights`: A file containing the weights obtained after a training on the dataset in `doc_images`.
- `yolov4.conv.137`: A file used to create the first backups of the weights if the CNN is strating from scratch. 

# **ISSUES**

 1. By doing the training execution on Google Colab, you need to restart the execution cell after the `^C` error. The weights are saved on every epoch in the backup folder so that you don't start again the training from 0.

