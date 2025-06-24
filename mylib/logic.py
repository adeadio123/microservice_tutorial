import wikipedia


def wiki(name="War Goddess", length=1):
    "This is a function that returns a summary of a Wikipedia page."

    my_wiki = wikipedia.summary(name, sentences=length)
    if not my_wiki:
        return "No summary found for the given name."

    # Ensure the summary is not too long
    if len(my_wiki) > 500:
        my_wiki = my_wiki[:500] + "..."

    # Replace newlines with spaces for better readability
    my_wiki = my_wiki.replace("\n", " ")
    return my_wiki


def search_wiki(name):
    """Search wikipedia for a given name."""

    results = wikipedia.search(name)
    if results:
        return results[0]
    else:
        return "No results found for the given name."
