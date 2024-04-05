import sys

def read_population_data(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            country, area, population = line.strip().split(',')
            data.append((country.strip(), float(area.strip()), int(population.strip())))
    return data

def sort_by_area(data):
    return sorted(data, key=lambda x: x[1])

def sort_by_population(data):
    return sorted(data, key=lambda x: x[2])

def main():
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

