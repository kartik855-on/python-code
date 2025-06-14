def main():
    try:
        a=int(input("enter a number:"))
        print(a)
        return

    except Exception as e:
        print(e)
        return
    finally:
        print("else is inside")

main()