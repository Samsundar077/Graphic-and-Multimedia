import tkinter as tk
from PIL import Image, ImageTk
from playsound import playsound
import cv2
import threading

def play_audio():
    playsound('sample_audio.mp3')

def play_video():
    cap = cv2.VideoCapture('sample_video.mp4')
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("Video", frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def load_image():
    img = Image.open('sample_image.jpg')
    img = img.resize((300, 300))
    img_tk = ImageTk.PhotoImage(img)
    panel.configure(image=img_tk)
    panel.image = img_tk

window = tk.Tk()
window.title("Multimedia App")

btn_img = tk.Button(window, text="Show Image", command=load_image)
btn_audio = tk.Button(window, text="Play Audio", command=lambda: threading.Thread(target=play_audio).start())
btn_video = tk.Button(window, text="Play Video", command=lambda: threading.Thread(target=play_video).start())

panel = tk.Label(window)
panel.pack()

btn_img.pack(pady=5)
btn_audio.pack(pady=5)
btn_video.pack(pady=5)

window.mainloop()
