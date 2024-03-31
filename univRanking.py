def getInformation(country, universityFile = "TopUni.csv", capitalFile = "capitals.csv"):
    country = country.lower()   # convert the country name to lower case

    try:    # try to open the files
        universityInfo = loadCSVData(universityFile)
        capitalInfo = loadCSVData(capitalFile)
    except:  # if any error occurs
        print("File not found")
        quit()

    # this removes any unnecessary columns that are left
    universityInfo = removeColumns(universityInfo, [4, 5, 6, 7])
    capitalInfo = removeColumns(capitalInfo, [2, 3, 4])

    # this combines the university data and the capitals data
    combinedData = combineData(universityInfo, capitalInfo)

    # all the data will be written into outputText
    outputText(combinedData, capitalInfo, country)


def availableCountries(data):
    countries = []  # empty list to store all countries
    for line in data:  # loop that goes through each line in data
        if line[2].strip().upper() not in countries:  # if the country is not in the list
            countries.append(line[2].strip().upper())  # adds the country into the countries list

    countries = ", ".join(countries)  # this joins the list with comma

    return countries


def availableContinents(data):
    continents = [] # empty list to store all continents
    for line in data: # loop that goes through each line in data
        if line[-1].strip().upper() not in continents:  # if the continent is not in the list
            continents.append(line[-1].strip().upper())  # add the continent into the continents list

    continents = ", ".join(continents)  # this joins the list with comma

    return continents


def rank(data, country, rankType):
    ranks = []  # empty list to hold the ranks of

    if rankType == "world":  # if world ranking
        columns = [0, 1]    # get the world rank and university name

    elif rankType == "national":    # if national ranking
        columns = [3, 1]    # get the national rank and university name

    for line in data:
        if line[2] == country:  # if country is same
            ranks.append([int(line[columns[0]]), line[columns[1]]]) # adds rank and university name

    # sort the list in ascending order on the basis of rank
    ranks.sort(key=lambda x: x[0])

    # returns the top university in the world
    return ranks[0]


def averageScore(data, country):
    totalScore = 0
    count = 0

    for line in data:
        if line[2] == country:  # if country is same
            totalScore += float(line[4])  # adds the score to totalscore
            count += 1  # count increases by 1

    return round(totalScore / count, 2)  # returns the average score


def findContinent(data, university):

    for line in data:  # loop goes through each line in data
        if line[1] == university:   # if the university is the same
            return line[-1]  # function returns the continent


def highestContinentScore(data, continent):

    highestScore = 0

    for line in data:  # loop goes through each line in data
        if line[-1] == continent:   # if continent is the same
            if float(line[4]) > highestScore:   # if score is greater than highest score
                highestScore = float(line[4])   # updates the highest score

    return highestScore  # returns the highest score


def relativeScore(data, country, university):

    avgScore = averageScore(data, country)  # gets the average score of the country
    continent = findContinent(data, university)  # gets the continent that the university is in
    highestScore = highestContinentScore(data, continent)  # gets the highest score of the continent

    return round((avgScore / highestScore) * 100, 2)  # returns the relative score of the country


def capitalCity(capitalList, country):

    for line in capitalList:  # loop that goes through capitalList
        if line[0] == country:  # checks if country is the same
            return line[1]  # if it is, return the capital


def universitiesWithCapital(data, capital):

    universities = []  # empty list to hold universities with a capital in its name

    for line in data:  # loop that goes through data
        if capital in line[1]:  # if a capital name is in the university name
            universities.append(line[1])  # adds the university name to list

    return universities  # return the list of universities


def loadCSVData(filename):
    # opens and then reads the information in the file
    fileContent = open(filename, "r", encoding="utf8")

    # empty list that will hold all data from TopUni.csv except for the first line
    data = []

    # skips the first line in fileContent
    next(fileContent)

    # loop goes through each line in fileContent
    for line in fileContent:  # loop goes through each line in fileContent
        line = line.split(',')  # everytime there is a comma, the string will be split
        line = [space.strip().lower() for space in line]  # remove the extra spaces
        data.append(line)  # adds each University's information to the list

    fileContent.close()

    # returns data
    return data


def removeColumns(data, columnList):
    # this sorts the list in descending order
    columnList.sort(reverse=True)

    # remove the unnecessary columns
    for line in data:
        for column in columnList:
            del line[column]    # delete the column

    # return the data
    return data


def combineData(universityInfo, capitalData):
    combinedData = []

    # merge data where country is same
    for uniLine in universityInfo:
        for capitalLine in capitalData:
            if uniLine[2] == capitalLine[0]:    # if country is same
                # merge the data
                combinedData.append(uniLine + capitalLine[1:])
                break

    # return the merged data
    return combinedData


def outputText(combinedData, capitalList, selectedCountry):

    OUTPUT_FILE = "output.txt"
    # open the file in write mode
    f = open(OUTPUT_FILE, "w", encoding="utf8")

    # This writes the total number of universities from the TopUni file into output.txt
    totalUniversities = len(combinedData)  # uses integer length of combinedData
    f.write("Total number of universities => " + str(totalUniversities) + "\n")

    # This writes the available countries from the list
    countries = availableCountries(combinedData)
    f.write("Available countries => " + str(countries.upper()) + "\n")

    # This writes the available continents from the list
    continents = availableContinents(combinedData)
    f.write("Available continents => " + str(continents.upper()) + "\n")

    # This writes the world rank of a specific university
    worldRank = rank(combinedData, selectedCountry, "world")
    f.write("At international rank => " + str(worldRank[0]) + "the university name is => " + str(worldRank[1].upper()) + "\n")

    # This writes the national rank of a specific university
    nationalRank = rank(combinedData, selectedCountry, "national")
    f.write("At national rank => " + str(nationalRank[0]) + "the university name is => " + str(nationalRank[1].upper()) + "\n")

    # This writes the average score
    avgScore = averageScore(combinedData, selectedCountry)
    f.write("The average score => " + str(avgScore) + "\n")

    # This writes the highest continent score
    continent = findContinent(combinedData, nationalRank[1])
    highContinentScore = highestContinentScore(combinedData, continent)

    # This writes the relative score
    rScore = relativeScore(combinedData, selectedCountry, nationalRank[1])
    f.write(f"The relative score to the top university in {continent.upper()} is => ({avgScore} / {highContinentScore}) x 100% = {rScore}%\n")

    # This writes the capital city of the selected country
    capital = capitalCity(capitalList, selectedCountry)
    f.write("The capital is => " + str(capital.upper()) + "\n")

    # This writes the names of the universities with the capital of the selected country in their names
    uniWithCapital = universitiesWithCapital(combinedData, capital)
    f.write(f"The universities that contain the capital name =>")
    for i in range(0, len(uniWithCapital)):
        f.write(" " + "#" + str(i+1) + " " + uniWithCapital[i])

    f.close()  # closes file



