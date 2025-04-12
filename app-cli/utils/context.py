from pathlib import Path

if __name__ != "__main__":
    from utils.section import Chapter,Section

else:
    from section import Chapter, Section


version = "MCQ_Py v1.0.0 Alpha"

ROOT = Path(__file__).parent.parent
q_setpath = ROOT / "quiz" / "sets"

        
modules = {}


ch1 = Chapter("1 Comments Data Variables Operators")
ch1.add_section("1.1 Comments Input Output and Errors",11)
ch1.add_section("1.2 Syntax",12)
ch1.add_section("1.3 Data", 13)
ch1.add_section("1.4 Variables",14)
ch1.add_section("1.5 Operators", 15)
ch1.add_section("1.6 Simple Functions and Calls", 16)
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

ch3 = Chapter("3 Conditionals")
ch3.add_section("3.1 Boolean Expressions",31)
ch3.add_section("3.2 Conditionals",32)
modules[ch3.name]=ch3

ch4 = Chapter("4 Iteration")
ch4.add_section("4.1 While Loops",41)
ch4.add_section("4.2 For Loops",42)
ch4.add_section("4.3 Iterate 1D Collections",43)
ch4.add_section("4.4 Iterate 2D Collections",44)
ch4.add_section("4.5 Iterators",45)
ch4.add_section("4.6 Generators",46)
modules[ch4.name]=ch4

ch5 = Chapter("5 Functions")
ch5.add_section("5.1 Functions",51)
ch5.add_section("5.2 Recursion",52)
ch5.add_section("5.3 Decorators",53)
modules[ch5.name]=ch5



