"""
@Time: 2025/8/24 19:33
@Author: yanzx
@Description:

4
xyxz

=> xyz

3
azz

zz
"""

import sys


def solve():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()

    initial_counts = [0] * 26
    for char_code_val in map(ord, s):
        initial_counts[char_code_val - ord('a')] += 1

    optimal_final_counts = [0] * 26
    optimal_final_counts[25] = initial_counts[25]
    for i in range(24, -1, -1):
        optimal_final_counts[i] = min(optimal_final_counts[i + 1], initial_counts[i])
    total_target_length = sum(optimal_final_counts)
    if total_target_length == 0:
        sys.stdout.write("\n")
        return
    suffix_char_counts = [[0] * 26 for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(26):
            suffix_char_counts[i][j] = suffix_char_counts[i + 1][j]
        suffix_char_counts[i][ord(s[i]) - ord('a')] += 1
    results_chars = []
    current_s_idx = 0
    needed_counts_copy = list(optimal_final_counts)

    while len(results_chars) < total_target_length:
        best_char_to_pick_code = -1
        best_char_to_pick_idx = -1
        for current_char_code in range(26):
            if needed_counts_copy[current_char_code] == 0:
                continue

            actual_char_pos_in_s = -1
            for k in range(current_s_idx, n):
                if ord(s[k]) - ord('a') == current_char_code:
                    actual_char_pos_in_s = k
                    break
            if actual_char_pos_in_s == -1:
                continue

            can_fullfill_remaining = True
            for c_code_later in range(26):
                remaining_needed_for_this_char = needed_counts_copy[c_code_later]
                if c_code_later == current_char_code:
                    remaining_needed_for_this_char -= 1
                if remaining_needed_for_this_char > 0:
                    if suffix_char_counts[actual_char_pos_in_s + 1][c_code_later] < remaining_needed_for_this_char:
                        can_fullfill_remaining = False
                        break
            if can_fullfill_remaining:
                best_char_to_pick_code = current_char_code
                best_char_to_pick_idx = actual_char_pos_in_s
                break
        if best_char_to_pick_code == -1:
            break
        results_chars.append(chr(ord('a') + best_char_to_pick_code))
        needed_counts_copy[best_char_to_pick_code] -= 1
        current_s_idx = best_char_to_pick_idx + 1
    # print("".join(results_chars))

    sys.stdout.write("".join(results_chars))


solve()
