def generate_product_id(flavor_name, capacity):
    words = flavor_name.split()
    
    product_id = ''.join([word[:3].lower() for word in words])
    
    product_id += str(capacity)
    
    return product_id

flavor_name = input("Enter the flavor name: ")
capacity = input("Enter the capacity (in mL or L): ")

if capacity.isdigit():
    product_id = generate_product_id(flavor_name, int(capacity))
    print(f"Generated Product ID: {product_id}")
else:
    print("Invalid capacity input. Please enter a valid number.")
