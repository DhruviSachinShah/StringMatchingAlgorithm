# import time
# import matplotlib.pyplot as plt
# import random
# import string
# from typing import List

# # Function to implement Rabin-Karp algorithm
# def rabin_karp(s: str, t: str) -> List[int]:
#     p = 31
#     m = 10**9 + 9
#     S = len(s)
#     T = len(t)

#     p_pow = [1] * max(S, T)
#     for i in range(1, len(p_pow)):
#         p_pow[i] = (p_pow[i-1] * p) % m

#     h = [0] * (T + 1)
#     for i in range(T):
#         h[i+1] = (h[i] + (ord(t[i]) - ord('a') + 1) * p_pow[i]) % m
#     h_s = 0
#     for i in range(S):
#         h_s = (h_s + (ord(s[i]) - ord('a') + 1) * p_pow[i]) % m

#     occurrences = []
#     for i in range(T - S + 1):
#         cur_h = (h[i+S] + m - h[i]) % m
#         if cur_h == h_s * p_pow[i] % m:
#             occurrences.append(i)

#     return occurrences

# # Function to implement Brute Force algorithm
# # Python3 program for KMP Algorithm


# def kmp(text, pattern):
#     # Compute the longest prefix which is also suffix array
#     lsp = [0] * len(pattern)
#     j = 0
#     for i in range(1, len(pattern)):
#         while j > 0 and pattern[i] != pattern[j]:
#             j = lsp[j - 1]
#         if pattern[i] == pattern[j]:
#             j += 1
#             lsp[i] = j
#     # Start the matching process
#     matches = []
#     j = 0
#     for i in range(len(text)):
#         while j > 0 and text[i] != pattern[j]:
#             j = lsp[j - 1]
#         if text[i] == pattern[j]:
#             j += 1
#             if j == len(pattern):
#                 matches.append(i - j + 1)
#                 j = lsp[j - 1]
#     return matches

# # Function to generate test cases
# def generate_test_cases():
#     test_cases = []
#     for _ in range(10):
#         text_length = random.randint(50, 1000)
#         pattern_length = random.randint(1, min(text_length, 10))
#         text = ''.join(random.choices(string.ascii_lowercase, k=text_length))
#         pattern_start = random.randint(0, text_length - pattern_length)
#         pattern = text[pattern_start:pattern_start + pattern_length]
#         test_cases.append((text, pattern))
#     return test_cases

# # Function to measure execution time of an algorithm
# def measure_execution_time(algorithm, text, pattern):
#     start_time = time.time()
#     matches = algorithm(text, pattern)  # Ensure results are captured but not used
#     end_time = time.time()
#     return end_time - start_time, len(matches)

# def plot_comparisons(test_cases):
#     algorithms = {'Rabin-Karp': rabin_karp, 'KMP': kmp}
#     data = {algo: [] for algo in algorithms}  # Dictionary to store times for each algo

#     for text, pattern in test_cases:
#         for algo_name, algo in algorithms.items():
#             time_taken, matches = measure_execution_time(algo, text, pattern)
#             data[algo_name].append((len(text), time_taken, matches))

#     # Plotting
#     for algo_name in algorithms:
#         lengths = [x[0] for x in data[algo_name]]
#         times = [x[1] for x in data[algo_name]]
#         plt.plot(lengths, times, marker='o', label=algo_name)

#     plt.xlabel('Text Length')
#     plt.ylabel('Execution Time (s)')
#     plt.title('Comparison of Execution Times')
#     plt.legend()
#     plt.grid(True)
#     plt.show()


# def main():
#     test_cases = generate_test_cases()
#     plot_comparisons(test_cases)


#     # algorithms = {'Rabin-Karp': rabin_karp, 'KMP Algorithm': kmp}
#     # results = {algo: [] for algo in algorithms}
#     # parameters = {'text_length': [], 'pattern_length': [], 'matches': [], 'execution_time': []}

#     # for text, pattern in test_cases:
#     #     for algo_name, algo_func in algorithms.items():
#     #         time_taken = measure_execution_time(algo_func, text, pattern)
#     #         matches = len(algo_func(text, pattern))
#     #         parameters['text_length'].append((len(text), time_taken))
#     #         parameters['pattern_length'].append((len(pattern), time_taken))
#     #         parameters['matches'].append((matches, time_taken))
#     #         parameters['execution_time'].append((time_taken, time_taken))
#     #         results[algo_name].append(time_taken)
#     #     for parameter, data in parameters.items():
#     #         # plt.figure(figsize=(10, 6))
#     #         for algo_name in algorithms:
#     #             values = [x[0] for x in data]
#     #             times = [x[1] for x in data]
#     #         plt.plot(values, times, label=f'{algo_name} ({parameter})')
#     #         plt.xlabel('Parameter Value')
#     #         plt.ylabel('Execution Time (s)')
#     #         plt.title(f'Performance Comparison by {parameter}')
#     #         plt.legend()
#     #         plt.grid(True)
#     #         plt.show()

