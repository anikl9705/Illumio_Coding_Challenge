# Illumio_Coding_Challenge
`coding_challenge.py` has the firewall function. To test, i used `data` file (which contains firewall rules) and test file (which contains test queries). I also created a `generate_data.py` that randomly generates a number of firewall rules. I hand wrote the test cases for a particular generation of data to check the correctness of the solution.

# Design decisions
- I used a dictionary to query the port number quickly and stored the start and end ranges for IP addresses at each port in the dictionary. These are stored using two arrays. The lists are sorted once all queries are read. This way, I can query the IP address ranges allowed in a particular port efficiently.

- Given more time, I could have merged ranges of IP addresses for increased efficiency.

- I initially thought of doing the other way around (querying IP address quickly by storing them in dictionary), but the no of combinations of IP addresses are much larger, thereby making that train of thought infeasible. 
