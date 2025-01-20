from pathlib import Path

if __name__ != "__main__":
    from utils.section import Chapter,Section

else:
    from section import Chapter, Section


version = "MCQ_Py v1.0.0 pre-Alpha"

ROOT = Path(__file__).parent.parent
q_setpath = ROOT / "quiz" / "q_sets"

        
modules = {}


ch1 = Chapter("1 Comments Data Variables Operators")
ch1.add_section("1.1 Comments Input Output and Errors",11)
ch1.add_section("1.2 Syntax",12)
ch1.add_section("1.3 Data", 13)
ch1.add_section("1.4 Variables",14)
ch1.add_section("1.5 Operators", 15)
ch1.add_section("1.6 Basic Function Calls", 16)
ch1.add_section("1.7 Strings",17)
ch1.add_section("builtins",18)
ch1.add_section("keywords",19)
modules[ch1.name]=ch1

ch2 = Chapter("2 Collections")
ch2.add_section("2.1 Lists" ,21)
ch2.add_section("2.2 Tuples" ,22)
ch2.add_section("2.3 Sets" ,23)
ch2.add_section("2.4 Dictionaries",24)
modules[ch2.name]=ch2

# ch3 = Chapter("3 Conditionals")



'''Testing'''
if __name__ == "__main__":

    for chapter, ch in modules.items():
        print(chapter)
        for section, sec in ch.sections.items():
            print("   * ", section)





# quiz_modules = {
#     "1 Comments Data Variables Operators" : 
    # {
    #     "1.1 Comments Input Output and Errors" : {"file" : "q_set11"},
    #     "1.2 Syntax" : {"file" : "q_set11" },
    #     "1.3 Data" : {"file" : "q_set11" },
    #     "1.4 Variables" : {"file" : "q_set11" },
    #     "1.5 Operators" : {"file" : "q_set11" },
    #     "1.6 Basic Function Calls" : {"file" : "q_set11" },
    #     "1.7 Strings" : {"file" : "q_set11" },
    #     "builtins" : {"file" : "q_set11" },
    #     "keywords" : {"file" : "q_set11" }
    # },
    # "2 Collections" : {
    #     "2.1 Lists" : {},
    #     "2.2 Tuples" : {},
    #     "2.3 Sets" : {},
    #     "2.4 Dictionaries" : {}
    # },
#     "3 Conditionals" : [
#         "3.1 Boolean Expressions",
#         "3.2 Conditionals"
#     ],
#     "4 Iteration" : [
#         "4.1 While Loops",
#         "4.2 For Loops",
#         "4.3 Iterate 1D Collections",
#         "4.4 Iterate 2D Collections",
#         "4.5 Iterators",
#         "4.6 Generators"
#     ],
#     "5 Functions" : [
#         "5.1 Functions",
#         "5.2 Recursion",
#         "5.3 Decorators"
#     ],
#     "6 Objects and Classes" : [
#         "6.1 Classes",
#         "6.2 Objects",
#         "6.3 Methods",
#         "6.4 Inheritance",
#         "6.5 Modules"
#     ],
#     "7 Advanced" : {
#         "Character Encoding" : [],
#         "Data Structures" : [],
#         "Exception Handling" : [],
#         "File Handling" : [],
#         "Importing Code" : [],
#         "Project Structure" : [],
#         "Regular Expressions" : [],
#     },
#     "8 Algorithms" : {
#         "Searching" : [],
#         "Sorting" : []
#     }



















# }


