#PAPER DOLL: Given a string, return a string where 
#for every character in the original there are three characters


def paper_doll(text):
    result = ''
    
    for _ in text:
       
        result += _ * 3
    
    return result

print(paper_doll('Hello'))
print(paper_doll('Mississippi'))