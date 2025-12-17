def find_anagrams(word, candidates):
    result = []

    word_lower = word.lower()
    word_dict = {}

    for letter in word_lower:
        if letter in word_dict:
            word_dict[letter] += 1
        else:
            word_dict[letter] = 1

    for candidate in candidates:
        candidate_lower = candidate.lower()

        if candidate_lower == word_lower:
            continue

        if len(candidate_lower) != len(word_lower):
            continue

        candidate_lower_dict = {}
        for letter in candidate_lower:
            if letter in candidate_lower_dict:
                candidate_lower_dict[letter] += 1
            else:
                candidate_lower_dict[letter] = 1

        if word_dict == candidate_lower_dict:
            result.append(candidate)

    return result