from ngym_template.wrappers.wrapper_template import YourWrapper

ALL_WRAPPERS = {'YourWrapper-v0': 'ngym_template.wrappers.wrapper_template:YourWrapper'}

def all_wrappers():
    return sorted(list(ALL_WRAPPERS.keys()))
