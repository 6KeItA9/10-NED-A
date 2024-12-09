#Taisnstūra izvadīšana
platums = 10 #zvaigznīšu skaits rindā
augstums = 5 #rindu skaits
for i in range (augstums):
    print ('*' * platums)

#Kvadrāta izvadīšana
malas_garums = 5 #zvaigznīšu skaits gan rindā, gan kolonā
for i in range (malas_garums):
    print ('*' * malas_garums)
    
    #Piramīdas izvadīšana
augstums = 5 #piramīdas augstums
for i in range (1, augstums + 1):
    atstarpes = '' * (augstums - i)
    zvaigznes = '*' * (2 * i - 1)
    print (atstarpes + zvaigznes)