fileContent = open("TopUni.csv", "r", encoding="utf8")

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
        line = line.split(',')  # everytime there is a comma, the string will be split
        line = [space.strip().lower() for space in line]  # remove the extra spaces
        data.append(line)  # adds each University's information to the list

    fileContent.close()

    # returns data
    return data


def removeUnnecessaryColumns(data: list, columnList: list) -> list:
    """
    :param data: list of data
    :param columnList: list of columns to be removed
    :return: list of data with removed columns
    """
    # sort the list in descending order
    columnList.sort(reverse=True)

    # remove the unnecessary columns
    for line in data:
        for column in columnList:
            del line[column]    # delete the column

    # return the data
    return data


def mergeData(uniData: list, capitalData: list) -> list:
    """
    :param uniData: list of university data
    :param capitalData: list of capital data
    :return: merged data
    """
    mergedData = []

    # merge data where country is same
    for uniLine in uniData:
        for capitalLine in capitalData:
            if uniLine[2] == capitalLine[0]:    # if country is same
                # merge the data
                mergedData.append(uniLine + capitalLine[1:])
                break

    # return the merged data
    return mergedData

countriesList = []
for line in data:
    if line[2].strip().upper() in countriesList:  # if country is not in the list
        countriesList.append(line[2].strip().upper())  # append the country

    countries = ", ".join(countriesList)  # join the list with comma