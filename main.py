import pygame

pygame.init()
largura = 800
altura = 600
window = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("The Game of Life")
background_color = (0, 0, 0)
window.fill(background_color)

square_size = 20
square_color = (0, 0, 0)
square_alive_color = (255, 255, 255)
square_type = ""


def live_dead():
    neighbors_count = []
    neighbors_black_count = []
    for square0 in grade:
        if square0["Color"] == square_alive_color:
            x0, y0 = square0["Square"][0], square0["Square"][1]
            neighbors = 0
            for square1 in grade:
                if square1["Color"] == square_alive_color:
                    x1, y1 = square1["Square"][0], square1["Square"][1]
                    if abs(x1 - x0) <= square_size and abs(y1 - y0) <= square_size and (x1, y1) != (x0, y0):
                        neighbors += 1
            #print(f"Neighbors: {neighbors}")
            neighbors_count.append({"Neighbors": neighbors, "Square": square0})
        if square0["Color"] == (0, 0, 0):
            x2, y2 = square0["Square"][0], square0["Square"][1]
            neighbors_black = 0
            for square1 in grade:
                if square1["Color"] == square_alive_color:
                    x3, y3 = square1["Square"][0], square1["Square"][1]
                    if abs(x3 - x2) <= square_size and abs(y3 - y2) <= square_size and (x3, y3) != (x2, y2):
                        neighbors_black += 1
            neighbors_black_count.append({"Neighbors": neighbors_black, "Square": square0})
    for neighbords_count1 in neighbors_count:
        if neighbords_count1["Neighbors"] < 2:
                square_nei = neighbords_count1["Square"]
                square_nei["Color"] = (0, 0, 0)
                square_nei.update(square_nei)
        if neighbords_count1["Neighbors"] == 2 or neighbords_count1["Neighbors"] == 3:
                square_nei = neighbords_count1["Square"]
                square_nei["Color"] = square_nei["Color"]
                square_nei.update(square_nei)
        if neighbords_count1["Neighbors"] > 3:
                square_nei = neighbords_count1["Square"]
                square_nei["Color"] = (0, 0, 0)
                square_nei.update(square_nei)
    for neighbords_black_count1 in neighbors_black_count:
        if neighbords_black_count1["Neighbors"] == 3:
                square_black_nei = neighbords_black_count1["Square"]
                square_black_nei["Color"] = square_alive_color
                square_black_nei.update(square_black_nei)

def all_squares_black():
    for square0 in grade:
        if square0["Color"] != (0, 0, 0):
            return False
    return True

grade = []
for x in range(0, largura, square_size):
    for y in range(0, altura, square_size):
        square = pygame.draw.rect(window, square_color, (x, y, square_size, square_size))
        grade.append({"Square": square, "Color": square_color, "Type": square_type})

generation = 0
window_open = True
start_simulation = 0
while window_open:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window_open = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                pos_mouse = pygame.mouse.get_pos()
                for square in grade:
                    if square["Square"].collidepoint(pos_mouse):
                        square["Color"] = (255, 255, 255)
            if event.button == pygame.BUTTON_RIGHT:
                start_simulation += 1
    for square in grade:
        pygame.draw.rect(window, square["Color"], square["Square"])
    if start_simulation % 2 != 0:
        live_dead()
        generation += 1
        print(generation)
        if all_squares_black():
            start_simulation = False
    if start_simulation % 2 == 0:
        start_simulation = False
    for x in range(0, largura, square_size):
        pygame.draw.line(window, (30, 30, 30), (x, 0), (x, altura))
    for y in range(0, altura, square_size):
        pygame.draw.line(window, (30, 30, 30), (0, y), (largura, y))
    pygame.display.flip()