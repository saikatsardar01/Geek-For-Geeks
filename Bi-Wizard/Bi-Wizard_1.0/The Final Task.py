def count_set_bits(arr, n):
	count = 0
    for a in arr:
        count += bin(a).count("1")
    return count
