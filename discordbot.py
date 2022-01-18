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
    game = discord.Game('坐等餵食')
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
    if message.content == '閉嘴':
        await message.channel.send('幹什麼東西!當本皇不在了嗎')
    if message.content == 'G哥睡了嗎':
        await message.channel.send('朕的僕人沒那麼早睡')
    if message.content == '我擦':
        await message.channel.send('文明點奴隸')
    if message.content == '喵':
        await message.channel.send('喵~')
    if message.content == '喵喵':
        await message.channel.send('吵什麼吵')
    if message.content == '汪':
        await message.channel.send('汪汪~')
    if message.content == '嗷呜':
        await message.channel.send('嗚~~~~~~~')
    if message.content == '嗷嗚':
        await message.channel.send('嗚~~~~~~~')
    if message.content == 'YT連結':
        await message.channel.send('https://www.youtube.com/channel/UCyhDMz3--0Hq_v_8D7tUyXw')
    if message.content == 'G哥YT':
        await message.channel.send('https://www.youtube.com/channel/UCyhDMz3--0Hq_v_8D7tUyXw')
    if message.content == '最近合作的NFT項目':
        await message.channel.send('CYBER NINJA 公售時間:1/21 13:30 mint價格:0.08eth 每人限mint20個')
    if message.content == '抽獎':
        await message.channel.send('最近抽白單項目為:GHart：Honor of gods 台灣時間1月23日晚上9點截止 請先觀看G哥影片，影片下方有抽獎方式')
    if message.content == '抽獎':
        await message.channel.send('https://www.youtube.com/watch?v=y75PjXMUhrk')
    
    
        
        

# Bot起動
client.run(TOKEN)
