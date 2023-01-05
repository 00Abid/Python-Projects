import random
when = [ ' A few years ago' , 'Yesterday' , 'Last Night' , 'A long Time Ago' , 'On 23th Jan']
who = ['a rabbit' , 'an elephant' , 'a mouse' , 'a turtle' , 'a cat']
name = ['Ali' , 'Marie' , 'Mustang' , 'Allen' , 'Alina']
residence = ['Barcelona' , 'India' , 'Germany' , 'Vetican City' , 'England']
went = ['cinema' , 'university' , 'seminar' , 'school' , 'laundry']
happend = ['made a lot of friends' , 'eats a suger ' , 'found a secret key' , 'solved a mistery' , 'wrote a book']


print(random.choice( when ) + ' ,  ' + random.choice( who )  + ' that lived in ' + random.choice( residence ) + ' went to the ' + random.choice( went ) + ' and ' +  random.choice( happend ))