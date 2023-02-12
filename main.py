import discord
import os
from TCGHelper import TCGHelper


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)


@client.event
async def on_message(message):
    discord_id = client.get_guild(782011135539937290)
    channels = ["bot-commands"]

    if str(message.channel) in channels:
        if message.content == "!users":
            await message.channel.send(f"""# of Members in GT Chat {discord_id.member_count}""")
        elif message.content == "!tcg-random":
            tcg_helper = TCGHelper("!random")
            await message.channel.send(f"```{tcg_helper.basic_commands()}```")
        elif message.content == "!tcg-all":
            tcg_helper = TCGHelper("!all")
            await message.channel.send(f"```{tcg_helper.basic_commands()}```")
        elif "!tcg-search" in message.content:
            tcg_helper = TCGHelper(message.content)
            await message.channel.send(f"```{tcg_helper.search_commmand()}```")
        elif message.content == "!tcg-decklist":
            tcg_helper = TCGHelper("!decklist")
            await message.channel.send(f"```{tcg_helper.basic_commands()}```")
    else:
        if message.content[0] == "!":
            await message.channel.send(f"I can't complete commands here! Utilize the {channels[0]} channel!")


client.run(f"{os.environ['BOT_TOKEN']}")
