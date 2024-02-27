from typing import final
from telegram import Update
from telegram.ext import Application,CommandHandler,MessageHandler,filters,ContextTypes
TOKEN :final="6360269794:AAHK7T7kOFEqBYIDMvO-EleixmOIEIncKKA"
BOT_USERNAME:final='@rinku_nitian_bot'
async def start_command(update:Update,context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello Friends! I am nitian bot. thankyou for using me how i can help you ?")

async def help_command(update:Update,context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello Friends! I am nitian bot. Please text your your issue ,so that i can help you.")
    
async def custom_command(update:Update,context: ContextTypes.DEFAULT_TYPE):
      await update.message.reply_text("Hello Friends! I am nitian bot. This is a custom command.")
async def chatgpt_command(update:Update,context: ContextTypes.DEFAULT_TYPE):
      await update.message.reply_text("Hello Friends! I am nitian bot. This is a chatgpt integrated platform ,How can i help you today ?.")
      import openai
      openai.api_key ="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"
      input_response= input("Enter your query:") 
      completion =openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=[{"role": "user","content": input_response}])
      print(completion.choices[0].message.content)     
#handle responses
def handle_response(text:str) -> str: 
    processed:str =text.lower() 
    if 'hello' in processed:
        return "I am good!"     
    if 'How are you' in processed:
        return "I am good!"  
    if "I love this bot" in processed:
        return "Thankyou for your feedback!"
    return "I do not understand What you wrote."

#handle_message
async def handle_message(update:Update,context: ContextTypes.DEFAULT_TYPE):
    message_type:str= update.message.chat.type
    text:str = update.message.text
    print(f'User ({update.message.chat.id}) in {message_type}:"{text}"')
      
    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text : str =text.replace(BOT_USERNAME, '').strip()
            response:str = handle_response(new_text)
        else:
            return
    else:
        response : str = handle_response(text)   
        
    print('BOT:',response)    
    await update.message.reply_text(response)
    
async def error(update:Update,context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')     
if __name__== '__main__':
    print('Starting  nitian Bot...')
    app =Application.builder().token(TOKEN).build()
    #commands
    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('help',help_command))
    app.add_handler(CommandHandler('custom',custom_command))
    app.add_handler(CommandHandler('chatgpt',chatgpt_command))
    #message
    app.add_handler(MessageHandler(filters.TEXT ,handle_message))
    
    
    #Errors
    app.add_error_handler(error)
    
    #Polls the bot
    print('Polling....')
    app.run_polling(poll_interval=3)
   