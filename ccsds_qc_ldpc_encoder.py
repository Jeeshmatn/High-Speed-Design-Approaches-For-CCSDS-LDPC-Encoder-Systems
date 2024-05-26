
info = [1,1,1,1,1,1,1,1]
print("info: \n",info)

gen = list('000001001111000000101111000000011111000010001111000011010001000011101000000001110100000010110010')
gen = [int(element) for element in gen if element.isdigit()]
gen = [gen[i:i+12] for i in range(0, len(gen), 12)]

print("\nGenMatrix:")
for row in gen:
  print(row)

M= 4
K = 2

out = [0]*(3*M)  #output length is 3*M = 12


# for i in range(2*M):
#     for j in range(3*M):
#         out[j] = out[j] ^ (info[i] and gen[i][j])
    


for i in range(K*M):            #input length is K*M = 8
    if info[i] == 1:
        for j in range(3*M):    #output length is 3*M = 12
            out[j] = out[j] ^ gen[i][j]



print("\nOutput:\n",out)
