def loadCSVDate(filename):
    """
    :param filename: name of the file to be loaded
    :return: list of data
    """
    # opens and then reads the information in the file
    fileContent = open(filename, "r", encoding="utf8")

    # empty list that will hold all data from TopUni.csv except for the first line
    data = []

    # skips the first line in fileContent
    next(fileContent)

    # loop goes through each line in fileContent
    for line in fileContent:
        line = line.split(",")
        line = [item.strip() for item in line]
        #line = line.split(',') # split the line on the basis of comma
         # remove the extra spaces
        data.append(line) # append the data to the list

    fileContent.close()  # close the file

    # return the data
    return data

print(loadCSVDate("TopUni.csv"))



