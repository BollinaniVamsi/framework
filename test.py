import pdb

def test_function():
    x = 10
    y = 0

    # Start pdb
    pdb.set_trace()
    
    # Add pdb commands to step through the code
    pdb.run('z = x / y')  # This will break and catch the error

test_function()
