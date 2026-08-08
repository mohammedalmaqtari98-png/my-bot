import telebot

API_TOKEN = "8646517225:AAEPUDPMsgN6D7QG5z98jS45GYHcO5gYn3U"

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(content_types=['photo', 'video', 'document', 'audio', 'voice'])
def handle_media(message):
    try:
        bot.copy_message(message.chat.id, message.chat.id, message.message_id)
        bot.delete_message(message.chat.id, message.message_id)
        print("تم إعادة النشر وحذف الأصلية.")
    except Exception as e:
        print(f"خطأ: {e}")

print("البوت يعمل سحابياً...")
bot.infinity_polling()
