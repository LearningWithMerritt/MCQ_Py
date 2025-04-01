'''Place preformmated questions and answers in the dictionary "questions" below.'''

setname = "set13"


questions = {}

'''Data Type Literals'''
s1 = {
"""Which of the following best describes 'Literal Data'?""": [
    "Actual values that do not represent anything else",
    "A variable that holds changing values",
    "A function used to manipulate data",
    "A type of programming loop"
],

"""Why is literal data important in programming?""": [
    "It provides fixed values that can be used directly in code",
    "It allows variables to change dynamically",
    "It is required for defining functions",
    "It helps debug errors in syntax"
]
}


'''Beginner Data Types'''
s2={
    """Which of the following best defines a boolean data type?""": [
        "A data type that represents True or False values",
        "A whole number without decimals",
        "A sequence of characters",
        "A collection of multiple items"
    ],

    """Which of the following is an example of an integer?""": [
        "5",
        "3.14",
        "'a'",
        '"Hello World"'
    ],

    """What is the key difference between an integer and a float?""": [
        "A float can contain decimal values, while an integer cannot",
        "An integer can contain decimal values, while a float cannot",
        "Integers are used for text, while floats are used for numbers",
        "Floats are whole numbers, while integers include decimals"
    ],

    """Which of the following is an example of a character data type?""": [
        "'a'",
        "5",
        "True",
        "[1, 2, 3]"
    ],

    """How is a string different from a character?""": [
        "A string contains multiple characters, while a character is a single symbol",
        "A string can only contain numbers, while a character is any symbol",
        "A character is a special kind of integer",
        "There is no difference between a string and a character"
    ],

    """Which of the following best describes a list in programming?""": [
        "A collection of multiple items called elements",
        "A single symbol stored in quotes",
        "A number that contains a decimal point",
        "A data type that only stores True or False"
    ],

    """How are indexes used in a list?""": [
        "They help access individual elements in a list",
        "They define the data type of the list",
        "They determine the size of a list",
        "They store decimal numbers in a list"
    ],

    """What is the first index of a list in most programming languages?""": [
        "0",
        "1",
        "2",
        "-1"
    ],

    """Which data type would be best for storing a name?""": [
        "String",
        "Integer",
        "Boolean",
        "Float"
    ],

    """Which of the following is NOT a beginner-friendly data type?""": [
        "Dictionary",
        "String",
        "Integer",
        "List"
    ]
}


'Mutable vs. Immutable Data'
s3 = {
    """What is the key difference between mutable and immutable data types?""": [
        "Mutable data can change, while immutable data cannot be changed",
        "Immutable data can change, while mutable data cannot be changed",
        "Mutable data is used for numbers, while immutable data is used for collections",
        "There is no difference between mutable and immutable data types"
    ],

    """Which of the following is a mutable data type?""": [
        "List",
        "Integer",
        "String",
        "Tuple"
    ],

    """Which of the following is an immutable data type?""": [
        "Tuple",
        "Dictionary",
        "Set",
        "List"
    ],

    """Why might you choose an immutable data type like a tuple instead of a list?""": [
        "Tuples ensure that data cannot be accidentally modified",
        "Tuples take up more memory than lists",
        "Tuples allow you to change values easily",
        "Tuples are the only way to store text data"
    ],

    """What happens if you try to modify an immutable data type?""": [
        "An error occurs because immutable data cannot be changed",
        "The value updates without any issues",
        "The data type automatically converts to mutable",
        "It creates a reference to the original value instead of modifying it"
    ]
}

