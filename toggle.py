print("Note: In 1.1.0, Bopimo will switch to OpenGL.")
path = input("Path to Bopimo (Client): ")
print("Toggling OpenGL in " + path)
input("Is that okay?")
f = open(path + "\override.cfg", "x")
print("Created override.cfg")
f.write("""[rendering]
renderer/rendering_method="gl_compatibility"""")
print("Toggled OpenGL")
print("OpenGL should be enabled!")
