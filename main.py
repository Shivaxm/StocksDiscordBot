import discord
import yfinance as yf

client = discord.Client(intents=discord.Intents.default())


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print(message.content)
    try:
        content = message.content
        stock = yf.Ticker(content.upper())
        price = stock.info['regularMarketPrice']

        await message.channel.send(f'The current price for {content} is ${price}')

    except:
        await message.channel.send("Please enter valid ticker")

'token removed from code due to public nature of repository'
client.run(token)
