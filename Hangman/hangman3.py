from random import choice

lists = [
    [
        "Lion",
        "Elephant",
        "Tiger",
        "Giraffe",
        "Zebra",
        "Penguin",
        "Kangaroo",
        "Panda",
        "Leopard",
        "Cheetah",
        "Bear",
        "Wolf",
        "Fox",
        "Deer",
        "Rabbit",
        "Raccoon",
        "Koala",
        "Owl",
        "Eagle",
        "Hawk",
        "Dolphin",
        "Whale",
        "Seal",
        "Otter",
        "Octopus",
        "Shark",
        "Crab",
        "Turtle",
        "Crocodile",
        "Alligator",
        "Frog",
        "Toad",
        "Lizard",
        "Snake",
        "Chameleon",
        "Armadillo",
        "Hedgehog",
        "Moose",
        "Bison",
        "Hyena",
        "Peacock",
        "Flamingo",
        "Parrot",
        "Swan",
        "Duck",
        "Goose",
        "Camel",
        "Horse",
        "Donkey",
        "Ox",
    ],
    [
        "Apple",
        "Apricot",
        "Avocado",
        "Banana",
        "Blackberry",
        "Blueberry",
        "Cherry",
        "Coconut",
        "Cranberry",
        "Cucumber",
        "Date",
        "Dragonfruit",
        "Durian",
        "Elderberry",
        "Feijoa",
        "Fig",
        "Gooseberry",
        "Grape",
        "Grapefruit",
        "Guava",
        "Honeydew",
        "Jackfruit",
        "Jujube",
        "Kiwi",
        "Kumquat",
        "Lemon",
        "Lime",
        "Lychee",
        "Mango",
        "Mangosteen",
        "Melon",
        "Mulberry",
        "Nectarine",
        "Olive",
        "Orange",
        "Papaya",
        "Passionfruit",
        "Peach",
        "Pear",
        "Persimmon",
        "Pineapple",
        "Plantain",
        "Plum",
        "Pomegranate",
        "Pomelo",
        "Quince",
        "Raspberry",
        "Rambutan",
        "Starfruit",
        "Strawberry",
        "Tamarind",
        "Tangerine",
        "Uglifruit",
        "Watermelon",
        "Yuzu",
    ],
    [
        "HarryPotter",
        "SherlockHolmes",
        "Batman",
        "Superman",
        "SpiderMan",
        "WonderWoman",
        "IronMan",
        "DarthVader",
        "LukeSkywalker",
        "PrincessLeia",
        "FrodoBaggins",
        "Gandalf",
        "Aragorn",
        "Legolas",
        "HermioneGranger",
        "RonWeasley",
        "JamesBond",
        "IndianaJones",
        "Wolverine",
        "Deadpool",
        "CaptainAmerica",
        "TheJoker",
        "HannibalLecter",
        "KatnissEverdeen",
        "Elsa",
        "Anna",
        "Simba",
        "Scar",
        "MickeyMouse",
        "DonaldDuck",
        "Goofy",
        "Shrek",
        "Donkey",
        "KungFuPanda",
        "BuzzLightyear",
        "Woody",
        "Moana",
        "Mulan",
        "Aladdin",
        "Genie",
        "Belle",
        "Beast",
        "Cinderella",
        "SnowWhite",
        "SleepingBeauty",
        "Rapunzel",
        "PeterPan",
        "TinkerBell",
        "Pinocchio",
        "WinniethePooh",
        "Tigger",
        "Eeyore",
        "Piglet",
        "ScoobyDoo",
        "Velma",
        "Fred",
        "Daphne",
        "Shaggy",
        "SpongeBobSquarePants",
        "PatrickStar",
        "Squidward",
        "MrKrabs",
        "NarutoUzumaki",
        "SasukeUchiha",
        "Goku",
        "Vegeta",
        "Luffy",
        "Zoro",
        "IchigoKurosaki",
        "LightYagami",
        "Ryuk",
        "AshKetchum",
        "Pikachu",
        "Mario",
        "Luigi",
        "PrincessPeach",
        "Bowser",
        "Link",
        "Zelda",
        "Kratos",
        "LaraCroft",
        "GeraltofRivia",
        "Ellie",
        "MasterChief",
        "SolidSnake",
        "EzioAuditore",
        "Altair",
        "ArthurMorgan",
        "JohnMarston",
        "TrevorPhilips",
        "MichaelDe Santa",
        "FranklinClinton",
    ],
]
HANGMANPICS = [
    r"""
  +---+
  |   |
      |
      |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",
]
play = "again"
while play == "again":
    try:
        group_list = int(input("\n1)Animals\n2)Fruits\n3)Characters\nchoose group: "))
        word_list = lists[group_list - 1]
        rand = choice(word_list)
        random_word = [w.lower() for w in rand]
        word = ["_"] * len(random_word)
        chance = 7
        guessed = []
    except:
        print("\nEnter valid number")
        continue

    print("enter [exit] to exit...")
    while chance > 0 and set(random_word) != {"-1"}:
        print(
            f"{HANGMANPICS[-chance]}\nword:  {' '.join(word)}\nGuessed: {' '.join(guessed)}"
        )
        guess = input("\nguess the word: ").lower().strip()
        if guess in guessed or len(guess) != 1 or not guess.isalpha():
            print("\nWHAT ARE YOU DOING?")
        elif guess == "exit":
            exit()
        else:
            guessed.append(guess)
            if guess in random_word:
                while guess in random_word:
                    idx = random_word.index(guess)
                    word[idx] = guess
                    random_word[idx] = "-1"
            else:
                chance -= 1
                print(f"\nWrong!\t{chance} chance left")
    (
        print(f"\nLoser!!!\tword was {rand}")
        if chance == 0
        else print(f"\ncongrats\tword was {rand}")
    )
    play = input("\ntype [again] to play again...\n")
