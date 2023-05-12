#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    all_names = dir(hidden_4)
    all_names.sort()
    for i in all_names:
        if i[:2] != '__':
            print(i)
