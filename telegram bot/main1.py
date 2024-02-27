from typing import final
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters

TOKEN: final = "YOUR_BOT_TOKEN"
BOT_USERNAME: final = '@rinku_nitian_bot'

def start_command(update: Update, context):
    update.message.reply_text("Hello Friends! I am nitian bot. Thank you for using me. How can I help you?")

def help_command(update: Update, context):
    update.message.reply_text("Hello Friends! I am nitian bot. Please text your issue so that I can help you.")

def custom_command(update: Update, context):
    update.message.reply_text("Hello Friends! I am nitian bot. This is a custom command.")

def handle_response(text: str) -> str: 
    processed = text.lower() 
    if 'hello' in processed or 'how are you' in processed:
        return "I am good!"     
    if "i love this bot" in processed:
        return "Thank you for your feedback!"
    return "I do not understand what you wrote."

def handle_message(update: Update, context):
    message_type = update.message.chat.type
    text = update.message.text
    print(f'User ({update.message.chat.id}) in {message_type}:"{text}"')
    
    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text = text.replace(BOT_USERNAME, '').strip()
            response = handle_response(new_text)
        else:
            return
    else:
        response = handle_response(text)   
    
    print('BOT:', response)    
    update.message.reply_text(response)

def error(update: Update, context):
    print(f'Update {update} caused error {context.error}')    

if __name__ == '__main__':
    print('Starting Bot...')
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('custom', custom_command))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    dp.add_error_handler(error)
    
    print('Polling....')
    updater.start_polling()
    updater.idle()
