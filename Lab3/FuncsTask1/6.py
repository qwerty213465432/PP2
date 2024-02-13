def rev(sentence):
    
    words = sentence.split()

    
    revwords = words[::-1]

    
    revsent= ' '.join(revwords)

    return revsent


sentence = input()
rev(sentence)

