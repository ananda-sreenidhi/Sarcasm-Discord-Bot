
# Sarcasm-Discord-Bot
A basic Discord bot written in Python that detects whether or not a given statement is sarcastic. (~83% accuracy, model based on Logistic Regression)

Developed by acridexception#5064. (Feel free to add me on Discord :))

## Usage
Install dependencies from `requirements.txt`. 

Then, go to [Discord Developers](https://discordapp.com/developers/applications/me) and create a new application. After filling out the details, click on "Create a Bot User" and confirm. 

Get the bot's token and paste in a file called `token.txt` stored in the same location as `bot.py`. 

Then go to OAuth2 and select "bot" and copy the URL generated, then paste in your browser. Select the server you want to add it to and click "authorize". You should be good to go!

Once the bot is in your server, you can call it using:

    !detect : predicts whether the latest message in the channel is sarcastic.
    !detect <string> : predicts whether the given string is sarcastic.

## Sample Usage
![enter image description here](https://lh3.googleusercontent.com/89OLWJYIPj7ZPOJdSkogrwY1VtBud8Q-iqUY-5MjRx17NjnITx_MUG9GWM2coi-NetDg5e2zyIPv7eMn4L76NqS9w_uEoX44UoZ064P66pjMRovsb8YqEtk0hlubd_CzshqFKJd8C-FBLG7Nd-zL75dwMmT-8vuhSF0XPrhfmkVcxKdKcyha4k2rXCckQpeon615nrBKkgpdyn04OACam2My-vHsek1lMlyPO7cobuikt7ew4VkTF4oU2ujkLAtwgZm9p6JAtiu8LwWtz6oL2aZ7gjOeiIOn0ualS3SLQu_vwKX9IfO5Ajj0_W5K1mN_7sdu50sBLPyyf3GOVqi4f9ZpnOD1ABet0PMEi6E7SfU8-fWB-qOqi7GpUsIfjhqo89btI8GJbjB1WmE06XlZiAS_rnMm8r7pzkTDcRvp3FPD2qG3C0DaBNZsZ60RQtMAv6mwNvcYm_hSC8YUjFWi6Gh2CF1c5Lgxbc5c8V3c9h_-b-fawCYoOIqQu7FJlFSpT_kz7T52z-s1PSTK8x4CnRab71_NyRNOBwdqkMZvx9q1a1ZMGThh0xWUKkTG216NlKbevVeCxUvD3IVFvuCvbCmMzaOhGnh9vVm_0P2mGhWUEFgyTvANVHqJgRhoONEJevy8y1fpyufID4yAxpHsWz780ymuw1EBJ9opQ6uvr8Wcouq3WWsbdbNOB56-=w590-h269-no)
