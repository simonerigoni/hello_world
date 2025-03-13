# Hello World docker from the current OS and architecture
#
# python docker_hello_world.py


import platform


if __name__ == '__main__':
    os_name = platform.system()
    architecture = platform.architecture()

    print(f"Hello Wordl! from {os_name} operating system on {architecture[0]} {architecture[1]} architecture")
else:
    pass