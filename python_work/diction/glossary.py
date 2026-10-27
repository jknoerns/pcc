glossary = {
    'if': 'Evaluates an expression and executes the code block if True.',
    'else': 'The "else" block will execute when the "if" condition evaluates to False',
    'elif': 'Allows for more conditions to evaluate other than just "if".',
    'list': 'An group of ordered values accessed by an index numuber.',
    'print': 'Displays content for the operator to view.',
    }

print("#" * 25, " Glossary ", "#" * 25)
print("Commands\tMeaning")
for key, value in glossary.items():
    print(f"{key}\t\t{value}\n")
