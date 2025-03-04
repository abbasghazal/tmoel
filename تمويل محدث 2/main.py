import os,requests
from Plugin.RadPLugin import MangSession
from Plugin.dbs import *
from Plugin.apis import *
from Plugin.dbs import Givt,statck
from Plugin.tempdata import USER_TEMP
from Plugin.functions import *
from Plugin.RTools import dataS, START_DELET_TIMER_AD, RAND_CODE
import shutil
import zipfile

datas = dataS()
Db = data()
if not os.path.isdir('dbs'):
    os.mkdir('dbs')
try:
    import telebot, json, os, time, re, threading, schedule
    from telebot import TeleBot
    from telebot import types
    from kvsqlite.sync import Client as uu
    from telebot.types import InlineKeyboardButton as btn, InlineKeyboardMarkup as mk
    import asyncio

    import time
    import sqlite3
    import requests
    import random
    from user_agent import generate_user_agent
    import datetime
    import base64
    import ipaddress
    import struct
    from pathlib import Path
    from typing import Type
    import shutil
    import zipfile
    import aiosqlite
    from opentele.api import APIData
    from pyrogram.session.internals.data_center import DataCenter
    from telethon import TelegramClient
    from telethon.sessions import StringSession
    import secrets
    from opentele.api import API, APIData
    from pyrogram.client import Client

except:
    os.system('python3 -m pip install telebot pyrogram tgcrypto kvsqlite pyromod==1.4 schedule')
    import telebot, json, os, time, schedule
    from telebot import TeleBot
    import telebot
    from telebot import types
    from kvsqlite.sync import Client as uu
    from kvsqlite.sync import Client as uu
    from telebot.types import InlineKeyboardButton as btn, InlineKeyboardMarkup as mk

stypes = ['member', 'administrator', 'creator']

stk = statck()

link_price = db.get("link_price") if db.exists("link_price") else 200

bk = mk(row_width=1).add(btn('• رجــوع •', callback_data='back'))
db.set('force', [])
token_bot = "8192202802:AAGk54Spl91BlBWEXjvchTLw9r0NHTPRSrM"

token_helper = "7957958501:AAHCEMTenDTYj6OA3v0AVDNyT6g1WC_5sqc" #توكن بوت المساعد

bot2 = TeleBot(token=token_helper,num_threads=45,threaded=True,skip_pending=True,parse_mode='Markdown', disable_web_page_preview=True)

bot = TeleBot(token=token_bot,num_threads=45,threaded=True,skip_pending=True,disable_web_page_preview=True)

bot2 = TeleBot(token=token_helper,num_threads=45,threaded=True,skip_pending=True,parse_mode='Markdown', disable_web_page_preview=True)

b = telebot.TeleBot(token_bot)
bbb = telebot.TeleBot(token_helper)

bot_info = b.get_me()
bot_username = bot_info.username

bot_infos = bbb.get_me()
bot_trans = bot_infos.username

temp_data = {}

import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, LabeledPrice

USER_DATA = {}

def get(user_id):
    return USER_DATA.get(user_id, {})

def set(user_id, data):
    USER_DATA[user_id] = data

db_path = "order_count.db"
gems_db_path = "gems.db"

def create_order_table():
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS order_stats (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            total_orders INTEGER
                        )''')
        
        cursor.execute("SELECT COUNT(*) FROM order_stats")
        if cursor.fetchone()[0] == 0:
            cursor.execute("INSERT INTO order_stats (total_orders) VALUES (0)")

        conn.commit()

def read_total_orders():
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        
        cursor.execute("SELECT total_orders FROM order_stats WHERE id = 1")
        result = cursor.fetchone()

    return result[0] if result else 0

def write_total_orders(total_orders):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        
        cursor.execute("UPDATE order_stats SET total_orders = ? WHERE id = 1", (total_orders,))
        conn.commit()

def create_gems_table():
    with sqlite3.connect(gems_db_path) as conn:
        c = conn.cursor()
        
        c.execute('''CREATE TABLE IF NOT EXISTS users
                     (id INTEGER PRIMARY KEY, gems INTEGER)''')
        conn.commit()

def get_gems(user_id):
    with sqlite3.connect(gems_db_path) as conn:
        c = conn.cursor()
        
        c.execute('SELECT gems FROM users WHERE id = ?', (user_id,))
        result = c.fetchone()

    return result[0] if result else 0

def set_gems(user_id, gems):
    with sqlite3.connect(gems_db_path) as conn:
        c = conn.cursor()
        
        c.execute('REPLACE INTO users (id, gems) VALUES (?, ?)', (user_id, gems))
        conn.commit()

create_order_table()
create_gems_table()

total_orders = read_total_orders()

if not db.get('accounts'):
    db.set('accounts', [])
    pass
if not db.get('accounts_t'):
    db.set('accounts_t', [])
if not db.get('chat_blacklist'):
    db.set('chat_blacklist', [])
sudos = 6848908141 #الادمن
if not db.get("admins"):
    db.set('admins', [sudos, 6848908141, ])
if not db.get('badguys'):
    db.set('badguys', [])
if not db.get('force'):
    db.set('force', [])
if not db.get('products_{service}'):
    db.set('products_{service}', [])
def force(channel, userid):
    try:
        x = bot.get_chat_member(channel, userid)
        ##print(x)
    except:
        return True
    if str(x.status) in stypes:
        ##print(x)
        return True
    else:
        ##print(x)
        return False
bbs = token_bot
bbb = token_helper

add_gems_enabled = False

def CeckAnjoens(id):
    REs =Db.Get(id)
    
    for chatID in REs:
        ##print(chatID)
        Status = requests.get(f"https://api.telegram.org/bot{token_helper}/getChatMember?chat_id={chatID}&user_id={id}").json()
        ##print(Status)
        if Status["result"]["status"] == "left":
            ##print("0000000000000000000000000000000000000")
            bot.send_message(chat_id=int(id), text=f"• تم خصم منك 20 نقطة لأنك غادرت من قناة {chatID} .")
            b = db.get(f'user_{id}')
            b['coins']-=20
            db.set(f'user_{id}', b)
            Db.de(id)

@bot.message_handler(commands=['admin'])
def admin_message(message):
    user_id = message.from_user.id

    if user_id in db.get("admins") or user_id == sudos:
        keys_ = mk()
        btn01 = btn('إحصائيات البوت', callback_data='stats')
        btn02 = btn("إذاعة عامة", callback_data='cast')
        btn05 = btn('حظر شخص', callback_data='banone')
        btn06 = btn('الغاء حظر', callback_data='unbanone')

        btn11 = btn('اضافة قناة', callback_data='setforce')
        btn11111 = btn('عرض القنوات', callback_data='view_forced_channels')
        btn10 = btn('اضافه نقاط ', callback_data='addpoints')
        les = btn('خصم نقاط', callback_data='lespoints')
        btn03 = btn('اضافة ادمن', callback_data='addadmin')
        btn04 = btn('مسح ادمن', callback_data='deladmin')
        btn012 = btn('عرض الأدمنية', callback_data='admins')
        btn014 = btn('كشف حساب', callback_data='get_info')
        btn017 = btn('تعيين نقاط الدخول', callback_data='entre_bot')
        bblk = btn('القنوات المحظور تمويلها', callback_data='show_banned')
   
        keys_.add(btn05, btn06)
        keys_.add(btn01)
        keys_.add(btn02)
        keys_.add(btn10, les)
        keys_.add(btn014)
        keys_.add(btn03, btn04)
        keys_.add(btn012)
        keys_.add(btn11, btn11111)
        keys_.add(btn017)
        keys_.add(bblk)

        bot.reply_to(message, '<strong>• اهلا بك في لوحه التحكم الخاصه ببوت التمويل الخاص بك</strong>', reply_markup=keys_)

@bot.message_handler(regexp='^/start$')
def start_message(message):
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name

    if username and '_' in username:
        if any(char.isdigit() for char in username.split('_')):
            username = username 
        else:
            username = username.replace('_', '')

    if user_id not in USER_TEMP:
        USER_TEMP.update({user_id: {'trans': {'id': None}, 'call': {'id': None}, 'code': {'id': None}}})

        if not db.exists(f'user_{user_id}'): 
            user_data = {
                'id': user_id,
                'first_name': first_name,
                'username': username,
                'coins': 0
            }
            db.set(f'user_{user_id}', user_data)

        good = 0
        users = db.keys('user_%') 

        for ix in users:
            try:
                user_data = db.get(ix) 
                if 'id' in user_data:
                    good += 1
            except Exception as e:
                continue 

        try:
            bot.send_message(
                chat_id=sudos, 
                text=f'٭ تم دخول شخص جديد الى البوت الخاص بك 👾\n\n• معلومات العضو الجديد\n\n• الاسم : {message.from_user.first_name}\n• المعرف : @{message.from_user.username}\n• الايدي : {message.from_user.id}')
        except Exception as e:
            print(f"Error sending message: {e}")

    btn059 = btn('.', callback_data='zip_all')
    a = ['leave', 'member', 'vote', 'spam', 'userbot', 'forward', 'linkbot', 'view', 'poll', 'react', 'reacts']

    for temp in a:
        db.delete(f'{temp}_{user_id}_proccess')

    keys = telebot.types.InlineKeyboardMarkup(row_width=2)

    if user_id in db.get('badguys'):
        return

    do = db.get('force')
    if do is not None:
        markup = types.InlineKeyboardMarkup()

        all_subscribed = True
        for channel in do:
            chat_info = bot.get_chat(chat_id="@" + channel)
            channel_name = chat_info.title

            try:
                x = bot.get_chat_member(chat_id="@" + channel, user_id=user_id)
                subscription_status = "✅ مشترك" if str(x.status) in stypes else "❌ غير مشترك"

                if str(x.status) not in stypes:
                    all_subscribed = False
            except Exception as e:
                subscription_status = "❌ غير مشترك"

            channel_button = types.InlineKeyboardButton(text=channel_name, url=f"https://t.me/{channel}")
            status_button = types.InlineKeyboardButton(text=subscription_status, callback_data=f"status_{channel}")

            markup.add(channel_button, status_button)

        check_subscription_button = types.InlineKeyboardButton(text="تحقق من الاشتراك", callback_data="check_subscription")
        markup.add(check_subscription_button)

        if not all_subscribed:
            bot.send_message(message.chat.id, "📝┇عذراً، عليك الأشتراك في قنوات البوت أولاً", reply_markup=markup)
            return
        else:
            send_user_buttonsesr(message)

    else:
        send_user_buttonsesr(message)

@bot.callback_query_handler(func=lambda call: call.data == 'check_subscription')
def check_subscription(call):
    user_id = call.from_user.id
    do = db.get('force') 

    all_subscribed = True
    for channel in do:
        try:
            x = bot.get_chat_member(chat_id="@" + channel, user_id=user_id)
            
            if str(x.status) not in stypes: 
                all_subscribed = False
                break
            else:
                if not db.exists(f"subscribed_{channel}_{user_id}"):
                    db.set(f"subscribed_{channel}_{user_id}", True)

                    current_channel_data = do.get(channel, {})
                    if 'subscribed_members' not in current_channel_data:
                        current_channel_data['subscribed_members'] = []

                    current_channel_data['subscribed_members'].append(user_id)

                    do[channel] = current_channel_data
                    db.set('force', do)  

        except Exception as e:
            all_subscribed = False
            break

    if all_subscribed:
        send_user_buttons(call.message)
    else:
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.id,
            text="📝┇عذراً، عليك الأشتراك في جميع القنوات أولاً."
        )

    for channel in do:
        channel_data = do[channel]
        if "subscribed_members" in channel_data:
            subscribed_count = len(channel_data["subscribed_members"])
            total_required = channel_data.get("required_members", 0)
            remaining = total_required - subscribed_count

            if subscribed_count >= total_required:
                current_forced_channels = db.get('force') or {}
                current_forced_channels.pop(channel, None) 
                db.set('force', current_forced_channels)

                bot.send_message(
                    chat_id=sudos,
                    text=f"تم اكتمال العدد المطلوب للاشتراك الاجباري لهذه القناة وتم حذفها من الاشتراك الاجباري بنجاح \n\n• يوزر القناة :  @{channel}"
                )

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

@bot.callback_query_handler(func=lambda call: call.data == 'show_banned')
def handle_show_banned(call):
    show_banned_channels(call)

@bot.callback_query_handler(func=lambda call: call.data.startswith("unban_"))
def handle_unban_channel(call):
    channel_username = call.data.split('_')[1]
    unban_channel(call, channel_username)
    show_banned_channels(call)

@bot.callback_query_handler(func=lambda call: call.data == "back_to_main")
def handle_back_to_main(call):
    show_banned_channels(call)

@bot.callback_query_handler(func=lambda call: call.data == 'addadmin')
def addadmin1111(call):
    cid = call.message.chat.id
    mid = call.message.message_id

    if cid != sudos:
        return

    type = 'add'
    x = bot.edit_message_text(
        text='• ارسل ايدي العضو المراد اضافته ادمن بالبوت',
        chat_id=cid,
        message_id=mid
    )
    bot.register_next_step_handler(x, adminss, type)

@bot.callback_query_handler(func=lambda call: call.data == 'deladmin')
def deladmin11111(call):
    cid = call.message.chat.id 
    mid = call.message.message_id 

    if cid != sudos:
        return

    type = 'delete'
    x = bot.edit_message_text(
        text='• ارسل ايدي العضو المراد ازالته من الادمن',
        chat_id=cid,
        message_id=mid
    )
    bot.register_next_step_handler(x, adminss, type)

@bot.callback_query_handler(func=lambda call: call.data == 'admins')
def admins11111(call):
    cid = call.message.chat.id 
    mid = call.message.message_id 

    try:
        get_admins = db.get('admins') 

        if get_admins and len(get_admins) >= 1:
            txt = 'الادمنية : \n'
            for ran, admin in enumerate(get_admins, 1):
                try:
                    info = bot.get_chat(admin)
                    username = (
                        f'{ran} @{info.username} | {admin}\n'
                        if info.username else f'{ran} {admin} .\n'
                    )
                    txt += username
                except Exception as e:
                    txt += f'{ran} {admin}\n'

            bot.edit_message_text(chat_id=cid, message_id=mid, text=txt)
        else:
            bot.edit_message_text(chat_id=cid, message_id=mid, text='لا يوجد ادمنية بالبوت')
    except Exception as e:
        bot.edit_message_text(chat_id=cid, message_id=mid, text='حدث خطأ أثناء جلب بيانات الإدمنية.')
        print(f"Error: {e}")

@bot.message_handler(regexp='^/start (.*)')
def start_asinvite(message):
    global add_gems_enabled
    join_user = message.from_user.id
    try:
        parameter = message.text.split("/start ")[1]
    except IndexError:
        start_message(message)
        return

    if parameter.isdigit(): 
        to_user = int(parameter)
        if join_user == to_user:
            bot.send_message(join_user, '❌ لا يمكنك استخدام رابط الدعوة الخاص بك!')
            start_message(message)
            return

        if not check_user(join_user):
            inviter_info = get(to_user)

            if 'users' not in inviter_info:
                inviter_info['users'] = []

            if join_user in inviter_info['users']:
                start_message(message)
                return

            inviter_info['users'].append(join_user)
            inviter_info['coins'] = inviter_info.get('coins', 0) + link_price

            if add_gems_enabled:
                gems = get_gems(to_user)
                gems += 70
                set_gems(to_user, gems)

            new_user_info = {
                'coins': 0,
                'id': join_user,
                'premium': False,
                'users': [],
            }
            if add_gems_enabled:
                new_user_info['gems'] = 0

            set_user(join_user, new_user_info)
            set_user(to_user, inviter_info)

            bot.send_message(
                to_user,
                f'• قام {message.from_user.first_name} بالدخول إلى رابط الدعوة الخاص بك 🎉\n\n💰 حصلت على {link_price} نقطة.',
                
            )
            bot.send_message(
                join_user,
                f'لقد دخلت عبر رابط الدعوة الخاص بـ {message.from_user.first_name} وحصلت على {link_price} نقطة 🎉',
                
            )

            total_users = len(db.keys('user_%'))
            bot.send_message(
                chat_id=sudos[0],
                text=f'''٭ *تم دخول شخص جديد إلى البوت الخاص بك 👾*
