from agent import ask_agent
from prompts import (
    ANALYZE_PROMPT,
    IMPROVE_PROMPT,
    INSPIRE_PROMPT,
)

import os

print("=" * 55)
print("✨ QuietScript ✨")
print("Your AI companion for literary analysis, writing improvement, and creative inspiration.")
print("=" * 55)

while True:

    print("\nWhat would you like to do?\n")

    print("📖 1. Analyze Literature")
    print("🪶 2. Improve Writing")
    print("🕊️ 3. Generate Inspiration")
    print("🤍 4. Exit")

    choice = input("\nSelect (1-4): ")

    if choice == "4":
        print("\n🤍 See you in your next story.\n")
        break

    if choice not in ["1", "2", "3"]:
        print("\n✖️ Please select a valid option.\n")
        continue

    # -------- ANALYZE --------
    if choice == "1":

        print("\nHow would you like to provide your text?\n")
        print("1. Paste text")
        print("2. Read a .txt file")

        input_choice = input("\nSelect (1-2): ")

        if input_choice == "1":

            print("\nPaste your text:\n")
            user_text = input("> ")

        elif input_choice == "2":

            filename = input("\nEnter the txt file name (example: story.txt): ")

            if not os.path.exists(filename):
                print("\n✖️ File not found.\n")
                continue

            print(f"\n📖 Reading {filename}...\n")

            with open(filename, "r", encoding="utf-8") as file:
                user_text = file.read()

        else:
            print("\n✖️ Invalid option.\n")
            continue

        result = ask_agent(ANALYZE_PROMPT, user_text)

    # -------- IMPROVE --------
    elif choice == "2":

        print("\nEnter your text:\n")
        user_text = input("> ")

        result = ask_agent(IMPROVE_PROMPT, user_text)

    # -------- INSPIRE --------
    else:

        print("\nDescribe what you need:\n")
        user_text = input("> ")

        result = ask_agent(INSPIRE_PROMPT, user_text)

    print("\n" + "=" * 55)
    print(result)
    print("=" * 55)

    save = input("\n📜 Save this result as Markdown? (y/n): ")

    if save.lower() == "y":

        filename = input("Enter a file name (without .md): ").strip()

        if not filename:
            filename = "analysis"

        with open(f"{filename}.md", "w", encoding="utf-8") as file:

            file.write("# QuietScript Report\n\n")

            file.write("## User Input\n\n")
            file.write(user_text)

            file.write("\n\n---\n\n")

            file.write("## AI Response\n\n")
            file.write(result)

        print(f"\n✔️ Saved as {filename}.md\n")