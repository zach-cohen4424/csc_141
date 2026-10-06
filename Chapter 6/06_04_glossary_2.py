# I created another glossary of Python terms and use a loop to print each term and its meaning. I added the lopp instead of printing each line out. 
glossary = {
    "variable": "A name used to hold a piece of information.",
    "list": "A group of different items stored in one place.",
    "dictionary": "A collection that stores information using keys and values.",
    "loop": "A way to repeat a section of code.",
    "string": "Text made up of characters inside quotation marks.",
    "integer": "A number without a decimal.",
    "float": "A number that has a decimal point.",
    "boolean": "A value that can be either True or False.",
    "function": "A section of code made to complete a certain task.",
    "comment": "Text in code that explains something but is not run by Python."
}

for word, meaning in glossary.items():
    print(word.title() + ": " + meaning + "\n")