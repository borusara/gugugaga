import html

from telegram.ext.filters import Filters
from telegram import Update, message, ParseMode
from telegram.ext import CallbackContext

from Messi.modules.helper_funcs.decorators import enmucmd, enmumsg
from Messi.modules.helper_funcs.channel_mode import user_admin, AdminPerms
from Messi.modules.sql.antichannel_sql import antichannel_status, disable_antichannel, enable_antichannel

@enmucmd(command="antichannelmode", group=100)
@user_admin(AdminPerms.CAN_RESTRICT_MEMBERS)
def set_antichannel(update: Update, context: CallbackContext):
    message = update.effective_message
    chat = update.effective_chat
    args = context.args
    if len(args) > 0:
        s = args[0].lower()
        if s in ["yes", "on"]:
            enable_antichannel(chat.id)
            message.reply_html(text=gs(chat.id, "active_antichannel").format(html.escape(chat.title)))
        elif s in ["off", "no"]:
            disable_antichannel(chat.id)
            message.reply_html(text=gs(chat.id, "disable_antichannel").format(html.escape(chat.title)))
        else:
            message.reply_text(text=gs(chat.id, "invalid_antichannel").format(s))
        return
    message.reply_html(
        text=gs(chat.id, "status_antichannel").format(antichannel_status(chat.id), html.escape(chat.title)))

@enmumsg(Filters.chat_type.groups, group=110)
def eliminate_channel(update: Update, context: CallbackContext):
    message = update.effective_message
    chat = update.effective_chat
    bot = context.bot
    if not antichannel_status(chat.id):
        return
    if message.sender_chat and message.sender_chat.type == "channel" and not message.is_automatic_forward:
        message.delete()
        sender_chat = message.sender_chat
        bot.ban_chat_sender_chat(sender_chat_id=sender_chat.id, chat_id=chat.id)
        
def helps(chat):
    return gs(chat, "antichannel_help")

__mod_name__ = "Anti Channel"

__help__ ="""
──「 Anti-Channels 」──

    ⚠️ WARNING ⚠️

IF YOU USE THIS MODE, THE RESULT IS IN THE GROUP FOREVER YOU CAN'T CHAT USING THE CHANNEL

Anti Channel Mode is a mode to automatically ban users who chat using Channels. 
This command can only be used by Admins.

/antichannelmode <'on'/'yes'> : enables anti-channel-mode
/antichannelmode <'off'/'no'> : disabled anti-channel-mode
"""
