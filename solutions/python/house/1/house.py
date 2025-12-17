def recite(start_verse, end_verse):
    subjects = [
        "the house that Jack built.",
        "the malt",
        "the rat",
        "the cat",
        "the dog",
        "the cow with the crumpled horn",
        "the maiden all forlorn",
        "the man all tattered and torn",
        "the priest all shaven and shorn",
        "the rooster that crowed in the morn",
        "the farmer sowing his corn",
        "the horse and the hound and the horn",
    ]

    actions = [
        "",
        "that lay in ",
        "that ate ",
        "that killed ",
        "that worried ",
        "that tossed ",
        "that milked ",
        "that kissed ",
        "that married ",
        "that woke ",
        "that kept ",
        "that belonged to ",
    ]

    tails = [""]

    for i in range(1, len(subjects)):
        tails.append(actions[i] + subjects[i - 1] + " " + tails[i - 1])

    verses = []
    for i in range(start_verse - 1, end_verse):
        verse = "This is " + subjects[i]
        if i > 0:
            verse += " " + tails[i].rstrip()
        verses.append(verse)

    return verses