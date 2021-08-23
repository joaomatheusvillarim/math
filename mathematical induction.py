#principio da induçao finita

x, transcript = input(), []
if "soma_pa" in x:
    x = x.replace("soma_pa", "progressoes.soma_pa")
elif "soma_pg" in x:
    x = x.replace("soma_pg", "progressoes.soma_pg")
for c in x:
    if c == "=":
        transcript.append("==")
    else:
        transcript.append(c)
transcript = "".join(transcript)

f = open("operation2.py", "w")
f.write("import progressoes\nn=1\n")
f.write("x = {}\n".format(transcript))

sub = transcript.split("==")
transcript = "{} - ({}) == {} - ({})".format(sub[0].replace("n", "(n+1)"), sub[0], sub[1].replace("n", "(n+1)"), sub[1])
f = open("operation2.py", 'a')
f.write("y = {}\n".format(transcript))
f.write("print(x and y)")