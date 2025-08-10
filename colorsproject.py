import random

def generate_random_color():
    """Generate a random color in hex format."""
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

def generate_color_palette(num_colors):
    """Generate a list of random color hex codes."""
    return [generate_random_color() for _ in range(num_colors)]

def display_palette(palette):
    """Display the color palette."""
    print("Random Color Palette:")
    for color in palette:
        print(color)

def show_colors(n):
    """Display 'n' random colors with their hex codes."""
    print("\nRandom Color Palette:")
    for _ in range(n):
        hex_color = generate_random_color()
        r = int(hex_color[1:3], 16)
        g = int(hex_color[3:5], 16)
        b = int(hex_color[5:7], 16)
        
        # Print colored block and hex code
        print(f"\033[48;2;{r};{g};{b}m      \033[0m  {hex_color}")

def main():
    num_colors = int(input("Enter the number of colors in the palette: "))
    color_palette = generate_color_palette(num_colors)
    display_palette(color_palette)
    
    # Show colors with blocks
    show_colors(num_colors)

if __name__ == "__main__":
    main()
