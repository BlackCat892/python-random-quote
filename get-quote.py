import random


def primary():
   #print("Keep it logically awesome.")

    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()

    last = len(quotes) - 1
    rnd = random.randint(0, last)
    print(quotes[rnd]*3)

   # f = open("quotes.txt", "a+")
   # f.write("The clearest way into the Universe is through a forest wilderness.\n")
    #f.write("The mountains are calling and I must go.\n")
    #f.close()

if __name__ == "__main__":
    primary()
