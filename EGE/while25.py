def count_paths(n, has_passed_ten):
    if n < 1:
        return 0
    if n == 1:
        return 1 if has_passed_ten else 0
    count = 0
    if n > 1:
        count += count_paths(n - 1, has_passed_ten or n == 10)
    if n % 2 == 0:
        count += count_paths(n // 2, has_passed_ten or n == 10)
    return count
print(count_paths)