#Bài 2:
import math

for n in range(17, 112):
    if n > 1:
        la_so_nguyen_to = True

        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                la_so_nguyen_to = False
                break

        if la_so_nguyen_to:
            print(n, end=" ")