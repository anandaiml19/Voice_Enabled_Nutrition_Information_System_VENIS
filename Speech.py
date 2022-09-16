import pyttsx3
from skimage import io
import matplotlib.pyplot as plt
fruveg = input("Enter a fruit/vegetable to know the nutrients:")
if fruveg.lower() == 'orange':
    text = "One navel orange of 140 gram provides 73 calories, 1.3 gram of protein, 16.5 gram of carbohydrates and 0.2 gram of fat. Oranges are an excellent source of vitamin C, fiber, and potassium. "
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for sound in voices:
        print("Voice:")
        print(" - ID: %s" % sound.id)
        print(" -Name: %s" % sound.languages)
        print(" -Gender %s" % sound.gender)
        print(" - Age %s" % sound.age)

    en_sound_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
    engine.setProperty('sound', en_sound_id)
    engine.say(text)
    engine.runAndWait()
if fruveg.lower() == 'orange':
        plt.rcParams["figure.figsize"] = [5.50, 3.50]
        plt.rcParams["figure.autolayout"] = True
        fig = "https://i.pinimg.com/564x/77/e5/1c/77e51c27e23c859a121bb443eef11a72.jpg"
        imm = io.imread(fig)
        plt.imshow(imm)
        plt.axis('off')
        plt.show()
if fruveg.lower() == 'apple':
    text = "One medium sized apple of 200 gram provides 104 calories, 0.5 grams of protein, 27.6 grams of carbohydrates, and 0.3 grams of fat. Apples also provide fiber, potassium, and vitamin C.  "
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for sound in voices:
        print("Voice:")
        print(" - ID: %s" % sound.id)
        print(" -Name: %s" % sound.languages)
        print(" -Gender %s" % sound.gender)
        print(" - Age %s" % sound.age)

    en_sound_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
    engine.setProperty('sound', en_sound_id)
    engine.say(text)
    engine.runAndWait()
if fruveg.lower() == 'apple':
    plt.rcParams["figure.figsize"] = [5.50, 3.50]
    plt.rcParams["figure.autolayout"] = True
    fig = "https://i.pinimg.com/564x/10/81/42/108142d48401aa32b3195d34bb44a8fb.jpg"
    imm = io.imread(fig)
    plt.imshow(imm)
    plt.axis('off')
    plt.show()
if fruveg.lower() == 'mango':
    text = "one cup of raw mango pieces of 165 grams provides  99 calories, mostly from carbohydrates. You'll get 25 grams of carbs in a single serving. of that, about 23 grams is naturally occurring sugar, and almost 2.6 grams is fiber, about 0.6 grams of fat, 1.4 grams of protein. "
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for sound in voices:
        print("Voice:")
        print(" - ID: %s" % sound.id)
        print(" -Name: %s" % sound.languages)
        print(" -Gender %s" % sound.gender)
        print(" - Age %s" % sound.age)

    en_sound_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
    engine.setProperty('sound', en_sound_id)
    engine.say(text)
    engine.runAndWait()
if fruveg.lower() == 'mango':
    plt.rcParams["figure.figsize"] = [5.50, 3.50]
    plt.rcParams["figure.autolayout"] = True
    fig = "https://i.pinimg.com/564x/88/b8/38/88b8383f4ffb3b98e471545b67b0097b.jpg"
    imm = io.imread(fig)
    plt.imshow(imm)
    plt.axis('off')
    plt.show()
if fruveg.lower() == 'banana':
    text = "One medium sized banana of 118g provides 105 calories, 27g of carbohydrates, 14.4g of sugars, and 1.3g of protein. Bananas are an excellent source of potassium, and one serving contains 422mg of potassium. "
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for sound in voices:
        print("Voice:")
        print(" - ID: %s" % sound.id)
        print(" -Name: %s" % sound.languages)
        print(" -Gender %s" % sound.gender)
        print(" - Age %s" % sound.age)

    en_sound_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
    engine.setProperty('sound', en_sound_id)
    engine.say(text)
    engine.runAndWait()
if fruveg.lower() == 'banana':
    plt.rcParams["figure.figsize"] = [5.50, 3.50]
    plt.rcParams["figure.autolayout"] = True
    fig = "https://i.pinimg.com/564x/85/9b/0f/859b0fbb26e7efd6c71e956392efecb3.jpg"
    imm = io.imread(fig)
    plt.imshow(imm)
    plt.axis('off')
    plt.show()
if fruveg.lower() == 'grapes':
    text = "One cup of grapes of 92g provides 62 calories, 0.6g of protein, 16g of carbohydrates, and 0.3g of fat. Grapes are an excellent source of vitamins C and K.  "
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for sound in voices:
        print("Voice:")
        print(" - ID: %s" % sound.id)
        print(" -Name: %s" % sound.languages)
        print(" -Gender %s" % sound.gender)
        print(" - Age %s" % sound.age)

    en_sound_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
    engine.setProperty('sound', en_sound_id)
    engine.say(text)
    engine.runAndWait()
