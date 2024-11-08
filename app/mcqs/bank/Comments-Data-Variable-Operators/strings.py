


'Basic Questions'

'Characters'
MCQ("Which of the following is a valid character representation in Python?","'2'","2","b","None of the above","All of the these","'2'")
MCQ("Which of the following correctly represents a space character in Python?","' '","'a'","'2'","'@'","None of the above","' '")
MCQ("Which of the following is a valid character representation in Python?","'@'","'2'","' '","None of the above","All of the these","All of the these")

'Special Characters'
MCQ("Which special character is used to insert a new line?",r"\n",r"\t","\\", "\'", "None of the above",r"\n")
MCQ("Which special character is used to insert horizontal spacing?",r"\t",r"\n",r"\\","'","None of the above",r"\t")
MCQ("Which special character is used to represent a single backslash character?","\\\\",r"\n",r"\t","'","None of the above","\\\\")
MCQ("Which special character is used to represent a single quote?","'",r"\n",r"\t","\\","None of the above","'")
MCQ("Which special character is used to represent a double quote?","\"",r"\n",r"\t","\\","None of the above","\"")
MCQ("Which special character is used to return the cursor to the beginning of the line?",r"\r",r"\n",r"\t","\\","None of the above",r"\r")
MCQ("Which special character is used to delete the preceding character?",r"\b",r"\n",r"\t",r"\\","None of the above",r"\b")

'Converting Characters'
MCQ("Which function returns the binary representation of a whole number (integer)?","bin()","hex()","ord()","chr()","None of the above","bin()")
MCQ("Which function returns the hexadecimal representation of a whole number (integer)?","hex()","bin()","oct()","ord()","None of the above","hex()")
MCQ("Which function returns the octal representation of a whole number (integer)?","oct()","bin()","hex()","ord()","None of the above","oct()")
MCQ("Which function returns the Decimal Unicode value of a single character string?","ord()","bin()","hex()","chr()","None of the above","ord()")
MCQ("Which function returns the single character Unicode string for a given integer?","chr()","bin()","hex()","ord()","None of the above","chr()")
MCQ("What is the binary representation of the number 32 returned by the bin() function?","0b100000","0x20","0o40","97","a","0b100000")
MCQ("What is the hexadecimal representation of the number 32 returned by the hex() function?","0x20","0b100000","0o40","97","a","0x20")
MCQ("What is the octal representation of the number 32 returned by the oct() function?","0o40","0b100000","0x20","97","a","0o40")
MCQ("What is the Decimal Unicode value of the character 'a' returned by the ord() function?","97","0b100000","0x20","0o40","a","97")
MCQ("What is the single character Unicode string for the Decimal value 97 returned by the chr() function?","a","0b100000","0x20","0o40","97","a")

'Strings Defined'
MCQ("How is a string represented in Python?","text in quotes","text in curly braces","text in square brackets","text in parentheses","None of the above","text in quotes")
MCQ("Which method can be used to create string literals that span multiple lines in Python?",
    "print('''\n         line 1\n         line 2\n         line 3\n         ''')",
    "print(###\n         line 1\n         line 2\n         line 3\n         ###)",
    "print(\"\n       line 1\n       line 2\n       line 3\n       \")",
    "print('\n       line 1\n       line 2\n       line 3\n       ')",
    "None of the above",
    "print('''\n         line 1\n         line 2\n         line 3\n         ''')")
MCQ("In Python, what is the type of a string object?","<class 'str'>","<class 'string'>","<type 'str'>","<type 'string'>","None of the above","<class 'str'>")

'> Strings Concatenation and Duplication'

MCQ("How do you concatenate strings in Python?","Using the + operator","Using the - operator","Using the * operator","Using the / operator","None of the above","Using the + operator")
MCQ("Which of the following correctly demonstrates string concatenation in Python?","'Hello' + 'World'","'Hello' - 'World'","'Hello' * 'World'","'Hello' / 'World'","None of the above","'Hello' + 'World'")
MCQ("Which operator is used to combine two or more strings into a single string in Python?","+","-","*","/","None of the above","+")
MCQ("In Python, how would you join 'Hello' and 'World' to form 'Hello World'?","'Hello' + ' ' + 'World'","'Hello' - ' ' - 'World'","'Hello' * ' ' * 'World'","'Hello' / ' ' / 'World'","None of the above","'Hello' + ' ' + 'World'")
MCQ("What is the result of 'Python' + 'Programming' in Python?","'PythonProgramming'","'Python Programming'","'ProgrammingPython'","'Python' 'Programming'","None of the above","'PythonProgramming'")

