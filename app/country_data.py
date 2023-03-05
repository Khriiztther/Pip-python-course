
def country_info(file, country):
  result = list(filter(lambda item: item['Country/Territory'] == country, file))
  return result

# def population_info(country):
#   population = {
#     '2022': int(country['2022 Population']),
#     '2020': int(country['2020 Population']),
#     '2015': int(country['2015 Population']),
#     '2010': int(country['2010 Population']),
#     '2000': int(country['2000 Population']),
#     '1990': int(country['1990 Population']),
#     '1980': int(country['1980 Population']),
#     '1970': int(country['1970 Population']),
    
#   }
#   labels = population.keys()
#   values = population.values()
#   return labels, values
    
def population_info(country):
  index[country] = index['World Population Percentage']
  return index

    