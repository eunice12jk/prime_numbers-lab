def primeNumbers(number):
    prime_number_list = []
    
    for i in range(2, number+1):
      prime = True
    
      for x in range(2,i):
        if i % x == 0:
          prime = False
        
      if prime == True:
            
        prime_number_list.append(i)
        
    return prime_number_list