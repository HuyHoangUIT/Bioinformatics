def read_input(filename):
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
    text = lines[0].strip()
    patterns = lines[1].strip().split()
    d = int(lines[2].strip())
    return text, patterns, d

def write_output(filename, results):
    with open(filename, 'w') as f:
        for pattern, positions in results.items():
            f.write(f"{pattern}: {' '.join(map(str, positions))}\n")

def approximate_pattern_matching(text, pattern, d):
    positions = []
    pattern_length = len(pattern)
    
    for i in range(len(text) - pattern_length + 1):
        # Count mismatches
        mismatches = 0
        for j in range(pattern_length):
            if text[i + j] != pattern[j]:
                mismatches += 1
            if mismatches > d:  # Early exit if mismatches exceed d
                break
        if mismatches <= d:
            positions.append(i)  # Store the starting index of the match
    
    return positions

def multiple_approximate_pattern_matching(text, patterns, d):
    results = {}
    for pattern in patterns:
        positions = approximate_pattern_matching(text, pattern, d)
        results[pattern] = positions
    return results

def main():
    text, patterns, d = read_input('input.txt')
    results = multiple_approximate_pattern_matching(text, patterns, d)
    write_output('output.txt', results)

if __name__ == "__main__":
    main()
