def find_pattern_positions(pattern, text):
    positions = []

    for i in range(len(text)):
        if is_match(pattern, text[i:]):
            positions.append(i)

    return positions

def is_match(pattern, text):
    if not pattern or not text:
        return True

    if pattern[0] == text[0] or pattern[0] == '.':
        if len(pattern) > 1 and pattern[1] == '*':
            return is_match(pattern[2:], text) or is_match(pattern, text[1:])
        else:
            return is_match(pattern[1:], text[1:])
    
    if pattern[0] == '^':
        return is_match(pattern[1:], text)
    
    if pattern[0] == '$' and not pattern[1:]:
        return not text

    if pattern[0] == '(':
        idx = pattern.find(')')
        if idx != -1:
            return is_match(pattern[idx+1:], text) or is_match(pattern[1:idx], text)
        else:
            return False

    if pattern[0] == '|':
        idx = pattern.find('|', 1)
        if idx != -1:
            return is_match(pattern[1:idx], text) or is_match(pattern[idx+1:], text)
        else:
            return False
    
    if pattern[0] == '[':
        idx = pattern.find(']')
        if idx != -1:
            return (pattern[1] == text[0] or pattern[1] == '.' or text[0] in pattern[1:idx]) and is_match(pattern[idx+1:], text[1:])
        else:
            return False

    return False

def main():
    # Read pattern from pattern.txt
    with open('pattern.txt', 'r') as pattern_file:
        pattern = pattern_file.read().strip()

    # Read text from text.txt
    with open('text.txt', 'r') as text_file:
        text = text_file.read().strip()

    # Find pattern positions
    positions = find_pattern_positions(pattern, text)
    
    # Write positions to output.txt
    with open('output.txt', 'w') as output_file:
        output_file.write("Pattern found at positions: " + ', '.join(map(str, positions)))

if __name__ == "__main__":
    main()
