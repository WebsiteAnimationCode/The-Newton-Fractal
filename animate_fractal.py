import pygame
from assets import assets

formula = input("f(x) = ")
solution = int(input("number of routs => "))

def set_text(string, coordx, coordy, fontSize, color=(255, 255, 255)): #Function to set text

    font = pygame.font.Font('freesansbold.ttf', fontSize) 
    #(0, 0, 0) is black, to make black text
    text = font.render(string, True, color) 
    textRect = text.get_rect()
    textRect.center = (coordx, coordy) 
    return (text, textRect)

tools = assets(solution)
tools.formula = formula

width = 700
height = 700

pygame.init()
back = (192,192,192)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('A bit Racey')
screen.fill(back)
clock = pygame.time.Clock()
running = True

center_x = width // 2
center_y = height // 2

rounding = 2
scale = 100

index = -1

width_of_button = 100
height_of_button = 50

index_pressed = -1

margin_right = 10
margin_top = 10

dist_buttons = 5

position_of_buttons_start = []
position_of_buttons_end = []

start_point_x = width - width_of_button - margin_right
start_point_y = height - height_of_button - margin_top

step_for_coordinates_output = 2

font_size_text_on_button_coof = 20
font_size_text_on_coordinates = 20

color_button_for_calculating_next_step = (0, 255, 51)
color_points = (69, 79, 219)
color_button_draw = (205, 0, 255)

freq_of_points = 0.05

points = []

width_of_button_next = 100
height_of_button_next = 50

margin_for_button_next_x = 10
margin_for_button_next_y = 10

margin_for_button_draw_x = 10
margin_for_button_draw_y = 65

size_of_points = 1
coof_size_circle = 5

for i in range(- int(width / 2 / scale / freq_of_points), int(width / 2 / scale / freq_of_points)):
    for g in range(- int(height / 2 / scale / freq_of_points), int(height / 2 / scale / freq_of_points)):
        points.append([i * freq_of_points, g * freq_of_points])

dubl_points = list(points)

for i in range(len(tools.coof)):
    position_of_buttons_start.append([start_point_x, start_point_y])
    position_of_buttons_end.append([start_point_x + width_of_button, start_point_y + height_of_button])

    start_point_y -= (height_of_button + dist_buttons)

draw = False

print(f'size of points => {len(points)}')

far_color = (0, 0, 0)
maximum_dist_from_solution = 0.5

fractal = False

