dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']
words = input().split()
error = False
for word in words:
    if word not in dictionary:
        print(word)
        error = True
if not error:
    print("OK")
