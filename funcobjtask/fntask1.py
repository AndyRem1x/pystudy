def func(arg1, arg2, arg3, *args, arg4=5, **argsdict):
    test_var_1 = 100
    test_var_2 = "Test variable"
    test_var_3 = 500
    test_var_4 = "Some text"
    test_var_5 = 1
    return len(locals()) - len([var for var in locals() if var.startswith("arg")])  # excluding the arguments of function


print(func(33, 44, 55, 66, 77, arg5=6, arg6=7))  # passing some args to function
