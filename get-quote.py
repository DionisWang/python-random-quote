import random
def primer():
  print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = len(quotes)-1
  rnd = random.randint(0,last)
  print("Quote of the day: "+quotes[rnd])
  cmd = input("Enter any key for another quote 'a' to add quotes or 'q' to exit: ")
  while(cmd != "q"):
      if(cmd == "a"):
          f=open("quotes.txt","w")
          nquote= input("Enter new quote: ")
          quotes.append(nquote)
          total=""
          for s in quotes:
              total += s
          f.write(total)
          f.close()
      else:
        rnd = random.randint(0,last)
        print(quotes[rnd])
      cmd = input("Enter any key for another quote 'a' to add quotes or 'q' to exit: ")
  

if __name__== "__main__":
  primer()
