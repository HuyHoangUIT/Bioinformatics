def read_input(filename):
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
    bwt_text = lines[0].strip()
    patterns = lines[1].strip().split()
    return bwt_text, patterns

def write_output(filename, results):
    with open(filename, 'w') as f:
        f.write(" ".join(map(str, results)) + "\n")

def preprocess_bwt(bwt_text):
    sorted_bwt = sorted(bwt_text)
    first_occurrence = {}
    for i, char in enumerate(sorted_bwt):
        if char not in first_occurrence:
            first_occurrence[char] = i
    count = {}
    for char in set(bwt_text):
        count[char] = [0] * (len(bwt_text) + 1)
    for i in range(len(bwt_text)):
        current_char = bwt_text[i]
        for char in count:
            count[char][i + 1] = count[char][i]
        count[current_char][i + 1] += 1
    return first_occurrence, count

def better_bw_matching(first_occurrence, last_column, pattern, count):
    top = 0
    bottom = len(last_column) - 1
    while top <= bottom:
        if pattern:
            symbol = pattern[-1]
            pattern = pattern[:-1]
            if symbol in first_occurrence:
                top = first_occurrence[symbol] + count[symbol][top]
                bottom = first_occurrence[symbol] + count[symbol][bottom + 1] - 1
            else:
                return 0
        else:
            return bottom - top + 1
    return 0

def count_pattern_occurrences(bwt_text, patterns):
    first_occurrence, count = preprocess_bwt(bwt_text)
    results = [better_bw_matching(first_occurrence, bwt_text, pattern, count) for pattern in patterns]
    return results

def main():
    bwt_text, patterns = read_input('input.txt')
    results = count_pattern_occurrences(bwt_text, patterns)
    write_output('output.txt', results)

if __name__ == "__main__":
    main()
