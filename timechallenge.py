# Write a small program to display information on the
# four clocks whose functions we have just looked at:
# i.e. time(), perf_counter, monotonic() and process_time().
#
# Use the documentation for the get_clock_info() function
# to work out how to call it for each of the clocks.

# used this link https://docs.python.org/3/library/time.html

import time

print(time.get_clock_info('time'))

print(time.get_clock_info('perf_counter'))

print(time.get_clock_info('monotonic'))

print(time.get_clock_info('process_time'))

# After the above, you can see that time() is adjustable where as others are not.



