import itertools

class n_gon:
    def __init__(self, n):
        num_lines = n

        self.lines = []
    
        for line in range(num_lines):
            self.lines.append([])
            for _ in range(3):
                self.lines[line].append(0)
    
    def set_with(self, outer, inner):
        # put inner nodes in lines
        for index, line in enumerate(self.lines):
            line[0] = outer[index] 
        
        for index, line in enumerate(self.lines):
            line[1] = inner[index]
            line[2] = inner[(index+1)%len(inner)]


    
    def check_valid(self, p=False):

        # check order is correct
        #  1. middle node first line equal to last node last line
        if self.lines[0][1] != self.lines[-1][-1]:
            if p:
                print("inner order wrong [1]")
            return False
        # current line last node equal to next line muiddle node
        for i in range(len(self.lines) - 1):
            if self.lines[i][-1] != self.lines[i+1][1]:
                if p: 
                    print("inner order wrong [2]")
                return False
        
        # check all outer nodes are unique
        outer_nodes = []
        for line in self.lines:
            outer_nodes.append(line[0])
        
        if len(outer_nodes) != len(set(outer_nodes)):
            if p:
                print("found duplicate outer nodes")
            return False
        
        # check all lines add up to same sum
        sums = []
        for line in self.lines:
            sums.append(sum(line))
        
        if len(set(sums)) != 1:
            if p:
                print("sums does not add up to same sum in lines", sums)
            return False
        
        return sums[0] # return sum if valid 
    
    def __repr__(self):
        s = ""
        for line in self.lines:
            s += str(line) + "\n"

        return s

def gen_line(n):
    # genereate all possible outer inner inner combinations
    # for a given n

    N = 2 * n

    lsts = list(range(1, N+1))

    for lst in itertools.permutations(lsts):
        yield list(lst[:n]), list(lst[n:])

def rotate_until_smallest_first(lst): 
    firsts = [lst[i][0] for i in range(len(lst))]
    while lst[0][0] != min(firsts):
        lst = lst[1:] + lst[:1]

    return lst

def nested_list_to_str(lst):
    s = ""
    for line in lst:
        for node in line:
            s += str(node)
    return s

if __name__ == "__main__":

    n = 5
    n_digit = 16

    lst = []
    seen = set()

    for outer, inner in gen_line(n):
        g = n_gon(n)
        g.set_with(outer, inner)
        valid = g.check_valid()
        if valid:

            s = g.lines
            s = rotate_until_smallest_first(s)

            str_s = nested_list_to_str(s)
            if str_s not in seen:
                print(str_s)
                seen.add(str_s)
                lst.append((valid, s))
                
    
    lst.sort(key=lambda x: x[0])
    for i in lst:
        print(i)
    
    if len(seen) != 0:
        s = max(map(int,filter(lambda x: len(x) == n_digit, list(seen))))
        print(f"maximum {n_digit} digit string for {n}-gon is {s}")
    else:
        print("no valid solutions")
