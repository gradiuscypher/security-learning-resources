# Quick functions to allow easy modification of the JSON file

import json
from pprint import pprint

PRESENTATION_ITEM_STRING = """
{
    "title": "",
    "description":"",
    "last_updated": "",
    "video_url": "",
    "slide_url": "",
    "presentation": {
        "date": "",
        "location": "",
        "authors": [
        ]
    },
    "tags": [
    ],
    "metadata": [
    ]
}
"""


def get_item_type(item_type):
    """
    Get the particular item from the JSON file (eg: presentation, blog, etc)
    Use to modify a particular item type.
    :param item_type:
    :return:
    """
    json_data = load_json()

    for item in json_data:
        if item_type in item.keys():
            return item

    return None


def add_entry(item_type, interactive=False, new_item=None):
    # TODO: Build interactive steps
    templates = {
        'presentations': PRESENTATION_ITEM_STRING
    }

    json_data = load_json()
    items = get_item_type(item_type)

    new_entry = json.loads(templates[item_type])
    new_entry['tags'].append('tag1')
    new_entry['tags'].append('tag2')
    new_entry['presentation']['authors'].append({"name": "name1", "contact": "twitterURL"})
    items['presentations'].append(new_entry)

    pprint(items)


def remove_entry():
    pass


def load_json():
    with open('../learning_resources.json') as f:
        json_data = json.load(f)
    return json_data


def save_json():
    pass