if fruveg.lower() == 'grapes':
    plt.rcParams["figure.figsize"] = [5.50, 3.50]
    plt.rcParams["figure.autolayout"] = True
    fig = "https://i.pinimg.com/564x/15/58/95/1558958328c8b7f138279865939362e2.jpg"
    imm = io.imread(fig)
    plt.imshow(imm)
    plt.axis('off')
    plt.show()
if fruveg.lower() == 'carrot':
    text = "One medium sized carrot of 61g provides 25 calories, 0.5g of protein, 6g of carbohydrates, and 0g of fat. Carrots are an excellent source of vitamin K, fiber, and vitamin A.  "
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for sound in voices:
        print("Voice:")
        print(" - ID: %s" % sound.id)
        print(" -Name: %s" % sound.languages)
        print(" -Gender %s" % sound.gender)
        print(" - Age %s" % sound.age)

    en_sound_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
    engine.setProperty('sound', en_sound_id)
    engine.say(text)
    engine.runAndWait()
if fruveg.lower() == 'carrot':
    plt.rcParams["figure.figsize"] = [5.50, 3.50]
    plt.rcParams["figure.autolayout"] = True
    fig = "https://i.pinimg.com/564x/4f/a8/f7/4fa8f706d8d22d78a4df6a4b0caabf56.jpg"
    imm = io.imread(fig)
    plt.imshow(imm)
    plt.axis('off')
    plt.show()
if fruveg.lower() == 'beetroot':
    text = "One cup of raw red beetroot of 136g provides 58 calories, 2.2g of protein, 13g of carbohydrates, and 0.2g of fat. Beets are an excellent source of vitamin C, fiber, and potassium "
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for sound in voices:
        print("Voice:")
        print(" - ID: %s" % sound.id)
        print(" -Name: %s" % sound.languages)
        print(" -Gender %s" % sound.gender)
        print(" - Age %s" % sound.age)

    en_sound_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
    engine.setProperty('sound', en_sound_id)
    engine.say(text)
    engine.runAndWait()
if fruveg.lower() == 'beetroot':
    plt.rcParams["figure.figsize"] = [5.50, 3.50]
    plt.rcParams["figure.autolayout"] = True
    fig = "https://i.pinimg.com/564x/28/fb/f6/28fbf68b46f3fa93aa0a655dbed762ad.jpg"
    imm = io.imread(fig)
    plt.imshow(imm)
    plt.axis('off')
    plt.show()
if fruveg.lower() == 'tomato':
    text = "One small tomato of 91g provides 16 calories, 0.8g of protein, 3.5g of carbohydrates, and 0.2g of fat. Tomatoes are an excellent source of vitamin C, fiber, and vitamin K. "
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for sound in voices:
        print("Voice:")
        print(" - ID: %s" % sound.id)
        print(" -Name: %s" % sound.languages)
        print(" -Gender %s" % sound.gender)
        print(" - Age %s" % sound.age)

    en_sound_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
    engine.setProperty('sound', en_sound_id)
    engine.say(text)
    engine.runAndWait()
if fruveg.lower() == 'tomato':
    plt.rcParams["figure.figsize"] = [5.50, 3.50]
    plt.rcParams["figure.autolayout"] = True
    fig = "https://i.pinimg.com/564x/e1/6b/01/e16b01cac19b7db280beb8890a00109c.jpg"
    imm = io.imread(fig)
    plt.imshow(imm)
    plt.axis('off')
    plt.show()
if fruveg.lower() == 'cucumber':
    text = "One-half cup of sliced cucumber of 52g, with the peel, provides 8 calories, 0.3g of protein, 1.9g of carbohydrates, and 0.1g of fat. Cucumbers are a good source of potassium and vitamins K and C. "
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for sound in voices:
        print("Voice:")
        print(" - ID: %s" % sound.id)
        print(" -Name: %s" % sound.languages)
        print(" -Gender %s" % sound.gender)
        print(" - Age %s" % sound.age)

    en_sound_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
    engine.setProperty('sound', en_sound_id)
    engine.say(text)
    engine.runAndWait()
if fruveg.lower() == 'cucumber':
    plt.rcParams["figure.figsize"] = [5.50, 3.50]
    plt.rcParams["figure.autolayout"] = True
    fig = "https://i.pinimg.com/564x/d3/a6/7f/d3a67f913209e98619248bf0ff82390e.jpg"
    imm = io.imread(fig)
    plt.imshow(imm)
    plt.axis('off')
    plt.show()

else:
    print("enter a proper fruit")
    #proo.spetxt(text)
    #timg = img.imread('orange.png')
    #plt.imshow(timg)
    #plt.title("Oranges")
    #plt.show()

#def nutr(fruveg):
#nutr(fruveg)


