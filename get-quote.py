import random

last = 13
rnd = random.randint(0, last)

def primary():
#    print("Keep it logically awesome.")

    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()

    print(quotes[rnd])

    print(quotes[11])

    print(quotes[5])

if __name__== "__primary__":
  main()
