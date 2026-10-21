from product_manager import add_product

while True:
    num = input("1, 2, 3, 4 = exit, 5 = test: ")

    match num:
        case "1":
            print("1")

        case "2":
            print("2")

        case "3":
            print("3")

        case "4":
            print("Exit")
            break

        case "5":

            add_product()

        case _:
            print("กรุณาเลือก 1-5")