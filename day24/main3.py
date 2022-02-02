# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
with open("../../PycharmProjects/day24/Input/Names/invited_names.txt") as names:
    # f = names.readline()
    # print(f)
    # print("..........")
    cont_f = 0
    for name in names:
        new_name = name.strip()
        with open("../../PycharmProjects/day24/Input/Letters/starting_letter.txt") as letters:
            # open(f"../../PycharmProjects/day24/Output/ReadyToSend/myFile{cont_f}.txt", "x")
            for line in letters:
                new_line = line.strip()
                if new_line == "Dear [name],":
                    aux = new_line.split()
                    new_line = aux[0] + " " + new_name + ","
                    file = f"myFile{cont_f}.txt"
                with open(f"../../PycharmProjects/day24/Output/ReadyToSend/{file}", mode="a") as output_1:
                    output_1.write(new_line+"\n")
            cont_f += 1
