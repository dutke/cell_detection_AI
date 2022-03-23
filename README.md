# cell_detection_AI

# **USER GUIDE**
## Setup the environment
  
  
1. At first, open a new notebook in [Google Colab](https://colab.research.google.com/)

2. Download the files from [this git](https://github.com/dutke/cell_detection_AI.git).  
```
    from google.colab import drive
    drive.mount('/content/drive')

    %cd "/content/drive/MyDrive/Colab Notebooks"

    !git clone https://github.com/dutke/cell_detection_AI.git
    
    %cd ./cell_detection_AI
    %pwd # display: /content/drive/MyDrive/Colab Notebooks/cell_detection_AI
    
    # The 2 last lines are here to save the changes on your Google Drive directly.
    
    drive.flush_and_unmount()
    print('All changes made in this colab session should now be visible in Drive.')
```

3. Then you need to download the *Darknet network*. You can do it from this [git.](https://github.com/AlexeyAB/darknet) or,  if you want to do it directly in Google Colab to save the *darknet* folder in your Drive with the easiest path, execute the command lines **below** at the beginning of your notebook. 

```   
    !git clone https://github.com/AlexeyAB/darknet
    
    %cd ./darknet
```

4. Download the files from the *doc_data* directory with the link : [***doc_data***](https://drive.google.com/drive/folders/1CN0wtB8tAOkvwMoFn3bnV_cpa7my7MFb?usp=sharing) \
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

5. If this is not already the case, put the ***darknet*** root directory win this git folder such as : 
```
cell_detection_AI
|
└───darknet
    └───3rdparty
    |...
|
|   custom_network.ipynb
|   image_yolo.ipynb
|   multiple_frame_yolo.ipynb
|   file_renamer_jpg.py
|   file_renamer_txt.py
|   README.md

```

4. Finally, your Google Drive should present a path to the *cell_detection _AI* folder such as :

```
drive
└───MyDrive
    └───Colab Notebook
        └───cell_detection_AI
            └───darknet
            |
            |   custom_network.ipynb
            |   ...

```

## Compile the Darknet network

**CARE: Please refer to the `custom_network.ipynb` notebook for the modifications you have to do in the `Makefile` before compiling darknet.**


> Open the **makefile** file and change these lines

> GPU=1 <br>
> CUDNN=1 <br>
> OPENCV=1 <br> 
> *Line 20, comment*: <br>
> `# ARCH= -gencode arch=compute_20,code=[sm_20,sm_21]` <br>
          `-gencode arch=compute_30, code=...` <br>

> For K80 GPU, add in *line 61* :<br>
> `ARCH= -gencode arch=compute_37, code=sm_37`



Now you can compile the network. To do so, execute the command lines **below**. (They are from the `custom_network.ipynb` notebook. Executing that notebook will execute this step for you) 

```   
    %cd "/content/drive/MyDrive/Colab Notebooks/cell_detection_AI/darknet"
    
    !chmod +rwx ./*
    
    !make
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
- `./test`: This folder contains an image that was used to evaluate the performance of the training with the `image_yolo.ipynb` script and a folder containing all the frames of a video that was used in the `multiple_frame_yolo.ipynb`. If you don't want to change the path in the `multiple_frame_yolo.ipynb` notebook, put the frames of the video in a folder like in *video_test*. (PS: you can put raw_data and rename them with the `file_renamer_jpg.py` script)
- `document_test.txt`: A map of the data used for the test.
- `document_training.txt`: A map of the data used for the training.
- `document.data`: A configuration map of the other maps.
- `document.names`: A map of the label for detection.
- `yolov4_custom.cfg`: A configuration file for the trining of the CNN.
- `yolov4.weights`: A file containing the weights obtained after a training on a the COCO dataset.
- `yolov4_custom_best.weights`: A file containing the weights obtained after a training on the dataset in `doc_images`.
- `yolov4.conv.137`: A file used to create the first backups of the weights if the CNN is strating from scratch. 



# **MAJOR ISSUES SOLUTIONS**

 1. In `custom_network.ipynb`, by executing the training on Google Colab, you need to restart the execution cell after the `^C` error. The weights are saved every hundred of epochs in the backup folder so that you don't start again the training from 0.
 2. Normally, all the other issues should be avoided by following the guided comments in the notebooks. Nonetheless, if you still have troubles, you can contact me.

