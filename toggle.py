print("Note: In 1.1.0, Bopimo will switch to OpenGL.")
path = input("Path to Bopimo (Client): ")
f = open(path + "override.cfg", "x")
f.write("""[rendering]\n
renderer/rendering_method="gl_compatibility""")
print("OpenGL should be enabled!")
