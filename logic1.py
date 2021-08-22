#logic

x = input()
transcript, variables = [], []
for c in x:
    if c.isalpha() and c!="v":
        transcript.append(c)
        variables.append(c)
    elif (c == "(") or (c == ")") or (c == " "):
        transcript.append(c)
    elif c == "^":
        transcript.append("and")
    elif c == "v":
        transcript.append("or")
    elif c == "=":
        transcript.append("==")
    elif c == "~":
        transcript.append("not")

transcript = "".join(transcript)
variables = list(set(variables))

f = open("operation.py", "w")
for n in range(len(variables)):
    f.write("\t"*n + "for {} in [True, False]:\n".format(variables[n]))
f.write("\t"*len(variables) + "print({})".format(transcript))

import operation