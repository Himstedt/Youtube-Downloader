import tkinter as tk
from pytube import YouTube
import moviepy.editor as mp
import speech_recognition as sr

window = tk.Tk()
window.geometry("900x550")
window.title("MasterLoader")
window.grid_columnconfigure(0, weight=1)

def disable_enable_button():
    check_button2.config(state=normal if var1.get() else disalbed)


def download_Youtube():
    if text_input.get():
        user_input = text_input.get()
        payload = {"text": user_input}
        yt = YouTube(user_input)

        #text_response =("Title: ", yt.title)

        #print("Number of views: ", yt.views)

        #print("Length of video: ", yt.length, "seconds")

        #print("Ratings: ", yt.rating)

        #print(yt.streams.filter(progressive=True))

        ys = yt.streams.get_highest_resolution()

        out_file = ys.download('Downloads')
        text_response ="Download complete!!"
        if (var1.get() == 1):
            clip = mp.VideoFileClip(out_file)
            clip.audio.write_audiofile(out_file.replace(".mp4", ".wav"))
        if (var2.get() == 1):
            r = sr.Recognizer()
            with sr.AudioFile('The new old people are going to suck  Lachlan Patterson.wav') as source:
                audio = r.listen(source)
                try:
                    text = r.recognize_google(audio)
                    print('Working on...')
                    print(text)
                except:
                    print('Sorry... run again...')
    else:
        text_response = "Text Input Can't Be Empty!"

    textwidget = tk.Text()
    textwidget.insert(tk.END, text_response)
    textwidget.grid(row=3, column=0, sticky="WE", padx=10, pady=10)


welcome_label = tk.Label(window,
                        text="Welcome! Insert a Youtube URL",
                        font=("Helvetica", 15))
welcome_label.grid(row=0, column=0, sticky="N", padx=20, pady=10)

text_input = tk.Entry()
text_input.grid(row=1, column=0, sticky="WE", padx=25)
download_button = tk.Button(text="DOWNLOAD YOUTUBE VIDEO", command=download_Youtube)
download_button.grid(row=2, column=0, sticky="WE", padx=10, pady=10)
var1 = tk.IntVar()
check_button = tk.Checkbutton(text="Seperate Audio", variable=var1, onvalue = 1, offvalue = 0, command=disable_enable_button).grid(row=4, sticky="W", padx=10, pady=10)
var2 = tk.IntVar()
check_button2 = tk.Checkbutton(text="Audio Trancsription", variable=var2, onvalue = 1, offvalue = 0).grid( row=5, sticky="W", padx=10, pady=10)






if __name__ == "__main__":
    window.mainloop()
