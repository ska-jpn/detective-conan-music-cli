from playsound import playsound

ask = input("Music detective conan (Y/N) \n > ")
if (ask == 'Y'):
    playsound('../sound/conan.mp3')
else:
    quit()

