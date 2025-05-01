import colorama
from  colorama import Fore, Style
from  textblob import TextBlob

colorama.init()

print(f"{Fore.CYAN}🥰😁Welcome to Sentiment Spy!")
user_name=input(f"{Fore.MAGENTA} Please enter your name:")
while(True):
    if not user_name:
     user_name=("Mystery Agent")
     user_choice=input("type exit to go out of the app")
     if user_choice==("exit"):
        break
     else:
        continue

print(f"welcome {user_name} lets check your emotions at the moment ")
sentiment_type=input("Enter your sentiment: ")
polarity=TextBlob(sentiment_type).sentiment.polarity
if (polarity>0.25):
    
    print (f"{Fore.GREEN}your emotion is positive")
elif(polarity<0.25):
    
    print(f"{Fore.RED}your emotion is negative")
else:
    print(f"{Fore.YELLOW}neutral")