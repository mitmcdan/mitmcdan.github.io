class Place(object):
    locationsList = []
    #initial method to construct all attributes and add locations to a list
    def __init__(self, name, location = "None"):
        self.__name = name
        self.__location = location
        self.__visited = False
        print(self.__name + " created.")
        Place.locationsList.append(self)
    ##method will be called when printing object to make sure the attributes print with it
    def __str__(self):
        reply = self.__name
        if self.__location == "None":
            pass
        else:
            reply += ", located in " + str(self.__location)
        if self.__visited == True:
            reply += " (visited)."
        else:
            reply += " (not visited)."
        return reply
    #enabling private attributes
    def get_name(self):
        return self.__name
    def set_name(self, name):
        return self.__name
    def get_location(self):
        return self.__location
    def set_location(self, location):
        if location == "":
            location == "None"
        return self.__location
    #locations needs to look at the locations list and then print each item in the list
    @staticmethod
    def locations():
        if Place.locationsList:
            print("The following locations exist:")
            for i in range(len(Place.locationsList)):
                print(Place.locationsList[i])
        else:
            print("No locations exist at this time. \n")
    #visit will need to check the attributes of what it is called on then switch those attributes
    #visisted value to true, if it is already true then print message
    def visit(self):
        if self.__visited:
            print(self.__name + " has already been visited.")
        else:
            visitedList = []
            print("You visit " + self.__name)
            self.__visited = True
        #should be using a for loop here to reprint this statement with each place nested in another
        #then once printed should set all of those locations visited variable to True
            print("\nThat means... You visit " + str(self.__location))
        #The bonus would have dealt with this or something similar, it would go through all of the locations
        #and what they are nested in and then print True if it was nested in the given location
            
#sub-class for home from Place
class Home(Place):
    def __init__(self, name, location, rooms, occ):
        #get init from Place then add rooms and occupancy
        super().__init__(name, location)
        self.rooms = rooms
        self.occ = occ

    def __str__(self):
        #this super is not working as it has not been called properly and so the new attributes dont show up
        #, most likey due to private class
        #get previous reply and add new line to it
        super().__str__()
        reply = "\n\tThis house has " + str(self.rooms) + " bedrooms, of which " + str(self.occ) + " are occupied."
        return reply
#sub-class for City from Place
class City(Place):
    def __init__(self, name, location, pop, mayor):
        #get init from Place then add population and mayor
        super().__init__(name, location)
        self.pop = pop
        self.mayor = mayor
    def __str__(self):
        #this super is not working as it has not been called properly and so the new attributes dont show up
        super().__str__()
        #get previous reply and add new line to it
        reply = "\n\tThis city has " + str(self.pop) + " residents, and the mayor is " + self.mayor
        return reply
#main Section 1
##iu = Place("IU Campus")
##library = Place("Wells Library", iu)
##
##print()
##print(iu)
##print(library)
#main Section 2
##Place.locations()
##iu = Place("IU Campus")
##library = Place("Wells Library", iu)
##Place.locations()
##
#main Section 3
##Place.locations()
##indiana = Place("Indiana")
##indy = City("Indianapolis", indiana, 853178, "Joseph Hogsett")
##btown = City("Bloomington", indiana, 80405, "John Hamilton")
##iu = Place("IU Campus", btown)
##library = Place("Wells Library" , iu)
##rental = Home("Rental House", btown, 5, 4)
##historic = Home("Elias Abel House", btown, 4, 0)
##
##Place.locations()
#main Section 4
indiana = Place("Indiana")
indy = City("Indianapolis", indiana, 853178, "Joseph Hogsett")
btown = City("Bloomington", indiana, 80405, "John Hamilton")
iu = Place("IU Campus", btown)
library = Place("Wells Library" , iu)
rental = Home("Rental House", btown, 5, 4)
historic = Home("Elias Abel House", btown, 4, 0)
print()
library.visit()
indiana.visit()
