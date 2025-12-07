import sys

# ANSI 256-Color Codes for Linux
# \033[38;5;{ID}m is the syntax for foreground colors
ORANGE = "\033[38;5;208m"  # Bright Orange for Fire
BLOOD = "\033[38;5;88m"  # Deep Dark Red for Blood
PURPLE = "\033[38;5;57m"  # Deep Violet/Purple for Shadow
RESET = "\033[0m"
BOLD = "\033[1m"
CLEAR_SCREEN = "\033[H\033[J"


def get_styled_name(char):
    char = char.lower()
    if char == "f":
        return f"{ORANGE}{BOLD}FIRE (Orange){RESET}"
    if char == "b":
        return f"{BLOOD}{BOLD}BLOOD (Dark Red){RESET}"
    if char == "s":
        return f"{PURPLE}{BOLD}SHADOW (Purple){RESET}"
    return char


def main():
    print(CLEAR_SCREEN)
    print(f"{BOLD}--- NECROPOLIS BOSS TRACKER ---{RESET}")
    print(
        "Since the pattern is random per run, enter the order you see. Add spaces between each letter."
    )
    print(
        f"Example input: {ORANGE}f{RESET} {BLOOD}b{RESET} {ORANGE}f{RESET} {PURPLE}s{RESET}"
    )
    print("Legend: f = Fire, b = Blood, s = Shadow")

    # 1. Setup the loop
    try:
        user_input = input(f"\n{BOLD}Enter Pattern > {RESET}").strip()
        if not user_input:
            print("No pattern entered. Exiting.")
            sys.exit()
        else:
            pattern = user_input.split()
    except KeyboardInterrupt:
        sys.exit()

    # 2. The Loop
    index = 0

    print(CLEAR_SCREEN)
    print(f"{BOLD}TRACKING STARTED.{RESET}")
    print("Press [ENTER] every time you play a card.")
    print("Press [Ctrl+C] to quit.\n")

    try:
        while True:
            target = pattern[index]
            display_name = get_styled_name(target)

            # Print the prompt
            # end='' prevents a double newline if we were doing fancy cursor movement,
            # but here we just want a clean output.
            print(f"Next Jump Target: [ {display_name} ] ", end="")

            # Wait for the Enter key
            input()

            # Move index
            index = (index + 1) % len(pattern)

    except KeyboardInterrupt:
        print(f"\n{RESET}Run complete.")
        sys.exit()


if __name__ == "__main__":
    main()
