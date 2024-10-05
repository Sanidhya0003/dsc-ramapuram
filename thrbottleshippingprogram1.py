def carton_breakup(bottles):

    carton_sizes = {
        "xl": 48,
        "large": 24,
        "medium": 12,
        "small": 6
    }
    
    
    result = {}
    
   
    for carton, capacity in carton_sizes.items():
        if bottles >= capacity:
            count = bottles // capacity
            result[carton] = count
            bottles = bottles % capacity
    
   


   
    for carton in result:
        print(f"{result[carton]} {carton}")
    
# Example usage
carton_breakup(140)
