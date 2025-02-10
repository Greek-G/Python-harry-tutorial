letter = ''' dear <|Name|,
             you are selected 
             <|date|>'''

print(letter.replace("<|Name|", "Lalit").replace("<|date|>","23rd arpril"))