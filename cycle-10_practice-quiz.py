# Charlie CCG 1/27/22


# Question 1
def food_costs(groceries,costs):
    groceries_mod = groceries
    for index, value in enumerate(groceries):
        for i, v in enumerate(value):
            groceries[index][i] += ': $' + str(costs[3 * index + i])
        
    return groceries_mod

print(food_costs([['apple','pear','banana',],['salmon','tuna','cod',],['milk','eggs','yogurt',]],[1.99,2.99,0.99,9.99,10.99,6.99,3.49,2.49,1.49]))
print(food_costs([['apple','pear','banana'],['salmon','tuna','cod'],['milk','eggs','yogurt']],[1.99,2.99,0.99,9.99,10.99,6.99,3.49,2.49,1.49]) == [['apple: $1.99','pear: $2.99','banana: $0.99'],['salmon: $9.99','tuna: $10.99','cod:$6.99'],['milk: $3.49','eggs: $2.49','yogurt: $1.49']])

# Question 2
def factorial(numb):
    end = 1
    for index in range(1, numb + 1):
        end *= index
    return end
print(factorial(5))

# Question 3
def fib_nums(numb):
    lst = [0,1]
    if numb == 1 or numb == 2:
        return lst[0:numb]
    else:
        for x in range(numb - 2):
            lst.append(lst[x] + lst[(len(lst) - 1)])
    return lst

print(fib_nums(5) == [0,1,1,2,3], fib_nums(10) == [0,1,1,2,3,5,8,13,21,34])
