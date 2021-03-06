"""
A restaurant recommendation system.

Here are some example dictionaries.  These correspond to the information in
restaurants_small.txt.

Restaurant name to rating:
# dict of {str: int}
{'Georgie Porgie': 87,
 'Queen St. Cafe': 82,
 'Dumplings R Us': 71,
 'Mexican Grill': 85,
 'Deep Fried Everything': 52}

Price to list of restaurant names:
# dict of {str, list of str}
{'$': ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything'],
 '$$': ['Mexican Grill'],
 '$$$': ['Georgie Porgie'],
 '$$$$': []}

Cuisine to list of restaurant names:
# dict of {str, list of str}
{'Canadian': ['Georgie Porgie'],
 'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'],
 'Malaysian': ['Queen St. Cafe'],
 'Thai': ['Queen St. Cafe'],
 'Chinese': ['Dumplings R Us'],
 'Mexican': ['Mexican Grill']}

With this data, for a price of '$' and cuisines of ['Chinese', 'Thai'], we
would produce this list:

    [[82, 'Queen St. Cafe'], [71, 'Dumplings R Us']]
"""

# The file containing the restaurant data.
FILENAME = 'restaurants.txt'


def recommend(file, price, cuisines_list):
    """(file open for reading, str, list of str) -> list of list of str

    Find restaurants in file that are priced according to price and that are
    tagged with any of the items in cuisines_list.  Return a list of lists of
    the form [rating%, restaurant name], sorted by rating%.
    """

    # Read the file and build the data structures.
    # - a dict of {restaurant name: rating%}
    # - a dict of {price: list of restaurant names}
    # - a dict of {cusine: list of restaurant names}
    name_to_rating, price_to_names, cuisine_to_names = read_restaurants(file)
    
    # Look for price or cuisines first?
    # Price: look up the list of restaurant names for the requested price.
    names_matching_price = price_to_names[price]
    
    # Now we have a list of restaurants in the right price range.
    # Need a new list of restaurants that serve one of the cuisines.
    names_final = filter_by_cuisine(names_matching_price, cuisine_to_names, cuisines_list)
    
    # Now we have a list of restaurants that are in the right price range and serve the requested cuisine.
    # Need to look at ratings and sort this list.
    result = build_rating_list(name_to_rating, names_final)

    # We're done!  Return that sorted list.
    return result

def build_rating_list(name_to_rating, names_final):
    """ (dict of {str: int}, list of str) -> list of list of [int, str]

    Return a list of [rating%, restaurant name], sorted by rating%
    
    >>> name_to_rating = {'Georgie Porgie': 87,
     'Queen St. Cafe': 82,
     'Dumplings R Us': 71,
     'Mexican Grill': 85,
     'Deep Fried Everything': 52}
    >>> names = ['Queen St. Cafe', 'Dumplings R Us']
    [[82, 'Queen St. Cafe'], [71, 'Dumplings R Us']]
    """
    rating_list=[]
    
    for name in names_final:
        rating_list.append([name_to_rating[name],name])
    
    rating_list.sort(key=None, reverse=True)
        
    return rating_list

def filter_by_cuisine(names_matching_price, cuisine_to_names, cuisines_list):
    """ (list of str, dict of {str: list of str}, list of str) -> list of str

    >>> names = ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything']
    >>> cuis = 'Canadian': ['Georgie Porgie'],
     'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'],
     'Malaysian': ['Queen St. Cafe'],
     'Thai': ['Queen St. Cafe'],
     'Chinese': ['Dumplings R Us'],
     'Mexican': ['Mexican Grill']}
    >>> cuisines = ['Chinese', 'Thai']
    >>> filter_by_cuisine(names, cuis, cuisines)
    ['Queen St. Cafe', 'Dumplings R Us']
    """
    filtered_restaurants = []
    
    for cuisine in cuisines_list:
        restaurants = cuisine_to_names[cuisine]
        for restaurant in restaurants:
            if restaurant in names_matching_price:
                filtered_restaurants.append(restaurant)
        
    return filtered_restaurants

def read_restaurants(file):
    """ (file) -> (dict, dict, dict)

    Return a tuple of three dictionaries based on the information in the file:

    - a dict of {restaurant name: rating%}
    - a dict of {price: list of restaurant names}
    - a dict of {cusine: list of restaurant names}
    """

    name_to_rating = {}
    price_to_names = {'$': [], '$$': [], '$$$': [], '$$$$': []}
    cuisine_to_names = {}
    
    file = open(FILENAME, 'r')
    
    lines = file.readlines()
    
    flag = 0
    for line in lines:
        flag = flag + 1
        if line.find('$')!=-1:
            price = line.strip()
        elif line.strip().endswith('%'):
            rating=line.strip()
            rating = rating[:rating.find('%')]
        elif flag==1:
            name=line.strip()
        elif len(line.strip())==0:
            flag=0
        else:        
            line = line.strip()
            cuisines = line.split(',')
            
            for cuisine in cuisines:
                if cuisine in cuisine_to_names:
                    cuisine_to_names[cuisine].append(name)
                else:
                    cuisine_to_names[cuisine] = [name]    
            price_to_names[price].append(name)
            name_to_rating[name]=rating
    
    file.close()
    return name_to_rating, price_to_names, cuisine_to_names

def main():
    file = open(FILENAME, 'r')
    print(recommend(file, '$$', ['Mexican']))
    file.close()

main()    