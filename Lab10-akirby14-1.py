'''
File Word Analyzer
Author: Adryiana Kirby
Purpose: The purpose of this program is to analyze word counts in a given file.
Date: 10/2/26
'''

from pathlib import Path

class WordAnalyzer:
    def __init__(self, filepath):
        self.filepath = filepath

def main():
    filepaths = {
        "1": ("Princess Mars (Chapter 1)", Path("Texts/princess_mars.txt")),
        "2": ("Tarzan (Chapter 1)", Path("Texts/Tarzan.txt")),
        "3": ("Treasure Island (Chapter 1)", Path("Texts/treasure_island.txt")),
        "4": ("Monte Cristo (Chapter 1)", Path("monte_cristo.txt")),
        "5": ("Exit", None)
    }
    print("\n--- Word Analyzer ---\nPlease select a file to analyze")
    choice = ""

    while choice != "5":
        for key, (title, _) in filepaths.items():
            print(f"{key}: {title}")
        print("5: Exit")
        choice = input("\nEnter your choice (1-5): ")

        if choice not in filepaths:
            print("\nInvalid choice. Please select from 1-5.")
            input("\nPress Enter to return to the menu...")
            main()

        else:
            print("its' there!")
    

if __name__ == "__main__":
    main()