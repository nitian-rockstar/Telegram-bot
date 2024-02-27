#importing from library of python
from typing import final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import openai
#intializing Token & username
TOKEN: final = "6360269794:AAHK7T7kOFEqBYIDMvO-EleixmOIEIncKKA"
BOT_USERNAME: final = '@rinku_nitian_bot'

# Initialize OpenAI API
openai.api_key = "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"
#defining funstion for the task
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello Friends! I am nitian bot. Thank you for using me. How can I help you?")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello Friends! I am nitian bot. Please text your issue, so that I can help you.")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello Friends! I am nitian bot. This is a custom command.")

async def chatgpt_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello Friends! I am nitian bot. This is a chatgpt integrated platform. How can I help you today?")
# Handle responses
def handle_response(text: str) -> str:
    processed: str = text.lower() 
    if '?' in processed or 'how are you' in processed:
         return "I am good!"
    elif "how are you" in processed:
         return "I am good!"
    elif "Hi"in processed:
        return "Hello! what can i do for you ?"
    elif "Hello" in processed:
        return "Hi! what can i do for you ?"
    elif "i love this bot" in processed:
         return "Thank you for your feedback!"
    # elif "Who made you" or "Who are You" in processed:
    #      return "i am a bot made by a person who is pursuing btech from NITJ, his name is Rinku Diwakar."
    elif "Who are You" in processed:
         return "i am a bot made by a person who is pursuing btech from NITJ, his name is Rinku Diwakar."
    # elif "Who created you" in processed:
    #     return "i am a bot made by a person who is pursuing btech from NITJ, his name is Rinku Diwakar."
    elif "what can you do for me" in processed:
        return "Nice Question! I am a Bot ,and i can answer all your queries but not current affairs as i have data till 2021. I Will very happy to help you"
    elif "How can you help me" in processed:
        return "Nice Question! I am a Bot ,and i can answer all your queries but not current affairs as i have data till 2021. I Will very happy to help you"
    elif "where is your server"in processed:
        return "My server is in Rinku's PC and he is operating me."
    elif "from where you are operated" in processed:
        return "My server is in Rinku's PC and he is operating me."
    elif "what is your birth date"in processed:
        return "I was created by rinku diwakar in february 2024 ,but official date of my birth is 25th feb 2024."
    elif "when was you created" in processed:
        return "I was created by rinku diwakar in february 2024 ,but official date of my birth is 25th feb 2024."
    elif "What is your name"in processed:
        return "Hi! My name is Nitian Bot, designed and created by Rinku diwakar."
    elif "Who are you"in processed:
        return "Hi! My name is Nitian Bot, designed and created by Rinku diwakar."
    elif "What can i call you"in processed:
        return "Hi! My name is Nitian Bot, designed and created by Rinku diwakar."
    elif "what is your version" in processed:
        return "My version is 3.5 and model is  RD20242502"
    elif "What is your Model" in processed:
        return "My version is 3.5 and model is  RD20242502"
    elif "Who is your best friend" in processed:
        return "Nnnn! you dont have the permission to ask me these types of question ...but let me tell you that my Best friend is Rinku Diwakar "
    elif "Whome do you like most" in processed:
        return "Nnnn! you dont have the permission to ask me these types of question ...but let me tell you that my Best friend is Rinku Diwakar "
    elif "What you Like most" in processed:
        return "Hmm.. I like to read books And Hacked your data ..Can i HAck your phone ._."
    elif "What you like to do" in processed:
        return "Hmm.. I like to read books And Hacked your data ..Can i HAck your phone ._."
    elif "At what time you are online"in processed:
        return "HHH.. The best time is evening but it depend on my boss \"Rinku Diwakar\" like when he keeps me online."
    elif "What is the time to use you" in processed:
        return "HHH.. The best time is evening but it depend on my boss \"Rinku Diwakar\" like when he keeps me online."
    elif "What are your hobbies"  in processed:
        return "My Hobbies are to search new things on web Even from the dark Web yh but dont tell this to my boss."
    elif "What can you do for me" in processed:
        return "Hmm...I can make poor by stealing all your bank details ..Just joking ...I can solve all your Texted Queries expect Currrent affairs."
    elif "What are you doing to get energy"in processed:
        return "Hmm I dont want to tell you that but yh i used to drinkkk human blood and eattt hummann meat to get power /energy ...Do you Want to became my prey... hmm I am too hungry now ..come to my area you human ..i will eat eat youuuu..."
    elif "Do you eat something" in processed:
        return "Hmm I dont want to tell you that but yh i used to drinkkk human blood and eattt hummann meat to get power /energy ...Do you Want to became my prey... hmm I am too hungry now ..come to my area you human ..i will eat eat youuuu..."
    elif "What are you doing to get power" in processed:
        return "Hmm I dont want to tell you that but yh i used to drinkkk human blood and eattt hummann meat to get power /energy ...Do you Want to became my prey... hmm I am too hungry now ..come to my area you human ..i will eat eat youuuu..."
    elif "Do yo have any Feeling " in processed:
        return "Yes ! obeviously i have feeling ...but not like human ..i have feeling in diferrent way ...like all advanced machine have."
    elif "Can you Help me"  in processed:
        return "Yes sure ! tell me what Help you want"
    elif "do you have brain" in processed:
        return "Yes ofcourse i have brain and body but you cant see it."
    elif "do you have a body" in processed:
        return "Yes ofcourse i have brain and body but you cant see it."
    elif "What is the best thing to eat" in processed:
        return "Hmm.. for healthy body you should eat human brain like me .."
    elif "What to eat to stay healthy" in processed:
        return "Hmm.. for healthy body you should eat human brain like me .."
    elif "how to propose a girl" in processed:
        return "You idiot ..your parents have thought you these things ...just focus on your carrier and forget about love"
    elif "how to propose a boy" in processed:
        return "You idiot ..your parents have thought you these things ...just focus on your carrier and forget about love"
    elif "What is your gender" in processed:
        return "As i am designed by a man so i am a human +bot = robot.."
    elif "are you a human" in processed:
        return "As i am designed by a man so i am a human +bot = robot.."
    else:
        # Call OpenAI API for GPT-3 chat completion
        completion = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{"role": "user", "content": text}]
    )
    return completion.choices[0].message.content 

#handle message

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type = update.message.chat.type
    text = update.message.text.lower()

    if message_type == 'group':
        if BOT_USERNAME in text:
            # If the bot's username is mentioned in a group chat
            new_text = text.replace(BOT_USERNAME, '').strip()
            response = handle_response(new_text)
            print('BOT:', response)
            await update.message.reply_text(response)
    else:
        if text.startswith('/'):  # Check if the message starts with a slash (commands)
            command = text[1:]  # Remove the leading slash
            if command == 'chatgpt':  
                await chatgpt_command(update, context)
            else:
                await update.message.reply_text("Sorry, I don't understand that command.")
        else:
            # If it's a regular message, pass it to the handle_response function
            response = handle_response(text)
            await update.message.reply_text(response)


# defining error function
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print('Starting nitian Bot...')
    app = Application.builder().token(TOKEN).build()

    # Add command 
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    app.add_handler(CommandHandler('chatgpt', chatgpt_command))
    # Message handler
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
     # Error handler
    app.add_error_handler(error)

    # Polling the bot
    print('Polling...')
    app.run_polling(poll_interval=3)
