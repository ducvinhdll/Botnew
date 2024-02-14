#Bé Sữa or Bé Gấu
import telebot
import datetime
import time
import os
import subprocess
import sqlite3
import hashlib
import requests
import sys
import socket
import zipfile
import io
import re
import threading

bot_token = '6497238274:AAHk29agf_aNNuaOAA61e-cUxNu0xYuLunU'# nhập token bot

bot = telebot.TeleBot(bot_token)

allowed_group_id = -1002116851541

allowed_users = []
processes = []
ADMIN_ID = 5789810284
proxy_update_count = 0
last_proxy_update_time = time.time()

connection = sqlite3.connect('user_data.db')
cursor = connection.cursor()

# Create the users table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        expiration_time TEXT
    )
''')
connection.commit()
def TimeStamp():
    now = str(datetime.date.today())
    return now
def load_users_from_database():
    cursor.execute('SELECT user_id, expiration_time FROM users')
    rows = cursor.fetchall()
    for row in rows:
        user_id = row[0]
        expiration_time = datetime.datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S')
        if expiration_time > datetime.datetime.now():
            allowed_users.append(user_id)

def save_user_to_database(connection, user_id, expiration_time):
    cursor = connection.cursor()
    cursor.execute('''
        INSERT OR REPLACE INTO users (user_id, expiration_time)
        VALUES (?, ?)
    ''', (user_id, expiration_time.strftime('%Y-%m-%d %H:%M:%S')))
    connection.commit()
@bot.message_handler(commands=['start', 'lenh'])
def lenh(message):
    help_text = '''
⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣶⡋⠉⠙⠒⢤⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣼⣟⡒⠒⠀⠀⠀⠀⠀⠙⣆⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣼⠷⠖⠀⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀
⠀⠀⠀⠀⠀⠀⣷⡒⠀⠀⢐⣒⣒⡒⠀⣐⣒⣒⣧⠀
⠀⠀⠀⠀⠀⢰⣛⣟⣂⠀⠘⠤⠬⠃⠰⠑⠥⠊⣿⠀
⠀⠀⠀⠀⠀⢸⣿⡿⠤⠀⠀⠀⠀⠀⢀⡆⠀⠀⣿⠀⠀
⠀⠀⠀⠀⠀⠈⠿⣯⡭⠀⠀⠀⠀⢀⣀⠀⠀⠀⡟⠀
⠀⠀⠀⠀⠀⠀⠀⠈⢯⡥⠄⠀⠀⠀⠀⠀⠀⡼⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱⡦⣄⣀⣀⣀⣠⠞⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⠛⠃⠀⠀⠀⢹⠳⡶⣤⡤⣄⠀
⠀⠀⠀⠀⣠⢴⣿⣿⣿⡟⡷⢄⣀⣀⣀⡼⠳⡹⣿⣷⠞⣳⠀
⠀⠀⠀⢰⡯⠭⠹⡟⠿⠧⠷⣄⣀⣟⠛⣦⠔⠋⠛⠛⠋⠙⡆⠀⠀
⠀⠀⢸⣿⠭⠉⠀⢠⣤⠀⠀⠀⠘⡷⣵⢻⠀⠀⠀⠀⣼⠀⣇
⠀⠀⡇⣿⠍⠁⠀⢸⣗⠂⠀⠀⠀⣧⣿⣼⠀⠀⠀⠀⣯⠀⢸

   𝐴𝑑𝑚𝑖𝑛 𝐵𝑜𝑡 : DuckVinh
