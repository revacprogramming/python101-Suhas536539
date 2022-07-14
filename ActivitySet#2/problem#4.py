def get_cs():
    """get string input"""
    s = ("Input a string")
    return s


def cs_to_lot(cs):
    """convert connected string to list of strings"""
    l=[]
    cs=cs.split(";")
    for i in cs:
        i=tuple(i.split("="))
    return l


def lot_to_cs(lot):
    """convert list of strings to connected string"""
    a=[]
    a.append(cs_to_lot)
    return lot    

def main():
    cs=get_cs()

    lot=cs_to_lot(cs)  # convert connect string to list of tuples
    print(lot)

    cs=lot_to_cs(lot)  # convert list of strings to connect string
    print(cs)


if __name__ == '__main__':
    main()


    
