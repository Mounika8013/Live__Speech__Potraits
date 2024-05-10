## Steps for executing it on Local 

---

## Introduction

Live Speech Portraits is designed to transform digital communication by creating real-time, photorealistic talking-head animations from audio inputs. By harnessing advanced machine learning technologies, this project enhances the realism of virtual interactions to mirror the naturalness of face-to-face conversations.

## Getting Started

### Requirements and Setup

#### Environment Setup
First, set up a dedicated Python environment:
```bash
conda create -n LSP python=3.6
conda activate LSP
```

#### Installation
Clone the repository and install necessary dependencies:
```bash
git clone https://github.com/YuanxunLu/LiveSpeechPortraits.git
cd LiveSpeechPortraits
sudo apt-get install ffmpeg  # Only for Linux users
pip install -r requirements.txt
```

### Demo

#### Prepare the Data
Download the pre-trained models and data from the provided Google Drive links into the `data` folder.

#### Run the Demo
Execute the demo with the following command:
```bash
python demo.py --id May --driving_audio ./data/Input/00083.wav --device cuda
```
Results from the demo will be stored in the `results` folder.


--- 


Here's a concise outline of the steps involved in executing the notebook for inclusion in the README file on GitHub:

---
## Google Coolab
## Live Speech Portraits Notebook

To execute the google coolab code, please use our [Google Colab notebook](https://colab.research.google.com/drive/1EyI5354t9EG5eCuPYPwZZMUJ9etwGsNZ?usp=sharing). This notebook is set up to guide you through the entire process, from setting up your environment to running the inference code.




## Execution Steps for the Notebook

This guide provides a detailed walkthrough of the steps required to execute the code within this notebook effectively:

### 1. **Check CUDA GPU Availability**
   - Verify that a CUDA-capable GPU is available in your setup to leverage accelerated computing capabilities, which are crucial for the performance of deep learning models.

### 2. **Set Up Python Environment and Project Dependencies**
   - Configure your Python environment by installing the required packages and libraries that are essential for running the project.

### 3. **Download Pre-trained Models**
   - Obtain the necessary pre-trained models which are fundamental for the animation process. These models can be downloaded from specified links provided within the notebook.

### 4. **Interactive Selection of Images for Animation**
   - Use the provided interactive tools to select images that will be used for animation. This step involves choosing an image from a predefined directory which will later be animated based on audio input.

### 5. **Running Inference to Animate Image with Audio**
   - Execute the inference script to animate the selected image using an audio file. This process maps the audio inputs to the facial movements in the image, creating a talking-head animation.

### 6. **Displaying the Latest Generated Animation Video**
   - Review the animation video generated by the inference process. This step displays the final output where the static image is transformed into a moving animation that syncs with the provided audio.

### Execution Guidance
To run these steps, ensure each command and instruction is followed as described in the notebook. Proper execution of these steps will lead to the successful animation of images using the designated audio files, viewable directly within the notebook or output directory.

Certainly! Here’s a simplified two-step guide for accessing and using the web application:

---

## How to Use the Web Application

### Step 1: Access and Authenticate
   - Open the Link:After executing the notebook, a URL will be generated in the output. Open this URL in your web browser.
   - Enter the Password:Use the password or endpoint IP provided in the previous output of the notebook to gain access if required.

### Step 2: Upload Content and Generate Animation
   - Capture or Upload an Image:You can either take a picture using your webcam directly through the web application or upload an existing image from your device.
   - Upload an Audio File:Select and upload an audio file. This audio will be used to animate the image.
   - Generate and View Animation:Click the 'Generate Animation' button to process your inputs. The application will then display the animated video where the image mimics the audio.

---

This streamlined approach ensures users can easily access and interact with the web application, allowing for a straightforward experience in creating talking-head animations.

---
