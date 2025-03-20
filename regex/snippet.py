import re

first = re.findall(r'c.t', 'cat cut c9t ctx')
print(first) # ['cat', 'cut', 'ctx']

second = re.findall(r' ab*', 'a ab abb abbb abc')
print(second) # [' ab', ' abb', ' abbb']

third = re.findall(r'ab+', 'a ab abb abbb abc')
print(third) # ['ab', 'abb', 'abbb']

fourth = re.findall(r'colou?r', 'color colour colouur')
print(fourth) # ['color', 'colour']

fifth = re.findall(r'a{3}', 'aa aaa aaaa aaaaa')
print(fifth) # ['aaa', 'aaa', 'aaa']

sixth = re.findall(r'a{2,4}', 'aa aaa aaaa aaaaa')
print(sixth) # ['aa', 'aaa', 'aaaa', 'aaaa']

seventh = re.findall(r'^Hello', 'Hello world\nWorld Hello', re.MULTILINE)
print(seventh) # ['Hello']

eighth = re.findall(r'worlds$', 'Hello world\nWorld Hello', re.MULTILINE)
print(eighth) # []

ninth = re.findall(r'[aeiou]', 'Hello world')
print(ninth) # ['e', 'o', 'o']

tenth = re.findall(r'[^aeiou]', 'Hello world')
print(tenth) # ['H', 'l', 'l', ' ', 'w', 'r', 'l', 'd']

eleventh = re.findall(r'\d+', 'abc123xyz')
print(eleventh) # ['123']

twelfth = re.findall(r'\D+', 'abc123xyz')
print(twelfth) # ['abc', 'xyz']

thirteenth = re.findall(r'\s+', 'Hello world')
print(thirteenth) # [' ']

fourthteenth = re.findall(r'\S+', 'Hello world')
print(fourthteenth) # ['Hello', 'world']

fifteenth = re.findall(r'\w+', 'Hello world_123')
print(fifteenth) # ['Hello', 'world_123']

sixteenth = re.findall(r'\W+', 'Hello, world!')
print(sixteenth) # [', ' ', '!']

seventeenth = re.findall(r'hello', 'Hello world', re.IGNORECASE)
print(seventeenth) # ['Hello']

eighteenth = re.findall(r'a.b', 'a\nb', re.DOTALL)
print(eighteenth) # ['a\nb']

nineteenth = re.match(r'Hello', 'Hello world')
print(nineteenth) # <re.Match object; span=(0, 5), match='Hello'>

twentieth = re.fullmatch(r'Hello world', 'Hello world')
print(twentieth) # <re.Match object; span=(0, 11), match='Hello world'>

twenty_first = re.search(r'\d+', 'There are 3 apples and 5 oranges')
print(twenty_first) # <re.Match object; span=(10, 11), match='3'>

twenty_second = re.sub(r'dog', 'cat', 'the dog is barking.')
print(twenty_second) # the cat is barking.

twenty_third = re.sub(r', ', ',\n', 'apple, banana, orange')
print(twenty_third) # apple,\nbanana,\norange