while running:
    screen.fill((0, 0, 0))

    if fractal == False:
        for i in range(len(points)):
            pygame.draw.circle(screen, color_points, (center_x + round(points[i][0], 2) * scale, center_y + round(points[i][1], 2) * scale), size_of_points, 100)
    else:  
        for i in range(len(points)):
            min_dist = 1e18
            index = -1
            for g in range(len(tools.coof)):
                dist = tools.magnitude(complex(points[i][0], points[i][1]) - tools.coof[g])

                if dist < min_dist:
                    min_dist = dist
                    index = g
                
            pygame.draw.circle(screen, tools.colors[index], (center_x + round(dubl_points[i][0], 2) * scale, center_y + round(dubl_points[i][1], 2) * scale), size_of_points, 100)



    start_point_x = width - width_of_button - margin_right
    start_point_y = height - height_of_button - margin_top

    pygame.draw.line(screen, (255, 255, 255), (center_x, 0), (center_x, height), 1)
    pygame.draw.line(screen, (255, 255, 255), (0, center_y), (width, center_y), 1)

    pygame.draw.rect(screen, color_button_for_calculating_next_step, pygame.Rect(margin_for_button_next_x, margin_for_button_next_y, width_of_button_next, height_of_button_next))
    pygame.draw.rect(screen, color_button_draw, pygame.Rect(margin_for_button_draw_x, margin_for_button_draw_y, width_of_button_next, height_of_button_next))

    # *************** drawing coordinates ****************
    
    x_pos = center_x
    y_pos = center_y

    while x_pos >= 0 and x_pos <= width:
        number_on_coordinate_system = float((x_pos - center_x) / scale)
        text = set_text(str(number_on_coordinate_system), x_pos, y_pos + font_size_text_on_coordinates / 2, font_size_text_on_coordinates)
        screen.blit(text[0], text[1])
        x_pos += (step_for_coordinates_output * scale)
    
    x_pos = center_x
    y_pos = center_y

    while x_pos >= 0 and x_pos <= width:
        number_on_coordinate_system = float((x_pos - center_x) / scale)
        text = set_text(str(number_on_coordinate_system), x_pos, y_pos + font_size_text_on_coordinates / 2, font_size_text_on_coordinates)
        screen.blit(text[0], text[1])
        x_pos -= (step_for_coordinates_output * scale)

    x_pos = center_x
    y_pos = center_y

    while y_pos >= 0 and y_pos <= height:
        number_on_coordinate_system = float((y_pos - center_y) / scale)
        text = set_text(str(number_on_coordinate_system), x_pos, y_pos + font_size_text_on_coordinates / 2, font_size_text_on_coordinates)
        screen.blit(text[0], text[1])
        y_pos += (step_for_coordinates_output * scale)
    
    x_pos = center_x
    y_pos = center_y

    while y_pos >= 0 and y_pos <= height:
        number_on_coordinate_system = float((y_pos - center_y) / scale)
        text = set_text(str(number_on_coordinate_system), x_pos, y_pos + font_size_text_on_coordinates / 2, font_size_text_on_coordinates)
        screen.blit(text[0], text[1])
        y_pos -= (step_for_coordinates_output * scale)
    
    # ****************** end drawing coordinates *************

    for i in range(len(tools.coof)):
        if index == i:
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(start_point_x, start_point_y, width_of_button, height_of_button))
            text = set_text(str(i + 1), start_point_x + width_of_button // 2, start_point_y + height_of_button // 2, font_size_text_on_button_coof)
            screen.blit(text[0], text[1])
        else:
            pygame.draw.rect(screen, (122, 209, 77), pygame.Rect(start_point_x, start_point_y, width_of_button, height_of_button))
            text = set_text(str(i + 1), start_point_x + width_of_button // 2, start_point_y + height_of_button // 2, font_size_text_on_button_coof)
            screen.blit(text[0], text[1])
        start_point_y -= (height_of_button + dist_buttons)

    for i in range(len(tools.coof)):
        pygame.draw.circle(screen, (255, 0, 0), (tools.coof[i].real * scale + center_x, tools.coof[i].imag * scale + center_y), coof_size_circle, 100)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN: # If the current event is the mouse button down event
            button_press = False
            pos = pygame.mouse.get_pos()

            x = list(pos)[0]
            y = list(pos)[1]

            for button_index in range(len(position_of_buttons_start)):
                if (x >= position_of_buttons_start[button_index][0] and
                    x <= position_of_buttons_end[button_index][0] and
                    y >= position_of_buttons_start[button_index][1] and
                    y <= position_of_buttons_end[button_index][0]):
                    index = button_index
                    button_press = True
                    break

            if button_press:
                continue

            next_button = False

            if (x >= margin_for_button_next_x and
                x <= margin_for_button_next_x + width_of_button_next and
                y >= margin_for_button_next_y and
                y <= margin_for_button_next_y + height_of_button_next):
                next_button = True

                for i in range(len(points)):
                    #points[i] = points[i] - (tools.f(points[i]) / tools.complex_derivative_f(points[i]))
                    point = complex(points[i][0], points[i][1])
                    #print(f'answer => {tools.complex_derivative_f(point)}')
                    answer = point - (tools.f(point) / tools.complex_derivative_f(point))
                    #print(f'answer => {answer}')
                    points[i] = [answer.real, answer.imag]
            
            if (x >= margin_for_button_draw_x and
                x <= margin_for_button_draw_x + width_of_button_next and
                y >= margin_for_button_draw_y and
                y <= margin_for_button_draw_y + height_of_button_next):

                fractal = True

                for i in range(len(points)):
                    points[i] = dubl_points[i]

                continue

            if index != -1 and next_button == False:
                tools.coof[index] = (complex(x, y) - complex(center_x, center_y)) / scale

            

    pygame.display.update()
    clock.tick(60)
pygame.quit()

quit()
