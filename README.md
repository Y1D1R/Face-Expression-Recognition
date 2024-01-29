# Face-Expression-Recognition
## Overview
This repository contains a Python application for emotion recognition using facial expressions.

The application utilizes computer vision techniques and deep learning models to analyze facial expressions , aiming to detect and classify emotions based on input images or video streams. The graphical user interface (GUI) is developed using PySide2.

## Introduction

Human communication involves two main aspects: verbal (auditory) and non-verbal (visual). In the realm of non-verbal communication, facial expressions play a crucial role. 

Recognizing emotional expressions is particularly significant in fields like psychiatry, providing unique insights into the emotional states of patients. This technology extends its applications beyond the medical domain, finding utility in areas such as road safety and human resources.

## Facial Expression Analysis
### Definition

Facial expression analysis is the science of analyzing and deciphering various expressions that can appear on a human face. This involves utilizing computer vision methods to translate facial expressions into emotions and classify them. 

The process includes face detection, feature extraction from detected faces, and emotion classification.

### Facial Expression

A facial expression visually represents an individual's mental state, cognitive activity, physiological condition, personality, and psychopathology. It relies on three fundamental features: the mouth, eyes, and eyebrows. 

There are seven universal facial expressions detectable on a face: anger, disgust, fear, joy, sadness, surprise, and neutrality.

## Basic Architecture for Emotion Recognition

Emotion analysis involves three phases, each with a well-defined function:
### Detection Phase
The detection of the human face is a crucial step in computer vision, aiming to determine the region of the human face in real-time images or videos. Its complexity arises from the significant variability in faces, encompassing factors such as skin color and the presence or absence of hair, among others.

To perform facial detection, we have adopted the approach proposed by P. Viola & M. Jones, based on Haar cascades, specifically designed for object detection. It's noteworthy that training this model requires a substantial number of positive images (containing a face) and negative images (without a face).

The algorithmic process can be explained in three distinct steps:

* Calculation of Haar Features: This involves extracting relevant features from the input images using the Haar cascades technique.
* Creation of Integral Images: Integral images are created to facilitate the rapid computation of rectangular features.
* Utilization of AdaBoost Method: AdaBoost is employed to boost the performance of the detection model by combining weak classifiers into a strong one.
### Extraction Phase

This phase is designed to extract meaningful information from facial expressions, employing primarily two distinct methods:

* Local Method Based on Geometric Features:
  
This method focuses on specific facial features, leveraging geometric characteristics to capture localized information. It identifies key facial landmarks and analyzes their spatial relationships to understand the nuances of expression. Common geometric features include the position and shape of the eyes, nose, and mouth.

* Global Method Based on Appearance:

In contrast to the local method, the global approach considers the entire facial image as a holistic entity. It utilizes well-established statistical analysis techniques to capture the overall appearance and expressions. This involves analyzing the distribution of pixel intensities, texture patterns, and other visual cues across the entire face.
### Classification Phase

Once all the features from the facial region have been extracted, the final step in an automatic facial expression analysis system is the classification of these features.

Specifically, this classification involves grouping the extracted features based on their similarities. Various classifiers are employed for this purpose, including artificial neural networks and linear classifiers. These classifiers use the information extracted from the facial expressions to categorize them into specific emotion classes.
## Database

The FER2013 database from Kaggle was used for training and testing the models.

It consists of grayscale images of 48x48 pixels, each categorized into seven emotions: anger, disgust, fear, joy, sadness, surprise, and neutrality.

The training set includes 28,709 examples, and the public test set includes 3,589 examples.


## Models

Different models, including MobileNetV2, ResNet50, and VGG19, were used for emotion recognition.

