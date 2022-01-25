import html
import random
import time

import Senku.modules.ExtraGifs_strings as ExtraGifs_strings
from Senku import dispatcher
from Senku.modules.disable import DisableAbleCommandHandler
from Senku.modules.helper_funcs.chat_status import is_user_admin
from Senku.modules.helper_funcs.extraction import extract_user
from telegram import ChatPermissions, ParseMode, Update
from telegram.error import BadRequest
from telegram.ext import CallbackContext



def hugbg(update: Update, context: CallbackContext):
    message = update.effective_message
    name = message.reply_to_message.from_user.first_name if message.reply_to_message else message.from_user.first_name
    first = message.from_user.first_name
    reply_animation = message.reply_to_message.reply_animation if message.reply_to_message else message.reply_animation
    reply_animation(
        random.choice(ExtraGifs_strings.HUGBG), caption=f'{first} hugs {name}')


def huggb(update: Update, context: CallbackContext):
    message = update.effective_message
    name = message.reply_to_message.from_user.first_name if message.reply_to_message else message.from_user.first_name
    first = message.from_user.first_name
    reply_animation = message.reply_to_message.reply_animation if message.reply_to_message else message.reply_animation
    reply_animation(
        random.choice(ExtraGifs_strings.HUGGB), caption=f'{first} hugs {name}')


def huggg(update: Update, context: CallbackContext):
    message = update.effective_message
    name = message.reply_to_message.from_user.first_name if message.reply_to_message else message.from_user.first_name
    first = message.from_user.first_name
    reply_animation = message.reply_to_message.reply_animation if message.reply_to_message else message.reply_animation
    reply_animation(
        random.choice(ExtraGifs_strings.HUGGG), caption=f'{first} hugs {name}')


def hugbb(update: Update, context: CallbackContext):
    message = update.effective_message
    name = message.reply_to_message.from_user.first_name if message.reply_to_message else message.from_user.first_name
    first = message.from_user.first_name
    reply_animation = message.reply_to_message.reply_animation if message.reply_to_message else message.reply_animation
    reply_animation(
        random.choice(ExtraGifs_strings.HUGBB), caption=f'{first} hugs {name}')
    

def hug(update: Update, context: CallbackContext):
    update.message.reply_text("Help for hug command- /huggb -Girl Hugging Boy, /hugbg -Boy Hugging Girl, /huggg -Girl Hugging Girl, /hugbb -Boy Hugging Boy")


def pat(update: Update, context: CallbackContext):
    message = update.effective_message
    name = message.reply_to_message.from_user.first_name if message.reply_to_message else message.from_user.first_name
    first = message.from_user.first_name
    reply_animation = message.reply_to_message.reply_animation if message.reply_to_message else message.reply_animation
    reply_animation(
        random.choice(ExtraGifs_strings.PAT), caption=f'{first} pats {name}')

def kiss(update: Update, context: CallbackContext):
    message = update.effective_message
    name = message.reply_to_message.from_user.first_name if message.reply_to_message else message.from_user.first_name
    first = message.from_user.first_name
    reply_animation = message.reply_to_message.reply_animation if message.reply_to_message else message.reply_animation
    reply_animation(
        random.choice(ExtraGifs_strings.KISS), caption=f'{first} kisses {name}')
    

def slap(update: Update, context: CallbackContext):
    message = update.effective_message
    name = message.reply_to_message.from_user.first_name if message.reply_to_message else message.from_user.first_name
    first = message.from_user.first_name
    reply_animation = message.reply_to_message.reply_animation if message.reply_to_message else message.reply_animation
    reply_animation(
        random.choice(ExtraGifs_strings.SLAPS), caption=f'*{first} slaps {name}**')



HUG_HANDLER = DisableAbleCommandHandler("hug", hug, run_async=True)
HUGBG_HANDLER = DisableAbleCommandHandler("hugbg", hugbg, run_async=True)
HUGGB_HANDLER = DisableAbleCommandHandler("huggb", huggb, run_async=True)
HUGGG_HANDLER = DisableAbleCommandHandler("huggg", huggg, run_async=True)
HUGBB_HANDLER = DisableAbleCommandHandler("hugbb", hugbb, run_async=True)
PAT_HANDLER = DisableAbleCommandHandler("pat", pat, run_async=True)
KISS_HANDLER = DisableAbleCommandHandler("kiss", kiss, run_async=True)
SLAP_HANDLER = DisableAbleCommandHandler("slap", slap, run_async=True)

dispatcher.add_handler(HUG_HANDLER)
dispatcher.add_handler(HUGBG_HANDLER)
dispatcher.add_handler(HUGGB_HANDLER)
dispatcher.add_handler(HUGGG_HANDLER)
dispatcher.add_handler(PAT_HANDLER)
dispatcher.add_handler(HUGBB_HANDLER)
dispatcher.add_handler(KISS_HANDLER)
dispatcher.add_handler(SLAP_HANDLER)

__handlers__ = [
    HUGBG_HANDLER, HUGGB_HANDLER, HUGGG_HANDLER, HUGBB_HANDLER, HUG_HANDLER, PAT_HANDLER, KISS_HANDLER, SLAP_HANDLER
]
