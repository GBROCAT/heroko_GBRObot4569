import discord
import googletrans
import os
from pprint import pprint
# 輸入自己Bot的TOKEN碼
TOKEN = os.environ['TOKEN']
SRCLanguage=os.environ['SRC']
DSTLanguage=os.environ['DST']

client = discord.Client()

# 起動時呼叫
@client.event
#async def on_ready():
    #print('成功登入')

#當機器人完成啟動時
async def on_ready():
    print('目前登入身份：',client.user)
    game = discord.Game('public sale-1/21 13:30!')
    #discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
    await client.change_presence(status=discord.Status.idle, activity=game)

# 收到訊息時呼叫
@client.event
async def on_message(message):
    # 送信者為Bot時無視
    if message.author.bot:
        return
    
    if client.user in message.mentions: # @判定
        translator = googletrans.Translator()
        robotName = client.user.name
        first, space, content = message.clean_content.partition('@'+robotName+' ')
        
        if content == '':
            content = first
        if translator.detect(content).lang == DSTLanguage:
            return
        if translator.detect(content).lang == SRCLanguage or SRCLanguage == '':
            remessage = translator.translate(content, dest='zh-tw').text
            await message.reply(remessage) 
           
    if message.content == '安安':
        await message.channel.send('安安各位好')
    if message.content == '早安':
        await message.channel.send('早起的喵喵有罐罐')
    if message.content == '午安':
        await message.channel.send('本喵皇的膳食呢?')
    if message.content == '晚安':
        await message.channel.send('真是辛苦的一天')
    if message.content == '早安':
        await message.channel.send('早起的喵喵有罐罐')
    if message.content == 'G哥睡了嗎':
        await message.channel.send('鄙人的僕人沒那麼早睡')
    if message.content == '我擦':
        await message.channel.send('文明點奴隸')
    
        

# Bot起動
client.run(TOKEN)
