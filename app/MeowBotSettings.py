from os.path import exists
from colorama import Fore
from json import load, dump
from urllib.request import urlopen
def printGood(text):
    print(Fore.GREEN, text, Fore.RESET)
def printError(text):
    print(Fore.RED, text, Fore.RESET)
MeowBotConfigUrl = "https://gitlab.com/OpenSourceBlackCat/MeowBotAssets/-/raw/main/config/MeowBotConfig.json"
def jsonFetch():
    global configBotFunction, optionBotConfig, inputBotString
    internalMeowBotConfigFile = urlopen("https://gitlab.com/OpenSourceBlackCat/meowbotassets/-/raw/main/config/internalMeowBotSetting.json")
    internalMeowBotConfig = load(internalMeowBotConfigFile)
    configBotFunction = internalMeowBotConfig["MeowConfigFile"]["configFunction"]
    optionBotConfig = internalMeowBotConfig["MeowConfigFile"]["optionConfig"]
    inputBotString = internalMeowBotConfig["MeowConfigFile"]["inputString"]
def configValidator(meowBotConfig, configFunction ,optionConfig, inputString):
    if configFunction == "botName" or configFunction == "botUrl":
        if meowBotConfig["MeowBotConfig"][configFunction] == "":
            print("\n")
            readingBot = str(input(Fore.BLUE+inputString+Fore.RESET)).lower()
            if configFunction == "botUrl": 
                readingBot = readingBot.replace("https://www.youtube.com/channel/", "")
            meowBotConfig["MeowBotConfig"][configFunction] = meowBotConfig["MeowBotConfig"][configFunction].replace(meowBotConfig["MeowBotConfig"][configFunction], str(readingBot))
            printGood("Settings Saved Successfully")
        else:
            pass
    elif configFunction == "emojiLimit" or configFunction == "wordLimit" or configFunction == "sayDelay" or configFunction == "timeOutTimeNormal" or configFunction == "timeOutTimeMod":
        if meowBotConfig["MeowBotConfig"][configFunction] == "":
            print("\n")
            try:
                readingBot = int(input(Fore.BLUE+inputString+Fore.RESET))
                meowBotConfig["MeowBotConfig"][configFunction] = meowBotConfig["MeowBotConfig"][configFunction].replace(meowBotConfig["MeowBotConfig"][configFunction], str(readingBot))
                printGood("Settings Saved Successfully")
            except: 
                printError("Invalid Option Entered!")
                configValidator(meowBotConfig=meowBotConfig, configFunction=configFunction, optionConfig=optionConfig, inputString=inputString)
        else:
            pass
    else:
        optionConfigList = optionConfig.split(", ")
        if meowBotConfig["MeowBotConfig"][configFunction] not in optionConfigList:
            print("\n")
            readingBot = str(input(Fore.BLUE+inputString+Fore.RESET)).lower()
            if readingBot in optionConfigList:
                meowBotConfig["MeowBotConfig"][configFunction] = meowBotConfig["MeowBotConfig"][configFunction].replace(meowBotConfig["MeowBotConfig"][configFunction], str(readingBot))
                printGood("Settings Saved Successfully")
            else:
                printError("Invalid Option Entered!")
                configValidator(meowBotConfig=meowBotConfig, configFunction=configFunction, optionConfig=optionConfig, inputString=inputString)
    meowBotConfigFile = open("config/MeowBotConfig.json", "w")
    dump(meowBotConfig, meowBotConfigFile)
        
def configCheck(meowBotConfig):
    jsonFetch()
    print("Meow Meow Meow!!!!", meowBotConfig)
    for i in range(len(configBotFunction)):
        print(meowBotConfig, configBotFunction[i], optionBotConfig[i])
        configValidator(meowBotConfig=meowBotConfig, configFunction=configBotFunction[i], optionConfig=optionBotConfig[i], inputString=inputBotString[i])
    
def configRun():
    if exists("MeowBotConfig.json"):
        meowBotConfigFile = open("config/MeowBotConfig.json", "r")
        try:
            meowBotConfig = load(meowBotConfigFile)
            configCheck(meowBotConfig=meowBotConfig)
        except:
            MeowBotConfigDefault = load(urlopen(MeowBotConfigUrl))
            with open("config/MeowBotConfig.json", "w") as configDefault:
                configDefault.write(str(MeowBotConfigDefault).replace("'", '"'))
            configRun()
    else:
        MeowBotConfigDefault = load(urlopen(MeowBotConfigUrl))
        with open("config/MeowBotConfig.json", "w") as configDefault:
            configDefault.write(str(MeowBotConfigDefault).replace("'", '"'))
        configRun()