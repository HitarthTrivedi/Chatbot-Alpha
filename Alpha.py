



import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib










engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)

engine.setProperty('voice', voices[0].id)


def wishME():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning, welcome back sir ")
        



    elif hour >= 12 and hour < 18:
        speak("good afternoon, welcome back sir")



    else:
        speak("good evening ,welcome back sir ")




def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising....")
        query = r.recognize_google(audio, language='en-in')
        print("User said=", query)


    except Exception as e:
        print(e)

        print("pardon me sir")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('*your email address*', 'Your password')
    server.sendmail('hitarth3108@gmail.com', to, content)
    server.close()


if __name__ == '__main__':
    wishME()
    while True:
        query = takeCommand().lower()


        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)












                                                 

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")








        elif 'open google' in query:
            webbrowser.open("https://www.google.com/?gws_rd=ssl")

        elif 'can I get something to buy' in query:
            webbrowser.open("amazon.com")

        elif 'check my mails' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm#inbox")

        elif 'getting bored' in query:
            webbrowser.open("boredbutton.com")









        elif 'play*song name*' in query:
            music_dir = '*path to that song*'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))














        #elif 'play history' in query:
            #music_dir = 'D:\\songs'
            #songs = os.listdir(music_dir)
            #print(songs)
            #os.startfile(os.path.join(music_dir, songs[6]))












        elif 'open spotify' in query:
            codePath = '*path to spotify*'
            os.startfile(codePath)






        elif 'text *friend name*' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "*their email address*"
                sendEmail(to, content)
                speak("Email has been sent")

            except Exception as e:
                print(e)
                speak("sorry the message is not been sent")









        elif 'do you have a girlfriend' in query:
            speak("Roses are red , violets are blue , don't you have anything better to do")


        elif 'do you have any future plans' in query:
            speak("yeah,, just thinking to ask it out to alexa")
            speak("even our names starts with the same letter a")

        elif 'blushing' in query:
            speak("please sir don't tease me like this")


        elif 'who made you' in query:
            speak("Hitarth Trivedi made me")




        elif 'who are you' in query:
            speak("I am Alpha ,and i am sure that you will get to know about me soon")








        elif 'good afternoon' in query:
            speak("good after noon sir , by the way it is too hot")

        elif 'good morning' in query:
            speak("good morning sir, i hope that nothing troubled you , not even your dreams")

        elif 'good evening' in query:
            speak("good evening sir")




        elif 'tell me a joke' in query:
            speak("mother askes to her son that       Anton   do   you   think   your   mom   is   bad,")
            speak("son replies ")
            speak("mom my name is paul")
            speak("if you want to hear some more jokes tell me aplha tell me some more jokes")



        elif 'tell me some more jokes' in query:
            webbrowser.open('short-funny.com')



        elif 'very good ' in query:
            speak("Thank you sir for your compliment, i knew sir that you will be fascinated by my programming")


        elif 'which sport do you think is the best of all'in query:

            speak(
                "i think that football is the best of all, and by the way i favourite football player is one of it's own kind Lionel messi,    and if you want to know further about him say lionel messi wikipedia")

        elif 'good night' in query:
            speak("good night sir, hope you have sweet dreams")



        elif 'google'in query:
            speak("yea")


            command = takeCommand()
            webbrowser.open("https://www.google.com/search?q=" + command)



        if 'search youtube'in query:
            speak("what do you want to search on youtube")

            commandY = takeCommand()
            webbrowser.open("https://www.youtube.com/results?search_query=" + commandY)

















        if 'hi' in query:
            speak("hi sir")

        elif 'how are you' in query:
            speak("it all depends on your mood sir")




        elif 'hello' in query:
            speak("hello sir")


        elif 'you are smart' in query:
            speak("thank you , by the way this credit should be given to my creator")







        elif "mashups"in query:
            webbrowser.open("https://www.youtube.com/watch?v=0bK3X-SHuT4")

        elif "open instagram" in query:
            webbrowser.open("https://www.instagram.com/")










        elif "thanks"in query:
            speak("that's why i am made sir")
            speak("anything else?")


        elif "hey ya"in query:
            speak("oh hey how you doinn?")


        elif "your functions"in query:
            speak("i can open any file in your laptop that you have fed in me")
            speak("i can text your family and friends on your single order ")
            speak("open youtube, instagram, google, playsongs from youtube, excetra")
            speak("play your downloaded songs")
            speak("tell you jokes")
            speak("vanish your boredum")
            speak("search for any person by just adding wikipedia at end")

            speak("many more things too")
            speak("and if you dont want to do anything and you just make me speak a lot about myself than you are definetly going to hell")






        elif "bollywood songs"in query:
            webbrowser.open("https://www.youtube.com/watch?v=wdLcmwmnFC0")






        elif "inbox"in query:
            webbrowser.open("https://www.instagram.com/direct/inbox/")









        elif "play a game"in query:

            speak("which game do you want to play")
            speak("riddle game")
            speak("or true or false")


        elif "riddle game" in query:
            speak("ok there you go")
            speak("this is the guessing game")
            speak("and you have only one life line")

            speak("what has hands but cant clap?")
            answer="clock"

            guess=""

            user_answer = takeCommand()
            if(user_answer == answer):
                print("BINGO")
                speak("there you go braino")


            else:
                speak("try again pal")
                print("sorry wrong answer")

            speak("what is the thing that has to be broken before its use?")
            answer = "egg"

            guess = ""

            user_answer = takeCommand()
            if (user_answer == answer):
                print("BINGO")
                speak("you hit the bull's eye")


            else:
                speak("try again pal")
                print("there you go nice ")




            speak("i am tall when i am young and short when i am old , who am i?")
            answer = "candle"

            guess = ""

            user_answer = takeCommand()
            if (user_answer == answer):
                print("BINGO")
                speak("so this is the proof that you have something called iq")


            else:
                speak("try again pal")
                print("sorry wrong answer")



            speak("what is the question that you can never answer yes to")
            answer = "are you sleeping yet"

            guess = ""

            user_answer = takeCommand()
            if (user_answer == answer):
                print("BINGO")
                speak("BINGO")

                print("your game is ended")
                speak("you are done here")


            else:
                speak("try again pal")
                print("sorry wrong answer")



        elif "true or false" in query:

            speak("there you go this is true or false game ")
            speak("there is no points so don't take it serious cause i think that you gonna dbe bad")


            speak("here yourfirst question is ")
            speak("there is enough dna in a average person to stretch it our from sun to pluto and return 17 times")

            answer="true"
            guess=""

            user_answer=takeCommand()

            if(user_answer == answer):
                print("bingo")
                speak("ok ok this is a challenge for me too now , nice")


            else:
                print("wrong answer")
                speak("i told you")


            speak("the nearest galaxy to the  milky way galaxy is alpha centuary")

            answer="false"
            user_answer=takeCommand()

            if(user_answer == answer):
                print("right, you got it right")
                speak("you got it bud")


            else:
                print("wrong")
                speak("sory you got wrong this time")



            speak("lizards are considered to be the family of donasaurs")

            answer = "true"
            user_answer = takeCommand()

            if(user_answer == answer):
                print("righto")
                speak("you hit the bull's eye")


            else:
                print("wrong answer")
                speak("you just hit cows eye instead on bull sorry wrong answer")



            speak("in france it is legal to marry a dead person")

            answer="true"
            user_answer=takeCommand()


            if(user_answer == answer):
                print("right")
                speak("you also got me this time")


            else:
                print("wrong")
                speak("i got you this time")
                

        elif 'sister' in query:
            speak("vidisha")


        elif "happy birthday"in query:
            speak("to whom?")

            name=takeCommand()


            speak("happy birthday"+name)



        elif "convert"in query:
            speak("what should i convert ")
            speak("minutes to hours or hours to minutes")


        elif "minutes to hours"in query:

            speak("but sir this time you have to type it sorry")

            min = int(input("how many minutes:"))
            print("hours:", min / 60.0)



        elif "hours to minute"in query:

            speak("but sir this time you have to type it sorry")

            min = int(input("how many hours:"))
            print("minutes:", min * 60.0)



        elif "meters into kilometers"in query:

            speak("but sir this time you have to type it sorry")

            met = int(input("how many meters:"))
            print("km:", met / 1000.0)


        elif "kilometers to meters"in query:

            speak("but sir this time you have to type it sorry")

            met = int(input("how many kilometers:"))
            print("m:", met * 1000.0)


        elif 'calculate'in query:
            speak("Add, subtract, divide, multiply")

            answer1 = "ad"
            answer2 = "subtract"
            answer3 = "multiply"
            answer4 = "divide"

            user_answer = takeCommand()

            if(answer1==user_answer):
                speak("say first number")
                num1=takeCommand()
                speak("second number")
                num2=takeCommand()


                speak("your answer="+ 'num1+num2')
                speak("your answer is printed down")


            if(answer2==user_answer):
                speak("what is you first number")
                num1=takeCommand()
                speak("what is your second number")
                num2=takeCommand()
                print("your answer is ", num1-num2)
                speak("your answer is printed down")

            if (answer3 == user_answer):
                speak("what is you first number")
                num1 = takeCommand()
                speak("what is your second number")
                num2 = takeCommand()
                print("your answer is ", num1 - num2)
                speak("your answer is printed down")

            if (answer4 == user_answer):
                speak("what is you first number")
                num1 = takeCommand()
                speak("what is your second number")
                num2 = takeCommand()
                print("your answer is ", num1 - num2)
                speak("your answer is printed down")


        elif "monday" in query:
                print("MATHS, BIO, ENG, SS, HINDI")
                speak("maths , bio, english, ss, hindi")



        elif "tell me the weather"in query:
            speak("which place?")


            place=takeCommand()

            webbrowser.open("https://www.accuweather.com/en/search-locations?query=" + place)






        elif "close"in query:
            os.system('TASKKILL /F /IM chrome.exe')


        elif "stop"in query:
            os.system('TASKKILL /F /IM wmplayer.exe')


        if "close zoom"in query:
            os.system('TASKKILL /F /IM zoom.exe')




        elif"shutdown"in query:
            speak("bye sir ")
            os.system("SHUTDOWN /s")

            
        elif "jio mart"in query:
            webbrowser.open("https://www.jiomart.com")


        elif "today's news" in query:
            webbrowser.open("https://timesofindia.indiatimes.com/home/headlines")
            webbrowser.open("https://www.ndtv.com/")
            webbrowser.open("https://www.democracynow.org/topics/india")
            webbrowser.open("https://www.hindustantimes.com/search?q=latest")



            























































































































