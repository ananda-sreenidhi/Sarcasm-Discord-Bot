# Sarcasm-Discord-Bot
A basic Discord bot written in Python that detects whether or not a given statement is sarcastic. (~83% accuracy, model based on Logistic Regression)

## Usage
Install dependencies from `requirements.txt`. 

Then, go to [Discord Developers](https://discordapp.com/developers/applications/me) and create a new application. After filling out the details, click on "Create a Bot User" and confirm. 

Get the bot's token and paste in a file called `token.txt` stored in the same location as `bot.py`. 

Then go to OAuth2 and select "bot" and copy the URL generated, then paste in your browser. Select the server you want to add it to and authorise. You should be good to go!

Once the bot is in your server, you can call it using:

    !detect : predicts whether the latest message in the channel is sarcastic.
    !detect <string> : predicts whether the given string is sarcastic.