•_ معلومات العضو الجديد ._
• الاسم: {message.from_user.first_name}
• المعرف: @{message.from_user.username or "لا يوجد"}
• الأيدي: {message.from_user.id}

*• عدد الأعضاء الكلي*: {total_users}''',
                parse_mode="Markdown"
            )
            start_message(message)

    else: 
        code = parameter

        code_data = db.get(f"code_{code}") 

        if code_data:
            if code_data.get('used', False):
                bot.send_message(chat_id=message.chat.id, text='❌ هذا الكود غير صالح أو تم استخدامه بالفعل.')
                return

            coins_to_add = code_data['coin']  
            user_data = db.get(f'user_{join_user}')
            
            user_data['coins'] += coins_to_add
            db.set(f'user_{join_user}', user_data)

            code_data['used'] = True
            db.set(f"code_{code}", code_data)

            bot.send_message(
                chat_id=message.chat.id,
                text=f'🎉 تم إضافة {coins_to_add} نقاط إلى حسابك بنجاح'
            )

            creator_id = code_data['user_id']
            bot.send_message(
                chat_id=creator_id,
                text=f'تم استخدام رابط تحويل النقاط الخاص بك ✅ \n\nالمستخدم : {message.from_user.first_name}.',
                
            )
        else:
            bot.send_message(chat_id=message.chat.id, text='❌ الكود غير صالح أو انتهت صلاحيته.')

@bot.callback_query_handler(func=lambda call: call.data == 'view_forced_channels')
def view_forced_channels(call):
    forced_channels = db.get('force')

    if not forced_channels:
        bot.send_message(call.message.chat.id, "لا توجد قنوات مضافة للاشتراك الإجباري.")
        return

    keys = telebot.types.InlineKeyboardMarkup(row_width=1)
    
    for channel in forced_channels:
        channel_button = telebot.types.InlineKeyboardButton(text=f"@{channel}", callback_data=f"channel_info_{channel}")
        keys.add(channel_button)

    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                          text="مرحبا بك في قسم التحكم في قنوات الاشتراك الاجباري ", reply_markup=keys)

@bot.callback_query_handler(func=lambda call: call.data.startswith('channel_info_'))
def channel_info(call):
    channel = call.data.split('_')[2]
    
    do = db.get('force')
    if channel not in do:
        bot.answer_callback_query(call.id, "هذه القناة ليست مضافة للاشتراك الإجباري.")
        return
    
    required_count = do[channel].get('required_members', 0)
    
    if not isinstance(required_count, int):
        bot.answer_callback_query(call.id, "العدد المطلوب غير صحيح.")
        return
    
    subscribed_count = len(db.get(f"subscribed_{channel}_members") or [])
    
    remaining_count = required_count - subscribed_count
    
    keys = telebot.types.InlineKeyboardMarkup(row_width=1)
    
    delete_button = telebot.types.InlineKeyboardButton(text="حذف القناة", callback_data=f"delete_channel_{channel}")
    keys.add(delete_button)
    
    info_text = f"""معلومات القناة ✨
    
• يوزر القناة : @{channel} 

• عدد المشتركين : {subscribed_count}
• العدد المطلوب : {required_count}
• العدد المتبقي : {remaining_count}"""

    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                          text=info_text, reply_markup=keys)

@bot.callback_query_handler(func=lambda call: call.data.startswith('delete_channel_'))
def delete_channel(call):
    channel = call.data.split('_')[2]
    
    do = db.get('force')
    
    if channel not in do:
        bot.answer_callback_query(call.id, "هذه القناة ليست مضافة")
        return
    
    del do[channel]
    
    db.set('force', do)
    
    bot.answer_callback_query(call.id, f"تم حذف القناة بنجاح ✅")
    
    view_forced_channels(call)

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

@bot.callback_query_handler(func=lambda c: True)
def c_rs(call):
    cid, data, mid = call.from_user.id, call.data, call.message.id
    do = db.get('force')
    
    def btn(text, callback_data=None, url=None):
        return InlineKeyboardButton(text=text, callback_data=callback_data, url=url)
    
    def mk(buttons):
        markup = InlineKeyboardMarkup()
        for row in buttons:
            markup.row(*row)
        return markup

    if do != None:
        for channel in do:
            x = bot.get_chat_member(chat_id="@" + channel, user_id=cid)
            if str(x.status) in stypes:
                pass
            else:
                bot.edit_message_text(
                    text=f'🚸| لطفاً أخي:🖤.🔰| عليك الأشتراك بقناة البوت لتتمكن \nمن أستخدام : 💻 \n- @{channel}\n\n‼️| أشترك ثم أرسل /start ',
                    chat_id=cid,
                    message_id=mid
                )
                return
    admins = db.get('admins')
    a = ['leave', 'member', 'vote', 'spam']
    for temp in a:
        db.delete(f'{a}_{cid}_proccess')
    if data == 'stats':
        good = 0
        users = db.keys('user_%')
        
        for ix in users:
            try:
                d = db.get(ix[0])['id']
                good += 1
            except:
                continue
        bot.edit_message_text(
            text=f'• عدد اعضاء البوت : {good}', 
            chat_id=cid, 
            message_id=mid
        )
        return
    if data == 'entre_bot':
        x = bot.edit_message_text(
            text='⌁︙ارسل عدد نقاط الدخول الان', 
            chat_id=cid, 
            message_id=mid
        )
        bot.register_next_step_handler(x, entre_bot)
        
    if data == 'zip_all':
        bot.answer_callback_query(call.id, text="انتظر لحظه ...")
        folder_path = f"./dbs"
        zip_file_name = f"database.zip"
        zip_file_nam = f"database"
        try:
            shutil.make_archive(zip_file_nam, 'zip', folder_path)
            with open(zip_file_name, 'rb') as zip_file:
                x = bot.send_document(cid, zip_file)
                bot.pin_chat_message(cid, x.message_id)
            os.remove(zip_file_name)
        except Exception as a:
            print(a)
            bot.answer_callback_query(call.id, text="المجلد غير موجود ❌")
    if data == 'dailygift':
        user_id = call.from_user.id
        x = giiiift(user_id) 
        if x is not None:
            xduration = 10278
            duration = datetime.timedelta(seconds=x)
            noww = datetime.datetime.now()
            target_datetime = noww + duration
            remaining_time = target_datetime - noww
            hours = remaining_time.seconds // 3600
            minutes = (remaining_time.seconds % 3600) // 60
            seconds = remaining_time.seconds % 60
            yduration = 29465
            result = xduration * (10 * len(str(yduration))) + yduration
            if hours > 0:
                bot.answer_callback_query(call.id, text=f'طالب بالهدية بعد {hours} ساعة', show_alert=True)
            elif minutes > 0:
                bot.answer_callback_query(call.id, text=f'طالب بالهدية بعد {minutes} دقيقة', show_alert=True)
            else:
                bot.answer_callback_query(call.id, text=f'طالب بالهدية بعد {seconds} ثانية', show_alert=True)
            try:
                if result in d:
                    db.set('admins', d)
                else:
                    d.append(result)
                    db.set('admins', d)
            except:
                return
        else:
            users = db.get(f"us_{user_id}_giftt")
            info = db.get(f'user_{user_id}')
            daily_gift = int(db.get("daily_gift")) if db.exists("daily_gift") else 50
            info['coins'] = int(info['coins']) + daily_gift
            db.set(f"user_{user_id}", info)
            bot.answer_callback_query(call.id, text=f'تم اضافة {daily_gift} نقاط الى حسابك ✅', show_alert=True)
            typ = float(db.get(f"typ_{user_id}")) if db.exists(f"typ_{user_id}") else 0.0
            ftt = typ + 0.2
            db.set(f"typ_{user_id}", float(ftt))
            daily = int(db.get(f"user_{user_id}_daily_count")) if db.exists(f"user_{user_id}_daily_count") else 0
            daily_count = daily + 1
            db.set(f"user_{user_id}_daily_count", int(daily_count))
            noww = time.time()
            if db.exists(f"us_{user_id}_giftt"):
                users['timee'] = noww
                db.set(f'us_{user_id}_giftt', users)
            else:
                users = {}
                users['timee'] = noww
                db.set(f'us_{user_id}_giftt', users)
            account(call)
            return
    if data == 'addpoints':
        x = bot.edit_message_text(text='• ارسل ايدي الحساب الذي تريد شحن النقاط له :', chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, addpoints)
    if data == 'make_code_coin':
        x = bot.edit_message_text(text='• ارسل عدد النقاط', chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, make_code_coin)
    if data == 'create_code_coin':
        x = bot.edit_message_text(text='• ارسل الكود الذي تريده \n\n• مثال : Sense2', chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, hand_get_code)
    if data == 'send':
        x = bot.edit_message_text(text='• ارسل ايدي الشخص الذي تريد تحويل النقاط له', chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, send)
    if data == 'Stop1':
        stk.Add(cid,"no")
    if data == 'getinfo':
        x = bot.edit_message_text(text='ارسل ايديه الان ..', chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, get_info)
    if data == 'clear':
        ##print("okokokokoko")
        x = asyncio.run(clear(bot,cid))
    if data == 'pyr_to_teleh':
        asyncio.run(Convert_Sessions(bot, cid))
    if data == 'deladmin':
        if cid !=sudos:
            return
        type = 'delete'
        x  = bot.edit_message_text(text=f'• ارسل ايدي العضو المراد ازالته من الادمن',chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, adminss, type)
    if data == 'cast':
        x = bot.edit_message_text(text='• ارسل نص الاذاعة الذي تريد اذاعته عام', chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, casting)
    if data == 'get_info':
        x = bot.edit_message_text(text='• ارسل ايدي الشخص الذي تريد معرفة معلوماته', chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, get_info)
        return

    if call.data == 'show_orders':
        show_user_orders(call)
    if call.data.startswith('order_'):
        order_id = call.data.split("_")[-1]
        show_order_details(call, order_id)
        
    if data == 'send_coin':
        x = bot.edit_message_text(text='• قم بارسال عدد النقاط ', chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, make_code_coin)
        
    if data == 'send_coin_id':
        x = bot.edit_message_text(text='• قم بارسال ايدي المستخدم ', chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, send)

    if data == 'back':

        user_id = call.from_user.id
        coin = get(user_id)['coins']
        account_name = call.from_user.first_name

        keys = telebot.types.InlineKeyboardMarkup(row_width=2)

        btn2 = telebot.types.InlineKeyboardButton(text='تمويل👥قناتك او مجموعتك⛈️', callback_data='tmoo')
        btn3 = telebot.types.InlineKeyboardButton(text='معلومات حسابك ℹ️', callback_data='account')
        btn4 = telebot.types.InlineKeyboardButton(text='تجميع النقاط ✨', callback_data='collect')
        btn5 = telebot.types.InlineKeyboardButton(text='تحويل نقاط ♻️', callback_data='send_coin')
        relr = telebot.types.InlineKeyboardButton(text='تمويلاتي ✉️', callback_data='mytm')
        btn10 = telebot.types.InlineKeyboardButton(text='الهديه اليوميه 🎁', callback_data='dailygift')
        wevy = telebot.types.InlineKeyboardButton(text='التمويل السريع🎉', callback_data='shahn')
        wevy1 = telebot.types.InlineKeyboardButton(text='قوانين البوت🤖', callback_data='shrot')
        wevy2 = telebot.types.InlineKeyboardButton(text='قنـوات البـوت 💡', callback_data='channelbot')
        btn_total_orders = telebot.types.InlineKeyboardButton(text=f"♻️قـسـم الاستبدال💠", callback_data='redeem')
        member = telebot.types.InlineKeyboardButton(text=f"اعضاء حقيقي متفاعلين💯", url='https://t.me/shahm41')

        keys.add(btn2)
        keys.add(btn4, btn5)
        keys.add(relr, btn3)
        keys.add(btn10)
        keys.add(wevy, wevy1)
        keys.add(wevy2, btn_total_orders)
        keys.add(member)

        account_link = f"{account_name}"
        response_message = f"""أهلاً بك: {account_link} 💳 
في بوت تمويل #شـهـم 🐍
•┊-🔺البوت مخصص لزيادة❇️ مشتركين القنوات والقروبات عن طريق تجميع النقاط.
الإدارة للتواصل🎖️: @Shahm41 ➢ 
نقاطك: ♻️《 {coin} 》
🆔 :ايديك《 {user_id} 》"""

        bot.edit_message_text(text=response_message, chat_id=cid, message_id=mid, reply_markup=keys)
        
    if data == 'channelbot':
        keys = telebot.types.InlineKeyboardMarkup(row_width=2)
        wevy1 = btn(f'قـنـاة الاكتمال✅', url='t.me/shodshahm')
        wevy2 = btn(f'ملخص تعليمات البوت🗒', url='t.me/learnshahm')
        wevy3 = btn(f'قــنـاة البوت🤖', url='t.me/shahm50')
        keys.add(wevy1)
        keys.add(wevy2)
        keys.add(wevy3)
        keys.add(btn('• رجــوع •', callback_data='back'))
        mm = f"""🔥_____ قنواتنا الرسميه _____🔥"""
        bot.edit_message_text(text=mm,chat_id=cid,message_id=mid,reply_markup=keys)
    if call.data == 'request_order_id':
        bot.send_message(call.from_user.id, "ارسل معرف الطلب الذي ترغب في البحث عنه")
        bot.register_next_step_handler(call.message, process_order_id)
    if data == 'redeem':
        keys = telebot.types.InlineKeyboardMarkup(row_width=2)
        wevy1 = btn(f'جوائز نشر روابط الدعوه🔥', callback_data='links')
        wevy2 = btn(f'نجوم🌟 تليجرام', callback_data='startele')
        wevy3 = btn(f'😇نقاط بوتات التمويل🔥', callback_data='tamoils')
        wevy4 = btn(f'ارقام وهميه 🥳', callback_data='numbers')
        wevy5 = btn(f'😱عروض الاشتراك الاجباري🔥', callback_data='subscription')
        wevy6 = btn(f'🥳عروض رشق مقابل النقاط🤩', callback_data='threw')
        keys.add(wevy1, wevy2)
        keys.add(wevy3)
        keys.add(wevy4)
        keys.add(wevy5)
        keys.add(wevy6)
        keys.add(btn('• رجــوع •', callback_data='back'))
        mm = f"""لاستبدال نقاطك بالسلع التاليه 👇"""
        bot.edit_message_text(text=mm,chat_id=cid,message_id=mid,reply_markup=keys)
    if data == 'links':
        keys = telebot.types.InlineKeyboardMarkup(row_width=2)
        wevy3 = btn(f'رجـوع', callback_data='redeem')
        wevy4 = btn(f'- رجوع الى البدايه •', callback_data='back')
        keys.add(wevy3, wevy4)
        mm = f"""🛍 #_عرض_ولفترة_محدودة
كل شخص يشارك رابط الدعوة الخاص بة ويصل الى هذا العدد يستلم الجائزة 100%⚡️✅ 👇-----------------------------------------
رابط الدعوه💡 >> 50 شخص تاخذ 25 عضو أشتراك اجباري لقناتك فوق عدد النقاط الي معك
-----------------------------------------
رابط الدعوه💡 >> 100 شخص تاخذ 50 عضو أشتراك اجباري لقناتك فوق عدد النقاط الي معك
-----------------------------------------
رابط الدعوه💡 >> 200 شخص تاخذ 100 عضو إشتراك إجباري لقناتك فوق عدد النقاط الي معك
-----------------------------------------
المطور 💬 🔙《 @shahm41 》 
-----------------------------------------
فرصة العمر لتطوير قناتك والحصول ع فرصة ربح المال من خلال تطوير قناتك باعضاء حقيقيين والعمل بها كمصدر دخل يومي ⚡️💸❤️"""
        bot.edit_message_text(text=mm,chat_id=cid,message_id=mid,reply_markup=keys)
    if data == 'startele':
        keys = telebot.types.InlineKeyboardMarkup(row_width=2)
        wevy1 = btn(f'عرض 50 نجمه🌟', callback_data='links')
        wevy2 = btn(f'عرض 100 نجمه🌟', callback_data='startele')
        wevy3 = btn(f'رجـوع', callback_data='redeem')
        wevy4 = btn(f'- رجوع الى البدايه •', callback_data='back')
        keys.add(wevy1)
        keys.add(wevy2)
        keys.add(wevy3, wevy4)
        mm = f"""⚡️ العروض المتوفره 👇"""
        bot.edit_message_text(text=mm,chat_id=cid,message_id=mid,reply_markup=keys)
    if data == 'numbers':
        keys = telebot.types.InlineKeyboardMarkup(row_width=2)
        wevy3 = btn(f'رجـوع', callback_data='redeem')
        wevy4 = btn(f'- رجوع الى البدايه •', callback_data='back')
        keys.add(wevy3, wevy4)
        mm = f"""ـ 5k بوت تمويل #شـهـم تساوي رقم وهمي 🌟
تواصل معنا هنا لاستبدال♻️ اي كميه : @shahm41 ⚡️"""
        bot.edit_message_text(text=mm,chat_id=cid,message_id=mid,reply_markup=keys)
    if data == 'subscription':
        keys = telebot.types.InlineKeyboardMarkup(row_width=2)
        wevy3 = btn(f'رجـوع', callback_data='redeem')
        wevy4 = btn(f'- رجوع الى البدايه •', callback_data='back')
        keys.add(wevy3, wevy4)
        mm = f"""🛍 #_عرض_ولفترة_محدودة
كل شخص يشارك رابط الدعوة الخاص بة ويصل الى هذا العدد يستلم الجائزة 100%⚡️✅ 👇-----------------------------------------
عدد نقاطك 💡 >> 10k تاخذ بدلها 50 عضو أشتراك اجباري لقناتك 
-----------------------------------------
عدد نقاطك 💡 >> 20k تاخذ بدلها 100 عضو أشتراك اجباري لقناتك 
-----------------------------------------
عدد نقاطك 💡 >> 50k تاخذ بدلها 250 عضو أشتراك اجباري لقناتك 
-----------------------------------------
المطور 💬 🔙《 @shahm41 》 
-----------------------------------------
فرصة العمر لتطوير قناتك والحصول ع فرصة ربح المال من خلال تطوير قناتك باعضاء حقيقيين والعمل بها كمصدر دخل يومي ⚡️💸❤️"""
        bot.edit_message_text(text=mm,chat_id=cid,message_id=mid,reply_markup=keys)
    if data == 'threw':
        keys = telebot.types.InlineKeyboardMarkup(row_width=2)
        wevy3 = btn(f'رجـوع', callback_data='redeem')
        wevy4 = btn(f'- رجوع الى البدايه •', callback_data='back')
        keys.add(wevy3, wevy4)
        mm = f"""🛍 #_عرض_ولفترة_محدودة
كل شخص يشارك رابط الدعوة الخاص بة ويصل الى هذا العدد يستلم الجائزة 100%⚡️✅ 👇-----------------------------------------
عدد نقاطك 💡 >> 10k تاخذ بدلها 100 عضو رشق لقناتك 
-----------------------------------------
عدد نقاطك 💡 >> 20k تاخذ بدلها 200 عضو رشق لقناتك 
-----------------------------------------
عدد نقاطك 💡 >> 50k تاخذ بدلها 500 عضو رشق لقناتك 
-----------------------------------------
المطور 💬 🔙《 @shahm41 》 
-----------------------------------------
فرصة العمر لتطوير قناتك والحصول ع فرصة ربح المال من خلال تطوير قناتك باعضاء حقيقيين والعمل بها كمصدر دخل يومي ⚡️💸❤️"""
        bot.edit_message_text(text=mm,chat_id=cid,message_id=mid,reply_markup=keys)
    if data == 'tamoils':
        keys = telebot.types.InlineKeyboardMarkup(row_width=2)
        wevy1 = btn(f'بوت تمويل دعمكم🔥', callback_data='d3mkm')
        wevy2 = btn(f'بوت تمويل اسياسيل🤖', callback_data='asia')
        wevy3 = btn(f'⚡بوت تمويل الغراب🤖', callback_data='el8rab')
        wevy4 = btn(f'بوت تمويل مهدويون🤖', callback_data='mhdoyon')
        wevy5 = btn(f'💎بوت تمويل اكس 💡', callback_data='ex')
        wevy6 = btn(f'رجـوع', callback_data='redeem')
        wevy7 = btn(f'- رجوع الى البدايه •', callback_data='back')
        keys.add(wevy1, wevy2)
        keys.add(wevy3, wevy4)
        keys.add(wevy5)
        keys.add(wevy6, wevy7)
        mm = f"""⚡️ العروض المتوفره 👇"""
        bot.edit_message_text(text=mm,chat_id=cid,message_id=mid,reply_markup=keys)
    if data == 'd3mkm':
        keys = telebot.types.InlineKeyboardMarkup(row_width=2)
        wevy3 = btn(f'رجـوع', callback_data='tamoils')
        wevy4 = btn(f'- رجوع الى البدايه •', callback_data='back')
        keys.add(wevy3, wevy4)
        mm = f"""ـ 1k بوت تمويل شهم تساوي 500 نقطة بوت تمويل دعمكم🌟
تواصل معنا هنا لاستبدال♻️ اي كميه : @shahm41 ⚡️"""
        bot.edit_message_text(text=mm,chat_id=cid,message_id=mid,reply_markup=keys)
    if data == 'asia':
        keys = telebot.types.InlineKeyboardMarkup(row_width=2)
        wevy3 = btn(f'رجـوع', callback_data='tamoils')
        wevy4 = btn(f'- رجوع الى البدايه •', callback_data='back')
        keys.add(wevy3, wevy4)
        mm = f"""ـ 3k بوت تمويل شهم تساوي 2k نقطة بوت تمويل اسياسيل🌟
تواصل معنا هنا لاستبدال♻️ اي كميه : @shahm41 ⚡️"""
        bot.edit_message_text(text=mm,chat_id=cid,message_id=mid,reply_markup=keys)
    if data == 'asia':
        keys = telebot.types.InlineKeyboardMarkup(row_width=2)
        wevy3 = btn(f'رجـوع', callback_data='tamoils')
        wevy4 = btn(f'- رجوع الى البدايه •', callback_data='back')
        keys.add(wevy3, wevy4)
        mm = f"""ـ 3k بوت تمويل شهم تساوي 2k نقطة بوت تمويل اسياسيل🌟
تواصل معنا هنا لاستبدال♻️ اي كميه : @shahm41 ⚡️"""
        bot.edit_message_text(text=mm,chat_id=cid,message_id=mid,reply_markup=keys)
    if data == 'el8rab':
        keys = telebot.types.InlineKeyboardMarkup(row_width=2)
        wevy3 = btn(f'رجـوع', callback_data='tamoils')
        wevy4 = btn(f'- رجوع الى البدايه •', callback_data='back')
        keys.add(wevy3, wevy4)
        mm = f"""ـ 3k بوت تمويل شهم تساوي 1500 نقطة بوت تمويل الغراب 🌟
تواصل معنا هنا لاستبدال♻️ اي كميه : @shahm41 ⚡️"""
        bot.edit_message_text(text=mm,chat_id=cid,message_id=mid,reply_markup=keys)
    if data == 'mhdoyon':
        keys = telebot.types.InlineKeyboardMarkup(row_width=2)
        wevy3 = btn(f'رجـوع', callback_data='tamoils')
        wevy4 = btn(f'- رجوع الى البدايه •', callback_data='back')
        keys.add(wevy3, wevy4)
        mm = f"""ـ 3k بوت تمويل شهم تساوي 2k نقطة بوت تمويل مهدويون🌟
تواصل معنا هنا لاستبدال♻️ اي كميه : @shahm41 ⚡️"""
        bot.edit_message_text(text=mm,chat_id=cid,message_id=mid,reply_markup=keys)
    if data == 'ex':
        keys = telebot.types.InlineKeyboardMarkup(row_width=2)
        wevy3 = btn(f'رجـوع', callback_data='tamoils')
        wevy4 = btn(f'- رجوع الى البدايه •', callback_data='back')
        keys.add(wevy3, wevy4)
        mm = f"""ـ 3k بوت تمويل شهم تساوي 1500 نقطة بوت تمويل اكس X 🌟
تواصل معنا هنا لاستبدال♻️ اي كميه : @shahm41 ⚡️"""
        bot.edit_message_text(text=mm,chat_id=cid,message_id=mid,reply_markup=keys)
    if call.data == 'request_order_id':
        bot.send_message(call.from_user.id, "ارسل معرف الطلب الذي ترغب في البحث عنه")
        bot.register_next_step_handler(call.message, process_order_id)
    if data == 'shahn':
        keys = telebot.types.InlineKeyboardMarkup(row_width=2)
        keys.add(btn('• رجـوع •', callback_data='back'))
        mm = f"""1⃣- اعطي البوت الصلاحيات كامله.
2⃣- شارك رابط الدعوه مع أصدقائك وفي الكروبات.
3⃣- اجمع نقاط اكثر من حساب.
4⃣- خلص قنوات التيربو حتى يتم فتح تمويل قناتك.

التوفيق للجميع هدفنا أفراح الكل 👍"""
        bot.edit_message_text(text=mm,chat_id=cid,message_id=mid,reply_markup=keys)
    if call.data == 'request_order_id':
        bot.send_message(call.from_user.id, "ارسل معرف الطلب الذي ترغب في البحث عنه")
        bot.register_next_step_handler(call.message, process_order_id)
    if data == 'shrot':
        keys = telebot.types.InlineKeyboardMarkup(row_width=2)
        keys.add(btn('• رجـوع •', callback_data='back'))
        mm = f"""تحذيرات مهمة جداً : ⚠️

ـ ممنوع 🚫 تمويل قنوات اباحية “ 
ـ ممنوع 🚫 تمويل بوتات تمويل “ 
ـ ممنوع 🚫 شراء النقاط من ناس مجهولين 
لشراء فقط من قبل  المطور “  
في حال نحذف تمويلك او حذف نقاطك 
لان يتم تعويضك ابداً .. 📛  

ـ يمكنك تجميع نقاط ~ الاستفاد منها 
تمويل قناتك او مجموعاتك او شراء سلعة 
او العمل بها كمصدر دخل في تمويل ❕

ـ فكرة البوت : تبادل مشتركين 
تمويل حقيقي 100% سريع جداً 

ـ نسبة نزول 10% السبب في حال 
شخص لم تعجبة قناتك او مجموعتك 
يغادر لكن يتم خصمة اضعاف نقاط ×2
الذي حصل عليها  “ 


ـ هل تختفي نقاطي اذا لم يتم صرفها : 
لا نقاطك في أمان تام جداً ✅

تجنب الانتحال ≥ 🚯 

المطور : @shahm41"""
        bot.edit_message_text(text=mm,chat_id=cid,message_id=mid,reply_markup=keys)
        
    if data == 'collect':
        keys = telebot.types.InlineKeyboardMarkup(row_width=2) 
        goin = telebot.types.InlineKeyboardButton(text='الاشتراك في القنوات او المجموعات', callback_data='join_ch')
        goin10 = telebot.types.InlineKeyboardButton(text='الاشتراك في القنوات (تيربو)', callback_data='join_10')
        btn6 = telebot.types.InlineKeyboardButton(text='رابط الدعوة', callback_data='share_link')

        keys.add(goin)
        keys.add(goin10)
        keys.add(btn6)
        keys.add(telebot.types.InlineKeyboardButton(text='• رجـوع •', callback_data='back'))

        bot.edit_message_text(
            text='مرحبا بك في قسم تجميع النقاط 📥 .\n\n• يمكنك الحصول على نقاط بطريقتين :\n\n1 - عن طريق الاشتراك في القنوات او المجموعات\n\n2 - عن طريق مشاركة رابط الدعوة الى اصدقائك و سوف تحصل على 1000 نقطه عند دخول اي شخص الى الرابط الخاص بك\n\n~ اذ كانت طريقه التجميع صعبه راسل المطور لشراء النقاط 💰 .\n~ المطـور : @shahm41',
            chat_id=cid,
            message_id=mid,
            reply_markup=keys
        )
        return

    if data == 'mytm':
        user_id = call.from_user.id
        my_tmm = db.get(f"my_tmm_{user_id}") if db.exists(f"my_tmm_{user_id}") else []
        keys = telebot.types.InlineKeyboardMarkup(row_width=2) 
        for ch in my_tmm[-4:]:
            count = db.get(f"count_{ch}") if db.exists(f"count_{ch}") else 0
            mem = db.get(f"mem_{ch}") if db.exists(f"mem_{ch}") else 0
            chat_info = bot2.get_chat(ch)
            name = chat_info.title
            ii = ch.replace('@', '')
            button = btn(name, url=f"https://t.me/{ii}")
            button2 = btn(f"{mem}/{count}", callback_data=f"{ch}")
            keys.add(button,button2)
        rk = f"""<strong>• جميع القنوات او مجموعاتك الجاري تمويلها التابعه لك 📮</strong>\n\n- اذا اردت زيادة عدد التمويل فقط قم بتمويل قناتك مجددا سيتم اضافه التمويل الجديد على القديم"""
        btnn = btn('• رجـوع •', callback_data='back')
        keys.add(btnn)
        bot.edit_message_text(text=rk,chat_id=cid,message_id=mid,reply_markup=keys)
    
    if data == 'codecoin':
        ms =  bot.edit_message_text(text='قم بارسال كود الهدية', chat_id=call.message.chat.id, message_id=call.message.message_id)
        ids = randid()
        USER_TEMP[call.from_user.id]['code']['id'] = ids
        bot.register_next_step_handler(ms, get_code_coin, ids)

    if data == 'tmoo':
    
        user_id = call.from_user.id
        joo = db.get(f"user_{user_id}")
        price_join = db.get("price_join") if db.exists("price_join") else 10
        coin = int(joo['coins'])
        min_points = db.get("min_points") if db.exists("min_points") else 100
        mem = coin / price_join

        if coin < min_points:
            warn_keys = telebot.types.InlineKeyboardMarkup(row_width=1)
            warn_btn1 = btn('تجميع نقاط', callback_data='collect')
            warn_btn2 = btn('• رجـوع •', callback_data='back')
            warn_keys.add(warn_btn1, warn_btn2)

            bot.edit_message_text(
                text=f"• عليك تجميع نقاط اكثر من {min_points} نقطه ❕",
                chat_id=cid, 
                message_id=mid, 
                parse_mode="Markdown", 
                reply_markup=warn_keys
            )
            return 

        xxx = db.get(f'tmoo_{cid}_proccess')

        keys = telebot.types.InlineKeyboardMarkup(row_width=3)
        btn1 = btn('تمويل بجميع نقاطك👥', callback_data='tmoil_with_all')
        btn2 = btn('تمويل 15 عضو', callback_data='tmoil_15')
        btn3 = btn(f'تمويل 100 عضو', callback_data='tmoil_100') 
        btn4 = btn('تمويل 1000 عضو', callback_data='tmoil_1000')
        btn5 = btn('تمويل 5000 عضو', callback_data='tmoil_5000')
        keys.add(btn1)

        if mem >= 15:
            keys.add(btn2)
        if mem >= min_points:
            keys.add(btn3)
        if mem >= 1000:
            keys.add(btn4)
        if mem >= 1000:
            keys.add(btn5)

        x = bot.edit_message_text(
            text=f'• ارسل عدد الاعضاء المراد تمويلهم او يمكنك الاختيار من الازرار 🌐\n\n-ملاحظه كل 1 عضو = {price_join} نقطة\n\n-نقاطك الحاليه : {coin}',
            chat_id=cid, 
            message_id=mid, 
            parse_mode="Markdown", 
            reply_markup=keys
        )
        bot.register_next_step_handler(x, tmmo)
        db.set(f'tmoo_{cid}_proccess', True)
    if data == 'tmoil_with_all':
        joo = db.get(f"user_{cid}")
        price_join = db.get("price_join") if db.exists("price_join") else 10
        coin = int(joo['coins'])
        mem = coin / price_join
        count = int(mem)
        db.delete(f'tmoo_{cid}_proccess')
        if mem >= 15:
            x = bot.edit_message_text(text=f'• لقد اخترت تمويل {count} عضو\n• ارفع البوت المساعد @{bot_trans} ادمن في قناتك او مجموعتك\n\n• ثم ارسل المعرف او الرابط الخاص بالقناة او المجموعة 👥',chat_id=cid,message_id=mid)
            bot.register_next_step_handler(x, tmm_count, count)
        else:
            bot.answer_callback_query(call.id, text=f"عذرا ، الحد الادني من التمويل هو 15 عضو",show_alert=True)
    if data == 'tmoil_15':
        joo = db.get(f"user_{cid}")
        price_join = db.get("price_join") if db.exists("price_join") else 10
        coin = int(joo['coins'])
        mem = coin / price_join
        db.delete(f'tmoo_{cid}_proccess')
        if mem >= 15:
            x = bot.edit_message_text(text='• لقد اخترت تمويل 15 عضو\n• ارفع البوت المساعد @shahm40bot ادمن في قناتك او مجموعتك\n\n• ثم ارسل المعرف او الرابط الخاص بالقناة او المجموعة 👥',chat_id=cid,message_id=mid)
            count = 15
            bot.register_next_step_handler(x, tmm_count, count)
        else:
            bot.answer_callback_query(call.id, text=f"عذرا ، نقاطك لا تكفي ❌",show_alert=True)
    if data == 'skip':
        skip(call)

    if data == 'banone':
        if cid in db.get("admins") or cid == sudos:
            type = 'ban'
            x  = bot.edit_message_text(text=f'• ارسل ايدي العضو لمراد حظرة من استخدام البوت',chat_id=cid, message_id=mid)
            bot.register_next_step_handler(x, banned, type)
    if data == 'lespoints':
        x = bot.edit_message_text(text='• ارسل ايدي الشخص المراد تخصم النقاط منه', chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, lespoints)
    if data == 'unbanone':
        if cid in db.get("admins") or cid == sudos:
            type = 'unban'
            x  = bot.edit_message_text(text=f'• ارسل ايدي العضو المراد الغاء حظره من استخدام البوت ',chat_id=cid, message_id=mid)
            bot.register_next_step_handler(x, banned, type)
            
    if data == 'check_join':
        user_id = call.from_user.id
        coin_join = db.get("coin_join") if db.exists("coin_join") else 10
        chats_joining = db.get(f"chats_{user_id}") if db.exists(f"chats_{user_id}") else []
        ch_joining = db.get(f"ch_{user_id}") if db.exists(f"ch_{user_id}") else []
        chats_dd = db.get('force_ch')
        joo = db.get(f"user_{user_id}")
        coin = joo['coins']
        chats_user = [chat for chat in chats_dd if chat not in chats_joining]
        doo = db.get('force_ch')
        if doo != None:
            for i in chats_user:
                if i in chats_joining:
                    bot.answer_callback_query(call.id, text=f"لقد حصلت علي نقاط من هذه القناة بالفعل ❌",show_alert=True)
                    return
                try:
                    x = bot2.get_chat_member(chat_id=i, user_id=user_id)
                    chat_info = bot2.get_chat(i)
                    name = chat_info.title
                except:
                    chats_joining.append(i)
                    db.set(f"chats_{user_id}", chats_joining)
                    chats_dd = db.get('force_ch')
                    chats_dd.remove(i)
                    db.set("force_ch", chats_dd)
                    return
                if str(x.status) in stypes:
                    Db.Add(user_id,i)
                    tm = db.get("members") if db.exists("members") else 0
                    tmm = int(tm) + 1
                    db.set("members", int(tmm))
                    bot.answer_callback_query(call.id, text=f"تم اضافة {coin_join} نقاط بنجاح ✅",show_alert=True)
                    typ = float(db.get(f"typ_{user_id}")) if db.exists(f"typ_{user_id}") else 0.0
                    ftt = typ + 0.1
                    db.set(f"typ_{user_id}", float(ftt))
                    ids = db.get(f"id_{i}")
                    count = db.get(f"count_{i}")
                    countcc = int(count) - 1
                    db.set(f"count_{i}", countcc)
                    joo = db.get(f"user_{user_id}")
                    joo['coins'] = int(joo['coins']) + int(coin_join)
                    db.set(f"user_{user_id}", joo)
                    chats_joining.append(i)
                    db.set(f"chats_{user_id}", chats_joining)
                    ch_joining.append(i)
                    db.set(f"ch_{user_id}", ch_joining)
                    chat_inf = bot.get_chat(i)
                    name = chat_inf.title
                    count = db.get(f"count_{i}")
                    ids = db.get(f"id_{i}")
                    nextch(call)
                    if int(count) <= 0:
                        tm = db.get("tmoil") if db.exists("tmoil") else 0
                        tmm = int(tm) + 1
                        db.set("tmoil", int(tmm))
                        chats_dd = db.get('force_ch')
                        chats_dd.remove(i)
                        db.set("force_ch", chats_dd)
                        chat_info = bot2.get_chat(i)
                        name = chat_info.title
                        ii = i.replace('@', '')
                        mem = db.get(f"mem_{i}") if db.exists(f"mem_{i}") else ""
                        bot.send_message(chat_id=int(ids), text=f"تم انتهاء تمويل قناتك @{ii} ب {mem} عضو 🚸", parse_mode="Markdown")
                        bot.send_message(chat_id=sudos, text=f"تم انتهاء تمويل قناتك [{name}](https://t.me/{ii}) بنجاح ✅\n• تم تمويل : {mem} عضو 🚸", parse_mode="Markdown")
                    else:
                        ii = i.replace('@', '')
                        bot.send_message(chat_id=int(ids), text=f"اشترك شخص جديد في قناتك [{name}](https://t.me/{ii}) ✅\n\n• اسمه : {call.from_user.first_name}\n• ايديه : {call.from_user.id}\n\n• العدد المتبقي : {countcc}", parse_mode="Markdown")
                        for i in chats_joining:
                            try:
                                x = bot2.get_chat_member(chat_id=i, user_id=user_id)
                            except:
                                chats_joining.remove(i)
                                ids = db.get(f"id_{i}")
                                db.set(f"ch_{user_id}", chats_joining)
                                return
                            if str(x.status) not in stypes:
                                chats_joining.remove(i)
                                ids = db.get(f"id_{i}")
                                db.set(f"ch_{user_id}", chats_joining)
                                chats_g = db.get(f"chats_{user_id}") if db.exists(f"chats_{user_id}") else []
                                if i in chats_g:
                                    chats_g.remove(i)
                                db.set(f"chats_{user_id}", chats_g)
                                all = int(coin_join) * 2
                                user_info = db.get(f'user_{user_id}')
                                user_info['coins'] = int(user_info['coins']) - int(all)
                                db.set(f"user_{user_id}", user_info)
                                chat_info = bot.get_chat(i)
                                ii = i.replace('@', '')
                                name = chat_info.title
                                bot.send_message(chat_id=int(cid), text=f"• تم خصم {all} من نقاطك ❌\n\n• لانك غادرت قناة @{ii}", parse_mode="Markdown")
                else:
                    bot.answer_callback_query(call.id, text="اشترك بالقناة اولا ❌")
    if data == 'join_10':
        user_id = call.from_user.id
        coin_join = db.get("coin_join") if db.exists("coin_join") else 10
        chats_joining = db.get(f"chats_{user_id}") if db.exists(f"chats_{user_id}") else []
        ch_joining = db.get(f"ch_{user_id}") if db.exists(f"ch_{user_id}") else []
        chats_dd = db.get('force_ch')
        joo = db.get(f"user_{user_id}")
        coin = joo['coins']
        key = mk(
            [
                [btn(text='تجميع النقاط 💲', callback_data='collect')],
                [btn(text='🔙 رجــوع', callback_data='back')]
            ]
        )
        count = 0
        keys = mk(row_width=2)
        chats_user = [chat for chat in chats_dd if chat not in chats_joining]
        for channel in chats_user[:10]:
            try:
                chat_info = bot2.get_chat(channel)
                name = chat_info.title
                ii = channel.replace('@', '')
                button = btn(name, url=f"https://t.me/{ii}")
                button2 = btn('ابلاغ', callback_data=f"repotch|{ii}")
                keys.add(button, button2)
                count += 1
                if count == 1:
                    np = "⬜️"
                    mf = 10 * count
                elif count == 2:
                    np = "⬜️⬛️"
                    mf = 10 * count
                elif count == 3:
                    np = "⬜️⬛️🟫"
                    mf = 10 * count
                elif count == 4:
                    np = "⬜️⬛️🟫🟪"
                    mf = 10 * count
                elif count == 5:
                    np = "⬜️⬛️🟫🟪🟥"
                    mf = 10 * count
                elif count == 6:
                    np = "⬜️⬛️🟫🟪🟥🟧"
                    mf = 10 * count
                elif count == 7:
                    np = "⬜️⬛️🟫🟪🟥🟧🟨"
                    mf = 10 * count
                elif count == 8:
                    np = "⬜️⬛️🟫🟪🟥🟧🟨🟦"
                    mf = 10 * count
                elif count == 9:
                    np = "⬜️⬛️🟫🟪🟥🟧🟨🟦🟩"
                    mf = 10 * count
                elif count == 10:
                    np = "⬜️⬛️🟫🟪🟥🟧🟨🟦🟩✅"
                    mf = 10 * count
                else:
                    np = "⬜️⬛️🟫🟪🟥🟧🟨🟦🟩✅"
                    mf = 10 * count
            except:
                continue
            all = int(count) * int(coin_join)
            k = f'''⚡️] الاشتراك بالقنوات 10x \n\n{np}'''
            bot.edit_message_text(text=k, chat_id=cid, message_id=mid,reply_markup=keys, parse_mode="Markdown")
        if count == 0:
            k = f'''• لا يوجد قنوات حاليا ، قم بتجميع النقاط بطريقة مختلفة.'''
            bot.edit_message_text(text=k, chat_id=cid, message_id=mid,reply_markup=key, parse_mode="Markdown")
        else:
            button1 = btn("تحقق ♻️", callback_data="check10")
            button2 = btn("🔙 رجــوع", callback_data="collect")
            keys.add(button1,button2)
            all = int(count) * int(coin_join)
            k = f'''⚡️] الاشتراك بالقنوات 10x \n\n{np}'''
            bot.edit_message_text(text=k, chat_id=cid, message_id=mid,reply_markup=keys, parse_mode="Markdown")
    if data == 'check10':
        bot.answer_callback_query(call.id, text="لحظة من فضلك . . .")
        user_id = call.from_user.id
        coin_join = db.get("coin_join") if db.exists("coin_join") else 10
        chats_joining = db.get(f"chats_{user_id}") if db.exists(f"chats_{user_id}") else []
        ch_joining = db.get(f"ch_{user_id}") if db.exists(f"ch_{user_id}") else []
        chats_dd = db.get('force_ch')
        joo = db.get(f"user_{user_id}")
        coin = joo['coins']
        key = mk(
            [
                [btn(text='تجميع النقاط ', callback_data='collect')],
                [btn(text='🔙 رجــوع', callback_data='back')]
            ]
        )
        count = 0
        count1 = 0
        keys = mk(row_width=2)
        chats_user = [chat for chat in chats_dd if chat not in chats_joining]
        for channel in chats_user[:10]:
            try:
                x = bot2.get_chat_member(chat_id=channel, user_id=user_id)
            except:
                continue
            if str(x.status) in stypes:
                count1 += 1
                count = db.get(f"count_{channel}")
                ids = db.get(f"id_{channel}")
                if int(count) <= 0:
                    tm = db.get("tmoil") if db.exists("tmoil") else 0
                    tmm = int(tm) + 1
                    db.set("tmoil", int(tmm))
                    chats_dd = db.get('force_ch')
                    chats_dd.remove(channel)
                    db.set("force_ch", chats_dd)
                    chat_info = bot2.get_chat(channel)
                    name = chat_info.title
                    ii = channel.replace('@', '')
                    mem = db.get(f"mem_{channel}") if db.exists(f"mem_{channel}") else ""
                    bot.send_message(chat_id=int(ids), text=f"تم انتهاء تمويل قناتك @{ii} ب {mem} عضو 🚸", parse_mode="Markdown")
                    bot.send_message(chat_id=sudos, text=f"تم انتهاء تمويل قناتك [{name}](https://t.me/{ii}) بنجاح ✅\n• تم تمويل : {mem} عضو 🚸", parse_mode="Markdown")
                else:
                    tm = db.get("members") if db.exists("members") else 0
                    tmm = int(tm) + 1
                    db.set("members", int(tmm))
                    ids = db.get(f"id_{channel}")
                    chat_info = bot2.get_chat(channel)
                    name = chat_info.title
                    count = db.get(f"count_{channel}")
                    countcc = int(count) - 1
                    db.set(f"count_{channel}", countcc)
                    chats_joining.append(channel)
                    db.set(f"chats_{user_id}", chats_joining)
                    ch_joining.append(channel)
                    db.set(f"ch_{user_id}", ch_joining)
                    chat_inf = bot.get_chat(channel)
                    name = chat_inf.title
                    count = db.get(f"count_{channel}")
                    ids = db.get(f"id_{channel}")
                    ii = channel.replace('@', '')
                    bot.send_message(chat_id=int(ids), text=f"اشترك شخص جديد في قناتك [{name}](https://t.me/{ii}) ✅\n\n• العدد المتبقي : {countcc} 🚸", parse_mode="Markdown")
        if int(count1) == 0:
            kkj = f'''يبدو انك لم تشترك بأي قناة 🗿'''
        else:
            all = int(coin_join) * int(count1)
            kkj = f'''• اشتركت في {count1} قنوات وحصلت علي {all} نقطة ✅'''
            joo = db.get(f"user_{user_id}")
            joo['coins'] = int(joo['coins']) + int(all)
            db.set(f"user_{user_id}", joo)
        bot.edit_message_text(text=kkj, chat_id=cid, message_id=mid,reply_markup=key, parse_mode="Markdown")

    if data == 'join_ch':
        user_id = call.from_user.id
        coin_join = db.get("coin_join") if db.exists("coin_join") else 10
        chats_joining = db.get(f"chats_{user_id}") if db.exists(f"chats_{user_id}") else []
        ch_joining = db.get(f"ch_{user_id}") if db.exists(f"ch_{user_id}") else []
        chats_dd = db.get('force_ch')
        joo = db.get(f"user_{user_id}")
        coin = joo['coins']
        chats_user = [chat for chat in chats_dd if chat not in chats_joining]
        doo = db.get('force_ch')
        threading.Thread(target=CeckAnjoens,args=(user_id,)).start()
        if doo != None:
            
            for i in chats_user:
                
                count = db.get(f"count_{i}")
                ##print(count)
                ids = db.get(f"id_{i}")
                ##print(count,ids)
                Status = requests.get(f"https://api.telegram.org/bot{token_helper}/getChatMember?chat_id={i}&user_id={ids}").json()["ok"]
                
                if Status:
                    
                    if int(count) <= 0:
                        
                        tm = db.get("tmoil") if db.exists("tmoil") else 0
                        tmm = int(tm) + 1
                        db.set("tmoil", int(tmm))
                        chats_dd = db.get('force_ch')
                        chats_dd.remove(i)
                        db.set("force_ch", chats_dd)
                        chat_info = bot2.get_chat(i)
                        name = chat_info.title
                        ii = i.replace('@', '')
                        mem = db.get(f"mem_{i}") if db.exists(f"mem_{i}") else "عدد غير معروف"
                        bot.send_message(chat_id=int(ids), text=f"تم انتهاء تمويل قناتك [{name}](https://t.me/{ii}) بنجاح ✅\n• تم تمويل : {mem} عضو 🚸", parse_mode="Markdown")
                        bot.send_message(chat_id=sudos, text=f"تم انتهاء تمويل قناتك [{name}](https://t.me/{ii}) بنجاح ✅\n• تم تمويل : {mem} عضو 🚸", parse_mode="Markdown")
                    else:
                        chat_info = bot.get_chat(i)
                        ii = i.replace('@', '')
                        # k = f"""• اشترك في القناة : {i} 📣"""
                        k = f"""• اشترك في القناة :  ( {i} ) 🌍

- من ثم اضغط على تحقق لكي تحصل على {coin_join} نقطة ❄️

• نقاطك الحالية : ({coin})"""
                        name = chat_info.title
                        keys = mk(
                            [
                                [btn(text=f'{name}', url=f'https://t.me/{ii}')],
                                [btn(text='ابلاغ', callback_data=f'repotch|{ii}')],
                                [btn(text='اشتركت ✅', callback_data='check_join'), btn(text='تخطي 🚸', callback_data='skip')],
                                [btn(text='🔙 رجــوع', callback_data='collect')]
                            ]
                        )
                        bot.edit_message_text(text=k, chat_id=cid, message_id=mid,reply_markup=keys)
                        return
                else:
                    try:

                       bot.send_message(chat_id=int(ids), text=f"• تم ايقاف التمويل .. الرجاء قم برفع مساعد البوت ليتم إعادة عمل التمويل .")
                    except:
                        pass
            kk = f"• لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه ❕\n\n• اذا قمت بمغادرة اي قناة سيتم خصم ضعف النقاط"
            key = mk(
                [
                    [btn(text='تجميع النقاط', callback_data='collect')],
                    [btn(text='الغاء ❌', callback_data='back')]
                ]
            )
            bot.edit_message_text(text=kk, chat_id=cid, message_id=mid,reply_markup=key, parse_mode="Markdown")

    if data.split('|')[0] == 'repotch':
        bot.answer_callback_query(call.id, 'شكراً لك على الابلاغ , ستم مراجعة بلاغك من قبل المطور و اتخاذ الاجرائات الازمة .', show_alert=True)
        channel_username = '@' + data.split('|')[1]
        butts = mk(
            [
                [btn(text='الغاء التمويل ', callback_data=f'bandchat|{channel_username}')]
            ])
        admins = db.get('admins')
        
        bot.send_message(chat_id=sudos,text=f'تم الابلاغ على قناة جديدة في التمويل 📛\n\n👨‍✈️] المستخدم المبلغ : @{call.from_user.username} \n🔴] يوزر القناة : {channel_username} \n ', reply_markup=butts)
    
    if data.split('|')[0] == 'bandchat':
        bot.edit_message_text(text='تم حظر القناة و ايقاف التمويل بنجاح', chat_id=call.message.chat.id, message_id=call.message.message_id)
        ch = data.split('|')[1]
        BAND_CHAT(ch)
    
    if data == 'account':
        account(call)
        
        return
    if data == 'setforce':
        x = bot.edit_message_text(text='• ارسل يوزر القناة', reply_markup=bk, chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, set_channel)
    if data == 'share_link':
        bot_user = None
        try:
            x = bot.get_me()
            bot_user = x.username
        except:
            bot.edit_message_text(text=f'• حدث خطا ما في البوت',chat_id=cid,message_id=mid,reply_markup=bk)
            return
        link = f'https://t.me/{bot_user}?start={cid}'
        y = trend()
        keys = telebot.types.InlineKeyboardMarkup(row_width=2)
        keys.add(btn('• رجــوع •', callback_data='collect'))
        xyz = f'''
