def get_cs():
   #"""get string input"""
   phrase = str(input("enter a string"))
   return phrase

def cs_to_lot(cs):
   # """convert connected string to list of strings"""
   
   cs_to_lot = list(cs)
   cs_to_lot = cs.split("=")
   cs_to_lot = cs.s("=")
   cs_to_lot = list(cs)
   cs_to_lot = cs.split("=")
   cs_to_lot = cs.s("=")

  #done
  #done
  #done
   
   
   
   print(cs_to_lot) 

def main():
   cs = get_cs()
   lot = cs_to_lot(cs)
   print(lot)

if __name__ == '__main__':
    main()
