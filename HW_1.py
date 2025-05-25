import queue


request_queue = queue.Queue()
request_id = 1


def generate_request():
    global request_id
    request = f"Заявка №{request_id}"
    request_queue.put(request)
    print(f"Додано {request}")
    request_id += 1


def process_request():
    if not request_queue.empty():
        request = request_queue.get()
        print(f"Завершено {request}")
    else:
        print("[!] Черга пуста")

def main():
    while True:
        print("\nМеню:")
        print("1. Створити нову заявку")
        print("2. Обробити заявку")
        print("3. Вийти")
        choice = input("Виберіть дію: ")

        if choice == '1':
            generate_request()
        elif choice == '2':
            process_request()
        elif choice == '3':
            print("Вихід")
            break
        else:
            print("Невірна дія, спробуйте ще раз.")

if __name__ == "__main__":
    main()