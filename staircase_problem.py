def main(n):
    if n <= 1:
        return 1
    
    return main(n - 1) + main(n - 2)

print(main(8))