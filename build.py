'''
Builds new populi file based on API reference found at Populi.
'''
import autopep8

from populi import build

output = build.imports

commands = build.get_commands()

for command in commands:
    output += "\n"
    output += str(command)
    output += "\n\n"

print(autopep8.fix_code(output, options={'aggressive': 2}))
