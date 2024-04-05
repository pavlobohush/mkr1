import unittest
from main import read_population_data, sort_by_area, sort_by_population

class TestPopulationData(unittest.TestCase):
    def setUp(self):
        self.file_path = "test_data.txt"
        self.population_data = [
            ("Україна", 603700, 44000000),
            ("Німеччина", 357022, 83190556),
            ("Франція", 551695, 67156000),
            ("Іспанія", 505990, 46733038),
            ("Італія", 301340, 60599936)
        ]
        with open(self.file_path, 'w', encoding='utf-8') as file:
            for country, area, population in self.population_data:
                file.write(f"{country}, {area}, {population}\n")

    def test_read_population_data(self):
        expected_data = self.population_data
        actual_data = read_population_data(self.file_path)
        self.assertEqual(actual_data, expected_data)

    def test_sort_by_area(self):
        expected_data = sorted(self.population_data, key=lambda x: x[1])
        actual_data = sort_by_area(self.population_data)
        self.assertEqual(actual_data, expected_data)

    def test_sort_by_population(self):
        expected_data = sorted(self.population_data, key=lambda x: x[2])
        actual_data = sort_by_population(self.population_data)
        self.assertEqual(actual_data, expected_data)

    def tearDown(self):
        import os
        os.remove(self.file_path)

if __name__ == '__main__':
    unittest.main()
