from problem69 import phi
from tqdm import tqdm


def is_permutation(a, b):
    return sorted(str(a)) == sorted(str(b))

if __name__ == "__main__":     
    # 87109 given by example 
    min_n_div_phi = 87109/phi(87109)
    min_n = 87109

    for n in tqdm(range(2, 10**7)): 
        phi_n = phi(n)
        
        if is_permutation(n, phi_n): 
            n_div_phi = n / phi_n
            if n_div_phi < min_n_div_phi:
                min_n_div_phi = n_div_phi
                min_n = n


    print(min_n, min_n_div_phi)
