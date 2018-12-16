cities={
    'los angeles':{
        'country': 'united states',
        'pop': '20 million',
        'fact':'sits on a major faultline',
        },
    'london':{
        'country': 'england',
        'pop': '15 million',
        'fact':'the capital of England',
        },
    'rome':{
        'country': 'italy',
        'pop': '8 million',
        'fact':'is called the eternal city because it has been continuously populated for thousands of years',
        },
    }
for city, info in cities.items():
    country = info['country']
    pop = info['pop']
    fact= info['fact']

    print ("The city of " + city.title() + " has a population of " + pop + " and is located in the country of " + country.title() + ". An interesting fact is that is " + fact + ".") 

wantvisit= ['rome', 'paris', 'berlin']
for visit in wantvisit:
    if visit not in cities:
        print ("A city I want to visit that is not listed here is: " + visit.title() + ".")
    