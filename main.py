CHANGE_THIS = "[name]"
with open("./input/Names/invited_names.txt", "r") as name:
    m = name.readlines()
with open("./input/Letters/starting_letter.txt", "r") as txt:
    text = txt.read()
for names in m:
    need = names.strip("\n")
    x = text.replace(CHANGE_THIS, f"{need}")
    with open(f"./output/ReadyToSend/send_to_{need}.txt", "w") as letter:
        letter.write(x)

