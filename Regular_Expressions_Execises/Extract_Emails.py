import re

sentence = input()
pattern = r"\b[a-z0-9._-]+@[a-z-]+(\.[a-z]+)+\b"
matches = re.finditer(pattern, sentence)

for match in matches:
    print(match.group())


INPUT
Please contact us at: support@github.com.
Just send email to s.miller@mit.edu and j.hopking@york.ac.uk for more information.
Many users @ SoftUni confuse email addresses. We @ Softuni.BG provide high-quality training @ home or @ class.–- steve.parker@softuni.de.