MCQ("How can you duplicate a string in Python?","Using the * operator","Using the + operator","Using the - operator","Using the / operator","None of the above","Using the * operator")
MCQ("Which of the following demonstrates string duplication in Python?","'Hello' * 3","'Hello' + 3","'Hello' - 3","'Hello' / 3","None of the above","'Hello' * 3")
MCQ("Which operator is used to duplicate a string in Python?","*","-","+","/","None of the above","*")
MCQ("What does 'Hello' * 2 evaluate to in Python?","'HelloHello'","'Hello Hello'","'Hello' 'Hello'","'HelloHelloHello'","None of the above","'HelloHello'")
MCQ("How can you repeat the string 'Python' three times in Python?","'Python' * 3","'Python' + 3","'Python' - 3","'Python' / 3","None of the above","'Python' * 3")

'> String Indexing'
MCQ("What is string indexing in Python?", "Accessing individual characters of a string by their position", "Combining multiple strings into one", "Counting the number of characters in a string", "Splitting a string into substrings", "Finding the length of a string", "Accessing individual characters of a string by their position")
MCQ("What is the index of the last character in a string?", "-1", "0", "1", "The length of the string", "The first character of the string", "-1")
MCQ("How can you access the third character of a string using indexing?", "string[2]", "string[3]", "string[0]", "string[-3]", "string[-2]", "string[2]")
MCQ("What is the index of the character 'e' in the string 'Hello'?", "1", "2", "3", "-1", "-2", "1")
MCQ("What happens if you try to access an index that is out of range for a string?", "You'll get an IndexError", "You'll get the last character of the string", "The program will crash", "You'll get the first character of the string", "You'll get a warning message", "You'll get an IndexError")

'> String Slicing'
MCQ("What does string slicing return in Python?", "A substring or a part of the original string", "A reversed version of the original string", "The original string with all characters converted to uppercase", "The length of the original string", "The index of the first occurrence of a specified character", "A substring or a part of the original string")
MCQ("What is the result of slicing word[:5] where word = 'Programming'?", "'Progr'", "'rogramming'", "'Progra'", "'Program'", "'ing'", "'Progr'")
MCQ("In Python string slicing, is the stop_index included in the slice?", "No, the stop_index is not included", "Yes, the stop_index is included", "It depends on the length of the string", "It depends on the start_index", "It depends on the slicing operator used", "No, the stop_index is not included")
MCQ("What happens if you try to modify a character in a string in Python?", "You'll get an error because Python strings are immutable", "The character will be replaced with the specified value", "The character will be removed from the string", "The character will be appended to the end of the string", "The character will be inserted at the specified index", "You'll get an error because Python strings are immutable")
MCQ("What is the result of slicing word[-5:-1] where word = 'Programming'?", "'mmin'", "'min'", "'gram'", "'ming'", "'Prog'", "'mmin'")

'> Built in String Function Calls'
MCQ("What does the len() function return when called on an empty string?", "0", "1", "None", "An error", "The length of the string", "0")
MCQ("What is the result of len('hello')?", "5", "6", "4", "10", "The letter 'h'", "5")
MCQ("What does len('Python') return?", "6", "5", "7", "1", "The letter 'P'", "6")
MCQ("What does len('1234567890') return?", "10", "9", "11", "0", "The number '1'", "10")
MCQ("What is the output of len('')?", "0", "1", "Null", "An error", "The length of the string", "0")


##################################################################################################################################################################################################################################################




'Advanced Questions'

