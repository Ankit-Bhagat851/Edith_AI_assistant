import pyttsx3

engine=pyttsx3.init()   # object creation
engine.setProperty('rate',200)  #set the rate of Jarvis
engine.setProperty('volume',1)   #set the volume of Jarvis
voices=engine.getProperty('voices') #get details of current voice
#print(voices[0]) 
for voice in voices:
    # to get the info. about various voices in our PC
    print("Voices")
    print("Voice Name %s"%voice.name)
    print("Voice ID %s"%voice.id)
    print("Voice Age %s"%voice.age)
    print("Voice Gender %s"%voice.gender)
    print("Voice Language %s"%voice.languages)
    

engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_ZIRA_11.0')    
#set the voice, istead of full id you can use voices[0] or voices[1]


engine.say("Hi Ankit, this is Jarvis.")
engine.runAndWait()
engine.stop()
