import pygame

def scale(x, y, WIDTH, HEIGHT):
    widthMin = 0
    heightMin = 0
    xMinMandelbrot = -2.5
    xMaxMandelbrot = 1
    yMinMandelbrot = -1
    yMaxMandelbrot = 1
    xReturn = (xMaxMandelbrot - xMinMandelbrot) * (x - widthMin) / (WIDTH - widthMin) + xMinMandelbrot
    yReturn = (yMaxMandelbrot - yMinMandelbrot) * (y - heightMin) / (HEIGHT - heightMin) + yMinMandelbrot
    return (xReturn, yReturn)


def genmadelbrot(WIDTH, HEIGHT):
    for x in range(0,WIDTH):
        for y in range(0, HEIGHT):
            (xcomp, ycomp) = scale(x, y, WIDTH, HEIGHT)
            xsquare = 0
            ysquare = 0
            zsquare = 0
            iteration = 0
            max_iteration = 1000

            while (xsquare + ysquare) < 4 and iteration < max_iteration:
                a = xsquare - ysquare + xcomp
                b = zsquare - xsquare - ysquare + ycomp
                xsquare = a*a
                ysquare = b*b
                zsquare = (a + b) * (a + b)
                iteration += 1
            if xsquare + ysquare < 4:
                screen.set_at((x,y), (255,0,0))
        print ("{0:.0%}".format(x / WIDTH))


def mainfunc(WIDTH, HEIGHT):
    drawing = True
    running = True
    while running:
        screen.set_at((250,150), (255,0,0))
        while drawing:
            genmadelbrot(WIDTH, HEIGHT)
            drawing = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()


if __name__ == "__main__":
    HEIGHT = 300
    WIDTH = 500
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Fractal stuffs")
    mainfunc(WIDTH, HEIGHT)