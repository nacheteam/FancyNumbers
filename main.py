import pythagorean_triple as pt

print("Which program do you wanna run? [Pythagoric Triple (pt)]")
choice = input()

if choice=="pt":
    print("Running Pythagoras Triples check program, tell me the limit")
    limit = int(input())
    pt.discoverPythagorasTriples(limit)
else:
    print("There isn't such option")
