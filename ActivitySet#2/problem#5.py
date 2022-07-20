def get_cs():
    """get string input"""
    cs=input("enter a string:")
    return cs

def cs_to_dict(cs):
    """convert connect string to a dictionary"""
    d = dict([cs.split(';') for x in cs[1:-1].split('=')])
    
    return d

def dict_to_cs(d):
    """convert a dictionary to connect string"""
    
    l =[]
    for i in d:
         tpl =i+"="+d[i]
         l.append(tpl)
         print(tpl)

def main():
    cs = get_cs()

    d = cs_to_dict(cs) # convert connect string to a dictionary
    print(d)

    cs = dict_to_cs(d)
if __name__ == '__main__':
    main()
