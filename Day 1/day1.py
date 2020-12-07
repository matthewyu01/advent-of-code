def main():
    nums = []
    with open('input.txt', 'r') as f:
        nums = [int(line) for line in f.readlines()]

    num_map = {}

    for num0 in nums:
        num_map[num0] = "1"
        if num_map.get(2020-num0):
            print(num0 * (2020 - num0))
            break

    for num1 in nums:
        for num2 in nums:
            if num_map.get(2020 - num1 - num2):
                print(num1 * num2 * (2020 - num1 - num2))
                return

                
if __name__ == "__main__":
    main()