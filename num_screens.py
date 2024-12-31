def generate_digit_templates():
    """
    Returns a dictionary containing string representations of digits 0-9.
    Each digit is represented in a 9x15 grid.
    """
    digit_templates = {
        "0": [
            "   #####   ",
            "  ##   ##  ",
            " ##     ## ",
            " ##     ## ",
            " ##     ## ",
            " ##     ## ",
            " ##     ## ",
            " ##     ## ",
            " ##     ## ",
            " ##     ## ",
            " ##     ## ",
            " ##     ## ",
            "  ##   ##  ",
            "   #####   ",
            "           ",
        ],
        "1": [
            "     ##    ",
            "    ###    ",
            "   ####    ",
            "     ##    ",
            "     ##    ",
            "     ##    ",
            "     ##    ",
            "     ##    ",
            "     ##    ",
            "     ##    ",
            "     ##    ",
            "     ##    ",
            "     ##    ",
            "   ######  ",
            "           ",
        ],
        "2": [
            "   #####   ",
            "  ##   ##  ",
            " ##     ## ",
            " ##     ## ",
            "        ## ",
            "        ## ",
            "       ##  ",
            "      ##   ",
            "     ##    ",
            "    ##     ",
            "   ##      ",
            "  ##       ",
            " ##        ",
            " ######### ",
            "           ",
        ],
        "3": [
            "   #####   ",
            "  ##   ##  ",
            " ##     ## ",
            "        ## ",
            "       ##  ",
            "     ##    ",
            "  ####     ",
            "     ##    ",
            "       ##  ",
            "        ## ",
            "        ## ",
            " ##     ## ",
            "  ##   ##  ",
            "   #####   ",
            "           ",
        ],
        "4": [
            "        #  ",
            "       ##  ",
            "      ###  ",
            "     ####  ",
            "    ## ##  ",
            "   ##  ##  ",
            "  ##   ##  ",
            " ##    ##  ",
            "###########",
            "       ##  ",
            "       ##  ",
            "       ##  ",
            "       ##  ",
            "      #### ",
            "           ",
        ],
        "5": [
            " ######### ",
            " ##        ",
            " ##        ",
            " ##        ",
            " ##        ",
            "   ##      ",
            "    ####   ",
            "       ##  ",
            "        ## ",
            "         ##",
            " ##      ##",
            " ##      ##",
            "  ##    ## ",
            "   #####   ",
            "           ",
        ],
        "6": [
            "   #####   ",
            "  ##   ##  ",
            " ##     ## ",
            " ##      ##",
            " ##        ",
            " ##        ",
            " ## #####  ",
            " ###    ## ",
            " ##      ##",
            " ##      ##",
            " ##      ##",
            " ##      ##",
            "  ##    ## ",
            "   #####   ",
            "           ",
        ],
        "7": [
            "###########",
            "        ## ",
            "        ## ",
            "       ##  ",
            "       ##  ",
            "      ##   ",
            "      ##   ",
            "   ######  ",
            "     ##    ",
            "    ##     ",
            "    ##     ",
            "   ##      ",
            "   ##      ",
            " #####     ",
            "           ",
        ],
        "8": [
            "   #####   ",
            "  ##   ##  ",
            " ##     ## ",
            " ##     ## ",
            " ##     ## ",
            "  ##   ##  ",
            "   #####   ",
            "  ##   ##  ",
            " ##     ## ",
            " ##     ## ",
            " ##     ## ",
            " ##     ## ",
            "  ##   ##  ",
            "   #####   ",
            "           ",
        ],
        "9": [
            "   #####   ",
            " ##    ##  ",
            "##      ## ",
            "##      ## ",
            "##      ## ",
            "##      ## ",
            " ##    ### ",
            "  ##### ## ",
            "        ## ",
            "        ## ",
            "##      ## ",
            " ##     ## ",
            "  ##   ##  ",
            "   #####   ",
            "           ",
        ],
        "B": [
            " #######   ",
            " ##    ##  ",
            " ##     ## ",
            " ##     ## ",
            " ##     ## ",
            " ##    ##  ",
            " #######   ",
            " ##    ##  ",
            " ##     ## ",
            " ##     ## ",
            " ##     ## ",
            " ##     ## ",
            " ##    ##  ",
            " #######   ",
            "           ",
        ],
        # Add more templates for 3-9
    }
    return digit_templates

def render_number(number):
    """
    Render a number or alphabet using the digit templates and display it in a 9x15 grid format.

    Args:
        number (str): The string to render (0-999 or supported alphabets).
    """
    templates = generate_digit_templates()
    number_str = f"{number:>4}"
    
    # Initialize the output lines
    output_lines = ["" for _ in range(15)]

    # Render each digit and combine into output_lines
    for digit in number_str:
        if digit in templates:
            digit_template = templates[digit]
            for i, line in enumerate(digit_template):
                output_lines[i] += line + " "

    # Print the final output
    for line in output_lines:
        print(line)