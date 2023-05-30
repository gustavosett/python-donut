import math

angle_one, angle_two = 0, 0
ansi_clear_screen = "\x1b[2J"
print(ansi_clear_screen, end='')

while True:
    screen_depth = [0] * 1760
    screen_pixels = [' '] * 1760

    for rotate_y in range(0, 628, 7):
        for rotate_x in range(0, 628, 2):
            sin_x = math.sin(rotate_x)
            cos_y = math.cos(rotate_y)

            sin_angle_one = math.sin(angle_one)
            sin_rotate_y = math.sin(rotate_y)
            cos_angle_one = math.cos(angle_one)

            rotation_distance = cos_y + 2
            screen_projection_ratio = 1 / (sin_x * rotation_distance * sin_angle_one + sin_rotate_y * cos_angle_one + 5)

            cos_rotate_x = math.cos(rotate_x)
            cos_angle_two = math.cos(angle_two)
            sin_angle_two = math.sin(angle_two)

            calculated_value = sin_x * rotation_distance * cos_angle_one - sin_rotate_y * sin_angle_one

            pixel_x = int(40 + 30 * screen_projection_ratio * (cos_rotate_x * rotation_distance * cos_angle_two - calculated_value * sin_angle_two))
            pixel_y = int(12 + 15 * screen_projection_ratio * (cos_rotate_x * rotation_distance * sin_angle_two + calculated_value * cos_angle_two))

            pixel_location = int(pixel_x + 80 * pixel_y)

            ascii_index = int(8 * ((sin_rotate_y * sin_angle_one - sin_x * cos_y * cos_angle_one) * cos_angle_two - sin_x * cos_y * sin_angle_one - sin_rotate_y * cos_angle_one - cos_rotate_x * cos_y * sin_angle_two))

            if 0 < pixel_y < 22 and 0 < pixel_x < 80 and screen_projection_ratio > screen_depth[pixel_location]:
                screen_depth[pixel_location] = screen_projection_ratio
                screen_pixels[pixel_location] = ".,-~:;=!*#$@"[ascii_index if ascii_index > 0 else 0]

    ansi_cursor_to_home = '\x1b[H'
    print(ansi_cursor_to_home, end='')
    for index in range(1761):
        print((screen_pixels[index] if index % 80 else '\n'), end='')
        angle_one += 0.00004
        angle_two += 0.00002
