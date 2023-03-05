import country_data

import read_csv
import charts


def run():
    readable = read_csv.read_csv('./app/data.csv')
    readable = list(filter(lambda x:x['Continent'] == 'South America', readable))
    print(readable[0])
    selected = input('Enter the country: ')
    country = country_data.country_info(readable, selected)
    # country = country_data.country_info(readable)
    print('****' * 10 )
    print(country)
    print('****' * 10 )
    if len(country) > 0:
        country = country[0]
        labels, values = country_data.population_info(country)
        charts.generate_bar(labels, values)
    countries = list(map(lambda x: x['Country/Territory'], readable))
    population = list(map(lambda x: x['World Population Percentage'], readable))

    charts.generate_pie(countries, population)

    # for i in readable:
    #   countries.append(readable[-1])
    # print(countries)


if __name__ == '__main__':
    run()
