import matplotlib.pyplot as plt

def main():
    alphabet =  [0 for i in range(26)] # index 0 = A, index 25 = Z
    
    with open('data.txt','r', encoding="utf8") as f:
        while True:
            char = f.read(1)
            if char.isalpha(): char = char.upper() 
            if(not char):
                break
            alphabetIndex = ord(char) - 65
            if alphabetIndex in range(26):
                alphabet[alphabetIndex] += 1
    
    totalLetters = sum(alphabet)
    frequency = [x/totalLetters for x in alphabet]
    for i,x in enumerate(alphabet):
        print(f'Letter: {chr(i+65)}\tTotal: {x}\tFrequency: {frequency[i]}')
    print(f'All Letters\tTotal: {totalLetters}')
    #plt.hist([[chr(i+65),x] for i,x in enumerate(alphabet)])
    #plt.hist(frequency,align='left')
    plt.bar(x=range(26),height=alphabet,tick_label=[chr(i) for i in range(65,91)])
    plt.show()


if __name__ == '__main__':
    main()

