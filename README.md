# BoneTumor-Vision

## Introduction
**BoneTumor Vision** is an innovative medical imaging application that combines tumor detection and bone-related object detection capabilities. This application empowers healthcare professionals with a powerful tool for diagnosing medical conditions related to both tumors and bones.

## Features
* **Tumor Detection**: Utilizes state-of-the-art machine learning models to identify and localize tumors within medical images.
* **Bone-Related Object Detection**: Detects and categorizes bone-related anomalies, including fractures and joint conditions, providing precise diagnostic insights.
* **Wide Range of Classes**: Supports multiple classes such as "elbow positive," "fingers positive," "forearm fracture," "humerus fracture," "shoulder fracture," and "wrist positive" for comprehensive bone-related diagnostics.
* **Intuitive User Interface**: User-friendly interface designed for ease of use by medical practitioners and researchers.
* **Fast and Efficient**: Enables quick and accurate medical image analysis, facilitating timely decision-making.
* **Versatile Applications**: Useful in radiology, orthopedics, and various medical specialties.

## About The Model
**BoneTumor Vision** harnesses the power of two separate Faster R-CNN models, both featuring ResNet-50 backbones. These models are meticulously fine-tuned to address distinct yet critical aspects of medical imaging: tumor detection and bone-related object detection.

## Tumor Detection Model
* **Model Name**: TumorVision
* **Architecture**: Faster R-CNN with ResNet-50 Backbone
* **Input Image Size**: 640x640 pixels
* **Training Data**: The TumorVision model has been fine-tuned on a diverse dataset comprising medical images with a primary focus on tumor detection. It has been meticulously trained to excel in identifying and localizing tumors with exceptional precision.

**https://universe.roboflow.com/tfg-2nmge/axial-dataset**


## Bone-Related Object Detection Model
+ **Model Name**: BoneVision
+ **Architecture**: Faster R-CNN with ResNet-50 Backbone
+ **Input Image Size**: 640x640 pixels
+ **Training Data**: The BoneVision model is trained on a comprehensive dataset that encompasses various bone-related anomalies, including fractures and joint conditions. This model provides precise categorization and localization of these bone-related objects within medical images.

**https://universe.roboflow.com/veda/bone-fracture-detection-daoon**

## Customization
* **Fine-Tuning** : While these models are pre-trained and fine-tuned for specific tasks, they are adaptable and can be further fine-tuned on custom medical datasets to suit unique clinical requirements.
* **Integration**: Both TumorVision and BoneVision models can seamlessly integrate into various medical imaging workflows and applications.

## Getting Started : 

```
pip install -r requirements.txt
```

```
git clone --depth 1 https://github.com/tensorflow/models
pip install numpy --upgrade

```

```
# Install the Object Detection API
cd models/research/
protoc object_detection/protos/*.proto --python_out=.
cp object_detection/packages/tf2/setup.py .
python -m pip install .

```

```
python Download_weights.py
streamlit run app.py
```