'> Builtin-Methods'
MCQ("What does the capitalize() function do to a string?", "Converts the first character to uppercase", "Converts the entire string to uppercase", "Converts the first character to lowercase", "Converts the entire string to lowercase", "None of the above", "Converts the first character to uppercase")
MCQ("What does the casefold() function do to a string?", "Converts the string to lowercase", "Converts the string to uppercase", "Returns a casefolded copy of the string, suitable for case-insensitive comparisons", "Returns the encoded version of the string", "None of the above", "Returns a casefolded copy of the string, suitable for case-insensitive comparisons")
MCQ("What does the center() function do to a string?", "Returns a centered string of a specified width", "Removes leading and trailing whitespace", "Returns the number of occurrences of a substring", "Returns the lowest index of a substring in the string", "Converts the string to lowercase", "Returns a centered string of a specified width")
MCQ("What does the count() function do to a string?", "Returns the number of occurrences of a substring in the string", "Finds the lowest index of a substring in the string", "Returns the encoded version of the string", "Checks if the string starts with a specified prefix", "None of the above", "Returns the number of occurrences of a substring in the string")
MCQ("What does the encode() function do to a string?", "Returns the encoded version of the string", "Decodes the string from Unicode to ASCII", "Converts the string to lowercase", "Returns the number of characters in the string", "Splits the string at line breaks and returns a list of lines", "Returns the encoded version of the string")
MCQ("What does the endswith() function do?", "Checks if the string ends with a specified suffix", "Checks if the string starts with a specified prefix", "Returns a centered string of a specified width", "Returns a casefolded copy of the string, suitable for case-insensitive comparisons", "None of the above", "Checks if the string ends with a specified suffix")
MCQ("What does the expandtabs() function do?", "Expands tabs in the string to spaces", "Converts the string to lowercase", "Returns a centered string of a specified width", "Returns a casefolded copy of the string, suitable for case-insensitive comparisons", "None of the above", "Expands tabs in the string to spaces")
MCQ("What does the find() function do?", "Returns the lowest index of a substring in the string", "Returns the number of occurrences of a substring in the string", "Checks if all characters in the string are alphanumeric", "Formats the string using a mapping", "None of the above", "Returns the lowest index of a substring in the string")
MCQ("What does the format() function do?", "Formats the string", "Converts the string to lowercase", "Returns a centered string of a specified width", "Expands tabs in the string to spaces", "None of the above", "Formats the string")
MCQ("What does the format_map() function do?", "Formats the string using a mapping", "Removes a suffix from the string", "Returns a casefolded copy of the string, suitable for case-insensitive comparisons", "Expands tabs in the string to spaces", "None of the above", "Formats the string using a mapping")
MCQ("What does the index() function do?", "Returns the lowest index of a substring in the string", "Checks if all characters in the string are alphanumeric", "Formats the string using a mapping", "Expands tabs in the string to spaces", "None of the above", "Returns the lowest index of a substring in the string")
MCQ("What does the isalnum() function do?", "Checks if all characters in the string are alphanumeric", "Returns a copy of the string converted to lowercase", "Expands tabs in the string to spaces", "Returns a centered string of a specified width", "None of the above", "Checks if all characters in the string are alphanumeric")
MCQ("What does the isalpha() function do?", "Checks if all characters in the string are alphabetic", "Checks if all characters in the string are numeric", "Checks if all characters in the string are lowercase", "Checks if all characters in the string are uppercase", "None of the above", "Checks if all characters in the string are alphabetic")
MCQ("What does the isascii() function do?", "Checks if the string contains only ASCII characters", "Checks if all characters in the string are alphabetic", "Returns a copy of the string converted to lowercase", "Expands tabs in the string to spaces", "None of the above", "Checks if the string contains only ASCII characters")
MCQ("What does the isdecimal() function do?", "Checks if all characters in the string are decimal", "Checks if all characters in the string are alphanumeric", "Checks if all characters in the string are numeric", "Returns a copy of the string converted to lowercase", "None of the above", "Checks if all characters in the string are decimal")
MCQ("What does the isdigit() function do?", "Checks if all characters in the string are digits", "Checks if the string contains only ASCII characters", "Returns a copy of the string converted to uppercase", "Expands tabs in the string to spaces", "None of the above", "Checks if all characters in the string are digits")
MCQ("What does the isidentifier() function do?", "Checks if the string is a valid identifier", "Checks if all characters in the string are alphabetic", "Returns a copy of the string converted to lowercase", "Checks if all characters in the string are alphanumeric", "None of the above", "Checks if the string is a valid identifier")
MCQ("What does the islower() function do?", "Checks if all characters in the string are lowercase", "Checks if all characters in the string are numeric", "Returns a copy of the string converted to uppercase", "Checks if all characters in the string are alphabetic", "None of the above", "Checks if all characters in the string are lowercase")
MCQ("What does the isnumeric() function do?", "Checks if all characters in the string are numeric", "Checks if all characters in the string are alphanumeric", "Returns a copy of the string converted to lowercase", "Checks if all characters in the string are uppercase", "None of the above", "Checks if all characters in the string are numeric")
MCQ("What does the isprintable() function do?", "Checks if all characters in the string are printable", "Checks if the string contains only ASCII characters", "Returns a copy of the string converted to lowercase", "Checks if all characters in the string are alphanumeric", "None of the above", "Checks if all characters in the string are printable")  
MCQ("What does the isspace() function do?", "Checks if all characters in the string are whitespaces", "Checks if all characters in the string are alphabetic", "Returns a copy of the string converted to lowercase", "Checks if all characters in the string are numeric", "None of the above", "Checks if all characters in the string are whitespaces")
MCQ("What does the istitle() function do?", "Checks if the string is titlecased", "Checks if all characters in the string are alphanumeric", "Returns a copy of the string converted to lowercase", "Checks if all characters in the string are uppercase", "None of the above", "Checks if the string is titlecased")
MCQ("What does the isupper() function do?", "Checks if all characters in the string are uppercase", "Checks if all characters in the string are alphanumeric", "Returns a copy of the string converted to lowercase", "Checks if all characters in the string are numeric", "None of the above", "Checks if all characters in the string are uppercase")
MCQ("What does the join() function do?", "Joins the elements of an iterable to create a string", "Checks if all characters in the string are numeric", "Returns a copy of the string converted to lowercase", "Expands tabs in the string to spaces", "None of the above", "Joins the elements of an iterable to create a string")
MCQ("What does the ljust() function do?", "Returns a left-justified string of a specified width", "Checks if all characters in the string are alphanumeric", "Checks if the string contains only ASCII characters", "Checks if all characters in the string are uppercase", "None of the above", "Returns a left-justified string of a specified width") 
MCQ("What does the lower() function do?", "Returns a copy of the string converted to lowercase", "Checks if all characters in the string are alphanumeric", "Checks if the string contains only ASCII characters", "Checks if all characters in the string are uppercase", "None of the above", "Returns a copy of the string converted to lowercase")
MCQ("What does the lstrip() function do?", "Returns a copy of the string with leading whitespace removed", "Checks if all characters in the string are numeric", "Checks if the string contains only ASCII characters", "Checks if all characters in the string are uppercase", "None of the above", "Returns a copy of the string with leading whitespace removed")
MCQ("What does the maketrans() function do?", "Returns a translation table usable for str.translate()", "Checks if all characters in the string are alphanumeric", "Returns a casefolded copy of the string, suitable for case-insensitive comparisons", "Returns a copy of the string with leading whitespace removed", "None of the above", "Returns a translation table usable for str.translate()")
MCQ("What does the partition() function do?", "Splits the string at the first occurrence of a separator", "Checks if all characters in the string are alphanumeric", "Returns a copy of the string with leading whitespace removed", "Returns a casefolded copy of the string, suitable for case-insensitive comparisons", "None of the above", "Splits the string at the first occurrence of a separator")
MCQ("What does the removeprefix() function do?", "Removes a prefix from the string", "Checks if all characters in the string are alphanumeric", "Returns a copy of the string with leading whitespace removed", "Returns a casefolded copy of the string, suitable for case-insensitive comparisons", "None of the above", "Removes a prefix from the string")
MCQ("What does the removesuffix() function do?", "Removes a suffix from the string", "Replaces occurrences of a substring in the string", "Finds the highest index of a substring in the string", "Right-justifies the string in a specified width", "None of the above", "Removes a suffix from the string")
MCQ("What does the replace() function do?", "Returns a copy of the string with occurrences of a substring replaced", "Checks if all characters in the string are alphanumeric", "Checks if the string contains only ASCII characters", "Checks if all characters in the string are uppercase", "None of the above", "Returns a copy of the string with occurrences of a substring replaced")
MCQ("What does the rfind() function do?", "Returns the highest index of a substring in the string", "Returns a copy of the string with leading whitespace removed", "Splits the string at the last occurrence of a separator", "Checks if all characters in the string are numeric", "None of the above", "Returns the highest index of a substring in the string")
MCQ("What does the rindex() function do?", "Returns the highest index of a substring in the string", "Formats the string", "Splits the string at the last occurrence of a separator", "Checks if all characters in the string are numeric", "None of the above", "Returns the highest index of a substring in the string")
MCQ("What does the rjust() function do?", "Returns a right-justified string of a specified width", "Removes a prefix from the string", "Splits the string at the last occurrence of a separator", "Checks if all characters in the string are numeric", "None of the above", "Returns a right-justified string of a specified width")  
MCQ("What does the rpartition() function do?", "Splits the string at the last occurrence of a separator", "Returns a copy of the string with leading and trailing whitespace removed", "Checks if the string starts with a specified prefix", "Converts all uppercase characters to lowercase and vice versa", "None of the above", "Splits the string at the last occurrence of a separator")
MCQ("What does the rsplit() function do?", "Splits the string into a list, starting from the right", "Removes a suffix from the string", "Checks if all characters in the string are alphanumeric", "Finds the highest index of a substring in the string", "None of the above", "Splits the string into a list, starting from the right")
MCQ("What does the splitlines() function do?", "Splits the string at line breaks and returns a list of lines", "Returns a copy of the string with leading whitespace removed", "Checks if all characters in the string are alphabetic", "Checks if all characters in the string are uppercase", "None of the above", "Splits the string at line breaks and returns a list of lines")
MCQ("What does the startswith() function do?", "Checks if the string starts with a specified prefix", "Formats the string", "Returns a copy of the string with leading whitespace removed", "Checks if all characters in the string are numeric", "None of the above", "Checks if the string starts with a specified prefix")
MCQ("What does the strip() function do?", "Returns a copy of the string with leading and trailing whitespace removed", "Replaces occurrences of a substring in the string", "Splits the string at line breaks and returns a list of lines", "Checks if all characters in the string are uppercase", "None of the above", "Returns a copy of the string with leading and trailing whitespace removed") 
MCQ("What does the swapcase() function do?", "Returns a copy of the string with uppercase characters converted to lowercase and vice versa", "Converts the string to title case", "Encodes the string using a specified encoding", "Converts all characters in the string to uppercase", "None of the above", "Returns a copy of the string with uppercase characters converted to lowercase and vice versa")
MCQ("What does the title() function do?", "Returns a titlecased version of the string", "Converts the string to uppercase", "Removes leading and trailing whitespace", "Returns a copy of the string with leading whitespace removed", "None of the above", "Returns a titlecased version of the string")
MCQ("What does the translate() function do?", "Returns a copy of the string where each character has been mapped through the given translation table", "Replaces occurrences of a substring in the string", "Checks if the string starts with a specified prefix", "Splits the string at the last occurrence of a separator", "None of the above", "Returns a copy of the string where each character has been mapped through the given translation table")
MCQ("What does the upper() function do?", "Returns a copy of the string converted to uppercase", "Splits the string into a list, starting from the right", "Checks if all characters in the string are numeric", "Finds the lowest index of a substring in the string", "None of the above", "Returns a copy of the string converted to uppercase")
MCQ("What does the zfill() function do?", "Returns a copy of the string padded with zeros to a specified width", "Splits the string at the last occurrence of a separator", "Returns a copy of the string with leading and trailing whitespace removed", "Checks if all characters in the string are alphabetic", "None of the above", "Returns a copy of the string padded with zeros to a specified width") 