╭─────────────────────────────╮
│✿ /check + [ 𝐻𝑜𝑠𝑡 ] : 𝐶ℎ𝑒𝑐𝑘 𝐴𝑛𝑡𝑖 𝐷𝑑𝑜𝑠
│✿ /downtik: 𝐷𝑜𝑤𝑛𝑙𝑜𝑎𝑑 𝑉𝑑 𝑇𝑖𝑘𝑇𝑜𝑘
│✿ /time : 𝐶ℎ𝑒𝑐𝑘 𝑡𝑖𝑚𝑒 𝑏𝑜𝑡 ℎ𝑜𝑎̣𝑡 𝑑𝑜̣̂𝑛𝑔
│✿ /sex : sex videos list,loan luan,boocon....
╰─────────────────────────────╯
'''
    bot.reply_to(message, help_text)
    
is_bot_active = True
@bot.message_handler(commands=['sjms'])
def lqm_sms(message):
    user_id = message.from_user.id
    if len(message.text.split()) == 1:
        bot.reply_to(message, '𝑉𝑈𝐼 𝐿𝑂̀𝑁𝐺 𝑁𝐻𝐴̣̂𝑃 𝑆𝑂̂́ 𝐷𝐼𝐸̣̂𝑁 𝑇𝐻𝑂𝐴̣𝐼 ')
        return

    phone_number = message.text.split()[1]
    if not phone_number.isnumeric():
        bot.reply_to(message, '𝑆𝑂̂́ 𝐷𝐼𝐸̣̂𝑁 𝑇𝐻𝑂𝐴̣𝐼 𝐾𝐻𝑂̂𝑁𝐺 𝐻𝑂̛̣𝑃 𝐿𝐸̣̂ !')
        return

    if phone_number in ['113','911','114','115','+84328774559','03623402']:
        # Số điện thoại nằm trong danh sách cấm
        bot.reply_to(message,"𝑀𝑢𝑜̂́𝑛 𝐷𝑖 𝑇𝑢̀ 𝐴̀ 𝑀𝑎̀ 𝑆𝑝𝑎𝑚 𝑆𝑜̂́ 𝑁𝑎̀𝑦 ❌")
        return

    file_path = os.path.join(os.getcwd(), "cc.py")    
    file_path2 = os.path.join(os.getcwd(), "sms.py")
    file_path3 = os.path.join(os.getcwd(), "n.py")
    file_path4 = os.path.join(os.getcwd(), "liem.py")
    process = subprocess.Popen(["python", file_path, phone_number, "400"])    
    process = subprocess.Popen(["python", file_path2, phone_number, "1000"])
    process = subprocess.Popen(["python", file_path3, phone_number, "300"])
    process = subprocess.Popen(["python", file_path4, phone_number, "300"])
    processes.append(process)
    username = message.from_user.username

    current_time = time.time()
    if username in cooldown_dict and current_time - cooldown_dict[username].get('free', 0) < 120:
        remaining_time = int(120 - (current_time - cooldown_dict[username].get('free', 0)))
        bot.reply_to(message, f"@{username} 𝑉𝑢𝑖 𝑙𝑜̀𝑛𝑔 𝑑𝑜̛̣𝑖 {remaining_time} 𝑔𝑖𝑎̂𝑦 𝑡𝑟𝑢̛𝑜̛́𝑐 𝑘ℎ𝑖 𝑠𝑢̛̉ 𝑑𝑢̣𝑛𝑔 𝑙𝑎̣𝑖 𝑙𝑒̣̂𝑛ℎ  /sms.")
        return
    video_url = "https://files.catbox.moe/eewee0.mp4"  # Replace this with the actual video URL      
    message_text =f'𝑆𝑝𝑎𝑚 𝑇ℎ𝑎̀𝑛ℎ 𝐶𝑜̂𝑛𝑔 ✔️\n𝐵𝑜𝑡: @spamsms20_bot\n𝑇𝑖𝑚𝑒 𝑆𝑝𝑎𝑚: 1000 𝐺𝑖𝑎̂𝑦\n𝐴𝑡𝑡𝑎𝑐𝑘 𝐵𝑦: @{username}\n𝑆𝑜̂́ 𝑇𝑎̂́𝑛 𝐶𝑜̂𝑛𝑔: {phone_number} \n𝐴𝑑𝑚𝑖𝑛: @begaudeptry\n'
    bot.send_video(message.chat.id, video_url, caption=message_text, parse_mode='html')            
@bot.message_handler(commands=['downtik'])
def luuvideo_tiktok(message):
  if len(message.text.split()) == 1:
    sent_message = bot.reply_to(message, '𝑉𝑈𝐼 𝐿𝑂̀𝑁𝐺 𝑁𝐻𝐴̣̂𝑃 𝐿𝐼𝑁𝐾 𝑉𝐼𝐷𝐸𝑂 /𝑡𝑖𝑘𝑡𝑜𝑘 [ 𝐿𝑖𝑛𝑘 𝑉𝑖𝑑𝑒𝑜 ]')
    return
  linktt = message.text.split()[1]
  data = f'url={linktt}'
  head = {
    "Host":"www.tikwm.com",
    "accept":"application/json, text/javascript, */*; q=0.01",
    "content-type":"application/x-www-form-urlencoded; charset=UTF-8",
    "user-agent":"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
  }
  response = requests.post("https://www.tikwm.com/api/",data=data,headers=head).json()
  linkz = response['data']['play']
  rq = response['data']
  tieude = rq['title']
  view = rq['play_count']
  sent_message = bot.reply_to(message, f'𝑋𝑖𝑛 𝑐ℎ𝑜̛̀ 𝑚𝑜̣̂𝑡 𝑡𝑖́.!😴\n+ 𝑇𝑖𝑒̂𝑢 𝑑𝑒̂̀: {tieude}\n+ 𝑆𝑜̂́ 𝑣𝑖𝑒𝑤: {view}')
  try:
   bot.send_video(message.chat.id, video=linkz, caption=f'𝐷𝑎̃ 𝑥𝑜𝑛𝑔 𝑐𝑎̉𝑚 𝑜̛𝑛 𝑏𝑎̣𝑛 𝑑𝑎̃ 𝑑𝑢̀𝑛𝑔 𝑏𝑜𝑡💮\n+ 𝑇𝑖𝑒̂𝑢 𝐷𝑒̂̀: {tieude}\n+ 𝑆𝑜̂́ 𝑣𝑖𝑒𝑤: {view}\n+ 𝐴𝑑𝑚𝑖𝑛: t.me/FesCyper_34', reply_to_message_id=message.message_id, supports_streaming=True)
  except Exception as e:
   bot.reply_to(message, f'𝑉𝑖𝑑𝑒𝑜 𝑞𝑢𝑎́ 𝑛𝑎̣̆𝑛𝑔 𝑡𝑜̂𝑖 𝑘ℎ𝑜̂𝑛𝑔 𝑡ℎ𝑒̂̉ 𝑔𝑢̛̉𝑖 𝑣𝑢𝑖 𝑙𝑜̀𝑛𝑔 𝑡𝑢̛̣ 𝑡𝑎̉𝑖: {linkz}')
  bot.delete_message(chat_id=message.chat.id, message_id=sent_message.message_id)
@bot.message_handler(commands=['off'])
def turn_off(message):
    user_id = message.from_user.id
    if user_id != ADMIN_ID:
        bot.reply_to(message, '𝐵𝑎̣𝑛 𝑘ℎ𝑜̂𝑛𝑔 𝑐𝑜́ 𝑞𝑢𝑦𝑒̂̀𝑛 𝑠𝑢̛̉ 𝑑𝑢̣𝑛𝑔 𝑙𝑒̣̂𝑛ℎ 𝑛𝑎̀𝑦.')
        return

    global is_bot_active
    is_bot_active = False
    bot.reply_to(message, '𝐵𝑜𝑡 𝑑𝑎̃ 𝑡𝑎̆́𝑡.𝑇𝑎̂́𝑡 𝑐𝑎̉ 𝑛𝑔𝑢̛𝑜̛̀𝑖 𝑑𝑢̀𝑛𝑔 𝑘ℎ𝑜̂𝑛𝑔 𝑡ℎ𝑒̂̉ 𝑠𝑢̛̉ 𝑑𝑢̣𝑛𝑔 𝑙𝑒̣̂𝑛ℎ.')

@bot.message_handler(commands=['sex'])
def sex(message):
    help_text = '''
   │LIST VIDEO SEX:) │
 https://disk.yandex.com/d/wj4vtfwYtBhu0Q
 https://disk.yandex.com/d/BkBjpIwrj3yWKw 
 https://disk.yandex.com/d/rh4NlxVjqqG_Uw 
 https://disk.yandex.com/d/9ATZExGaHGrWqA
 https://disk.yandex.com/d/EKuXJU5aumkYtQ
 https://disk.yandex.com/d/Olb9bjW8laWtPQ
 https://disk.yandex.com/d/CC0ba1BOygtNyw
 https://disk.yandex.com/d/DNr2F4T2ZW2l8g
 https://disk.yandex.com/d/1heTaKFDNNUq3A
 https://disk.yandex.com/d/P3D6-KAoJweLbA
 https://disk.yandex.com/d/uwEoXvcfNoz3eA
 https://disk.yandex.com/d/uBvrF2uK0DsRyg
 https://disk.yandex.com/d/WHTTJraEjF1AmA
 https://disk.yandex.com/d/WVwTyFj5mpI09g
 https://disk.yandex.com/d/K6I99NnJl4nwOA
   
   ●Watch Have Fun, Guys, check the link yourself.

                   ---Random Video List---
      
