import cv2, os
import subprocess

def write_video_with_audio():
    fps, fourcc = 60, cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('aa.mp4', fourcc, fps, (512, 512))
    for root, dirs, directory in os.walk("no"):
        for i in range(len(directory)):
            img = cv2.imread(root+"/"+directory[i])
            img = cv2.resize(img, (512, 512))
            out.write(img)
    out.release() 
write_video_with_audio()
cmd = 'ffmpeg -i aa.mp4 -vcodec h264 output.mp4'
subprocess.call(cmd, shell=True) 
video_tmp_path = "output.mp4"
audio_path = "data/Input/00083.wav"
output_path = "00083.mp4"
cmd = 'ffmpeg -i "' + video_tmp_path + '" -i "' + audio_path + '" -c:v copy -c:a aac "' + output_path + '"'
subprocess.call(cmd, shell=True) 

