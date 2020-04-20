# Hand Grip Type detection model for objects

## Description
This implementation using darknet's pytorch implementation to detect objects and classify them as per the type of grip used by the human hand to interact with the object.

## Grip classificaton

Type of Grip | Example objects taken
-- | -
Key Grip | Keys, Credit Cards
Pinch Grip | Nuts, bolts
Precision Grip | Forcep, Pen
Power Grip | Bottles, Tin Cans
Trigger Grip | Handgun, Hair Dryer

## Usage

### Training

* Copy create_list_images.py inside data/python create_list_images.py && mv list.txt ../train.txt 

* Inside train/ run the following command to create list of absolute file paths
```bash
python create_list_images.py && mv list.txt ../train.txt 
```

* Repeat same for validation/
```bash
python create_list_images.py && mv list.txt ../val.txt 
```

* Edit training/config/coco.data and set train and val path as path of the created text files under data

* Install the environment.yml file

```bash
conda env create -f environment.yml
```

* Run train.py under training -

usage: train.py [-h] [--epochs EPOCHS] [--image_folder IMAGE_FOLDER]
                [--batch_size BATCH_SIZE]
                [--model_config_path MODEL_CONFIG_PATH]
                [--data_config_path DATA_CONFIG_PATH]
                [--weights_path WEIGHTS_PATH] [--class_path CLASS_PATH]
                [--conf_thres CONF_THRES] [--nms_thres NMS_THRES]
                [--n_cpu N_CPU] [--img_size IMG_SIZE]
                [--checkpoint_interval CHECKPOINT_INTERVAL]
                [--checkpoint_dir CHECKPOINT_DIR] [--use_cuda USE_CUDA]

optional arguments:
  -h, --help            show this help message and exit
  --epochs EPOCHS       number of epochs
  --image_folder IMAGE_FOLDER
                        path to dataset
  --batch_size BATCH_SIZE
                        size of each image batch
  --model_config_path MODEL_CONFIG_PATH
                        path to model config file
  --data_config_path DATA_CONFIG_PATH
                        path to data config file
  --weights_path WEIGHTS_PATH
                        path to weights file
  --class_path CLASS_PATH
                        path to class label file
  --conf_thres CONF_THRES
                        object confidence threshold
  --nms_thres NMS_THRES
                        iou thresshold for non-maximum suppression
  --n_cpu N_CPU         number of cpu threads to use during batch generation
  --img_size IMG_SIZE   size of each image dimension
  --checkpoint_interval CHECKPOINT_INTERVAL
                        interval between saving model weights
  --checkpoint_dir CHECKPOINT_DIR
                        directory where model checkpoints are saved
  --use_cuda USE_CUDA   whether to use cuda if available
  
  
* Example command to ignore depreciation warnings, savinf errors in error.txt and log in log.txt
```bash
python -u -W  ignore train.py --epochs 200 --checkpoint_interval 5 --batch_size 4 --weights_path config/yolov3.weights --n_cpu 4 2>error.txt | tee log1.txt 
```

* Your weights after each checkpoint will be stored under checkpoints/

### Testing
```python test.py```
1. Put images to detect inside testing/toDetect/ directory _(Some images giving good output already present)_
1. run test.py
1. your predictions will be saved under prections/

### References
[pytorch darknet training](https://github.com/cfotache/pytorch_custom_yolo_training)
[pytorch darknet testing](https://github.com/cfotache/pytorch_objectdetecttrack)
[Open Images Download Kit](https://github.com/EscVM/OIDv4_ToolKit)
