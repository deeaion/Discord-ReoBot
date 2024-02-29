from typing import Final
import os
from discord import Intents,Client,Message
from dotenv import load_dotenv
import discord

from responses import get_response
from validator import validate_parameters
def command_to_string(command: list) ->str :
    full_command: str = ""
    if (len(command) == 1):
        return  command[0]
    else:
        return ' '.join(command)
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
#setting up the bot

intents: Intents = Intents.default()
intents.message_content = True  # NOQA
intents.members= True #NOQA
client: Client = Client(intents=intents)

async def send_message(message: Message,command:list,other_user:str,channel):
    try:
        response,gif_url= get_response(message.author,command,channel,other_user)
        await message.channel.send(response)
    except Exception as e:
        print(e)
#handling start up
@client.event
async def on_ready():
    print(f'{client.user} is now running!')

@client.event
async def on_message(message:Message):
    if message.author== client.user:
        return
    if message.content.startswith("reo"):
        #it means the bot is called
        params= message.content.split(" ")
        username=message.author
        command: list[str]= params[1:(len(params)-1)]
        other_user= params[-1]
        channel=message.channel
        #validating parameters to check if they are correct
        try:
            await validate_parameters(command,other_user,message)
        except Exception as e:
            #handling the exception
            error_message= discord.Embed(title="Invalid input!", description=e,colour=discord.Color.red())
            sent= await message.channel.send(embed=error_message)
            return
        #else the input is valid so we will do the task
        await send_message(message,command_to_string(command),other_user,channel)


#main entry point
def main():
    client.run(token=TOKEN)
if __name__ == '__main__':
    main()




