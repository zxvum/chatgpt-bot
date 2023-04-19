import openai_secret_manager
import telebot
import openai
import re

openai.api_key = "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"

bot = telebot.TeleBot("6171102900:AAEY_FEemObkKyCHgNuq5lHLns85LhJEl5Y")

# Handle /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hi! I'm a language model trained by OpenAI. Send me a message and I'll try my best to respond.")

# Handle all other messages
@bot.message_handler(func=lambda message: True)
def generate_response(message):
    try:
        prompt = f"Conversation with user:\nUser: {message}\nAI:"
        print(prompt)
        # Use OpenAI to generate a response
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=1024,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        # Send the generated response back to the user
        bot.reply_to(message, response.choices[0].text)
        print(response.choices[0].text)
    except Exception as e:
        # If an error occurs, send an error message back to the user
        bot.reply_to(message, "Sorry, something went wrong. Please try again later.")

# Start the bot
bot.polling()
