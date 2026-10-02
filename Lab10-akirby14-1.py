'''
File Word Analyzer
Author: Adryiana Kirby
Purpose: The purpose of this program is to analyze word counts in a given file.
Date: 10/2/26
'''

from itertools import count
from pathlib import Path
import string

class WordAnalyzer:
    def __init__(self, filepath):
        self.__filepath = Path(filepath)
        self.__frequencies = {}

    def process_file(self):
        try:
            if not self.__filepath.exists():
                raise FileNotFoundError

            punctuation_table = str.maketrans("", "", string.punctuation)

            with self.__filepath.open("r", encoding="utf-8") as file:
                for line in file:

                    cleaned_line = line.translate(punctuation_table).lower()
                    words = cleaned_line.split()

                    for word in words:
                        if word in self.__frequencies:
                            self.__frequencies[word] += 1
                        else:
                            self.__frequencies[word] = 1
            return True

        except FileNotFoundError:
            print(f"Error: The file at '{self.__filepath}' was not found.")
            return False

    def print_report(self):
        sorted_words = sorted(self.__frequencies.keys())

        for word in sorted_words:
            count = self.__frequencies[word]
            print(f"{word.ljust(7)} :: {count}")
def main():
    filepaths = {
        "1": ("Princess Mars (Chapter 1)", Path("Texts/princess_mars.txt")),
        "2": ("Tarzan (Chapter 1)", Path("Texts/Tarzan.txt")),
        "3": ("Treasure Island (Chapter 1)", Path("Texts/treasure_island.txt")),
        "4": ("Monte Cristo (Chapter 1)", Path("Texts/monte_cristo.txt")),
        "5": ("Exit", None)
    }
    while True:
        print("\n--- Word Analyzer ---\nPlease select a file to analyze")

        for key, (title, _) in filepaths.items():
                print(f"{key}: {title}")
        
        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "5":
            print("\nGoodbye!")
            break

        elif choice in filepaths:
            title, path_obj = filepaths[choice]
            print(f"\nProcessing '{path_obj.name}'...\n")

            analyzer = WordAnalyzer(str(path_obj))
            if analyzer.process_file():
                analyzer.print_report()

            input("\nPress Enter to return to the menu...")
        else:
            print("\nInvalid choice. Please select a valid option (1-5).")
            input("\nPress Enter to return to the menu...")


if __name__ == "__main__":
    main()