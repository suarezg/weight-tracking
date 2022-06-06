
# File paths
# todo save constants in a config file or something and import
AUTOGEN_MD_PATH = "autogen.md"
MANUAL_MD_PATH = "manual.md"
OUT_PATH = "README.md"

# Open files
readme = open(OUT_PATH, "w+")
manual = open(MANUAL_MD_PATH, "r")
autogen = open(AUTOGEN_MD_PATH, "r")


# write contents of MANUAL_MD_PATH and AUTOGEN_MD_PATH to OUT_PATH
for _, line in enumerate(manual):
    readme.write(line)

for _, line in enumerate(autogen):
    readme.write(line)

# close files
readme.close()
manual.close()
autogen.close()


