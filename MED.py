
'''Recursive method to compute the minimum edit distance between two words
A -> 1st word
B -> 2nd word (misspelled word)
i -> current place in word A
j -> current place in word B
returns the minimum edit distance between the two words'''
def MinDistRecursion(A, B, i, j):
    '''If one of the words is longer than the other'''
    if i == 0 and j > 0:
        return j
    if j == 0 and i > 0:
         return i
    '''If we have made it to the _ character'''
    if i == 0:
        return 0
    if j == 0:
        return 0
    '''Return the minimum edit distance, we can either delete, insert or just move on'''
    return min(1 + MinDistRecursion(A, B, i-1, j), 1 + MinDistRecursion(A, B, i, j-1), MinDistRecursion(A, B, i-1, j-1) + (A[i] != B[j]))

'''Dynamic method to compute the minimum edit distance between two words
A -> 1st word 
B -> 2nd word (misspelled word)
returns the minimum edit distance between the two words'''
def MinDistance(A, B):
    m = len(B)
    n = len(A)
    '''Creating our cache
    2D array, the major axis is the place in A and the minor axis is the place in B '''
    C = [[0 for j in range(m)] for i in range(n)]

    '''Fill in our base cases, when we are at the _ of either word'''
    for i in range(0, n):
        C[i][0] = i
    for j in range(0,  m):
        C[0][j] = j

    '''Compute the three options from our previous computations, and then fill in the minimum value'''
    for i in range(1, n):
        for j in range(1, m):
            x = C[i-1][j] + 1
            y = C[i][j-1] + 1
            z = C[i-1][j-1] + (A[i] != B[j])
            C[i][j] = min(x, y, z)

    '''Return our final solution, -1 because of the _ included in the length of the string'''
    return C[n-1][m-1]

'''Method to read the Wikipedia words from our Misspellings.txt file into a dictionary 
filename -> Misspellings
returns a dictionary with misspelled and correctly spelled words from the file'''
def read_in_words(filename):
    '''Dictionary to hold the words and their misspellings
    key : value -> misspelled word : correctly spelled word '''
    T = {}
    path = filename + ".txt"
    with open(path) as fp:
        line = fp.readline()
        while line:
            '''Splitting the input on the arrows '''
            temp = (line.strip()).replace(',', '->').split('->')
            '''The correctly spelled word is the last word in the list after splitting'''
            base = '_' + temp[len(temp)-1]
            '''Adding all the misspelled words with their correctly spelled counterpart'''
            for i in range(0, len(temp)-1):
                T['_' + temp[i] ] = base
            line = fp.readline()
    fp.close()
    return T

'''Method to write our results to the Results.txt file
D -> key : value  edit distance : number of pairs here 
X -> key : value  edit distance : misspelled word spelled word misspelled word word...
path -> Results.txt
returns nothing'''
def write_results(D, X, path):
    with open(path, 'w') as fp:
        for y in D:
            '''writing the distance lengths | number of pairs captured in this distance'''
            s = str(y) + "  |  " + str(D[y]) + "\n"
            fp.write(s)

        '''Finding the maximum edit distance that we observed'''
        max_dist = max(X, key=int)
        fp.write(str(max_dist) + "  ->  ")

        '''Writing all of the words which have the maximum edit distance'''
        for i in X[max_dist]:
            for j in i:
                fp.write(str(j).rstrip('\n'))
    fp.close()

def main():
    '''T contains the words and their mispellings from the Misspellings.txt file
    key: value -> mispelled word: correct word'''
    T = read_in_words('Misspellings')
    '''D is going to keep count of the number of pairs per distance value 
    key: value -> distance:count'''
    D = {}
    '''X is going to keep track of the word pairs and their distance
    key : value -> distance : wrong spelling, right spelling, wrong spelling, right spelling.....'''
    X = {}
    path = 'Results.txt'
    '''for i in T:
        x = MinDistance(i, T[i])
        if x in D:
            D[x] = D[x]+1
            X[x] = X[x] + " " + i + " " + T[i]
        else:
            D[x] = 1
            X[x] = i + " " + T[i] + " "
    write_results(D, X, path)'''
    #print(MinDistRecursion( '_will', '_iwll', 4, 4))
    print(MinDistance('_iwllgt', '_willat'))

if __name__ == '__main__':
    main()
