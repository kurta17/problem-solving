s = str(input())
answers = []

def recurse(t, alphabet):
    if len(alphabet) == 0:
        answers.append(t)
        return
    
    for ch in set(alphabet):
        new_t = t + ch
        new_alphabet = alphabet.replace(ch, '', 1)
        recurse(new_t, new_alphabet)
        
recurse("", s)

print(len(answers))
# k = sorted(answers)
for t in sorted(answers):
    print(t)