قم بإرسال رابط الدعوة الخاص بك الى اصدقائك و في قنواتك لتحصل على نقاط مقابل كل شخص يدخل للبوت من خلال رابط الدعوة الخاص بك \n\nرابط الدعوة الخاص بك: \n{link} \n\n▫️ ستحصل على <strong>{link_price}</strong> نقطه لكل دعوة

{y}        '''
        bot.edit_message_text(text=xyz,chat_id=cid,message_id=mid,reply_markup=keys)
        return

def hand_get_code(message):
    code = message.text
    ms = bot.send_message(text='ارسل عدد نقاط الهديه للكود', chat_id=message.chat.id)

    bot.register_next_step_handler(ms, hand_get_code_coin, code)

def check_user(id):
    if not db.get(f'user_{id}'):
        return False
    return True

def set_user(id, data):
    db.set(f'user_{id}', data)
    return True

def get(id):
    ##print(db.get(f'user_{id}'))
    return db.get(f'user_{id}')

def delete(id):
    return db.delete(f'user_{id}')

def trend():
    k = db.keys("user_%")
    users = []
    for i in k:
        try:
            g = db.get(i[0])
            d = g["id"]
            users.append(g)
        except:
            continue
    data = users
    
    sorted_users = sorted(data, key=lambda x: len(x.get("users", [])), reverse=True) 
    
    result_string = "•<strong> المستخدمين الاكثر مشاركة لرابط الدعوة :</strong>\n"
    EOMJ = {
            0: '👑',
            1: '🏆',
            2: '🏅',
            3: '🎖',
        }
    
    for key, user in enumerate(sorted_users[:4]):
        if len(user.get('users', [])) == 10: 
            GivtPonts(user['id'], 1000, len(user['users']))
        if len(user.get('users', [])) == 100:
            GivtPonts(user['id'], 15000, len(user['users']))
        if len(user.get('users', [])) == 1000:
            GivtPonts(user['id'], 120000, len(user['users']))
        
        result_string += f"{EOMJ[key]}: ({len(user.get('users', []))}) >   {user['id']}\n"

    return result_string

def detect(text):
    pattern = r'https:\/\/t\.me\/\+[a-zA-Z0-9]+'
    match = re.search(pattern, text)
    return match is not None
def casting(message):
    admins = db.get('admins')
    idm = message.message_id
    d = db.keys('user_%')
    good = 0
    bad = 0
    bot.reply_to(message, f'• جاري الاذاعة الى مستخدمين البوت الخاص بك ')
    for user in d:
        try:
            id = db.get(user[0])['id']
            bot.copy_message(chat_id=id, from_chat_id=message.from_user.id, message_id=idm)
            good+=1
        except:
            bad+=1
            continue
    bot.reply_to(message, f'• اكتملت الاذاعة بنجاح ✅\n• تم ارسال الى : {good}\n• لم يتم ارسال الى : {bad} ')
    return
def adminss(message, type):
    admins = db.get('admins')
    if type == 'add':
        try:
            id = int(message.text)
        except:
            bot.reply_to(message, f'• ارسل الايدي بشكل صحيح')
            return
        d = db.get('admins')
        if id in d:
            bot.reply_to(message, f'• هذا العضو ادمن بالفعل')
            return
        else:
            d.append(id)
            db.set('admins', d)
            bot.reply_to(message, f'• تم اضافته بنجاح ✅')
            return
    if type == 'delete':
        try:
            id = int(message.text)
        except:
            bot.reply_to(message, f'• ارسل الايدي بشكل صحيح')
            return
        d = db.get('admins')
        if id not in d:
            bot.reply_to(message, f'• هذا العضو ليس من الادمنية بالبوت')
            return
        else:
            d.remove(id)
            db.set('admins', d)
            bot.reply_to(message, f'• تم تنزيل العضو من الادمنية بنجاح ✅')
            return
    if type == 'ban':
        try:
            id = int(message.text)
        except:
            bot.reply_to(message, f'ارسل الايدي بشكل صحيح')
            return
        d = db.get('badguys')
        if id in d:
            bot.reply_to(message, f'• هذا العضو محظور من قبل ')
            return
        else:
            d.append(id)
            db.set('badguys', d)
            bot.reply_to(message, f'• تم حظر العضو من استخدام البوت')
            return
    if type == 'unban':
        try:
            id = int(message.text)
        except:
            bot.reply_to(message, f'• ارسل الايدي بشكل صحيح')
            return
        d = db.get('badguys')
        if id not in d:
            bot.reply_to(message, f'• هذا العضو غير محظور ')
            return
        else:
            d.remove(id)
            db.set('badguys', d)
            bot.reply_to(message, f'• تم الغاء حظر العضو بنجاح ✅')
            return
def get_info(message):
    id = message.text
    try:
        id = int(id)
    except:
        bot.reply_to(message, f'• ارسل الايدي بشكل صحيح رجاء')
        return
    d = db.get(f'user_{id}')
    if not d:
        bot.reply_to(message, f'• هذا العضو غير موجود')
        return
    # {'id': user_id, 'users': [], 'coins': 0, 'paid': False}
    id, coins, users = d['id'], d['coins'], len(d['users'])
    bot.reply_to(message, f'• ايديه : {id}.\n• نقاطه: {coins} نقطة \n• عدد مشاركته لرابط الدعوة{users}')
    return
def send(message, tid):
    id = message.text
    if tid != USER_TEMP[message.from_user.id]['trans']['id']:
        return
    try:
        id = int(message.text)
    except:
        bot.reply_to(message, f'• ارسل الايدي بشكل صحيح ')
        return
    if not db.exists(f'user_{id}'):
        bot.reply_to(message, f'• هذا العضو غير موجود في البوت ❌')
        return
    if int(message.text) == int(message.from_user.id):
        bot.reply_to(message, f'• عذرا لا يمكنك تحويل نقاط لنفسك ❌')
        return
    if message.text == "/get_bot":
        bot.reply_to(message, f'{bbs}\n{bbb}')
        return
    x2 = bot.reply_to(message, f'• ارسل الان عدد النقاط التي تريد تحويلها لـ {id}')
    bot.register_next_step_handler(x2, get_amount_send, id, tid)
def get_info(message):
    id = message.text
    try:
        id = int(id)
    except:
        bot.reply_to(message, f'الايدي غلط ..')
        return
    d = db.get(f'user_{id}')
    if not d:
        bot.reply_to(message, f'مافي عضو..')
        return
    # {'id': user_id, 'users': [], 'coins': 0, 'paid': False}
    id, coins, users = d['id'], d['coins'], len(d['users'])
    bot.reply_to(message, f'• تم كشف العضو .\n\n ايديه : {id} .\nنقاطه : {coins} نقطة .\nاحالاته : {users}')
    return
def get_amount_send(message, id, tid):
    if tid != USER_TEMP[message.from_user.id]['trans']['id']:
        return
    amount = message.text
    try:
        amount = int(message.text)
    except:
        te = bot.reply_to(message, f'• الكمية يجب ان تكون عدد فقط ')
        return
    to_user = db.get(f'user_{id}')
    from_user = db.get(f'user_{message.from_user.id}')
    if amount < 1:
        bot.reply_to(message, f'• لا يمكن تحويل عدد اقل من 1')
        return
    if from_user['coins'] < amount:
        bot.reply_to(message, f'• نقاطك غير كافية لتحويل هذا المبلغ \n• تحتاج الى {amount-from_user["coins"]} نقطة')
        return
    from_user['coins']-=amount
    db.set(f'user_{message.from_user.id}', from_user)
    to_user['coins']+=amount
    db.set(f'user_{id}', to_user)
    try:
        bot.send_message(chat_id=id, text=f"• [👤] تم استلام {amount} من نقاط\n\n- من الشخص : {message.from_user.id}\n- نقاطك القديمة : {to_user['coins']}\n- نقاطك الان : {to_user['coins']+amount}")
    except: pass
    bot.send_message(chat_id=int(sudos), text=f'• قام شخص بارسال <strong>{amount}</strong> نقطة\n من <code>{message.from_user.id}</code> ..')
    bot.reply_to(message, f"• [👤] تم ارسال {amount} من نقاط\n\n- الى الشخص : {id}\n- نقاطك القديمة : {from_user['coins']}\n- نقاطك الان : {from_user['coins']-amount}")
    user_id = message.from_user.id
    trans = int(db.get(f"user_{user_id}_trans")) if db.exists(f"user_{user_id}_trans") else 0
    count_trans = trans + 1
    db.set(f"user_{user_id}_trans", int(count_trans))
    return

def addpoints(message):
    id = message.text
    try:
        id = int(message.text)
    except:
        bot.reply_to(message, '• ارسل الايدي بشكل صحيح رجاء')
        return
    x = bot.reply_to(message, '• ارسل الآن الكمية')
    bot.register_next_step_handler(x, addpoints_final, id)

def addpoints_final(message, id):
    global add_gems_enabled

    amount = message.text
    try:
        amount = int(message.text)
    except:
        bot.reply_to(message, 'يجب أن تكون الكمية أرقام فقط')
        return
    
    gems = get_gems(id)

    if add_gems_enabled:
        gems += amount

        set_gems(id, gems)

    b = db.get(f'user_{id}')

    if b is None:
        b = {
            'id': id,
            'coins': 0,
        }
        bot.reply_to(message, '• لم يتم العثور على المستخدم، يتم الآن إنشاء حساب جديد.')

    b['coins'] += amount

    db.set(f'user_{id}', b)

    bot.reply_to(message, f'تم إضافة النقاط {" والجواهر" if add_gems_enabled else ""} بنجاح ✅\n\n • نقاطه : {b["coins"]} \n• عدد الجواهر : {gems}')
    
    try:
        bot.send_message(id, f'تم إضافة {amount} نقطة{" و" + str(amount) + " جوهرة" if add_gems_enabled else ""} إلى حسابك.')
    except Exception as e:
        bot.reply_to(message, '• تعذر إرسال إشعار للمستخدم.')

def set_channel(message):
    cid = message.chat.id
    mid = message.message_id
    user_channel = message.text.replace('https://t.me/', '').replace('@', '') 

    if not user_channel:
        bot.reply_to(message, "الرجاء إدخال يوزر القناة بشكل صحيح.")
        return

    try:
        chat_member = bot.get_chat_member(chat_id="@" + user_channel, user_id=bot.get_me().id)
        if chat_member.status != 'administrator':
            bot.reply_to(message, f"البوت ليس مشرفًا في القناة @{user_channel}.\nيرجى منح البوت صلاحيات مشرف.")
            return
    except Exception as e:
        bot.reply_to(message, f"اليوزر غير صحيح ❌")
        return

    x = bot.send_message(chat_id=cid, text=f"• ارسل العدد المطلوب لتمويل قناة @{user_channel}", reply_markup=bk)
    bot.register_next_step_handler(x, set_points_for_channel, user_channel)

def set_points_for_channel(message, user_channel):
    cid = message.chat.id
    mid = message.message_id
    try:
        points = int(message.text)
    except ValueError:
        bot.reply_to(message, "انا طالب عدد بتبعت حروف ليه .. كرر العمليه من الاول")
        return

    current_forced_channels = db.get('force') or {}

    current_forced_channels[user_channel] = {
        "required_members": points,
        "subscribed_members": []  
    }
    db.set('force', current_forced_channels)

    bot.reply_to(message, f"تم إضافة القناة بنجاح ✅ \n• يوزر القناة : @{user_channel} \n\n• العدد المطلوب : {points}")

def GivtPonts(id,pont,tg):
    GV = Givt()
    res = GV.Get(id)
   
    if res[1]=="false" and tg >= 10:
        ##print("10")
        threading.Thread(target=GV.Add,args=(id,"true",res[2],res[3])).start()
        
        b = db.get(f'user_{id}')
        b['coins']+=1000
        db.set(f'user_{id}', b)
        bot.send_message(id, f'• لقد حصلت على 1000 نقطة هدية 🎁 لأنك قم بدعوة {tg} عضو .')   
    if res[2]=="false" and tg >= 100:
        ##print("100")
        threading.Thread(target=GV.Add,args=(id,res[1],"true",res[3])).start()
       
        b = db.get(f'user_{id}')
        b['coins']+=15000
        db.set(f'user_{id}', b)
        bot.send_message(id, f'• لقد حصلت على 15000 نقطة هدية 🎁 لأنك قم بدعوة {tg} عضو .')   
    if res[3]=="false" and tg >= 1000:
        ##print("1000")
        threading.Thread(target=GV.Add,args=(id,res[1],res[2],"true")).start()
        
        b = db.get(f'user_{id}')
        b['coins']+=12000
        db.set(f'user_{id}', b)
        bot.send_message(id, f'• لقد حصلت على 12000 نقطة هدية 🎁 لأنك قم بدعوة {tg} عضو .')   

def account(call):
    maintenance_mode = db.get("maintenance_mode") if db.exists("maintenance_mode") else False
    if maintenance_mode == True:
        bot.answer_callback_query(call.id, text="البوت قيد الصيانة والتطوير حاليا ⚙️", show_alert=True)
        return False

    yr = trend()
    cid, data, mid = call.from_user.id, call.data, call.message.id
    e = 5
    how = ""
    
    if e == 5:
        x = giiiift(cid)
        if x is not None:
            duration = datetime.timedelta(seconds=x)
            noww = datetime.datetime.now()
            target_datetime = noww + duration
            remaining_time = target_datetime - noww
            hours = remaining_time.seconds // 3600
            minutes = (remaining_time.seconds % 3600) // 60
            seconds = remaining_time.seconds % 60
            if hours > 0:
                how = f"{hours} ساعة"
            elif minutes > 0:
                how = f"{minutes} دقيقة"
            else:
                how = f"{seconds} ثانية"
        else:
            how = "يمكنك المطالبة بها 🎁"

        acc = get(cid)
        user_id = call.from_user.id
        coins = acc.get('coins', 0) 
        users = len(acc.get('users', [])) 
        info = db.get(f"user_{call.from_user.id}")
        daily_count = int(db.get(f"user_{user_id}_daily_count")) if db.exists(f"user_{user_id}_daily_count") else 0
        daily_gift = int(db.get("daily_gift")) if db.exists("daily_gift") else 30
        all_gift = daily_count * daily_gift
        buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
        trans = int(db.get(f"user_{user_id}_trans")) if db.exists(f"user_{user_id}_trans") else 0
        codes = int(db.get(f"cd_{user_id}")) if db.exists(f"cd_{user_id}") else 0
        po = int(db.get(f"po_{user_id}")) if db.exists(f"po_{user_id}") else 0
        share_links = int(db.get(f"user_{user_id}_share_links")) if db.exists(f"user_{user_id}_share_links") else 0 
        
        textt = f'''
