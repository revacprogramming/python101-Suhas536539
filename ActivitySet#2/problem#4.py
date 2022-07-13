from re import I


global I

def get_cs():
    """get string input"""
    s = ("Input a string")
    return s


def cs_to_lot(cs):
    """convert connected string to list of strings"""
    l=[]
    cs=cs.split(";")
    for I in cs:
        I=tuple(I.split("="))
    return l


def lot_to_cs(lot):
    """convert list of strings to connected string"""
    l=list()
    l.append(I)
    return lot    

def main():
    cs=get_cs()

    lot=cs_to_lot(cs)  # convert connect string to list of tuples
    print(lot)

    cs=lot_to_cs(lot)  # convert list of strings to connect string
    print(cs)


if __name__ == '__main__':
    main()


    
