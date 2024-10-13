#TallyTraker
inventory = []
amount = []
unit_list = []
input_list = []
stop_go = 'go'
while stop_go != 'stop':
    item = str(input('\nName of Item:'))
    number = 0
    unit = 'none'
    if item.lower() != 'delete' and item.lower() != 'stop':
        number = float(input('Amount of Item:'))
    def Tally_Tracker(item,number,unit):
        found = False
        num_found = False
        index_num = 0
        if item.lower() !='delete'and item != 'stop':
            input_list.append(item)
            input_list.append(number)
            for i in range(len(input_list)):
                for j in range(len(inventory)):
                    if inventory[j] == input_list[i] and i % 2 == 0:    #finds the input item in the inventory list
                        found = True 
                        index_num = j
                        break
                    if found and i % 2 != 0:                            #adds the input amount with the current amount
                        found = False
                        num_found = True
                        new_amount = amount[index_num] + input_list[i]
                        amount.remove(amount[index_num])
                        amount.insert(index_num,new_amount)
                if not found and not num_found and i % 2 ==0:            #adds new input items to the list
                    unit = str(input('Unit of Measure:'))
                    input_list.append(unit)
                    for i in range(len(input_list)):
                        if i == 0:
                            inventory.append(input_list[i])
                        elif i == 1:
                            amount.append(input_list[i])
                        elif i == 2 and unit != 'none':
                            unit_list.append(input_list[i])
                            break
                num_found = False
            input_list.clear()
        if item.lower() == 'delete':                                    #finds item to delete form list 
            delete_item = str(input('Item to Delete:'))
            input_list.append(delete_item)
            for i in range(len(input_list)):
                for j in range(len(inventory)):
                    if inventory[j] == input_list[i]:                   #finds the input item in the inventory list to delete
                        found = True 
                        index_num = j
                    if found:
                        amount.remove(amount[index_num])
                        inventory.remove(input_list[i])
                        unit_list.remove(unit_list[index_num])
                        break
                if not found:
                    print('Item not Found')
            input_list.clear()
        def inventory_display(inventory,amount,unit_list):                        #prints inventory list
            print('\nInventory List')
            for i in range(len(inventory)):
                print(f'{inventory[i]}: {amount[i]} {unit_list[i]}')
                
        return inventory_display(inventory,amount,unit_list)
    if item == 'stop':
        break
    

    x = Tally_Tracker(item,number,unit)
    
x = Tally_Tracker(item,number,unit)