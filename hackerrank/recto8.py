import sys

def main():
    # Leer el valor de N
    try:
        line = sys.stdin.readline()
        if not line:
            return
        n = int(line.strip())
    except (EOFError, ValueError):
        return

    phone_book = {}

    # Guardar los N contactos
    for _ in range(n):
        entry = sys.stdin.readline().split()
        if entry:
            phone_book[entry[0]] = entry[1]

    # Leer las consultas una a una hasta llegar al final (EOF)
    while True:
        query = sys.stdin.readline()
        if not query:
            break  # Se termina cuando ya no hay mas lineas
        
        query_name = query.strip()
        if query_name in phone_book:
            print(f"{query_name}={phone_book[query_name]}")
        else:
            print("Not found")

if __name__ == "__main__":
    main()