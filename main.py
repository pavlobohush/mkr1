import sys


def read_population_data(file_path):
    """
    Function to read population data from a file.

    Args:
        file_path (str): The path to the file containing population data.

    Returns:
        list: A list of tuples, each containing data about a country (name, area, population).
    """
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            country, area, population = line.strip().split(',')
            data.append((country.strip(), float(area.strip()), int(population.strip())))
    return data


def sort_by_area(data):
    """
    Function to sort data by area.

    Args:
        data (list): A list of tuples with data about a country (name, area, population).

    Returns:
        list: A list of tuples sorted by area.
    """
    return sorted(data, key=lambda x: x[1])


def sort_by_population(data):
    """
    Function to sort data by population.

    Args:
        data (list): A list of tuples with data about a country (name, area, population).

    Returns:
        list: A list of tuples sorted by population.
    """
    return sorted(data, key=lambda x: x[2])


def main():
    """
    Main function to execute the program.

    Reads population data from a file, sorts it by area and population,
    and prints the result to the console.
    """
    try:
        population_data = read_population_data(r"c:\Users\User\mkr\text.txt")
        sorted_by_area = sort_by_area(population_data)
        sorted_by_population = sort_by_population(population_data)

        print("Дані, відсортовані за площею:")
        for country, area, population in sorted_by_area:
            print(f"{country}: Площа - {area} км², Населення - {population}")

        print("\nДані, відсортовані за населенням:")
        for country, area, population in sorted_by_population:
            print(f"{country}: Площа - {area} км², Населення - {population}")
    except FileNotFoundError:
        print("Файл не знайдено.")
    except Exception as e:
        print("Сталася помилка:", e)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding='utf-8')
    main()

