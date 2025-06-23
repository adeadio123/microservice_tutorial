import wikipedia


def wiki(name="War Goddess", length=1):
    "This is a function that returns a summary of a Wikipedia page."

    my_wiki = wikipedia.summary(name, sentences=length)
    return my_wiki
