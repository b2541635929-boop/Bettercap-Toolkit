def print_key_values(items):
    width = max((len(str(k)) for k, _ in items), default=0)
    for key, value in items:
        print(f"{str(key):<{width}} : {value}")
