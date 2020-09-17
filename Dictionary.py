locations = {'North America': {'USA': ['Mountain View']}}
locations["Asia"] = {"India": ['Bangalore']}
locations['North America']['USA'].append('Atlanta')
locations["Africa"] = {"Egypt": ['Cairo']}
locations["Asia"]["China"] = ['Shanghai']

print(1)
for l in sorted(locations["North America"]["USA"]):
    print l
    
print(2)  
asian_cities = []
for pais in locations["Asia"].keys():
    for city in locations["Asia"][pais]:
        asian_cities.append(city+' - '+pais)

for cities_ordered in sorted(asian_cities):
    print cities_ordered
