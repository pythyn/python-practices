from random import choice

word_list = [
    "photon",
    "quark",
    "isotope",
    "neutrino",
    "tunneling",
    "wavefunction",
    "entropy",
    "collimator",
    "radiograph",
    "attenuation",
    "superposition",
    "dosimeter",
    "algorithm",
    "consciousness",
    "paradox",
    "obsidian",
    "synapse",
    "euphoria",
    "metaphor",
    "serendipity",
    "equanimity",
    "archipelago",
    "savannah",
    "peninsula",
    "himalayas",
    "reykjavik",
    "kathmandu",
    "sahara",
    "fjord",
    "tundra",
    "atoll",
    "jinx",
    "quiz",
    "zeal",
    "glib",
    "lynx",
    "cyst",
    "vex",
    "wry",
    "pyre",
    "koi",
    "pixel",
    "avatar",
    "genshin",
    "cosplay",
    "rhythm",
    "easteregg",
    "emulator",
    "fandom",
    "sidekick",
    "bossfight",
    "catalyst",
    "boolean",
    "syntax",
    "ubuntu",
    "proxy",
    "kernel",
    "cipher",
    "dystopia",
    "nebula",
    "terraform",
    "plasma",
    "monolith",
    "fractal",
    "zenith",
    "eclipse",
    "quasar",
    "spectrum",
    "oxymoron",
    "dichotomy",
    "conundrum",
    "mirage",
    "hologram",
    "nexus",
    "parallax",
    "renaissance",
    "halcyon",
    "halogen",
    "velocity",
    "isomer",
    "spectrometer",
    "incandescent",
    "permafrost",
    "cybernetics",
    "aurora",
    "quantum",
    "lens",
    "circuit",
    "nanobot",
    "gravity",
    "solstice",
    "cadence",
    "matrix",
    "cranium",
    "parallax",
    "threshold",
    "vortex",
    "calibrate",
    "firmware",
    "chronotope",
    "heuristic",
    "anomaly",
    "glyph",
    "tangent",
    "fibonacci",
    "obsidian",
    "trilobite",
    "convection",
    "emulator",
    "syntax",
    "bitrate",
    "beryllium",
    "diode",
    "magnetron",
    "phasewave",
    "redux",
    "debug",
    "cache",
    "compiler",
    "isotope",
    "algorithm",
    "refract",
    "simulate",
    "render",
    "artifact",
    "fusion",
    "eclipse",
    "singularity",
    "catalyst",
    "ergonomics",
    "biometrics",
    "temporal",
    "apex",
    "havoc",
    "quartz",
    "nexus",
    "plasma",
    "zenith",
    "cryogenics",
]

rand = choice(word_list)
random_word = [w.lower() for w in rand]

word = ["_"] * len(random_word)
chance = len(random_word) * 2

print("enter [exit] to exit...")

print(f"you have {chance} chande.")
while chance > 0 and set(random_word) != {"-1"}:
    print("\n", word)
    guess = input("\nguess the word: ").lower().strip()
    if guess.isalpha() and len(guess) == 1:
        if guess in random_word:
            while guess in random_word:
                idx = random_word.index(guess)
                word[idx] = guess
                random_word[idx] = "-1"
        else:
            chance -= 1
            print(f"Wrong!\t{chance} chance left")
    elif guess == "exit":
        exit()
    else:
        print("\n enter valid alphabet")
(
    print(f"\nLoser!!!\tword was {rand}")
    if chance == 0
    else print(f"\ncongrats\tword was {rand}")
)
