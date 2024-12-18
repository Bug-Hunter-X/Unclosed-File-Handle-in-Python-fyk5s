def function_with_closed_file(filename):
    try:
        with open(filename, 'r') as f:
            # ... some code that processes the file ...
            contents = f.read()
            return contents  # File automatically closed by 'with' statement
    except FileNotFoundError:
        return None  # Handle file not found error