import os

def generate_files():
    x = 1
    y_range = range(1, 12)  # 1から11まで
    z_range = ['A', 'B', 'C', 'D']
    
    for y in y_range:
        for z in z_range:
            filename = f"ALDS{x}_{y}_{z}.py"
            with open(filename, 'w') as f:
                f.write(f"# This is {filename}")
            print(f"Created: {filename}")

if __name__ == "__main__":
    generate_files()