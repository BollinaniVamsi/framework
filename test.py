import pdb

def test_function():
    x = 10
    y = 0
    pdb.set_trace()  # Set breakpoint
    z = x / y
    print(z)

test_function()
