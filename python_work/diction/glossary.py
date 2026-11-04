glossary = {
    'if': 'Evaluates an expression and executes the code block if True.',
    'else': 'The "else" block will execute when the "if" condition evaluates to False',
    'elif': 'Allows for more conditions to evaluate other than just "if".',
    'list': 'An group of ordered values accessed by an index numuber.',
    'print': 'Displays content for the operator to view.',
    'for': 'Loops over a group of values, such as a list or a dictionary.',
    'while': 'Evaluates a boolean condition and loops while the condition is true.',
    'list': 'An ordered group of values referenced by index numbers.',
    'dictionary': 'An unordered group of values referenced by key values.',
    }

print("#" * 25, " Glossary ", "#" * 25)
print("Commands\tMeaning")
for key, value in glossary.items():
    if len(key) > 5:
        print(f"{key}\t{value}\n")
    else:
        print(f"{key}\t\t{value}\n")