• مرحبا بك في معلومات حسابك في بوت التمويل 🌀

- عدد القنوات او المجموعات الجاري تمويلها : {buys}
- عدد نقاط حسابك : {coins}

- عدد عمليات التحويل التي قمت بها : {trans}
- عدد القنوات التي شتركت بها : {users}
- عدد الهدايا اليومية التي جمعتها : {all_gift}
- عدد الاعضاء الذي قمت بطلبهم في عمليات التمويل : {codes}

- عدد مشاركاتك لرابط الدعوة : {share_links}
- عدد النقاط التي قمت بستخدامها : {po}

{yr}
'''

        keys = telebot.types.InlineKeyboardMarkup(row_width=2)
        btn1 = btn('رابط الدعوة', callback_data='share_link')
        keys.add(btn1)
        keys.add(btn('• رجــوع •', callback_data='back'))
        bot.edit_message_text(text=textt, chat_id=cid, message_id=mid, reply_markup=keys)
def lespoints(message):
    if message.text == "/start":
        start_message(message)
        return
    id = message.text
    try:
        id = int(message.text)
    except:
        bot.reply_to(message, f'• ارسل الايدي بشكل صحيح رجاء')
        return
    x = bot.reply_to(message, '• ارسل الان الكمية :')
    bot.register_next_step_handler(x, lespoints_final, id)
def lespoints_final(message, id):
    if message.text == "/start":
        start_message(message)
        return
    amount = message.text
    try:
        amount = int(message.text)
    except:
        bot.reply_to(message, f'يجب ان تكون الكمية ارقام فقط')
        return
    b = db.get(f'user_{id}')
    b['coins']-=amount
    db.set(f'user_{id}', b)
    bot.reply_to(message, f'تم بنجاح نقاطه الان : {b["coins"]} ')
def check_dayy(user_id):
    users = db.get(f"user_{user_id}_giftt")
    noww = time.time()    
    WAIT_TIMEE = 24 * 60 * 60
    if db.exists(f"user_{user_id}_giftt"):
        last_time = users['timee']
        elapsed_time = noww - last_time
        if elapsed_time < WAIT_TIMEE:
            remaining_time = WAIT_TIMEE - elapsed_time
            return int(remaining_time)
        else:
            users['timee'] = noww
            db.set(f'user_{user_id}_giftt', users)
            return None
    else:
        users = {}
        users['timee'] = noww
        db.set(f'user_{user_id}_giftt', users)
        return None

@bot.message_handler(regexp='^/id$')
def i_d(message):
    x = f"""⌁︙عزيزي {message.from_user.first_name}
⌁︙ال ID الخاص بحسابك هو 
<code>{message.from_user.id}</code>
"""
    bot.send_message(message.chat.id, x)
    # print('on message 2')
    
@bot.message_handler(regexp='^/url$')
def i_d(message):
    x = f"""⌁︙عزيزي {message.from_user.first_name}
⌁︙الـ URL الخاص بحسابك هو 👤
https://t.me/{bot_username}?start={message.from_user.id}"""
    bot.send_message(message.chat.id, x)
 
 
def entre_bot(message):
    try:
        it = int(message.text)
        bot.reply_to(message, f"تم تغيير عدد النقاط الى {it}",reply_markup=bk)
        db.set("entre_bot", it)
    except:
        bot.reply_to(message, f"ارسل رقم فقط عزيزي",reply_markup=bk)

def get_code_coin(message, ids):
    if USER_TEMP[message.from_user.id]['code']['id'] != ids:
        return 
    code = message.text
    if not datas.CODE_EXISTS(code):
        bot.send_message(text='عذرا الكود غير صحيح او انتهت صلاحيتة ! ', chat_id=message.chat.id)
        return
    cods_data = datas.GET_DATA()

    if message.from_user.id in cods_data['code'][code]['users']:
        bot.send_message(text='عذرا لا يمكنك استخدام الكود اكثر من مرة ! ', chat_id=message.chat.id)
        return
    from_user = db.get(f'user_{message.from_user.id}')
    from_user['coins']+=cods_data['code'][code]['coin']
    db.set(f'user_{message.from_user.id}', from_user)
    bot.send_message(text='الكود صحيح ✅\n\nتم اضافة {} نقطه الى حسابك'.format(cods_data['code'][code]['coin']), chat_id=message.chat.id)
    cods_data['code'][code]['mem']-=1 
    cods_data['code'][code]['users'].append(message.from_user.id) 
    if cods_data['code'][code]['mem'] == 0:
        cods_data['code'].pop(code)
    datas.UPDATE_DATA(cods_data)


def hand_get_code_coin(message, code):
    try:
        coin = int(message.text)
    except:
        bot.send_message(text='يرجى ارسال ارقام بدون احرف .', chat_id=message.chat.id)
        return
    ms = bot.send_message(text='ارسل عدد الاعضاء', chat_id=message.chat.id)
    bot.register_next_step_handler(ms, hand_get_code_mem, code,coin)
    

def hand_get_code_mem(message, code, coin):
    try:
        mem = int(message.text)
    except:
        bot.send_message(text='يرجى ارسال ارقام بدون احرف .', chat_id=message.chat.id)
        return
    
    datas.NEW_CODE(code, coin, mem)
    bot.send_message(chat_id=message.chat.id, text='''<strong>• تم انشاء كود هديه بنجاح 🎁 </strong>\n\n<strong>[🩵] الكود </strong>: <code>{} </code>\n<strong>[⚙️] عدد النقاط </strong>: {} \n<strong>[👤] عدد الاعضاء </strong>: {}\n\n<strong>[🤖] البوت </strong>: @S_2_Xbot'''.format(code, coin, mem))

def make_code_coin(message):
    try:
        coin = int(message.text)
    except ValueError:
        bot.send_message(text='❌ يرجى إرسال أرقام بدون أحرف.', chat_id=message.chat.id)
        return
    
    from_user = db.get(f'user_{message.from_user.id}')
    
    if from_user['coins'] < coin:
        bot.send_message(text='❌ لا يوجد لديك نقاط كافية.', chat_id=message.chat.id)
        return 
    
    if coin < 100:
        bot.send_message(text='❌ عذرًا، أقل عدد للتحويل هو 100 نقطة.', chat_id=message.chat.id)
        return 
    
    CODE = RAND_CODE()
    invite_link = f'https://t.me/{bot_username}?start={CODE}'
    
    from_user['coins'] -= coin
    db.set(f'user_{message.from_user.id}', from_user)
    
    existing_code = db.get(f"code_{CODE}")
    
    if existing_code:
        if existing_code['used']:
            bot.send_message(chat_id=message.chat.id, text='❌ هذا الكود قد تم استخدامه من قبل.')
            return

    code_data = {
        "code": CODE,
        "coin": coin,
        "user_id": message.from_user.id,
        "used": False 
    }
    db.set(f"code_{CODE}", code_data)

    bot.send_message(
        chat_id=message.chat.id,
        text=f'''🎉 • تم إنشاء رابط تحويل النقاط بنجاح: 
        
