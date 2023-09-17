import sys
new_path = "E:\\Programming\\Python\\repos\\pystudy\\mtasks\\mtask1"
sys.path.append(new_path)
print(sys.path)  # check if sys.path was updated
import module1  # try to import module from added dir in sys.path
print(module1.generate_question("Andrew"))  # try to use module's function