'Determining Type of Data'
s4 = {
    """What does the type() function do in Python?""": [
        "Returns the type of the data passed as an argument",
        "Changes the type of the given data",
        "Creates a new data type",
        "Converts data into a string"
    ],

    """Which of the following is the correct syntax for using the type() function?""": [
        "type(data)",
        "data.type()",
        "typeof data",
        "getType(data)"
    ],

    """What happens if you call type() without an argument?""": [
        "An error occurs because type() requires an argument",
        "It returns 'None'",
        "It defaults to checking the type of the last variable used",
        "It returns 'unknown'"
    ],

    """What will type(3.14) return in Python?""": [
        "<class 'float'>",
        "<class 'int'>",
        "<class 'string'>",
        "<class 'list'>"
    ],

    """Which of the following statements about type() is true?""": [
        "It helps determine the type of a variable at runtime",
        "It can be used to change a variable's data type",
        "It only works with numeric data types",
        "It returns a string representation of the type"
    ],
        """What will type(42) return in Python?""": [
        "<class 'int'>",
        "<class 'float'>",
        "<class 'string'>",
        "<class 'boolean'>"
    ],

    """What will type(True) return in Python?""": [
        "<class 'bool'>",
        "<class 'int'>",
        "<class 'string'>",
        "<class 'float'>"
    ],

    """What will type('Hello') return in Python?""": [
        "<class 'str'>",
        "<class 'char'>",
        "<class 'list'>",
        "<class 'tuple'>"
    ],

    """What will type(['a', 'b', 'c']) return in Python?""": [
        "<class 'list'>",
        "<class 'tuple'>",
        "<class 'set'>",
        "<class 'dict'>"
    ],

    """What will type(('x', 'y', 'z')) return in Python?""": [
        "<class 'tuple'>",
        "<class 'list'>",
        "<class 'set'>",
        "<class 'dict'>"
    ],

    """What will type({'name': 'Alice', 'age': 25}) return in Python?""": [
        "<class 'dict'>",
        "<class 'list'>",
        "<class 'set'>",
        "<class 'tuple'>"
    ],
}

'Data Literals'
s5 = {
    """What is a data literal in programming?""": [
        "A notation for representing a fixed actual value",
        "A variable that can change over time",
        "A function that modifies data",
        "A reference to another value"
    ],

    """Which of the following best describes the purpose of a literal?""": [
        "To directly represent a fixed value in code",
        "To store changing values dynamically",
        "To execute a function on a value",
        "To create a reference to another variable"
    ],

    """Which of the following is an example of a literal?""": [
        "3.14",
        "x = 5",
        "def add(a, b): return a + b",
        "my_list = [1, 2, 3]"
    ],
        """What is the definition of a literal in programming?""": [
        "A notation for representing a fixed actual value",
        "A variable that can be reassigned",
        "A function used to modify data",
        "A reference to another value"
    ],

    """Which statement best defines a literal?""": [
        "A direct representation of a fixed value in code",
        "A name assigned to a changing value",
        "A function that calculates values dynamically",
        "A placeholder for user input"
    ],

    """How is a literal defined in programming?""": [
        "A value written exactly as it is meant to be used",
        "A symbolic name for a stored value",
        "A function that operates on data",
        "A reference to a memory location"
    ],

    """What does the term 'literal' mean in the context of programming?""": [
        "A fixed value that does not represent something else",
        "A variable that holds changing data",
        "A type of function used in code",
        "A reference to an object in memory"
    ]
}


