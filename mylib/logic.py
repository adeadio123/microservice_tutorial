import wikipedia


def wiki(name="War Goddess", length=10):
    "This is a function that returns a summary of a Wikipedia page."

    my_wiki = wikipedia.page(name, length)
    return my_wiki
