def famous_births(people_dict):
    # Sort by date_of_birth
    sorted_people = sorted(people_dict.values(), key=lambda person: int(person["date_of_birth"]))
    
    # Print each person's info
    for person in sorted_people:
        print(f'{person["name"]} is a great scientist born in {person["date_of_birth"]}.')

# Example usage
if __name__ == "__main__":
    women_scientists = {
        "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
        "cecilia": { "name": "Cecilia Payne", "date_of_birth": "1900" },
        "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
        "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
    }

    famous_births(women_scientists)