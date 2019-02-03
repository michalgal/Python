def check_missing(input_collection, n):
    missing_collection = []
    number_collection = []
    i = 1
    while i <= n:
        if i in input_collection:
            number_collection.append(i)
        else:
            missing_collection.append(i)
        i += 1
    print("Input list was: ", number_collection)
    if not missing_collection:
        print("There are no missing numbers!")
    else:
        print("Missing numbers: ", missing_collection)
check_missing([1,3,4,8,9],10)
