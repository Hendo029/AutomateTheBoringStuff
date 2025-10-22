import re

message = 'Agent Joris and Agent Hendriksen'

namesRegex = re.compile(r'Agent (.*)')
names2Regex = re.compile(r'Agent (\w)\w+')
print(namesRegex.findall( message))
print(names2Regex.sub(r'Agent \1', message))



