import speech_recognition as sr
import os
import pyttsx3
import webbrowser
import openai
import datetime
from config import apikey

openai.api_key = apikey
def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()




def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            query =r.recognize_google(audio,language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some error occurred"


def chat(query):
    chatstr = ""
    print(chatstr)
    chatstr += "Jarvis: "
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant with knowledge about various topics."},
            {"role": "user", "content": query},
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    try:
        say(response["choices"][0]["message"]["content"])
        chatstr += f"{response['choices'][0]['message']['content']}\n"
        print(chatstr)
    except Exception as e:
        say("Some error occurred")




def ai(query):#can be saved in the .txt file
    system_message = "You are a helpful assistant with knowledge about various topics."
    text = f"OpenAI response for Prompt: {query} \n *************************\n\n"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": query},
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    try:
        text += response["choices"][0]["message"]["content"]
        with open(f"Openai_output/{query[8:]}.txt", "w") as f:
            f.write(text)
        say(text)
    except Exception as e:
        say("Some error occurred")



if __name__ == "__main__":


    say("Hello How may I Help you")

    while(1):
        print("Listening for requests")
        say("Listening for requests")
        query = takecommand()


        if query.lower() == "close it": 
            say("Thank you")
            break
        

        if "open" in query.lower():
            sites = [["youtube","http://www.youtube.com"]]
            for site in sites:
                if f"open {site[0]}".lower() in query.lower():
                    say(f"Opening {site[0]}")
                    webbrowser.open(site[1])

            apps = [["Discord", r"C:\Users\hp\OneDrive\Desktop\Discord.lnk"]]
            for app in apps:
                if f"open {app[0]}".lower() in query.lower():
                    say(f"Opening {app[0]}")
                    os.system(f"start {app[1]}")

                
            if "open video" in query.lower():
                videopath = r"C:\Users\hp\Downloads\We.mp4"
                os.system(f"start {videopath}")

            if "open video" in query.lower():
                musicpath = r"C:\Users\hp\Downloads\We.mp4"
                os.system(f"start {musicpath}")

        elif "the time" in query.lower():
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir time is {hour} {min} minutes")
        
        else:
            if "using ai".lower() in query.lower():
                ai(query)
            else:
                chat(query)
