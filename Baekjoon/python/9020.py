import sys, math

sys.stdin = open('input.txt', 'r')

var = list(map(int, sys.stdin.read().splitlines()))

for i in range(1, len(var)) :
    testcase = var[i]
    # prime_num = []
    # partition_list = []
    # diff_partition = []

    #입력값보다 작은 소수 list 생성
    #입력받은 testcase보다 작은 자연수 중 소수 판별

    # for num in range(2, testcase) :
    #     for devi_num in range(2, int(math.sqrt(num))+1) : # num = 2에서 for loop 수행되지 않음
            
    #         if num % devi_num == 0 :
    #             break

    #     else :
    #         prime_num.append(num)

    ####1
    # for each_prime_num in prime_num :

    #     target = testcase - each_prime_num

    #     if target > 1 :

    #         for target_num in range(2, target) :
            
    #             if target % target_num == 0 :
    #                 break

    #         else :
    #             partition_list.append([each_prime_num, target])

    ###2
    # for each_prime_num1 in prime_num :

    #     target = testcase - each_prime_num1

    #     for each_prime_num2 in prime_num :

    #         if target == each_prime_num2 :

    #             partition = [each_prime_num1, each_prime_num2]
    #             partition_list.append(partition)

    ####3
    # for i in range(len(prime_num)) :

    #     target = testcase - prime_num[i]

    #     for j in range(len(prime_num)) :

    #         if target == prime_num[j] :
    #             partition = [prime_num[i], prime_num[j]]
    #             partition_list.append(partition)


    # for each_partition in partition_list :

    #     diff_partition.append(each_partition[1] - each_partition[0])

    # diff_partition_val = sorted(diff_partition, key=abs)[0]
    
    # target_partition_index = diff_partition.index(diff_partition_val)

    # print(*partition_list[target_partition_index])

    def is_prime (temp) :
        for k in range(2, int(math.sqrt(temp))+1) :
            if temp % k == 0 :
                return False

        else :
            return True

    num1 = testcase // 2
    num2 = testcase // 2

    while num1 > 0 :

        if is_prime (num1) and is_prime (num2) :
            print(num1, num2)
            break

        else :
            num1 = num1 - 1
            num2 = num2 + 1