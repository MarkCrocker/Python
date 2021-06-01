try:
    raise ValueError("A value error.")
except NameError:
    print("A name error occured.")
except IndexError:
    print("An index error occured.")
except:
    print("Some other error.")
