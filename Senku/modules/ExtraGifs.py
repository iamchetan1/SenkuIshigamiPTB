








def hugbg(update: Update, context: CallbackContext):
    message = update.effective_message
    name = message.reply_to_message.from_user.first_name if message.reply_to_message else message.from_user.first_name
    first = message.from_user.first_name
    reply_animation = message.reply_to_message.reply_animation if message.reply_to_message else message.reply_animation
    reply_animation(
        random.choice(ExtraGifs_strings.HUGBG), caption=f'{first} hugs {name}')

@run_async
def huggb(update: Update, context: CallbackContext):
    message = update.effective_message
    name = message.reply_to_message.from_user.first_name if message.reply_to_message else message.from_user.first_name
    first = message.from_user.first_name
    reply_animation = message.reply_to_message.reply_animation if message.reply_to_message else message.reply_animation
    reply_animation(
        random.choice(ExtraGifs_strings.HUGGB), caption=f'{first} hugs {name}')

@run_async
def huggg(update: Update, context: CallbackContext):
    message = update.effective_message
    name = message.reply_to_message.from_user.first_name if message.reply_to_message else message.from_user.first_name
    first = message.from_user.first_name
    reply_animation = message.reply_to_message.reply_animation if message.reply_to_message else message.reply_animation
    reply_animation(
        random.choice(ExtraGifs_strings.HUGGG), caption=f'{first} hugs {name}')

@run_async
def hugbb(update: Update, context: CallbackContext):
    message = update.effective_message
    name = message.reply_to_message.from_user.first_name if message.reply_to_message else message.from_user.first_name
    first = message.from_user.first_name
    reply_animation = message.reply_to_message.reply_animation if message.reply_to_message else message.reply_animation
    reply_animation(
        random.choice(ExtraGifs_strings.HUGBB), caption=f'{first} hugs {name}')
    
@run_async
def hug(update: Update, context: CallbackContext):
    update.message.reply_text("Help for hug command- /huggb -Girl Hugging Boy, /hugbg -Boy Hugging Girl, /huggg -Girl Hugging Girl, /hugbb -Boy Hugging Boy")

@run_async
def pat(update: Update, context: CallbackContext):
    message = update.effective_message
    name = message.reply_to_message.from_user.first_name if message.reply_to_message else message.from_user.first_name
    first = message.from_user.first_name
    reply_animation = message.reply_to_message.reply_animation if message.reply_to_message else message.reply_animation
    reply_animation(
        random.choice(ExtraGifs_strings.PAT), caption=f'{first} pats {name}')

@run_async
def kiss(update: Update, context: CallbackContext):
    message = update.effective_message
    name = message.reply_to_message.from_user.first_name if message.reply_to_message else message.from_user.first_name
    first = message.from_user.first_name
    reply_animation = message.reply_to_message.reply_animation if message.reply_to_message else message.reply_animation
    reply_animation(
        random.choice(ExtraGifs_strings.KISS), caption=f'{first} kisses {name}')
    


HUG_HANDLER = DisableAbleCommandHandler("hug", hug)
HUGBG_HANDLER = DisableAbleCommandHandler("hugbg", hugbg)
HUGGB_HANDLER = DisableAbleCommandHandler("huggb", huggb)
HUGGG_HANDLER = DisableAbleCommandHandler("huggg", huggg)
HUGBB_HANDLER = DisableAbleCommandHandler("hugbb", hugbb)
PAT_HANDLER = DisableAbleCommandHandler("pat", pat)
KISS_HANDLER = DisableAbleCommandHandler("kiss", kiss)


dispatcher.add_handler(HUG_HANDLER)
dispatcher.add_handler(HUGBG_HANDLER)
dispatcher.add_handler(HUGGB_HANDLER)
dispatcher.add_handler(HUGGG_HANDLER)
dispatcher.add_handler(PAT_HANDLER)
dispatcher.add_handler(HUGBB_HANDLER)
dispatcher.add_handler(KISS_HANDLER)

__handlers__ = [
    HUGBG_HANDLER, HUGGB_HANDLER, HUGGG_HANDLER, HUGBB_HANDLER, HUG_HANDLER, PAT_HANDLER, KISS_HANDLER
]