'> Format Strings: f-strings'
MCQ("What is the primary purpose of f-strings in Python?", "To create formatted strings with embedded expressions", "To split strings into substrings based on a delimiter", "To remove whitespace from the beginning and end of a string", "To convert strings to uppercase", "None of the above", "To create formatted strings with embedded expressions")
MCQ("Which symbol is used to denote an f-string in Python?", "Prefixing the string with an 'f' or 'F'", r"Using curly braces '{}'", "Adding a colon ':' after the string", "Placing a dollar sign '$' before the string", "None of the above", "Prefixing the string with an 'f' or 'F'")
MCQ("How do you embed variables or expressions within an f-string?", r"By placing them inside curly braces '{}'", "By enclosing them in square brackets '[]'", "By using single quotation marks around them", "By separating them with commas", "None of the above", r"By placing them inside curly braces '{}'")
MCQ("Which of the following is a correct usage of f-strings?", r"f'Hello, {name}!'", r"'Hello, f{name}!'", "'Hello, {f name}!'", "'Hello, name!'", "None of the above", r"f'Hello, {name}!'")
MCQ("What happens if an invalid expression is used within an f-string?", "It raises a SyntaxError", "It ignores the expression and continues execution", "It converts the expression to a string", "It prompts the user for input", "None of the above", "It raises a SyntaxError")
MCQ("Which of the following is a valid way to format numbers within an f-string?", r"f'The price is {price:.2f}'", "f'The price is {price.2f}'", r"f'The price is {price}$'", r"f'The price is {price} dollars'", "None of the above", r"f'The price is {price:.2f}'")
MCQ("What does the '.2f' in an f-string represent?", "It formats a floating-point number to have 2 decimal places", "It converts the string to uppercase", "It removes leading and trailing whitespace", "It indicates the number of characters to pad the string with", "None of the above", "It formats a floating-point number to have 2 decimal places")
MCQ("Can f-strings be used to format non-string data types?", "Yes, they automatically convert other data types to strings", "No, f-strings only work with string data types", "Yes, but only if the data type is explicitly converted to a string", "No, f-strings can only contain string literals", "None of the above", "Yes, they automatically convert other data types to strings")

