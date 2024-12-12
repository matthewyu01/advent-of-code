with open('input.txt', 'r') as f:
    LINES = [line[:-1] for line in f.readlines()]
with open('test1.txt', 'r') as f:
    test1 = [line[:-1] for line in f.readlines()]

from collections import defaultdict
import subprocess


def is_safe(nums):
    inc = True
    n0, n1 = nums[0], nums[1]
    if n1 > n0:
        inc = True
    else:
        inc = False
    for n1, n2 in zip(nums[:-1], nums[1:]):
        if inc:
            if 1 <= n2 - n1 <= 3:
                pass
            else:
                break
        else:
            if 1 <= n1 - n2 <= 3:
                pass
            else:
                break
    else:
        return True

    return False


def part1(lines=LINES):
    i = 0
    count = 0

    while i < len(lines):
        line = lines[i]
        splt = line.split()
        # left, right = line.split()
        count += 0

        nums = [int(n) for n in splt]
        if is_safe(nums):
            count += 1


        i += 1

    return count

def part2(lines=LINES):
    i = 0
    count = 0

    while i < len(lines):
        line = lines[i]
        splt = line.split()
        # left, right = line.split()

        nums = [int(n) for n in splt]
        inc = True
        n0, n1 = nums[0], nums[1]
        if n1 > n0:
            inc = True
        else:
            inc = False
        if is_safe(nums[1:]):
            count += 1
        else:

            for j in range(len(nums)-1):
                n1 = nums[j]
                n2 = nums[j+1]
                if inc:
                    if 1 <= n2 - n1 <= 3:
                        pass
                    else:
                        l1 = nums[:j] + nums[j+1:]
                        l2 = nums[:j+1] + nums[j+2:]
                        if is_safe(l1) or is_safe(l2):
                            count += 1
                        break

                else:
                    if 1 <= n1 - n2 <= 3:
                        pass
                    else:
                        l1 = nums[:j] + nums[j+1:]
                        l2 = nums[:j+1] + nums[j+2:]
                        if is_safe(l1) or is_safe(l2):
                            count += 1
                        break
            else:
                count += 1

        i += 1

    return count

print(f'Part 1 Test Output: {part1(test1)}')
p1_actual = part1(LINES)
subprocess.run("clip", text=True, input=str(p1_actual))
print(f'Part 1 ACTUAL: {p1_actual}   COPIED!')

print(f'Part 2 Test Output: {part2(test1)}')
p2_actual = part2(LINES)
subprocess.run("clip", text=True, input=str(p2_actual))
print(f'Part 2 ACTUAL: {p2_actual}   COPIED!')
