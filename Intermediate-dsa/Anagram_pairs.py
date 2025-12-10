def check_anagram(lis):
    anagram_groups = {}
    
    for word in lis:
        key = "".join(sorted(word.lower()))
        if key not in anagram_groups:
            anagram_groups[key] = []
        anagram_groups[key].append(word)
    total_pairs = 0
    for key in anagram_groups:
        count = len(anagram_groups[key])
        if count >= 2:
            total_pairs += count * (count - 1) // 2
    return total_pairs

word_list = ['ram', 'mar', 'amr', 'amar', 'ink', 'kin']
print('Total anagram pairs found:', check_anagram(word_list))