import random

import aiohttp

from gif_interactions import gif_links
from verb_mapping import verb_mapping


def get_response(author_user,command,channel,other_user):
    if command in gif_links:
        gif_url=random.choice(gif_links[command])
        message=f"{author_user} {verb_mapping[command]} {other_user}! \n {gif_url}"
        return message,gif_url