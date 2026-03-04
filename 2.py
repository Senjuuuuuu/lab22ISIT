import telebot

bot = telebot.TeleBot("8532835857:AAHFT2JXEGB0RCrCX2nhuRQErpjjCaUXcMo")

@bot.message_handler(content_types=['voice'])
def handle_voice_message(message):
    bot.reply_to(message, "спс за гс😘")

bot.polling()
