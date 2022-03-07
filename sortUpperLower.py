InfyTQ Hands-ON
A string with Alphabets containing both uppercase and lower case is given. You shoud print the
string in ascending order as Upper case followed by lower case.
Eg:
INPUT:
hoLLywOoD
OUTPUT:
DhLLOoowy
INPUT:
AaZzxXtTBbBBb
OUTPUT:
AaBBBbbTtXxZz
'''

def arrange_string(string):
	string=sorted(string)
	string.sort(key=str.lower)
	return "".join(string)

string=input()
print(arrange_string(string))
