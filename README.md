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

# **ISSUES**

 1. By doing the training execution on Google Colab, you need to restart the execution cell after the `^C` error. The weights are saved on every epoch in the backup folder so that you don't start again the training from 0.





#### **History**
### First training

1. The dataset was only composed of 132 annoted frames from 4 videos. The number of epochs was of 2000 with a learning rate of 0.0015. At 1300 epochs, the mAP gave an accuracy of 53% (the accuracy is equal to $\frac{*TP* + *FP*}{*TP* + *FP* + *TN* + *FN*}$, with *TP* the number of true positives, *FP* the number of false positives, *TN* the number of true negatives and *FN* the number of false negatives)
