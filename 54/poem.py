import textwrap

INDENTS = 4

poem =  """
        He took a sip of the drink. He wasn't sure whether he liked it or not, but at this moment it didn't matter. She had made it especially for him so he would have forced it down even if he had absolutely hated it. That's simply the way things worked. She made him a new-fangled drink each day and he took a sip of it and smiled, saying it was excellent.
        """

def print_hanging_indents(poem):
    print(poem)
    print(textwrap.shorten(poem, width=30))
    pass

print_hanging_indents(poem)