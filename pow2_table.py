# Файл: pow2_table.py
# Автор: Юсупалиева А.Х.
# Назначение: Генератор таблицы степеней двойки

def main():
    print("\n--- Генератор таблицы степеней двойки ---")
    
    try:
        n = int(input("Введите степень N (целое неотрицательное число): "))
        if n < 0:
            print("Ошибка: введите неотрицательное число.")
            return
        
        print(f"\nТаблица степеней двойки от 0 до {n}:")
        print("Степень\tDEC\tBIN\t\tHEX")
        print("-" * 40)
        
        for power in range(n + 1):
            value = 2 ** power
            print(f"{power}\t{value}\t{bin(value)}\t{hex(value)}")
            
    except ValueError:
        print("Ошибка: введите целое число.")

if __name__ == "__main__":
    main()