def calculate_love_score(name1, name2):
    combinednames = name1.upper() + name2.upper()
    true_count = 0
    love_count = 0
    true_count = sum(combinednames.count(letter) for letter in 'TRUE')
    love_count = sum(combinednames.count(letter) for letter in 'LOVE')
    print(str(true_count) + str(love_count))
    '''
    #the the above letter checks for occurrence at one go for each letter
    #but  below method is beginner version that reads for each letter one by one
    for letter in name3:

        if letter in 'TRUE':
            #print(f'letter is {letter}')
            true_count+=1

    for letter in name3:

        if letter in 'LOVE':
            #print(f'letter is {letter}')
            love_count+=1

    comb=str(true_count)+str(love_count)
    print(comb)
    '''


calculate_love_score('Kanye West', 'Kim Kardashian')


