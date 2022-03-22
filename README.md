# cell_detection_AI

#### **USER GUIDE**
### Setup your environment
    
1. Open a command prompt 

With the `cd` command, navigate to the directory where you want to download that git.
```
    git clone https://github.com/dutke/cell_detection_AI.git
```

Download the files from the *doc_data* directory with the link : [***doc_data***](https://drive.google.com/drive/folders/1CN0wtB8tAOkvwMoFn3bnV_cpa7my7MFb?usp=sharing)
Put the files in a folder in darknet root directory with the following structure :
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
Then, browse to the "**/PE**" folder.
    
```
   cd "/PE"
```

 
 1. By doing the training execution on Google Colab, you need to restart the executtion cell after the `^C` error. The weights are saved on every epoch in the backup folder so that you don't start again the training from 0.

#### **History**
### First training

1. The dataset was only composed of 132 annoted frames from 4 videos. The number of epochs was of 2000 with a learning rate of 0.0015. At 1300 epochs, the mAP gave an accuracy of 53% (the accuracy is equal to $\frac{*TP* + *FP*}{*TP* + *FP* + *TN* + *FN*}$, with *TP* the number of true positives, *FP* the number of false positives, *TN* the number of true negatives and *FN* the number of false negatives)
