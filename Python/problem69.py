from tqdm import tqdm
from sympy.ntheory import factorint

def phi(n):
    factors = n
    for a in factorint(n):
        factors -= factors // a
    return factors


def find_largest(N):

    max_phi_div_n = 0
    max_n = 0

    for n in tqdm(range(2, N+1)):
        phi_n = phi(n)
        phi_div_n = n / phi_n

        if phi_div_n > max_phi_div_n:
            max_phi_div_n = phi_div_n
            max_n = n
    return max_n, max_phi_div_n

if __name__ == "__main__": 
    print(find_largest(1_000_000))
