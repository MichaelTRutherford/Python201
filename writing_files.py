with open('writing_files.txt', 'w') as file:
    file.write("\nA second line!")
    file.write("\n\tThis is tabbed!")

with open('writing_files.txt', 'a') as file:
    file.write("\nA second line!")
    file.write("\n\tThis is tabbed!")
