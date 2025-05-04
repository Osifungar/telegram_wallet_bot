from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = '7218020350:AAFsiB6uBxM8D0m08CazUJ2T6ECTDZEHxIw'

# תפריט ראשי עם כפתורים
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("מה זה Telegram Wallet?", callback_data='wallet')],
        [InlineKeyboardButton("איך משתמשים בארנק?", callback_data='how')],
        [InlineKeyboardButton("למה כדאי להשתמש?", callback_data='why')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("ברוך הבא! 👋\nבחר אחת מהאפשרויות:", reply_markup=reply_markup)

# טיפול בלחיצה על כפתור
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == 'wallet':
        await query.edit_message_text(
            "🪙 *Telegram Wallet* הוא שירות שמאפשר שליחת וקבלת מטבעות דיגיטליים (כמו TON) בתוך טלגרם עצמה, בלי צורך באפליקציות אחרות.",
            parse_mode='Markdown'
        )
    elif query.data == 'how':
        await query.edit_message_text(
            "📌 איך מתחילים:\n1. חפש בטלגרם את הבוט @wallet\n2. לחץ על Start\n3. פתח ארנק ותתחיל להשתמש!",
        )
    elif query.data == 'why':
        await query.edit_message_text(
            "✅ היתרונות של הארנק:\n- שימוש קל ומהיר\n- מאובטח ע\"י טלגרם\n- אידיאלי לשליחת טיפים ותשלומים בין חברים"
        )

# הגדרת הבוט
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

app.run_polling()
