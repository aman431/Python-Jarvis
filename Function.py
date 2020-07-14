import jarvis
import datetime
import os
import wikipedia
import webbrowser
import Cal
import operator

#Wishing me jarvis according to the time
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        jarvis.speak("Good Morning")

    elif hour >= 12 and hour < 18:
        jarvis.speak("Good Afternoon")

    else:
        jarvis.speak("Good evening")

    jarvis.speak("I am Jarvis sir! please tell me how may i help you")

#Various operation where user want to execute
def operation():
  while True:
    query = jarvis.takeCommand().lower()

#Reading a Wikipedia according to user want
    if 'wikipedia' in query:
        jarvis.speak('Searching wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        jarvis.speak("According to wikipedia")
        print(results)
        jarvis.speak(results)

    elif 'calculation' in query:
        jarvis.speak('What operation do you want to perform')
        text = jarvis.takeCommand().lower()

        def get_operation(op):
            return {
                '+': operator.add,
                '-': operator.sub,
                '*': operator.mul,
                '/': operator.__truediv__

            }[op]

        def perform(op1,oper,op2):
            op1,op2 = int(op1),int(op2)
            return get_operation(oper)(op1,op2)

        print(perform(*(text.split())))
        jarvis.speak(perform(*(text.split())))

#Telling the time of system to user
    elif 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        jarvis.speak("sir the Time is")
        print(strTime)
        jarvis.speak(strTime)

#open a code according want path u pass
    elif 'open' in query:
        codepath = '/usr/local/share'
        os.system('explore codepath:\bin{}'.format(query.replace('Open','')))
        continue

#search from google open the querie in google
    elif 'search' in query:
        jarvis.speak('yes sir what you want to search')
        print('yes sir what you want to search')
        text = jarvis.takeCommand().lower()

        try:
           #chrome_path = '/usr/bin/firefox /usr/lib/firefox/ etc/firefox /usr/share/man/man1/firefox.1.gz %s'
           print('opening sir...')
           jarvis.speak('opening sir')
           text_path = 'https://www.google.co.in/search?q=' + text
           webbrowser.open(text_path)
           break

        except:
            print('Something went wrong')
            break

    elif 'find' in query:
        jarvis.speak('yes sir what operation do you want to perform')
        text = jarvis.takeCommand().lower()
        Cal.operations(text)

    else:
        if 1:
            # speak('what operation want\'s you')
            # print("what operation want\'s you...")
            # w2n.word_to_num(query)
            for word in query.split(' '):
                if word in Cal.operations.keys():
                    try:
                        # w2n.word_to_num(query)
                        #l = Cal.extract_numbers_from_text(query)
                        r = Cal.operations[word]()#(l[0], l[1]
                        print()
                        break
                    except:
                        print("Something is wrong please retry")
                        break

                else:
                    jarvis.speak('sir this is not in my database')
                    print('sir this is not in my database')
