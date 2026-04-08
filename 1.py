import statistics
import matplotlib.pyplot as plt
import sys

# ========== Функция статистического анализа ==========
def statistical_analysis():
    print("\nВведите числа через пробел:")
    user_input = input()

    try:
        numbers = list(map(float, user_input.split()))
        
        if len(numbers) < 2:
            print("Ошибка: нужно ввести минимум два числа.")
            return  

        mean = statistics.mean(numbers)
        median = statistics.median(numbers)
        minimum = min(numbers)
        maximum = max(numbers)
        stdev = statistics.stdev(numbers)

        print("\nРезультаты анализа:")
        print("Среднее значение:", mean)
        print("Медиана:", median)
        print("Минимум:", minimum)
        print("Максимум:", maximum)
        print("Стандартное отклонение:", stdev)

        sorted_numbers = sorted(numbers)
        print("Отсортированный список:", sorted_numbers)

        # Сохранение в файл (перезапись)
        with open("result.txt", "w", encoding="utf-8") as f:
            f.write("=== Статистический анализ ===\n")
            f.write(f"Среднее: {mean}\n")
            f.write(f"Медиана: {median}\n")
            f.write(f"Минимум: {minimum}\n")
            f.write(f"Максимум: {maximum}\n")
            f.write(f"Стандартное отклонение: {stdev}\n")
            f.write(f"Отсортированный список: {sorted_numbers}\n")

        # Построение гистограммы
        plt.hist(numbers)
        plt.title("Гистограмма распределения чисел")
        plt.xlabel("Значения")
        plt.ylabel("Частота")
        plt.grid(True)
        plt.show()
        
        print("Результаты сохранены в файл result.txt")

    except ValueError:
        print("Ошибка: введите только числа.")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")

# ========== Функция преобразования системы счисления ==========
def convert_base():
    print("\n=== Перевод систем счисления ===")
    print("Поддерживаются: 2 (двоичная), 10 (десятичная), 16 (шестнадцатеричная)")
    
    try:
        value = input("Введите число: ")
        from_base = int(input("Введите исходную систему (2/10/16): "))
        to_base = int(input("Введите целевую систему (2/10/16): "))
        
        # Сначала переводим в десятичную
        if from_base == 2:
            decimal_value = int(value, 2)
        elif from_base == 10:
            decimal_value = int(value)
        elif from_base == 16:
            decimal_value = int(value, 16)
        else:
            print("Ошибка: поддерживаются только 2, 10, 16")
            return
        
        # Из десятичной в целевую
        if to_base == 2:
            result = bin(decimal_value)[2:]
        elif to_base == 10:
            result = str(decimal_value)
        elif to_base == 16:
            result = hex(decimal_value)[2:].upper()
        else:
            print("Ошибка: целевая система должна быть 2, 10 или 16")
            return
        
        print(f"Результат: {result}")
        
        # Сохраняем результат в тот же файл result.txt (добавляем в конец)
        with open("result.txt", "a", encoding="utf-8") as f:
            f.write("\n=== Перевод систем счисления ===\n")
            f.write(f"Вход: {value} (система {from_base}) -> Выход: {result} (система {to_base})\n")
        print("Результат также добавлен в файл result.txt")
        
    except ValueError:
        print("Ошибка: неверный формат числа для указанной системы")
    except Exception as e:
        print(f"Ошибка: {e}")

# ========== Главное меню ==========
def main():
    while True:
        print("\n========== Меню ==========")
        print("1. Статистический анализ")
        print("2. Перевод систем счисления")
        print("3. Выход")
        choice = input("Выберите действие (1/2/3): ")
        
        if choice == "1":
            statistical_analysis()
        elif choice == "2":
            convert_base()
        elif choice == "3":
            print("До свидания!")
            break
        else:
            print("Неверный ввод, попробуйте снова.")

if __name__ == "__main__":
    main()
