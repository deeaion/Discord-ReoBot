from discord import Message

from gif_interactions import gif_links


def is_user_in_server(guild, mentioned_user_id):
    for member in guild.members:
        if member.id ==mentioned_user_id:
            return True
    return False


async def validate_parameters(command:list,other_user,message:Message)->Exception :
    if len(command)==0:
        raise AttributeError("You have to enter the interaction and user you want to connect with! :face_with_hand_over_mouth:  ")
        return
    full_command:str=""
    if(len(command)==1):
        full_command=command[0]
    else:
        full_command=' '.join(command)
    if full_command not in gif_links:
        raise AttributeError("There is no such interaction :(. I am sorry")
        return
    if len(message.mentions) ==0:
        raise AttributeError("Kri kri no user !")
        return
    mentioned_user_id=message.mentions[0].id
    if message.author.id==mentioned_user_id:
        raise Exception("That is lowkey sad :(! Do you need a hug? Here you go! https://tenor.com/view/hug-day-gif-13503238880928885669")
    is_in_server=is_user_in_server(message.guild,mentioned_user_id)
    if not is_in_server:
        raise Exception("I do not know them! :(")