'''
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['on'])
def turn_on(message):
    user_id = message.from_user.id
    if user_id != ADMIN_ID:
        bot.reply_to(message, '𝐵𝑎̣𝑛 𝑘ℎ𝑜̂𝑛𝑔 𝑐𝑜́ 𝑞𝑢𝑦𝑒̂̀𝑛 𝑠𝑢̛̉ 𝑑𝑢̣𝑛𝑔 𝑙𝑒̣̂𝑛ℎ 𝑛𝑎̀𝑦.')
        return

    global is_bot_active
    is_bot_active = True
    bot.reply_to(message, '𝐵𝑜𝑡 𝑑𝑎̃ 𝑑𝑢̛𝑜̛̣𝑐 𝑎𝑑𝑚𝑖𝑛 𝑘ℎ𝑜̛̉𝑖 𝑑𝑜̣̂𝑛𝑔 𝑙𝑎̣𝑖\n𝑇𝑎̂́𝑡 𝑐𝑎̉ 𝑛𝑔𝑢̛𝑜̛̀𝑖 𝑑𝑢̀𝑛𝑔 𝑐𝑜́ 𝑡ℎ𝑒̂̉ 𝑠𝑢̛̉ 𝑑𝑢̣𝑛𝑔 𝑙𝑎̣𝑖 𝑏𝑖̀𝑛ℎ 𝑡ℎ𝑢̛𝑜̛̀𝑛𝑔.')

is_bot_active = True

@bot.message_handler(commands=['check'])
def check_ip(message):
    if len(message.text.split()) != 2:
        bot.reply_to(message, '𝑉𝑢𝑖 𝑙𝑜̀𝑛𝑔 𝑛ℎ𝑎̣̂𝑝 𝑑𝑢́𝑛𝑔 𝑐𝑢́ 𝑝ℎ𝑎́𝑝.\n𝑉𝑖́ 𝑑𝑢̣: /𝑐ℎ𝑒𝑐𝑘 + [ 𝑙𝑖𝑛𝑘 𝑤𝑒𝑏𝑠𝑖𝑡𝑒 ]')
        return

    url = message.text.split()[1]
    
    # Kiểm tra xem URL có http/https chưa, nếu chưa thêm vào
    if not url.startswith(("http://", "https://")):
        url = "http://" + url

    # Loại bỏ tiền tố "www" nếu có
    url = re.sub(r'^(http://|https://)?(www\d?\.)?', '', url)
    
    try:
        ip_list = socket.gethostbyname_ex(url)[2]
        ip_count = len(ip_list)

        reply = f"??𝑃 𝑐𝑢̉𝑎 𝑤𝑒𝑏𝑠𝑖𝑡𝑒: {url}\nLà: {', '.join(ip_list)}\n"
        if ip_count == 1:
            reply += "𝑊𝑒𝑏𝑠𝑖𝑡𝑒 𝑐𝑜́ 1 𝑖𝑝 𝑐𝑜́ 𝑘ℎ𝑎̉ 𝑛𝑎̆𝑛𝑔 𝑘ℎ𝑜̂𝑛𝑔 𝑎𝑛𝑡𝑖𝑑𝑑𝑜𝑠."
        else:
            reply += "𝑊𝑒𝑏𝑠𝑖𝑡𝑒 𝑐𝑜́ 𝑛ℎ𝑖𝑒̂̀𝑢 ℎ𝑜̛𝑛 1 𝑖𝑝 𝑘ℎ𝑎̉ 𝑛𝑎̆𝑛𝑔 𝑎𝑛𝑡𝑖𝑑𝑑𝑜𝑠 𝑟𝑎̂́𝑡 𝑐𝑎𝑜.\n𝐾ℎ𝑜̂𝑛𝑔 𝑡ℎ𝑒̂̉ 𝑡𝑎̂́𝑛 𝑐𝑜̂𝑛𝑔 𝑤𝑒𝑏𝑠𝑖𝑡𝑒 𝑛𝑎̀𝑦."

        bot.reply_to(message, reply)
    except Exception as e:
        bot.reply_to(message, f"𝐶𝑜́ 𝑙𝑜̂̃𝑖 𝑥𝑎̉𝑦 𝑟𝑎: {str(e)}")

@bot.message_handler(commands=['admin'])
def send_admin_link(message):
    bot.reply_to(message, "𝐴𝑑𝑚𝑖𝑛: DuckVinh")
@bot.message_handler(commands=['sms'])
def sms(message):
    pass


# Hàm tính thời gian hoạt động của bot
start_time = time.time()
@bot.message_handler(commands=['time'])
def show_uptime(message):
    current_time = time.time()
    uptime = current_time - start_time
    hours = int(uptime // 3600)
    minutes = int((uptime % 3600) // 60)
    seconds = int(uptime % 60)
    uptime_str = f'{hours} 𝐺𝑖𝑜̛̀, {minutes} 𝑃ℎ𝑢́𝑡, {seconds} 𝐺𝑖𝑎̂𝑦'
    bot.reply_to(message, f'𝐵𝑜𝑡 𝐷𝑎̃ 𝐻𝑜𝑎̣𝑡 𝐷𝑜̣̂𝑛𝑔 𝐷𝑢̛𝑜̛̣𝑐: {uptime_str}')


@bot.message_handler(func=lambda message: message.text.startswith('/'))
def invalid_command(message):
    bot.reply_to(message, '𝐿𝑒̣̂𝑛ℎ 𝑘ℎ𝑜̂𝑛𝑔 ℎ𝑜̛̣𝑝 𝑙𝑒̣̂. 𝑉𝑢𝑖 𝑙𝑜̀𝑛𝑔 𝑠𝑢̛̉ 𝑑𝑢̣𝑛𝑔 𝑙𝑒̣̂𝑛ℎ /𝑙𝑒𝑛ℎ 𝑑𝑒̂̉ 𝑥𝑒𝑚 𝑑𝑎𝑛ℎ 𝑠𝑎́𝑐ℎ 𝑙𝑒̣̂𝑛ℎ')

bot.infinity_polling(timeout=60, long_polling_timeout = 1)
