# MASTER YODA: Given a sentence, return a sentence with the words reversed

def master_yoda(text):
    
    sentence = text.split()
    
    reversed_sentence = sentence[::-1]
    
    return " ".join(reversed_sentence)


# Check
print(master_yoda('I am home'))
# Check
print(master_yoda('We are ready'))