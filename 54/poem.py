import textwrap


INDENTS = 4
INDENTS_STR = INDENTS * ' '

shakespeare_unformatted = """
                          To be, or not to be, that is the question:
                          Whether 'tis nobler in the mind to suffer

                          The slings and arrows of outrageous fortune,
                          Or to take Arms against a Sea of troubles,
                          """
rosetti_unformatted = """
                      Remember me when I am gone away,
                      Gone far away into the silent land;
                      When you can no more hold me by the hand,

                      Nor I half turn to go yet turning stay.

                      Remember me when no more day by day
                      You tell me of our future that you planned:
                      Only remember me; you understand
                      """

poem = shakespeare_unformatted


def print_hanging_indents(poem):

    first_split = []
    first_split = poem.split('\n\n')

    for item in first_split:
        item = item.lstrip()

        print(textwrap.fill(item, expand_tabs=True, width=50, tabsize=0,
                            initial_indent='', subsequent_indent=INDENTS_STR))


print_hanging_indents(poem)
