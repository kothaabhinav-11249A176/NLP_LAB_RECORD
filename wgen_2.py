
forms = {
    ("write", "VBD"): "wrote",
    ("write", "VBN"): "written",
    ("stop", "VBG"): "stopping",
    ("study", "VBZ"): "studies",
    ("die", "VBG"): "dying",
    ("play", "VBD"): "played"
}

# (a) Generate verb forms
for key, value in forms.items():
    print(key[0], key[1], "->", value)

# (b) Orthographic rules
print("stop -> stopping: double consonant")
print("study -> studies: y changes to ies")
print("die -> dying: ie changes to ying")

# (c) Irregular forms
print("Check irregular dictionary first, then apply rules.")