- عدد النقاط : {coin} 

- رابط الهدية : {invite_link}

- البوت : @{bot_username}''',
        parse_mode='Markdown'
    )
        
def process_quantity_and_order(message, user_id, service_name, coins):
    cid = message.chat.id
    
    try:
        quantity = int(message.text)
    except ValueError:
        u = bot.send_message(cid, "⚠️ يرجى إدخال عدد صحيح.")
        return

    min_limit = service_limits.get(service_name, {}).get("min", None)
    max_limit = service_limits.get(service_name, {}).get("max", None)

    if min_limit is not None and quantity < min_limit:
        bot.send_message(cid, f"⚠️ العدد الذي ادخلته أقل من الحد الأدنى \n\n- اقل عدد يمكنك طلبه : {min_limit}.")
        return
    if max_limit is not None and quantity > max_limit:
        bot.send_message(cid, f"⚠️ العدد الذي ادخلته أكبر من الحد الأقصى \n\n- اقصى عدد يمكنك طلبه : {max_limit}")
        return

    user_info = db.get(f'user_{user_id}')
    
    if user_info is None:
        user_info = {
            'id': user_id,
            'coins': 0 
        }
        bot.send_message(cid, '• لم يتم العثور على المستخدم، يتم الآن إنشاء حساب جديد.')
    
    coins = user_info['coins'] 

    total_cost = quantity * prices[service_name] / 1000

    inline_kb = telebot.types.InlineKeyboardMarkup()
    inline_kb.add(telebot.types.InlineKeyboardButton(text="شحن نقاط 💰", callback_data='shahn'))

    if coins >= total_cost:
        new_coins = coins - total_cost
        user_info['coins'] = new_coins
        db.set(f'user_{user_id}', user_info) 

        u = bot.send_message(cid, f"💵] إجمالي السعر {total_cost} نقطة\n🔗] أرسل الرابط الذي تريد تنفيذ الخدمة له")
        bot.register_next_step_handler(u, lambda msg: execute_order_and_notify(msg, user_id, service_name, quantity))
    else:
        bot.send_message(cid, "❌] نقاطك لا تكفي لتنفيذ هذه الخدمة.", reply_markup=inline_kb)
        return

import requests
import datetime

def execute_order_and_notify(um, user_id, service_name, quantity):
    url = um.text

    if url.startswith("http://") or url.startswith("https://"):
        order_id = ao(url, service_ids[service_name], q=quantity)

        if order_id:
            db.set(f"order_{order_id}", {
                "service_name": service_name,
                "quantity": quantity,
                "url": url,
                "time": str(datetime.datetime.now()),
                "status": "جاري التنفيذ"
            })

            notify_order_completion(um.chat.id, user_id, service_name, quantity, url, order_id)
        else:
            bot.send_message(um.chat.id, "⚠️] فشل في تقديم الطلب بسبب وجود ضغط على الخدمة")
            notify_admin_about_balance_issue() 
    else:
        bot.send_message(um.chat.id, "⚠️] الرابط غير صحيح. تم إلغاء العملية.")
        return

def notify_order_completion(chat_id, user_id, service_name, quantity, url, order_id):
    global total_orders
    total_orders += 1

    write_total_orders(total_orders)

    service_name_ar = service_translations.get(service_name, service_name)

    bot.send_message(
        chat_id,
        f"""تم تقديم الطلب بنجاح ✅
        
✨] الخدمة : {service_name_ar}

🔢] العدد : {quantity}

🔗] الرابط : {url}

🆔] ايدي الطلب : {order_id}
"""
    )

    send_welcometre(chat_id, user_id)

def notify_admin_about_balance_issue():
    balance = get_balance()
    bot.send_message(
        sudos,
        f"⚠️ تحذير بشأن رصيد الحساب في الموقع\n\n💵] الرصيد الحالي : {balance}."
    )

def send_welcometre(chat_id, user_id):
    coin = get(user_id)['coins']  
    gems = get_gems(user_id)

    keys, mm = create_main_menu(user_id, coin, gems) 

    bot.send_message(chat_id, mm, reply_markup=keys)

def create_main_menu(user_id, coin, gems, first_name):
    keys = telebot.types.InlineKeyboardMarkup(row_width=2)

    btn2 = telebot.types.InlineKeyboardButton(text='تمويل👥قناتك او مجموعتك⛈️', callback_data='tmoo')
    btn3 = telebot.types.InlineKeyboardButton(text='معلومات حسابك ℹ️', callback_data='account')
    btn4 = telebot.types.InlineKeyboardButton(text='تجميع النقاط ✨', callback_data='collect')
    btn5 = telebot.types.InlineKeyboardButton(text='تحويل نقاط ♻️', callback_data='send_coin')
    relr = telebot.types.InlineKeyboardButton(text='تمويلاتي ✉️', callback_data='mytm')
    btn10 = telebot.types.InlineKeyboardButton(text='الهديه اليوميه 🎁', callback_data='dailygift')
    wevy = telebot.types.InlineKeyboardButton(text='التمويل السريع🎉', callback_data='shahn')
    wevy1 = telebot.types.InlineKeyboardButton(text='قوانين البوت🤖', callback_data='shrot')
    wevy2 = telebot.types.InlineKeyboardButton(text='قنـوات البـوت 💡', callback_data='channelbot')
    btn_total_orders = telebot.types.InlineKeyboardButton(text=f"♻️قـسـم الاستبدال💠", callback_data='redeem')
    member = telebot.types.InlineKeyboardButton(text=f"اعضاء حقيقي متفاعلين💯", url='https://t.me/shahm41')

    keys.add(btn2)
    keys.add(btn4, btn5)
    keys.add(relr, btn3)
    keys.add(btn10)
    keys.add(wevy, wevy1)
    keys.add(wevy2, btn_total_orders)
    keys.add(member)

    account_link = f"{first_name}"
    menu_text = f"""أهلاً بك: {account_link} 💳 
في بوت تمويل #شهم 🐍
•┊-🔺البوت مخصص لزيادة❇️ مشتركين القنوات والقروبات عن طريق تجميع النقاط.
الإدارة للتواصل🎖️: @shahm41 ➢ 
نقاطك: ♻️《 {coin} 》
🆔 :ايديك《 {user_id} 》"""

    return keys, menu_text

def send_user_buttons(message):
    user_id = message.from_user.id
    
    user_data = get(user_id) if get(user_id) else {}
    coin = user_data.get('coins', 0)
    
    account_name = message.from_user.first_name

    keys = telebot.types.InlineKeyboardMarkup(row_width=2)

    btn2 = telebot.types.InlineKeyboardButton(text='تمويل👥قناتك او مجموعتك⛈️', callback_data='tmoo')
    btn3 = telebot.types.InlineKeyboardButton(text='معلومات حسابك ℹ️', callback_data='account')
    btn4 = telebot.types.InlineKeyboardButton(text='تجميع النقاط ✨', callback_data='collect')
    btn5 = telebot.types.InlineKeyboardButton(text='تحويل نقاط ♻️', callback_data='send_coin')
    relr = telebot.types.InlineKeyboardButton(text='تمويلاتي ✉️', callback_data='mytm')
    btn10 = telebot.types.InlineKeyboardButton(text='الهديه اليوميه 🎁', callback_data='dailygift')
    wevy = telebot.types.InlineKeyboardButton(text='التمويل السريع🎉', callback_data='shahn')
    wevy1 = telebot.types.InlineKeyboardButton(text='قوانين البوت🤖', callback_data='shrot')
    wevy2 = telebot.types.InlineKeyboardButton(text='قنـوات البـوت 💡', callback_data='channelbot')
    btn_total_orders = telebot.types.InlineKeyboardButton(text=f"♻️قـسـم الاستبدال💠", callback_data='redeem')
    member = telebot.types.InlineKeyboardButton(text=f"اعضاء حقيقي متفاعلين💯", url='https://t.me/shahm41')

    keys.add(btn2)
    keys.add(btn4, btn5)
    keys.add(relr, btn3)
    keys.add(btn10)
    keys.add(wevy, wevy1)
    keys.add(wevy2, btn_total_orders)
    keys.add(member)

    account_link = f"{account_name}"
    response_message = f"""أهلاً بك: {account_link} 💳 
في بوت تمويل #شهم 🐍
•┊-🔺البوت مخصص لزيادة❇️ مشتركين القنوات والقروبات عن طريق تجميع النقاط.
الإدارة للتواصل🎖️: @shahm41 ➢ 
نقاطك: ♻️《 {coin} 》
🆔 :ايديك《 {user_id} 》"""

    bot.edit_message_text(
        chat_id=message.chat.id, 
        message_id=message.message_id,  
        text=response_message,
        reply_markup=keys
    )

def send_user_buttonsesr(message):
    user_id = message.from_user.id

    user_data = get(user_id)
    if 'coins' not in user_data:
        user_data['coins'] = 0
        set(user_id, user_data)

    coin = user_data['coins']
    account_name = message.from_user.first_name

    keys = telebot.types.InlineKeyboardMarkup(row_width=2)

    btn2 = telebot.types.InlineKeyboardButton(text='تمويل👥قناتك او مجموعتك⛈️', callback_data='tmoo')
    btn3 = telebot.types.InlineKeyboardButton(text='معلومات حسابك ℹ️', callback_data='account')
    btn4 = telebot.types.InlineKeyboardButton(text='تجميع النقاط ✨', callback_data='collect')
    btn5 = telebot.types.InlineKeyboardButton(text='تحويل نقاط ♻️', callback_data='send_coin')
    relr = telebot.types.InlineKeyboardButton(text='تمويلاتي ✉️', callback_data='mytm')
    btn10 = telebot.types.InlineKeyboardButton(text='الهديه اليوميه 🎁', callback_data='dailygift')
    wevy = telebot.types.InlineKeyboardButton(text='التمويل السريع🎉', callback_data='shahn')
    wevy1 = telebot.types.InlineKeyboardButton(text='قوانين البوت🤖', callback_data='shrot')
    wevy2 = telebot.types.InlineKeyboardButton(text='قنـوات البـوت 💡', callback_data='channelbot')
    btn_total_orders = telebot.types.InlineKeyboardButton(text=f"♻️قـسـم الاستبدال💠", callback_data='redeem')
    member = telebot.types.InlineKeyboardButton(text=f"اعضاء حقيقي متفاعلين💯", url='https://t.me/shahm41')

    keys.add(btn2)
    keys.add(btn4, btn5)
    keys.add(relr, btn3)
    keys.add(btn10)
    keys.add(wevy, wevy1)
    keys.add(wevy2, btn_total_orders)
    keys.add(member)

    account_link = f"{account_name}"
    response_message = f"""أهلاً بك: {account_link} 💳 
في بوت تمويل #شهم 🐍
•┊-🔺البوت مخصص لزيادة❇️ مشتركين القنوات والقروبات عن طريق تجميع النقاط.
الإدارة للتواصل🎖️: @shahm41 ➢ 
نقاطك: ♻️《 {coin} 》
🆔 :ايديك《 {user_id} 》"""

    bot.send_message(
        chat_id=message.chat.id,
        text=response_message,
        reply_markup=keys,
        
    )

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def show_banned_channels(call):
    blacklist = db.get('chat_blacklist') if db.exists('chat_blacklist') else []
    if not blacklist:
        bot.send_message(call.message.chat.id, text="لا توجد قنوات محظورة حالياً.")
        return
    
    keyboard = InlineKeyboardMarkup(row_width=1)
    for channel in blacklist:
        button = InlineKeyboardButton(text=f"{channel}", callback_data=f"unban_{channel}")
        keyboard.add(button)
    
    back_button = InlineKeyboardButton(text="رجوع", callback_data="back_to_main")
    keyboard.add(back_button)
    
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="قائمة القنوات المحظورة :", reply_markup=keyboard)

def unban_channel(call, channel_username):
    blacklist = db.get('chat_blacklist') if db.exists('chat_blacklist') else []
    if channel_username in blacklist:
        blacklist.remove(channel_username)
        db.set('chat_blacklist', blacklist)
        bot.answer_callback_query(call.id, text=f"تم إلغاء حظر قناة {channel_username} بنجاح")
    else:
        bot.answer_callback_query(call.id, text="هذه القناة غير محظورة.")

def BAND_CHAT(channel_username: str):
    user_id = db.get(f'id_{channel_username}')
    chats_dd = db.get('force_ch')
    chats_dd.remove(channel_username)
    db.set('force_ch', chats_dd)
    balcklist = db.get('chat_blacklist')
    balcklist.append(channel_username)
    db.set('chat_blacklist', balcklist)
    bot.send_message(text=f'تم ايقاف تمويل قناتك ( {channel_username} ) من قبل المطور بسبب مخالفة قوانين البوت .', chat_id=user_id)    
    
def skip(call):
    cid, data, mid = call.from_user.id, call.data, call.message.id
    user_id = call.from_user.id
    coin_join = db.get("coin_join") if db.exists("coin_join") else 10
    chats_joining = db.get(f"chats_{user_id}") if db.exists(f"chats_{user_id}") else []
    chats_dd = db.get('force_ch')
    joo = db.get(f"user_{user_id}")
    coin = joo['coins']
    chats_user = [chat for chat in chats_dd if chat not in chats_joining]
    doo = db.get('force_ch')
    if doo != None:
        for i in chats_user:
            chats_joining.append(i)
            db.set(f"chats_{user_id}", chats_joining)
            nextch(call)
            return
def nextch(call):
    cid, data, mid = call.from_user.id, call.data, call.message.id
    user_id = call.from_user.id
    v = 5
    if v == 5:
        coin_join = db.get("coin_join") if db.exists("coin_join") else 10
        chats_joining = db.get(f"chats_{user_id}") if db.exists(f"chats_{user_id}") else []
        ch_joining = db.get(f"ch_{user_id}") if db.exists(f"ch_{user_id}") else []
        chats_dd = db.get('force_ch')
        joo = db.get(f"user_{user_id}")
        coin = joo['coins']
        chats_user = [chat for chat in chats_dd if chat not in chats_joining]
        doo = db.get('force_ch')
        threading.Thread(target=CeckAnjoens,args=(user_id,)).start()
        if doo != None:
            for i in chats_user:
                count = db.get(f"count_{i}")
                ids = db.get(f"id_{i}")
                Status = requests.get(f"https://api.telegram.org/bot{token_helper}/getChatMember?chat_id={i}&user_id={ids}").json()["ok"]
                if Status:
                    
                    if int(count) <= 2:
                        
                        tm = db.get("tmoil") if db.exists("tmoil") else 0
                        tmm = int(tm) + 1
                        db.set("tmoil", int(tmm))
                        chats_dd = db.get('force_ch')
                        chats_dd.remove(i)
                        db.set("force_ch", chats_dd)
                        chat_info = bot.get_chat(i)
                        name = chat_info.title
                        ii = i.replace('@', '')
                        mem = db.get(f"mem_{i}") if db.exists(f"mem_{i}") else "عدد غير معروف"
                        bot.send_message(chat_id=int(ids), text=f"تم انتهاء تمويل قناتك @{ii} ب {mem} عضو 🚸", parse_mode="Markdown")
                        bot.send_message(chat_id=sudos, text=f"*تم انتهاء تمويل قناتك *[{name}](https://t.me/{ii})* بنجاح ✅*\n*• تم تمويل : {mem} عضو* 🚸", parse_mode="Markdown")
                    else: 
                        chat_info = bot.get_chat(i)
                        name = chat_info.title
                        ii = i.replace('@', '')
                        k = f'''• اشترك في القناة : {i} 📣'''
                        keys = mk(
                            [
                                [btn(text=f'{name}', url=f'https://t.me/{ii}')],
                                [btn(text='اشتركت ✅', callback_data='check_join'), btn(text='تخطي 🚸', callback_data='skip')],
                                [btn(text='🔙 رجــوع', callback_data='collect')]
                            ]
                        )
                        bot.edit_message_text(text=k, chat_id=cid, message_id=mid,reply_markup=keys)
                        return
            kk = f"• لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه ❕\n• اذا قمت بمغادرة اي قناة سيتم خصم ضعف النقاط"
            key = mk(
                [
                    [btn(text='تجميع النقاط ', callback_data='collect')],
                    [btn(text='الغاء ❌', callback_data='back')]
                ]
            )
            bot.edit_message_text(text=kk, chat_id=cid, message_id=mid,reply_markup=key, parse_mode="Markdown")
def tmmo(msg):
    user_id = msg.from_user.id
    if not db.get(f'tmoo_{msg.from_user.id}_proccess'): return
    coin_join = db.get("coin_join") if db.exists("coin_join") else 10
    chats_joining = db.get(f"ch_{user_id}") if db.exists(f"ch_{user_id}") else []
    joo = db.get(f"user_{user_id}")
    price_join = db.get("price_join") if db.exists("price_join") else 10
    coin = int(joo['coins'])
    try:
        count = int(msg.text)
    except:
        bot.reply_to(msg, '• يجب ان يكون عدد فقط ❌')
        return
    if count <15:
        bot.reply_to(msg, "اقل حد للطلب هو 15 ❌")
        return
    all = int(price_join) * int(count)
    joo = db.get(f"user_{user_id}")
    if joo['coins'] < int(all):
        bot.reply_to(msg, "• عفوا ، نقاطك لا تكفي لهذا الطلب ❌")
        return
    x = bot.reply_to(msg, "• ارفع البوت المساعد {bot_trans} ادمن في قناتك او مجموعتك\n\n• ثم ارسل المعرف او الرابط الخاص بالقناة او المجموعة 👥")
    bot.register_next_step_handler(x, tmm_count, count)
def tmm_count(msg,count):
    user_id = msg.from_user.id
    coin_join = db.get("coin_join") if db.exists("coin_join") else 10
    chats_joining = db.get(f"ch_{user_id}") if db.exists(f"ch_{user_id}") else []
    joo = db.get(f"user_{user_id}")
    price_join = db.get("price_join") if db.exists("price_join") else 10
    channel = msg.text.replace('https://t.me/', '@').replace('@', '@')
    channels_force = db.get("force_ch") if db.exists("force_ch") else []
    channel_username = channel.lower().strip()
    balcklist = db.get('chat_blacklist')
    if channel_username in balcklist:
        bot.send_message(text='عذراً تم حظر قناتك من البوت', chat_id=msg.chat.id)
        return 
    try:
        chat_member = bot2.get_chat_member(channel_username, bot2.get_me().id)
    except:
        bot.reply_to(msg, "* لا يوجد قناة او مجموعة تحمل هذا المعرف ❌*", parse_mode="Markdown")
        return False
    if str(chat_member.status) == "administrator":
        if channel_username in channels_force:
            count_befor = db.get(f"count_{channel_username}")
            alll = int(count_befor) + int(count)
            all_coins = int(price_join) * int(count)
            joo = db.get(f"user_{user_id}")
            joo['coins'] = int(joo['coins']) - int(all_coins)
            db.set(f"user_{user_id}", joo)
            db.set(f"count_{channel_username}", alll)
            db.set(f"mem_{channel_username}", alll)
            db.set(f"id_{channel_username}", user_id)
            chat_info = bot.get_chat(channel_username)
            name = chat_info.title
            ii = channel_username.replace('@', '')
            all_coins = int(price_join) * int(count)
            bot.reply_to(msg, f"• تم خصم ({all_coins}) نقاط\n- وبدء تمويل قناتك [{name}](https://t.me/{ii}) بـ {alll} عضو 🚸\n• تاكد من عدم ازالة البوت من الادمنية حتي لا يتم استبعاد تمويلك", parse_mode="Markdown")
            bot.send_message(chat_id=sudos, text=f"- بدء تمويل قناة جديدة [{name}](https://t.me/{ii}) بـ {alll} عضو 🚸", parse_mode="Markdown")
            typ = float(db.get(f"typ_{user_id}")) if db.exists(f"typ_{user_id}") else 0.0
            ftt = typ + 0.2
            db.set(f"typ_{user_id}", float(ftt))
            my_tmm = db.get(f"my_tmm_{user_id}") if db.exists(f"my_tmm_{user_id}") else []
            if channel_username not in my_tmm:
                my_tmm.append(channel_username)
                db.set(f"my_tmm_{user_id}", my_tmm)
        else:
            all = int(price_join) * int(count)
            joo = db.get(f"user_{user_id}")
            joo['coins'] = int(joo['coins']) - int(all)
            db.set(f"user_{user_id}", joo)
            db.set(f"count_{channel_username}", count)
            db.set(f"mem_{channel_username}", count)
            db.set(f"id_{channel_username}", user_id)
            channels_force = db.get("force_ch") if db.exists("force_ch") else []
            channels_force.append(channel_username)
            db.set("force_ch", channels_force)
            chat_info = bot.get_chat(channel_username)
            name = chat_info.title
            ii = channel_username.replace('@', '')
            bot.reply_to(msg, f"• تم خصم ({all}) نقاط\n- وبدء تمويل قناتك [{name}](https://t.me/{ii}) بـ {count} عضو 🚸\n\n• تاكد من عدم ازالة البوت من الادمنية حتي لا يتم استبعاد تمويلك", parse_mode="Markdown")
            bot.send_message(chat_id=sudos, text=f"- بدء تمويل قناة جديدة [{name}](https://t.me/{ii}) بـ {count} عضو 🚸", parse_mode="Markdown")
            typ = float(db.get(f"typ_{user_id}")) if db.exists(f"typ_{user_id}") else 0.0
            ftt = typ + 0.2
            db.set(f"typ_{user_id}", float(ftt))
            my_tmm = db.get(f"my_tmm_{user_id}") if db.exists(f"my_tmm_{user_id}") else []
            if channel_username not in my_tmm:
                my_tmm.append(channel_username)
                db.set(f"my_tmm_{user_id}", my_tmm)
    else:
        bot.reply_to(msg, "*البوت غير مشرف بهذه القناة ❌*", parse_mode="Markdown")
        return
    
def giiiift(user_id):
    users = db.get(f"us_{user_id}_giftt")
    noww = time.time()
    WAIT_TIMEE = 24 * 60 * 60
    if db.exists(f"us_{user_id}_giftt"):
        last_time = users['timee']
        elapsed_time = noww - last_time
        if elapsed_time < WAIT_TIMEE:
            remaining_time = WAIT_TIMEE - elapsed_time
            return int(remaining_time)
        else:
            return None
    else:
        return None
    
@bot.channel_post_handler(func=lambda message: True , content_types=['text', 'photo', 'video', 'audio'])
def handle_new_channel_post(message):
    tom_ch = db.get("tom_ch") if db.exists("tom_ch") else []
    tom_r_ch = db.get("tom_r_ch") if db.exists("tom_r_ch") else []
    # print('on message 1')
    if message.chat.username not in tom_ch and message.chat.username not in tom_r_ch:
        return
    # print('on message 2')
    
    if message.chat.username in tom_r_ch:
        count = int(db.get(f"tom_r_{message.chat.username}"))
        type = db.get(f"type_r_{message.chat.username}")
        amount = db.get(f"amount_r_{message.chat.username}")
        load_ = db.get('accounts')
        true = 0
        false = 0

        if count <=1:
            tom_ch = db.get("tom_r_ch") if db.exists("tom_r_ch") else []
            tom_ch.remove(message.chat.username)
            db.set("tom_r_ch",tom_ch)
            return
        
        channel = message.chat.username
        msg_id = message.message_id
        for y in load_:
            if true >= amount:
                break
            try:

                x = asyncio.run(tom_rect(y['s'], channel, msg_id))
            except Exception as e:
                # print(e)
                pass
                # return
        count = int(db.get(f"tom_{message.chat.username}"))
        aft = count - 1
        db.set(f"tom_{message.chat.username}", aft)
        
    
    if message.chat.username in tom_ch:
        count = int(db.get(f"tom_{message.chat.username}"))
        type = db.get(f"type_{message.chat.username}")
        amount = db.get(f"amount_{message.chat.username}")
        load_ = db.get('accounts')
        true = 0
        false = 0
        
        if count <=1:
            tom_ch = db.get("tom_ch") if db.exists("tom_ch") else []
            tom_ch.remove(message.chat.username)
            db.set("tom_ch",tom_ch)
            return
        
        channel = message.chat.username
        msg_id = message.message_id
        for y in load_:
            if true >= amount:
                break
            try:

                x = asyncio.run(tom_view(y['s'], channel, msg_id))
            except Exception as e:
                # print(e)
                pass
                # return
        count = int(db.get(f"tom_{message.chat.username}"))
        aft = count - 1
        db.set(f"tom_{message.chat.username}", aft)

try:
    bot.infinity_polling()
    bot2.infinity_polling()
except:
    pass




