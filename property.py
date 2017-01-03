# NEED TO ADD JAIL
# GO square

class Property(object):
    def __init__(self, property_name, cost, color, rent_details, mortgage_val,
                 house_hotel_cost, color_cost, color_all=False, owner_name=mglobals.BANK):
        self.property_name = property_name
        self.cost = cost
        self.color = color
        self.rent_details = rent_details
        self.mortgage_val = mortgage_val
        self.house_hotel_cost = house_hotel_cost
        self.color_cost = color_cost
        self.color_all = color_all
        self.owner_name = owner_name

        self.house_count = 0
        self.purchased = False
        self.mortgaged = False

    def purchase(self, owner_name):
        self.owner_name = owner_name
        self.purchased = True

    def mortgage(self):
        self.mortgaged = True
        return self.mortgage_val

    def can_mortgage(self):
        if self.house_count != 0:
            return (False, 'Cannot mortgage property with houses!')
        return True

    def can_unmortgage(self, balance):
        if balance >= self.mortgage_val * 1.1:
            return True
        return (False, 'Not enough balalnce!')

    def unmortgage(self):
        self.mortgaged = False
        return int(self.mortgage_val * 1.1)

    def compute_rent(self):
        if self.mortgaged:
            return 0
        if self.house_count == 0 and self.color_all:
            return self.rent_details[self.house_count] * 2
        return self.rent_details[self.house_count]

    def build_house(self):
        if not color_all:
            return (False,'Buy all properties of this color FIRST!!')
        #check owner, cash and even number of houses

class UtilityProperty(object):
    def __init__(self, property_name, cost, mortgage, owner_name=mglobals.BANK):
        self.property_name = property_name
        self.cost = cost
        self.mortgage = mortgage
        self.owner_name = owner_name

    def purchase(self):
        pass

    def compute_rent(self):
        pass


class RailwayProperty(object):
    def __init__(self, property_name, cost, mortgage, owner_name=mglobals.BANK):
        self.property_name = property_name
        self.cost = cost
        self.mortgage = mortgage
        self.owner_name = owner_name

    def purchase(self):
        pass

    def compute_rent(self):
        pass

class PropertyColor(object):
    pass


UTILITIES = [
        UtilityProperty('Electric Company', 150, 75),
        UtilityProperty('Water Works', 150, 75),
]

RAILWAYS = [
        RailwayProperty('Kings Cross Station', 200, 100),
        RailwayProperty('Marylebone Station', 200, 100),
        RailwayProperty('Fenchurch St. Station', 200, 100),
        RailwayProperty('Liverpool Street Station', 200, 100),
]

PROPERTIES = [
        # Brown
        Property('Old Kent Road', 60, 'brown', {0: 2, 1: 10, 2: 30, 3: 90, 4: 160, 5: 250}, 50, 30, 2, False),
        Property('Whitechapel Road', 60, 'brown', {0: 4, 1: 20, 2: 60, 3: 180, 4: 360, 5: 450}, 50, 30, 2, False),

        # Sky Blue
        Property('The Angel Islington', 100, 'sky_blue', {0: 6, 1: 30, 2: 90, 3: 270, 4: 400, 5: 550}, 50, 50, 2, False),
        Property('Euston Road', 100, 'sky_blue', {0: 6, 1: 30, 2: 90, 3: 270, 4: 400, 5: 550}, 50, 50, 2, False),
        Property('Pentonville Road', 120, 'sky_blue', {0: 8, 1: 40, 2: 100, 3: 300, 4: 450, 5: 600}, 60, 50, 2, False),

        # Pink
        Property('Pall Mall', 140, 'pink', {0: 10, 1: 50, 2: 150, 3: 450, 4: 625, 5: 750}, 70, 100, 2, False),
        Property('Whitehall', 140, 'pink', {0: 10, 1: 50, 2: 150, 3: 450, 4: 625, 5: 750}, 70, 100, 2, False),
        Property('Northumberland Avenue', 160, 'pink', {0: 12, 1: 60, 2: 180, 3: 500, 4: 700, 5: 900}, 80, 80, 2, False),

        # Orange
        Property('Bow Street', 180, 'orange', {0: 14, 1: 70, 2: 200, 3: 550, 4: 750, 5: 950}, 90, 100, 2, False),
        Property('Marlborough Street', 180, 'orange', {0: 14, 1: 70, 2: 200, 3: 550, 4: 750, 5: 950}, 90, 100, 2, False),
        Property('Vine Street', 200, 'orange', {0: 16, 1: 80, 2: 220, 3: 600, 4: 800, 5: 1000}, 100, 100, 2, False),

        # Red
        Property('Strand', 220, 'red', {0: 18, 1: 90, 2: 250, 3: 700, 4: 875, 5: 1050}, 110, 150, 2, False),
        Property('Fleet Street', 220, 'red', {0: 18, 1: 90, 2: 250, 3: 700, 4: 875, 5: 1050}, 110, 150, 2, False),
        Property('Trafalgar Square', 240, 'red', {0: 20, 1: 100, 2: 300, 3: 750, 4: 925, 5: 1100}, 120, 150, 2, False),

        # Yellow
        Property('Leicester Square', 260, 'yellow', {0: 22, 1: 110, 2: 330, 3: 800, 4: 975, 5: 1150}, 150, 150, 2, False),
        Property('Coventry Street', 260, 'yellow', {0: 22, 1: 110, 2: 330, 3: 800, 4: 975, 5: 1150}, 150, 150, 2, False),
        Property('Piccadilly', 280, 'yellow', {0: 22, 1: 120, 2: 360, 3: 850, 4: 1025, 5: 1200}, 150, 140, 2, False),

        # Green
        Property('Regent Street', 300, 'green', {0: 26, 1: 130, 2: 390, 3: 900, 4: 1100, 5: 1275}, 200, 150, 2, False),
        Property('Oxford Street', 300, 'green', {0: 26, 1: 130, 2: 390, 3: 900, 4: 1100, 5: 1275}, 200, 150, 2, False),
        Property('Bond Street', 320, 'green', {0: 28, 1: 150, 2: 450, 3: 1000, 4: 1200, 5: 1400}, 200, 160, 2, False),

        # Blue
        Property('Park Lane', 350, 'blue', {0: 35, 1: 175, 2: 500, 3: 1100, 4: 1300, 5: 1500}, 175, 200, 2, False),
        Property('Mayfair', 400, 'blue', {0: 50, 1: 200, 2: 600, 3: 1400, 4: 1700, 5: 2000}, 200, 200, 2, False),
]

