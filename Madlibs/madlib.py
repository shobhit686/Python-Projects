from wonderwords import RandomWord

r = RandomWord()
random_adj1= r.word(include_parts_of_speech=["adjectives"])
random_adj2 = r.word(include_parts_of_speech=["adjectives"])
random_noun = r.word(include_parts_of_speech=["nouns"]).capitalize()
random_verb = r.word(include_parts_of_speech=["verbs"])

print(f"{random_noun} is so {random_adj1}. It makes me so {random_adj2} because I love to {random_verb}")
# Have Fun :)