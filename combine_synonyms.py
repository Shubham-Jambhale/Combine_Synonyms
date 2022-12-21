def get_combined_list ( syn_list ) :
    i = 0
    while i < len(syn_list):
        flag = False
        list1 = syn_list[i]
        for j in range(i+1,len(syn_list)):
            list2 = syn_list[j]
            abc = set(list1).intersection(set(list2))
            if abc:
                flag = True
                for k in range(len(list2)):
                    if list2[k] not in syn_list[i]:
                        syn_list[i].append(list2[k])
                syn_list.pop(j)
                break
        if flag:
            i = 0
        else:
            i+= 1       
    return syn_list