'> Raw Strings'
MCQ("What is the primary purpose of using raw strings in Python?", "To interpret backslashes as literal characters rather than escape characters","To convert strings to lowercase", "To convert strings to uppercase", "To split strings into substrings based on a delimiter", "To remove whitespace from the beginning and end of a string", "To interpret backslashes as literal characters rather than escape characters")
MCQ("Which symbol is used to denote a raw string in Python?", "Prefixing the string with an 'r' or 'R'", "Using curly braces '{}'", "Adding a colon ':' after the string", "Placing a dollar sign '$' before the string", "None of the above", "Prefixing the string with an 'r' or 'R'")
MCQ("How does Python handle escape sequences within raw strings?", "It treats them as literal characters", "It interprets them as special characters", "It ignores them completely", "It prompts the user for input", "None of the above", "It treats them as literal characters")
MCQ("Which of the following is a valid usage of raw strings in Python?", r"r'C:\Users\User'", r"'C:\Users\User'", r"'C:\Users\User'", r"'C:/Users/User'", r"None of the above", r"r'C:\Users\User'")
MCQ("What happens if a raw string contains an invalid escape sequence?", "It treats the backslash and following character as two separate characters", "It raises a SyntaxError", "It ignores the escape sequence and continues execution", "It prompts the user for input", "None of the above", "It treats the backslash and following character as two separate characters")

'> Bytes Strings'
MCQ("Which data type in Python is used to represent sequences of bytes?", "Bytes", "String", "Integer", "Float", "List", "Bytes")
MCQ("What is the primary difference between bytes strings and regular strings in Python?", "Bytes strings contain raw binary data, while regular strings contain Unicode text data", "Bytes strings are mutable, while regular strings are immutable", "Bytes strings can only contain ASCII characters, while regular strings can contain any Unicode character", "Bytes strings are not iterable, while regular strings are iterable", "None of the above", "Bytes strings contain raw binary data, while regular strings contain Unicode text data")
MCQ("Which function is used to convert a regular string to a bytes string in Python?", "encode()", "decode()", "to_bytes()", "from_bytes()", "convert()", "encode()")
MCQ("What is the b prefix used for in Python?", "To denote a bytes string literal", "To denote a regular string literal", "To denote a binary literal", "To denote a hexadecimal literal", "To denote a boolean literal", "To denote a bytes string literal")
MCQ("Which of the following methods is used to convert a bytes string to a regular string in Python?", "decode()", "encode()", "to_string()", "from_bytes()", "convert()", "decode()")