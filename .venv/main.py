import random
# to start a random generaor impor the statement seen above


# this generates a random number between 1 and 6
x = random.randint(1,6)

# his method generates a random number between 0 and 1
y = random.random()


# here we have a list of three strings where a random choice will be displayed
mylist = ["rock","paper","scissors"]
z = random.choice(mylist)


# lastly a "Deck" of cards printed or as seen below "shuffled out at random
cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
random.shuffle(cards)


print(cards)