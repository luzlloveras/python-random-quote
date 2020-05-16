import random

last = 13
rnd = random.randint(0, last)

def primary():
#    print("Keep it logically awesome.")

    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()

    print(quotes[rnd])

if __name__== "__primary__":
  main()
