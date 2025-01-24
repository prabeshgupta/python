while True:
    try:
        a = int(input("Enter number 1 "))
        b = int(input("Enter number 2 "))
        print(a/b)
    except ValueError:
        print("Input must be numbers.")
    except ZeroDivisionError:
        print("Can't divide by 0.")
    except:
        print("An error has occured.")
    # except Exception as e:
    #     print(type(e))
    finally:
        print("See you again")