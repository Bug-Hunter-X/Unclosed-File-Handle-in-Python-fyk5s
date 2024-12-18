def function_with_unclosed_file(filename):
    f = open(filename, 'r')
    # ... some code that processes the file ... 
    # Missing f.close() or using with statement
    return  # File remains open, leading to resource leaks