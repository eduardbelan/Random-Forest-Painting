import colorgram


COLOR_LIST = []


def color_extractor(number_of_colors):
    """
    Extracts set number of colors from a given image
    and puts the rgb-tuples into a list.
    """

    # set counter
    number = 0

    # choose image file for color extraction, set path if needed, file name only if image in root directory
    all_colors = colorgram.extract("image.jpg", number_of_colors)

    # extract rgb values and convert them into a tuple
    for _ in range(number_of_colors):
        single_color = all_colors[number]
        color_tuple = (single_color.rgb.r, single_color.rgb.g, single_color.rgb.b)
        COLOR_LIST.append(color_tuple)
        number += 1

    # prepare the data for export
    data = f"color_list = {COLOR_LIST}\n"

    # create a new file and add the extracted color data
    filename = "colors-extracted.py"
    with open(filename, "a") as file:
        file.write(data)


color_extractor(number_of_colors=30)
