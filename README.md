

# [COLAB LINK](https://colab.research.google.com/drive/1EyI5354t9EG5eCuPYPwZZMUJ9etwGsNZ?usp=sharing)
# LIVE SPEECH PORTRAITS: REAL-TIME PHOTOREALISTIC TALKING-HEAD ANIMATION -Team -10
Contributions: - Supraj Bejugam, Arun Kusuma, Vaibhavi Rachamalla,Prakathesh Kumarasamy Samynathan ,Mounika Devabhaktuni


Live Speech Portraits is designed to transform digital communication by creating real-time, photorealistic talking-head animations from audio inputs. By harnessing advanced machine learning technologies, this project enhances the realism of virtual interactions to mirror the naturalness of face-to-face conversations.

Link to Original Github-[https://github.com/YuanxunLu/LiveSpeechPortraits/tree/main)

Link to Project Report-[Report](https://docs.google.com/document/d/1bEy8TEzwLRFBtvq0ZIUokv3UQtq91Z2Fo6JcgcQGzTI/edit?usp=sharing)

## Link to Google Coolab Live Speech Portraits Notebook

To execute the google coolab code, please use our [Google Colab notebook](https://colab.research.google.com/drive/1EyI5354t9EG5eCuPYPwZZMUJ9etwGsNZ?usp=sharing). This notebook is set up to guide you through the entire process, from setting up your environment to running the inference code.

## How to Install Manually

Ensure your system meets the following requirements for successful installation:

- **Operating System:** Tested on Windows 10, but should work on Linux (not tested)
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

1.npm install localtunnel

2.import urllib

print("Password/Enpoint IP for localtunnel is:",urllib.request.urlopen('https://ipv4.icanhazip.com').read().decode('utf8').strip("\n")) 

3.!streamlit run app.py &>/content/logs.txt & 

4.!npx localtunnel --port 8501








