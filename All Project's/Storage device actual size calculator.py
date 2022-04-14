                            #Storage device actual size calculator

inp_in_GB       = int(input("Enter the size of your SSD/HDD in Gigabyte: "))
conv_to_TB      = inp_in_GB*1000000000
actual_size = conv_to_TB/1024/1024/1024
print(actual_size)
