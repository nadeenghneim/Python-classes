import pygame 
pygame.init()
screen=pygame.display.set_mode((700,700))
pygame.display.set_caption("Drawing shapes and writing text!")
done=False
while not done:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            done=True
    pygame.draw.polygon(screen,'orange',[(410,100),(510,100),(550,175),(510,250),(410,250),(370,175)],4)
    pygame.draw.rect(screen,'pink',pygame.Rect(100,150,160,80))
    font=pygame.font.SysFont('Times New Roman',40)
    surface=font.render("Hello Teacherr!",True,'white')
    text_rect = surface.get_rect()
    screen.blit(surface,text_rect)
    pygame.display.flip()