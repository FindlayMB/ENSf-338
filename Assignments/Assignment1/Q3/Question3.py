import matplotlib.pyplot as plt
def main():
    alphabet =  [0 for i in range(26)] # index 0 = A, index 25 = Z
    with open('data.txt','r', encoding="utf8") as f:
        content = f.read().upper()

    for char in content:
        alphabetIndex = ord(char) - 65
        if alphabetIndex in range(26):
            alphabet[alphabetIndex] += 1
    totalLetters = sum(alphabet)
    frequency = [x/totalLetters for x in alphabet]
    for i,x in enumerate(alphabet):
        print(f'Letter: {chr(i+65)}\tTotal: {x}\tFrequency: {frequency[i]}')
    print(f'All Letters\tTotal: {totalLetters}')
    plt.bar(x=range(26),height=frequency,tick_label=[chr(i) for i in range(65,91)])
    plt.xlabel('Letters')
    plt.ylabel('Frequency')
    plt.title('Letter frequency of The Brothers Karamazov by Fyodor Dostoyevsky')
    plt.show()

if __name__ == '__main__':
    main()
