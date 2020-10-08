def index_string_generator(array):
    res = ""
    for i in array:
        res += ":"+str(i)

    return res
def generator(current_index, range, array):
    i = 1
    list = []
    while current_index + range + i <= len(array):
        j = 0
        # l = array[current_index+i:current_index+range+i]
        l = []
        l.append(current_index)
        while current_index+i+j < current_index+range+i:
            l.append(current_index+i+j)
            j = j+1
        # l.insert(0, array[current_index])
        list.append(l)
        i = i +1

    return list
mapper = {}
array = [2, 3,6,7]
a = generator(0, 4, array)
# print(a)
i = 0
while i < len(array):
    mapper[index_string_generator([i])] = array[i]
    i = i + 1
i = 1
current_index = 0
result = []
while i < len(array):
    current_index = 0
    while current_index + i < len(array):
        print(i)
        generated_list = generator(current_index, i, array)
        for generated_item in generated_list:
            mapper[index_string_generator(generated_item)] = mapper[index_string_generator(generated_item[:len(generated_item) - 1])] + mapper[index_string_generator(generated_item[len(generated_item)-1:len(generated_item)])]
            if mapper[index_string_generator(generated_item)] == 9:
                result.append(generated_item)
        current_index = current_index + 1
    i = i + 1
print(result)