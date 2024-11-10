import pdb
import logging

# Set up logging to display debug info in Jenkins console
logging.basicConfig(level=logging.DEBUG)

def test_function():
    x = 10
    y = 0
    logging.debug(f'Variables before division: x={x}, y={y}')
    pdb.set_trace()  # or just use logging without an interactive pdb prompt
    z = x / y
    print(z)

test_function()
