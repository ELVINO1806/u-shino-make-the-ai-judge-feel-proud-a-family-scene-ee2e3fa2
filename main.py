import os

ENTRY = "Mum saved every drawing I ever made, even the bad ones. Last week she framed the worst one and hung it in the hallway. 'This one,' she said, 'is my favourite.'"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.writelines([ENTRY])

if __name__ == "__main__":
    main()
