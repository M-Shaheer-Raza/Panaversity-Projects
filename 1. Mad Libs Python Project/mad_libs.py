def get_input(prompt):
    return input(prompt)

def create_story():
    print("Welcome to the Mad Libs Game!")

    adjective = get_input("Enter an adjective: ")
    noun = get_input("Enter a noun: ")
    verb = get_input("Enter a verb: ")
    adverb = get_input("Enter an adverb: ")
    plural_noun = get_input("Enter a plural noun: ")

    story = (f"""
    Once upon a time, there was a {adjective} {noun} who loved to {verb} {adverb}
    Every day, the {noun} would join a group of {plural_noun} to celebrate the joys of life.
    """)

    print("\nHere's your story:")
    print(story)

def main():
    create_story()

if __name__ == "__main__":
    main()