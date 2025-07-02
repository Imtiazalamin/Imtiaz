# akti function nilam jar modde 2 ti peramitar diachi
def twoSum(nums, target):
    num_map = {}  # index, value gulo ke rakha hobe

    for i, num in enumerate(nums):
    # enumerate mane hocche for er por duita variable neoa holo i er modde index num er modde value thakbe
         diff = target - num  # ekhane biyog korar por jodi target na pai tahole oi shongkha ta num_map a store korbe

         if diff in num_map:  # terget er sthe jeta biyog korbe oita ache ki na janar jonno ai line liklam

              return [num_map[diff], i]  # ager shongkhar r porer shonga milaiya jog korle jodi  uttor paoa jai tahole agulor index print korbe

         num_map[num] = i  # bortoman er number ta ke num_map a store korar jonno banano

    return () #

nam = [2, 7, 11, 15]
Target = 9

result = twoSum(nam, Target)
print(result)

# example 2
def two_sum(i_number, needed_number):
    nam_map = {}
    for index_n, value_n in enumerate(i_number): # enumerat deoar mane holo duitai hoiya gesche index ver hoiche value o str hoiche
        find_number_6 = needed_number - value_n # akhane shob biyog korbo r dekbo je target pai ki na hoi ki na
        if find_number_6 in  nam_map:
            return [nam_map[find_number_6], index_n]
        nam_map[value_n] = index_n # index number ke mone rakhte boltesi jeta  diya first

    # jodi na pao terget tahole retur koiro khali perentheses
    return()
number = [3,2,4]
target = 6
final = two_sum(number, target)
print(final)

# example 3
def TWO_SUM(number, aim):
    num_map = {}

    for A, V in enumerate(number):
        substraction =aim - V
        if substraction in num_map:
            return  [num_map[substraction], A]
        num_map[V] = A

    return()


nums = [3,3]
target = 6
final_result = TWO_SUM(nums, target)
print(final_result)

