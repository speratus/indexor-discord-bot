from discord import Embed


def dict_to_discord_message(info: dict):
    attr_map = {
        "embed": convert_embed,
        "embeds": convert_embeds,
    }

    converted_info = {}

    for k, v in info:
        if hasattr(attr_map, k):
            converted_info[k] = attr_map[k](v)

    return converted_info


def convert_embed(info: dict):
    return Embed(**info)


def convert_embeds(embeds: list):
    embeds_list = []
    for e in embeds:
        embeds_list.append(convert_embed(e))

    return embeds_list
