"""
Diophantine equation  (optimal solution)
f (x,y,D) = x^2 - Dy^2 = 1

"""

def sol(d):  
    
    root = int(d**0.5)

    a = root
    num = 0
    den = 1

    p_n = [0, 1, root]
    q_n = [0, 0, 1]

    while a != 2*root:
       
        num = den * a - num
        den = (d - num**2) // den
        a = (root + num) // den

        p_n.append(a * p_n[-1] + p_n[-2])
        q_n.append(a * q_n[-1] + q_n[-2])

        if p_n[-1]**2 - d * q_n[-1]**2 == 1:
            return p_n[-1], q_n[-1]
    
    # if the solution is after one period, search the next periods until the solution is found
    while p_n[-1]**2 - d * q_n[-1]**2 != 1:
        print(p_n[-1], q_n[-1])
        num = den * a - num
        den = (d - num**2) // den
        a = (root + num) // den

        p_n.append(a * p_n[-1] + p_n[-2])
        q_n.append(a * q_n[-1] + q_n[-2])
    
    return p_n[-1], q_n[-1]

if __name__ == "__main__":
    max_x = 0
    max_d = 0
    for d in range(1000): 
        if int(d**0.5) != d**0.5:
            x,y = sol(d)
            print(d, (x,y))
            if x > max_x:
                max_x = x
                max_d = d

    print(max_d, max_x)
