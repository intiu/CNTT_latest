import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
       speak("Chào buổi sáng!")
       
    elif hour>=12 and hour<18:
        speak("Chào buổi chiều!")   

    else:
        speak("Chào buổi tối!")  
        
    speak("Tôi là người máy. Vui lòng cho tôi biết bạn muốn gì")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    
    with sr.Microphone() as source:

        print("Ðang nghe...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Ðang ghi âm...")    
        query = r.recognize_google(audio, language='vi-VN')
        print(f"Bạn nói: {query}\n")

    except Exception as e:
        # print(e)    
        print("Làm ơn hãy nhắc lại...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login('ltpntu@gmail.com', 'phuonglove2')
    server.sendmail('ltpntu@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
        
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Wikipedia đang tìm...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("Theo Wikipedia")
            print(results)
            speak(results)
            
        elif 'mở youtube' in query:
            #webbrowser.open("youtube.com")
            sr.Microphone(device_index=1)
            r=sr.Recognizer()
            r.energy_threshold=5000
            with sr.Microphone() as source:
                print("Bạn muốn tìm kiếm")
                audio=r.listen(source)
                try:        
                    text=r.recognize_google(audio, language='vi-VN')
                    print("You said : {}".format(text))
                    url='https://www.youtube.com/results?q='
                    search_url=url+text
                    webbrowser.open(search_url)
                except:
                    print("Không thể tìm thấy nội dung bạn đang tìm")

        elif 'mở google' in query:
            #webbrowser.open("google.com.vn")
            sr.Microphone(device_index=1)
            r=sr.Recognizer()
            r.energy_threshold=5000
            with sr.Microphone() as source:
                print("Bạn muốn tìm kiếm")
                audio=r.listen(source)
                try:        
                    text=r.recognize_google(audio, language='vi-VN')
                    print("You said : {}".format(text))
                    url='https://www.google.co.in/search?q='
                    search_url=url+text
                    webbrowser.open(search_url)
                except:
                    print("Không thể tìm thấy nội dung bạn đang tìm")
            
        elif 'mở stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'mở nhạc' in query:
            music_dir ='C:\\Users\\ASUS\\Desktop\\am_nhac'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
           
        elif 'lời bài hát' in query:
            r = sr.Recognizer()

            audio = 'Dung Yeu Nua Em Met Roi - MIN (online-audio-converter.com).wav'

            with sr.AudioFile(audio) as source:
                audio = r.record(source)
                print ('Đã dịch xong!')

            try:
                text = r.recognize_google(audio)
                print (text)
    
            except Exception as e:
                print (e)

        elif 'thời gian' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'mở code' in query:
            codePath = "C:\\Users\\ASUS\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'mở powerpoint' in query:
            codePath="C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(codePath)

        elif 'mở c' in query:
            codePath="C:\\Program Files (x86)\\Dev-Cpp\\devcpp.exe"
            os.startfile(codePath)
            
        elif 'mở sublime text 3' in query:    
            codePath="C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
            os.startfile(codePath)
            
        elif 'gửi email đến phương' in query:
            try:
                speak("tôi nên nói gì?")
                content = takeCommand()
                to = 'phuong.lt.59cntt@ntu.edu.vn'    
                sendEmail(to, content)
                speak("Email đã được gửi!")
            except Exception as e:
                print(e)
                speak("Xin lỗi bạn. Tôi không thể gửi email này")
        elif 'thoát' in query:

                engine.say("Shutting down")
                engine.runAndWait()
                print("Đã tắt...")
                break