# #     # Plot results
# #     plt.figure(figsize=(10, 6))
# #     for algo_name, execution_times in results.items():
# #         plt.plot(execution_times, label=algo_name)
# #     plt.xlabel('Test Case')
# #     plt.ylabel('Execution Time (s)')
# #     plt.title('Comparison of String Matching Algorithms')
# #     plt.legend()
# #     plt.grid(True)
# #     plt.show()
  

# # def main():
# #     test_cases = generate_test_cases(10, 500, 10000)  # 100 test cases with text length from 50 to 1000
# #     plot_comparisons(test_cases)

# if __name__ == "__main__":
#     main()



# # # Main function to compare algorithms and plot results
# # def main():
# #     test_cases = generate_test_cases()
# #     algorithms = {'Rabin-Karp': rabin_karp, 'KMP Algorithm': KMPSearch}
# #     results = {algo: [] for algo in algorithms}

# #     for text, pattern in test_cases:
# #         for algo_name, algo_func in algorithms.items():
# #             execution_time = measure_execution_time(algo_func, text, pattern)
# #             results[algo_name].append(execution_time)

# #     # Plot results
# #     plt.figure(figsize=(10, 6))
# #     for algo_name, execution_times in results.items():
# #         plt.plot(execution_times, label=algo_name)
# #     plt.xlabel('Test Case')
# #     plt.ylabel('Execution Time (s)')
# #     plt.title('Comparison of String Matching Algorithms')
# #     plt.legend()
# #     plt.grid(True)
# #     plt.show()

# # if __name__ == "__main__":
# #     main()

import matplotlib.pyplot as plt
import random
import string
import time
from typing import List

def rabin_karp(s: str, t: str) -> List[int]:
    p = 31
    m = 10**9 + 9
    S = len(s)
    T = len(t)

    p_pow = [1] * max(S, T)
    for i in range(1, len(p_pow)):
        p_pow[i] = (p_pow[i-1] * p) % m

    h = [0] * (T + 1)
    for i in range(T):
        h[i+1] = (h[i] + (ord(t[i]) - ord('a') + 1) * p_pow[i]) % m
    h_s = 0
    for i in range(S):
        h_s = (h_s + (ord(s[i]) - ord('a') + 1) * p_pow[i]) % m

    occurrences = []
    for i in range(T - S + 1):
        cur_h = (h[i+S] + m - h[i]) % m
        if cur_h == h_s * p_pow[i] % m:
            occurrences.append(i)

    return occurrences

# Function to implement Brute Force algorithm
# Python3 program for KMP Algorithm


def kmp(text, pattern):
    # Compute the longest prefix which is also suffix array
    lsp = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = lsp[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            lsp[i] = j
    # Start the matching process
    matches = []
    j = 0
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = lsp[j - 1]
        if text[i] == pattern[j]:
            j += 1
            if j == len(pattern):
                matches.append(i - j + 1)
                j = lsp[j - 1]
    return matches

def generate_test_cases(num_cases, min_len, max_len):
    test_cases = []
    for _ in range(num_cases):
        text_length = random.randint(min_len, max_len)
        pattern_length = random.randint(1, min(10, text_length // 2))  # Ensuring sensible pattern lengths
        text = ''.join(random.choices(string.ascii_lowercase, k=text_length))
        pattern_start = random.randint(0, text_length - pattern_length)
        pattern = text[pattern_start:pattern_start + pattern_length]
        test_cases.append((text, pattern))
    return test_cases

def measure_execution_time(algorithm, text, pattern):
    start_time = time.time()
    matches = algorithm(text, pattern)
    end_time = time.time()
    return end_time - start_time, len(matches)

def plot_metrics(data, metric_name):
    for algo_name in data:
        x = [x[0] for x in data[algo_name]]
        y = [y[1] for y in data[algo_name]]
        plt.plot(x, y, marker='o', label=f'{algo_name}')
    
    plt.xlabel('Text Length')
    plt.ylabel(metric_name)
    plt.title(f'Comparison of {metric_name} by Algorithm')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    num_cases = 10
    min_len = 10
    max_len = 10000
    algorithms = {'Rabin-Karp': rabin_karp, 'KMP': kmp}
    metrics = {'Execution Time': {}, 'Number of Matches': {}, 'Pattern Length': {}}

    for algo_name in algorithms:
        metrics['Execution Time'][algo_name] = []
        metrics['Number of Matches'][algo_name] = []
        metrics['Pattern Length'][algo_name] = []

    test_cases = generate_test_cases(num_cases, min_len, max_len)

    for text, pattern in test_cases:
        pattern_length = len(pattern)
        for algo_name, algo in algorithms.items():
            execution_time, match_count = measure_execution_time(algo, text, pattern)
            metrics['Execution Time'][algo_name].append((len(text), execution_time))
            metrics['Number of Matches'][algo_name].append((len(text), match_count))
            metrics['Pattern Length'][algo_name].append((len(text), pattern_length))

    # Plot each metric
    for metric_name in metrics:
        plot_metrics(metrics[metric_name], metric_name)

if __name__ == "__main__":
    main()