s6 = {
    """What does the 'None' literal represent in Python?""": [
        "A null value or the absence of a value",
        "An empty string",
        "A boolean value",
        "A numeric value of zero"
    ],

    """Which of the following is the correct way to define a null value in Python?""": [
        "None",
        "null",
        "undefined",
        "nil"
    ],

    """What is the data type of None in Python?""": [
        "<class 'NoneType'>",
        "<class 'int'>",
        "<class 'str'>",
        "<class 'float'>"
    ],
        """What are the two possible values of a boolean literal in Python?""": [
        "True and False",
        "0 and 1",
        "Yes and No",
        "On and Off"
    ],

    """Which of the following represents a boolean literal in Python?""": [
        "False",
        '"True"',
        "None",
        "undefined"
    ],

    """What is the data type of the literal True in Python?""": [
        "<class 'bool'>",
        "<class 'int'>",
        "<class 'str'>",
        "<class 'NoneType'>"
    ],
    """What does an integer literal represent in Python?""": [
        "A whole number with no fractional part",
        "A number with decimals",
        "A sequence of characters",
        "A boolean value"
    ],

    """Which of the following is a valid integer literal in Python?""": [
        "100",
        "3.14",
        "'Hello'",
        "True"
    ],

    """How are large integer literals written to improve readability in Python?""": [
        "By using underscores",
        "By using commas",
        "By writing them in scientific notation",
        "By writing them as strings"
    ],

    """What will type(1_000_000) return in Python?""": [
        "<class 'int'>",
        "<class 'float'>",
        "<class 'str'>",
        "<class 'bool'>"
    ],

    """What is the result of using scientific notation like 1E9 in Python?""": [
        "It returns a float value",
        "It returns an integer value",
        "It causes an error",
        "It returns a string"
    ],

    """What is the value of 1E9 in Python?""": [
        "1000000000.0",
        "1000000000",
        "1E9",
        "None"
    ],

    """Which of the following is an invalid integer literal in Python?""": [
        "3.14",
        "1_000_000",
        "1000",
        "-200"
    ],

    """How does Python handle large integer literals with underscores like 1_000_000?""": [
        "It removes the underscores but keeps the value the same",
        "It throws an error",
        "It treats it as a string",
        "It rounds the number"
    ],
    """What is a float literal in Python?""": [
        "A fractional number that includes a decimal point",
        "A whole number with no decimal point",
        "A sequence of characters",
        "A boolean value"
    ],

    """Which of the following is a valid float literal in Python?""": [
        "3.141592653589",
        "1000",
        "'Hello'",
        "True"
    ],

    """What does the decimal point in a float literal represent?""": [
        "It separates the whole number from the fractional part",
        "It indicates the start of a string",
        "It marks the start of a scientific notation",
        "It is used to represent negative numbers"
    ],

    """True or False: A float literal must always contain a decimal point.""": [
        "True",
        "False"
    ],

    """What is the data type of 3.14159 in Python?""": [
        "<class 'float'>",
        "<class 'int'>",
        "<class 'str'>",
        "<class 'NoneType'>"
    ],

    """True or False: Float literals in Python can have fractional parts but no decimal point.""": [
        "False",
        "True"
    ],

    """What will type(-78.91) return in Python?""": [
        "<class 'float'>",
        "<class 'int'>",
        "<class 'str'>",
        "<class 'bool'>"
    ],

    """Which of the following is an example of a float literal in Python?""": [
        "1.12",
        "100",
        "True",
        "'Python'"
    ], 

    """Which of the following is a complex literal datatype?""": [
        "3 + 2j",
        "3 + 2",
        "3.14",
        "True"
    ],
        """What is a character literal in Python?""": [
        "A single unit of text, such as a letter, digit, punctuation mark, symbol, or whitespace",
        "A string of multiple characters",
        "A boolean value",
        "A floating-point number"
    ],

    """Which of the following is a valid character literal in Python?""": [
        "'A'",
        "'Hello'",
        "'True'",
        "['A', 'B', 'C']"
    ],

    """True or False: In Python, a character literal is treated as a single-length string. True or False?""": [
        "True",
        "False"
    ],

    """Which of the following represents a whitespace character literal in Python?""": [
        "' '",
        "'\n'",
        "'\t'",
        "'\\'"
    ],

    """Which of the following represents a valid escape sequence for a newline character in Python?""": [
        "'\\n'",
        "'\\t'",
        "'\t'",
        "'\\a'"
    ],
        """What is a string literal in Python?""": [
        "A collection of characters",
        "A single character",
        "A sequence of numbers",
        "A boolean value"
    ],

    """Which of the following is a valid string literal in Python?""": [
        "\"Hello World!\"",
        "5",
        "True",
        "'a'"
    ],

    """True or False: A string literal in Python can contain letters, numbers, and symbols. True or False?""": [
        "True",
        "False"
    ],

    """Which of the following is an example of a string literal in Python?""": [
        "\"Python\"",
        "3.14",
        "'A'",
        "3 + 4j"
    ],

    """True or False: A string literal in Python must be enclosed in quotes (single or double). True or False?""": [
        "True",
        "False"
    ],
    """What is a list literal in Python?""": [
        "A collection of comma-separated elements enclosed in square brackets",
        "A sequence of characters enclosed in double quotes",
        "A collection of key-value pairs",
        "A single element enclosed in curly braces"
    ],

    """Which of the following is a valid list literal in Python?""": [
        "[1, 2, 3, 4]",
        "{1, 2, 3, 4}",
        "(1, 2, 3, 4)",
        "'1, 2, 3, 4'"
    ],

    """True or False: Lists in Python are mutable, meaning their elements can be changed after creation. True or False?""": [
        "True",
        "False"
    ],

    """Which of the following is used to access the first element of a list?""": [
        "Index 0",
        "Index 1",
        "The list length",
        "None of the above"
    ],

    """True or False: Lists in Python allow duplicate elements. True or False?""": [
        "True",
        "False"
    ],
    """What index is used to access the second element of the list ['a', 'b', 'c']?""": [
        "1",
        "2",
        "0",
        "3"
    ],
    """What is a tuple literal in Python?""": [
        "A collection of ordered, immutable elements enclosed in parentheses",
        "A collection of ordered, mutable elements enclosed in square brackets",
        "A collection of unordered elements enclosed in curly braces",
        "A collection of characters enclosed in double quotes"
    ],

    """Which of the following is a valid tuple literal in Python?""": [
        "('a', 'b', 'c')",
        "[1, 2, 3]",
        "{'a': 1, 'b': 2}",
        "'a', 'b', 'c'"
    ],

    """True or False: Tuples in Python are immutable, meaning their elements cannot be changed after creation. True or False?""": [
        "True",
        "False"
    ],

    """Which of the following is used to access the second element of the tuple ('a', 'b', 'c')?""": [
        "Index 1",
        "Index 2",
        "Index 0",
        "Index 3"
    ],

    """True or False: Tuples in Python allow duplicate elements. True or False?""": [
        "True",
        "False"
    ],
    """What is a dictionary literal in Python?""": [
        "A collection of key-value pairs enclosed in curly braces",
        "A collection of ordered elements enclosed in square brackets",
        "A sequence of elements enclosed in parentheses",
        "A collection of key-value pairs enclosed in parentheses"
    ],

    """Which of the following is a valid dictionary literal in Python?""": [
        "{'a': 1, 'b': 2, 'c': 3}",
        "[1, 2, 3]",
        "{'a', 'b', 'c'}",
        "'a': 1, 'b': 2"
    ],

    """True or False: Dictionaries in Python allow duplicate keys. True or False?""": [
        "False",
        "True"
    ],

    """Which of the following is used to access the value associated with the key 'b' in the dictionary {'a': 1, 'b': 2, 'c': 3}?""": [
        "dictionary['b']",
        "dictionary[1]",
        "dictionary('b')",
        "dictionary.get('b')"
    ],

    """True or False: In a dictionary, the keys must be unique. True or False?""": [
        "True",
        "False"
    ],

    """What is a set literal in Python?""": [
        "A collection of unordered, mutable elements enclosed in curly braces",
        "A collection of ordered elements enclosed in square brackets",
        "A sequence of elements enclosed in parentheses",
        "A collection of key-value pairs enclosed in curly braces"
    ],

    """Which of the following is a valid set literal in Python?""": [
        "{1, 2, 3}",
        "[1, 2, 3]",
        "('a', 'b', 'c')",
        "{'a': 1, 'b': 2}"
    ],

    """True or False: Sets in Python allow duplicate elements. True or False?""": [
        "False",
        "True"
    ],

    """What will be the output of the following code: {1, 2, 3, 3}?""": [
        "{1, 2, 3}",
        "{1, 2, 3, 3}",
        "Error",
        "{3, 2, 1}"
    ],

    """True or False: In a set, the elements are ordered and can be accessed by an index. True or False?""": [
        "False",
        "True"
    ],
    """What is a data structure in computer science?""": [
        "A specialized format for organizing, processing, retrieving, and storing data",
        "A collection of elements",
        "A method for accessing data",
        "A type of programming language"
    ],

    """Which of the following best defines a collection?""": [
        "A data structure that holds multiple elements",
        "A single element in a list",
        "A type of algorithm",
        "A function that processes data"
    ],

    """What is a member in the context of a collection?""": [
        "An item stored within a collection",
        "A method for accessing elements",
        "A specific index in a list",
        "A synonym for a data type"
    ],

    """Which of the following is a synonym for a member in a collection?""": [
        "Element",
        "Index",
        "Function",
        "Key"
    ],

    """What does it mean if a collection is ordered?""": [
        "It has a specific order, such as 0, 1, 2, ...",
        "It allows changes to its elements",
        "It stores elements randomly",
        "It does not use indexes"
    ],

    """Which of the following best describes an indexed collection?""": [
        "Elements are associated with a specific identifier (index), which can be used to directly locate and access the data",
        "Elements are unordered and cannot be accessed directly",
        "It contains only unique elements",
        "It is immutable"
    ],

    """What does it mean if a collection is mutable?""": [
        "Its elements can change",
        "Its elements cannot be changed",
        "It does not allow duplicate elements",
        "It stores elements in a specific order"
    ],

    """What does it mean if a collection is immutable?""": [
        "Its elements cannot change",
        "Its elements can change",
        "It has no specific order",
        "It allows duplicate elements"
    ]


}

# {question : [answer, *options]}
questions.update(s1)
questions.update(s2)
questions.update(s3)
questions.update(s4)
questions.update(s5)
questions.update(s6)
# questions.update(s7)
# questions.update(s8)
# questions.update(s9)
# questions.update(s10)







if __name__ == "__main__":
    print(len(questions))

    # for question, options in questions.items():
    #     print(question, *options, sep="\n")
    #     input()