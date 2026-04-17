# Exception handling

# Exceptions raise when something goes wrong

import logging

# raise <exception>, lets you force raise the exception(good for tests)

#Explicit, best practice to be explicit
#values = [10, 2, 6, 4, 3, 0, 8]

#for value in values:
#    try:
        #print(10 / value)
#        print(int("Hello"))
        # when dividing by zero it displays this error message
#    except ValueError as e:
#        print(str(e))
#    except ZeroDivisionError as e:
        #print(str(e))
#        pass
    # FOR THIS EXCEPTION ITS BEST TO IMPORT LOGGING
#    except Exception as e:
#        logging.exception(e)

#Multiple Exceptions
values = [10, 2, 6, 4, 3, 0, 8]

for value in values:
    try:
        print(10 / int(value))
    except (ValueError, ZeroDivisionError) as e:
        pass
    except AttributeError as e:
        print("Hello World")
        continue
    except Exception as e:
        logging.exception(e)

    # finally gets ran no matter what in the end
    finally:
        print("ABC")


#Basic, throws a custom error message
#try:
#    print(10 / 0)
#except:
#    print("Error occured! Division failed!")

#print("Hello")


#Pass, will pass over values that throw error
#values = [1, 3, 5, 0, 2]

#for value in values:
#    try:
#        print(10 / value)
#    except:
#        pass


