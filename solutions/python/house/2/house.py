def recite(start_verse, end_verse):
    noun_verb = ["the house that Jack built.",
                 "the malt that lay in",
                 "the rat that ate",
                 "the cat that killed",
                 "the dog that worried",
                 "the cow with the crumpled horn that tossed",
                 "the maiden all forlorn that milked",
                 "the man all tattered and torn that kissed",
                 "the priest all shaven and shorn that married",
                 "the rooster that crowed in the morn that woke",
                 "the farmer sowing his corn that kept",
                 "the horse and the hound and the horn that belonged to"]

    
    tail = []
    for i in range(len(noun_verb)):
        if i == 0:
            tail.append(noun_verb[i])
        else:
            tail.append(f"{noun_verb[i]} {tail[i-1]}")

    paragraph = []
    for i in range(len(noun_verb)):
        paragraph.append(f"This is {tail[i]}")

    start_idx = start_verse - 1
    end_idx = end_verse - 1
    return paragraph[start_idx:end_idx + 1]