def rev(sentence):
    
    words = sentence.split()

    
    revwords = words[::-1]

    
    revsent= ' '.join(reversed_words)

    return revsent


sentence = input()
rev(sentence)

