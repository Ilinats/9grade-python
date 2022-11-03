def is_anagram (fst_word, snd_word):
    
    if sorted(fst_word) == sorted(snd_word):
        print("True")
    else:
        print("False")

def count_words(arr):
    
    count = dict()
    
    for word in arr:
        if word not in count:
            count[word] = 1
        else:
            count[word] +=1
        
    print(count)
    
def nan_expand(num):
    while num > 0:
        num = num-1
        print("Not a ", end = "")
        
    print("NaN")

is_anagram("beard", "baredd")

count_words(["apple", "banana", "apple", "pie"])

nan_expand(4)