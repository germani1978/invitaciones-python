with open('./name/name.txt') as file:
    list_name = file.readlines()
    
for name in list_name:
    name_strip = name.strip()
    with open('./carta/carta.txt') as carta_file:
        carta = carta_file.read()
        carta_new = carta.replace('[name]', name_strip)
        with open(f'./out/{name_strip}.txt','w') as f_out:
            f_out.write(carta_new)
    


