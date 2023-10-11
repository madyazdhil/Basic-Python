
def story():
    print(f"this is my story")

def main():
    print("Welcome to mystory")
    q = True
    while q != False:
        story()
        q = input("again?")
        if q == "tidak":
            print("thanks for playing")
            q = False

main()