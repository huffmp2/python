def country(city, country):
    """Properly format the city and country names."""
    citylocate= city + ', ' + country
    return citylocate.title()
city = country('paris', 'france')
print(city)
city = country('berlin', 'germany')
print(city)
city = country('moscow', 'russia')
print(city)