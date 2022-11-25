from problem69 import phi

# it can be shown that the length of a Farey sequence can be expressed as a sum of the totient function
# https://www.nature.com/articles/s41598-021-99545-w#:~:text=The%20length%20of%20each%20Farey,that%20are%20coprime%20with%20n. 

# F_n = 1 + sum(phi(k)) for k in n

def farey_sequence_length(n):
    return sum([phi(k) for k in range(2, n+1)])


if __name__ == "__main__":
    print(farey_sequence_length(1_000_000))