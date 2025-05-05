def get_language():
    languages = ["es", "en"]
    while True:
        language = input(f"Choose your language {languages} : ").strip().lower()
        if language in languages:
            return language
        else:
            "not an implemented language"


def get_level():
    levels = ["A2", "B1"]
    while True:
        level = input(f"Choose your language {levels} : ").strip().upper()
        if level in levels:
            return level
        else:
            "not an implemented level"
