

locations = {'North America': {'USA': ['Raleigh']}}
locations['North America']['USA'].append('Boston')
locations['Asia'] = {'Australia': ['Brisbane'], 'China': ['Beijing']}
locations['Africa'] = {'South Africa': ['Johannesburg']}


print("Show cities in USA:")
print("\n".join(sorted(locations['North America']['USA'])))

print("===")
print("Print cities alphabetically along with their country:")
countries = locations.get('Asia').values()
asian_countries = []
for cities in countries:
    for city in cities:
        asian_countries.append(city)

for sorted_city in sorted(asian_countries):
    for country, city in locations.get('Asia').items():
        if sorted_city in city:
            print("%s - %s" % (sorted_city, country))

