list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
direction = input("Would you like to encode or decode a text ")
text = input("Please enter the text ")
shift = int(input("Enter the number for shift "))

def caesar_cipher(text_start,shift_amount,direction):
    updated_text = ""
    if(direction == "decode"):
            shift_amount *= -1
    for i in range(len(text_start)):
        position = list.index(text[i])
        
        new_position = position+shift_amount
        updated_text += list[new_position]
    print(updated_text)
    
caesar_cipher(text_start=text,shift_amount=shift,direction = direction)

