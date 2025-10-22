import re

while True:
# get and make string
    print('Paste your string here, end with character in between < > to say what to remove. Do not use spaces before <...>: ')
    strip = str(input('>>>'))

    # Check for extra argument
    stripCharRegex = re.compile(r'<(.+)>')
    mo = stripCharRegex.findall(strip)
    if mo == None:
        stripChar = ' '
    else:
        stripChar = mo[0]
        strip = stripCharRegex.sub('', strip)

    # Regex for finding beginning and ending characters
    startRegex = re.compile(r'^(\%s*)\b' %stripChar)
    endRegex = re.compile(r'\b(\%s*)$' %stripChar)
    newStrip = startRegex.sub('', strip)
    newStrip = endRegex.sub('', newStrip)

    print(newStrip)
    break


