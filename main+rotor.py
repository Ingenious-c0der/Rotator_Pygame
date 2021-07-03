import pygame,sys,math




pygame.init()


clock = pygame.time.Clock()
screen = pygame.display.set_mode((1500,840))
green = (0, 255, 0)
blue = (0, 0, 128)



#image loading area
#axes
axis = pygame.image.load('axis.png')
axis_rect = axis.get_rect(center= [400,400])
axis2 = pygame.image.load('axis2.png')
axis_rect2 = axis.get_rect(center= [400,400])


#masses
mass1 = pygame.image.load('mass_smol.png')
mass_rect1=mass1.get_rect(center=[400,400])
mass2 = pygame.image.load('mass_smol.png')
mass_rect2=mass2.get_rect(center=[400,400])
mass3 = pygame.image.load('mass_smol.png')
mass_rect3=mass3.get_rect(center=[400,400])
mass4 = pygame.image.load('mass_smol.png')
mass_rect4=mass4.get_rect(center=[400,400])
half_length=323
d=0
angle=0
weight=1
rpm=5
#Textbox
font = pygame.font.Font('freesansbold.ttf', 25)
c=0
font2 = pygame.font.Font('freesansbold.ttf',60)



def rotate(surface,angle):

    rotated_surface = pygame.transform.rotozoom(surface, angle, 1)
    rotated_rect = rotated_surface.get_rect(center=(400, 400))

    return rotated_surface,rotated_rect

def massrotate(surface,origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    """

    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    rotated_surface = pygame.transform.rotozoom(surface, angle, 1)
    rotated_rect = rotated_surface.get_rect(center=(qx, qy))
    return rotated_surface, rotated_rect



#main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    while d<=323:
        if d>=200:
            axis = pygame.image.load('axis_dark_render.png')
            axis_rect = axis.get_rect(center=[400, 400])
            axis2 = pygame.image.load('axis2_sark_render.png')
            axis_rect2 = axis.get_rect(center=[400, 400])

            # masses
            mass1 = pygame.image.load('smol_mass_dark_.png')
            mass_rect1 = mass1.get_rect(center=[400, 400])
            mass2 = pygame.image.load('smol_mass_dark_.png')
            mass_rect2 = mass2.get_rect(center=[400, 400])
            mass3 = pygame.image.load('smol_mass_dark_.png')
            mass_rect3 = mass3.get_rect(center=[400, 400])
            mass4 = pygame.image.load('smol_mass_dark_.png')
            mass_rect4 = mass4.get_rect(center=[400, 400])



        angle+=int((323/(323-d))**2)
        screen.fill((87-d if 87-d>=0 else 0, 89-d if 89-d>=0 else 0,222-d if 222-d>=0 else 0))


        #texting
        text = font.render(f"Net force applied at this instance : {(round(4 * weight * (((323/(323-d))**2)) * (half_length - d)))} N", True, green, blue)
        textRect = text.get_rect()
        textRect.center = (400, 20)
        text1 = font.render(f"Number of rotations completed {angle//360}",True,green,blue)
        textRect1 = text1.get_rect()
        textRect1.center = (400, 750)

        text2 = font2.render(" First Stage : " if 0<d<100 else " Second stage :"if 100<d<180 else " Third Stage :" if 180<d<250 else " Fourth Stage :",True,green,(87-d if 87-d>=0 else 0, 89-d if 89-d>=0 else 0,222-d if 222-d>=0 else 0))
        text3 =font.render(" The torque is on the greater side  "if 0<d<100 else "Increase in rpm,decrease in torque, Applied force " if 100<d<180 else "The F applied now is going beyond human capacity"if 180<d<250 else "The final stage,only possible on paper",True,green,(87-d if 87-d>=0 else 0, 89-d if 89-d>=0 else 0,222-d if 222-d>=0 else 0))
        text4 = font.render("and the masses are slowly pushed towards the centre" if 0<d<100 else "required to move masses towards centre increases" if 100<d<180 else "Force provided is utilised as centrifugal oppsotion"if 180<d<250 else "or during heavy star collapse to form blackhole",True,green,(87-d if 87-d>=0 else 0, 89-d if 89-d>=0 else 0,222-d if 222-d>=0 else 0))
        textRect2 = text2.get_rect()
        textRect2.center = (1150, 200)
        textRect3 = text3.get_rect()
        textRect3.center = (1180, 430)
        textRect4 = text4.get_rect()
        textRect4.center = (1150, 460)
        screen.blit(text2,textRect2)
        screen.blit(text3, textRect3)
        screen.blit(text4, textRect4)






        d+=0.06
        #mass rotation
        mass_rotated1,mass_rotated_rect1=massrotate (mass1,(400,400),(400,80+d),math.radians(~angle))  #increasing the y cod of point brings it closer to the centre,
        mass_rotated2, mass_rotated_rect2 = massrotate(mass2, (400, 400), (80+d, 400), math.radians(~angle)) #increasing x cod brings it closer to the centre
        mass_rotated3, mass_rotated_rect3 = massrotate(mass3, (400, 400), (723-d, 400), math.radians(~angle)) #reducing x cod brings it closer to the centre,
        mass_rotated4, mass_rotated_rect4 = massrotate(mass4, (400, 400), (400, 723-d), math.radians(~angle)) #reducing y cod brings it closer to the centre

        #axis rotation
        axis_rotated,axis_rotated_rect=rotate(axis,angle)
        axis_rotated2, axis_rotated_rect2 = rotate(axis2, angle)

        #graphing















        #bliting
        screen.blit(axis_rotated,axis_rotated_rect)
        screen.blit(axis_rotated2,axis_rotated_rect2)
        screen.blit(mass_rotated1, mass_rotated_rect1)
        screen.blit(mass_rotated2, mass_rotated_rect2)
        screen.blit(mass_rotated3, mass_rotated_rect3)
        screen.blit(mass_rotated4, mass_rotated_rect4)
        screen.blit(text,textRect)
        screen.blit(text1,textRect1)

        pygame.display.flip()
        clock.tick(80)

    screen.blit(text, textRect)
    screen.blit(text1, textRect1)
