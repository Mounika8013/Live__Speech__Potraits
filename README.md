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

This version of the README file is structured to provide clear, concise instructions for setting up and running the Live Speech Portraits project, ensuring it is accessible for new users.
