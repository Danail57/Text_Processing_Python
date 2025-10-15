import re

pattern = r'#([a-zA-Z]+)'

message = input()
match = re.findall(pattern, message, re.IGNORECASE)
print(match)

INPUT
I'm learning #Python and #cyberSecurity in #SoftUni!
