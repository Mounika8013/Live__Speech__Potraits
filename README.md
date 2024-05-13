

# [COLAB LINK](https://colab.research.google.com/drive/1EyI5354t9EG5eCuPYPwZZMUJ9etwGsNZ?usp=sharing)
# LIVE SPEECH PORTRAITS: REAL-TIME PHOTOREALISTIC TALKING-HEAD ANIMATION -Team -10
Contributions: - Supraj Bejugam, Arun Kusuma, Vaibhavi Rachamalla,Prakathesh Kumarasamy Samynathan ,Mounika Devabhaktuni


Live Speech Portraits is designed to transform digital communication by creating real-time, photorealistic talking-head animations from audio inputs. By harnessing advanced machine learning technologies, this project enhances the realism of virtual interactions to mirror the naturalness of face-to-face conversations.

## Abstract:
This project harnesses advanced deep learning techniques to create photorealistic talking-head animations directly from audio input. Our approach integrates speech representation learning, head pose estimation from audio, and video-based facial reenactment to produce animations that are not only realistic but also dynamically correspond to the nuances of spoken audio. The system architecture is designed to efficiently handle real-time processing challenges, ensuring scalability and integration across platforms. This repository contains all necessary scripts, pretrained models, and detailed steps for setting up the environment, executing the scripts, and deploying the model both locally and via Google Colab and also a real time web application to  capture an image using webcam and generate the output.
![alt text](https://github.com/Mounika8013/Live__Speech__Potraits/blob/main/doc.png)


Link to Original Github-[https://github.com/YuanxunLu/LiveSpeechPortraits/tree/main)

Link to Project Report-[Report](https://docs.google.com/document/d/1bEy8TEzwLRFBtvq0ZIUokv3UQtq91Z2Fo6JcgcQGzTI/edit?usp=sharing)

Link to Google Cooolab -[Google Colab notebook](https://colab.research.google.com/drive/1EyI5354t9EG5eCuPYPwZZMUJ9etwGsNZ?usp=sharing)

Link to recorded real time ouput video It tells how to execute Real time application the output for this mentioned in below link-[link](https://github.com/Mounika8013/Live__Speech__Potraits/blob/6bea0c148cd73997ac8a421a7a7d1300a6018d81/Output%20Recorded%20video/video1576803031.mp4)





Output link-[Output link](https://github.com/Mounika8013/Live__Speech__Potraits/blob/23fdecf6899646384a7675ab70d5e28356f6f447/Output%20Recorded%20video/final%20output%20.mp4)


## Link to Google Coolab Live Speech Portraits Notebook

To execute the google coolab code, please use our [Google Colab notebook](https://colab.research.google.com/drive/1EyI5354t9EG5eCuPYPwZZMUJ9etwGsNZ?usp=sharing). This notebook is set up to guide you through the entire process, from setting up your environment to running the inference code.

1.It includes everything from setting up your environment to running the inference code. Each section of the notebook is well-documented with instructions and comments to ensure you can easily understand and follow the procedures.

2.Additionally, the notebook is designed to be interactive, allowing you to modify parameters and immediately see the effects, thereby enhancing your learning and experimentation experience.



## How to Install Manually(Local Implementation)
Link to google Drive-[Google Drive](https://drive.google.com/drive/folders/1rV9TOFbnv34LdKmxE_UFVKGnhzsGQlOk?usp=drive_link)

Ensure your system meets the following requirements for successful installation:

- **Operating System:** Tested on Windows 10,and MAC
- **Python Version:** Python 3.6
- **Deep Learning Framework:** PyTorch 1.7 (lower versions may work but are not tested)
- **Additional Software:** FFmpeg is required for combining audio with silent generated videos

### Environment Setup

We recommend setting up a new conda environment specifically for this project:
```bash
conda create -n LSP python=3.6
conda activate LSP
 ```



### Installation Steps



1.**Clone the Repository**
   - Clone the Live Speech Portraits repository from GitHub:
     ```bash
     git clone https://github.com/YuanxunLu/LiveSpeechPortraits.git
     cd LiveSpeechPortraits
     ```

2.**Install FFmpeg**
   - For Windows, please check [FFmpeg's official site](https://ffmpeg.org/download.html) for installation instructions.
   - For Linux users, install FFmpeg using:
     ```bash
     sudo apt-get install ffmpeg
     ```

3. **Install Dependencies**
   - Install the required Python packages:
     ```bash
     pip install -r requirements.txt
     ```
4. **Download Pretrained Models**
- Download the pre-trained models and data from [Google Drive](https://drive.google.com/drive/folders/1sHc2xEEGwnb0h2rkUhG9sPmOxvRvPVpJ?usp=sharing) to the `data` folder.  Five subjects data are released (May, Obama1, Obama2, Nadella and McStay).

### Running the Demo

Execute the demo script to animate portraits using provided audio files:
```bash
python demo.py --id May --driving_audio ./data/Input/00083.wav --device cuda
```
Results will be stored in the `results` folder.Now you view in the [Results](https://github.com/Mounika8013/Live__Speech__Potraits/tree/577a5204dd83c2f45f67ac485868c75fe5c9018d/results) on the browser.

## Execute App

The steps include(which are provided in cocolab last cells [Google Colab notebook](https://colab.research.google.com/drive/1EyI5354t9EG5eCuPYPwZZMUJ9etwGsNZ?usp=sharing)) :

To run the app, you'll need to follow these steps:

1. **Install LocalTunnel**: You can install LocalTunnel via npm using the following command:
   ```
   npm install -g localtunnel
   ```

2. **Import urllib**: If you're running this code outside of Python, you might not be able to use the `urllib` library directly. You can achieve similar functionality using Node.js's `http` or `axios` module. Here's an example using `axios`.Now after executing it you will get a password which you have to enter after openning the link generated in step4
   ```javascript
   const axios = require('axios');

   axios.get('https://ipv4.icanhazip.com')
     .then(response => {
       console.log("Password/Endpoint IP for localtunnel is:", response.data.trim());
     })
     .catch(error => {
       console.error('Error fetching IP:', error);
     });
   ```

3. **Run the Streamlit App**: You can run the Streamlit app using the following command:
   ```
   streamlit run app.py &> logs.txt &
   ```

4. **Run LocalTunnel**: Once your Streamlit app is running, you can use LocalTunnel to expose it to the internet. Run the following command:
   ```
   npx localtunnel --port 8501
   ```
   This command will provide you with a public URL that you can share to access your Streamlit app remotely.

Make sure you have your Streamlit app (`app.py`) in the correct directory, and you have the necessary permissions to run these commands. Additionally, if you're using the code outside of a Python environment, ensure you have Node.js installed to execute the JavaScript code.







