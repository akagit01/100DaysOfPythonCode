from pathlib import Path

# Set base directory to the folder where your script is located
base_dir = Path(__file__).parent
print(base_dir)
input_letters_path = base_dir / "input" / "letters" / "start_letters.txt"
names_path = base_dir / "input" / "names" / "invited_names.txt"
output_dir = base_dir / "output" / "ready_to_send"

#first_names = []

with open(input_letters_path) as letter_template:
    content = letter_template.read()
    # print(content)

with open(names_path) as names:
    fnames = names.read().splitlines()
    #first_names = fnames.split("\n")

#

for name in fnames:
    output_file=output_dir / f"letter_for_{name}.txt"
    with open(output_file,mode='w') as letter:
        letter.write(content.replace("[name]", name))
