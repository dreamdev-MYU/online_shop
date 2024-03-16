from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Token o'rniga o'z botingizning tokenini qo'yasiz
TOKEN = "6695415590:AAFmonZAOzRDDwueLkhRPxEWEEbSzEGIIRw"

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("""Assalomu alaykum! Buyurtma berish uchun /buyurtma buyrug'ini jo'nating.""")

def buyurtma(update: Update, context: CallbackContext) -> None:
    # Buyurtmangizni shu yerga yozing
    buyurtma = update.message.text
    # Buyurtmani qabul qilish va ishlash qismi
    # Masalan, buyurtmani bazaga saqlab olish, e-mail orqali bildirish, boshqa bot bilan bog'lanish va h.k.
    # Buyurtmani qabul qilish uchun sizning kerakli funksiyalaringizni yozing

    # Buyurtmani qabul qilgandan so'ng foydalanuvchiga javob qaytarish
    update.message.reply_text('Buyurtmangiz qabul qilindi! Tez orada siz bilan bog\'lanamiz.')

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("buyurtma", buyurtma))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
