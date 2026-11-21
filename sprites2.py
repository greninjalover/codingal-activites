import pygame
pygame.init()
SCREEN_WIDTH,SCREEN_HEIGHT= 500,500
display_surface=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Adding image and Background image')
background_image=pygame.transform.scale(pygame.image.load("bg1.png").convert(),(SCREEN_WIDTH,SCREEN_HEIGHT))
sprite2=pygame.transform.scale(pygame.image.load('sprite2.png').convert_alpha(), (200,200))
srect=sprite2.get_rect(center=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2-30))

txt=pygame.font.Font(None, 36).render('Hello World',True,pygame.Color('black'))
text_rect=txt.get_rect(center=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2+110))

def game_loop():
    clock=pygame.time.Clock()
    running=True
    while running:
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                running=False

        display_surface.blit(background_image,(0,0))
        display_surface.blit(sprite2, srect)
        display_surface.blit(txt, text_rect)

        pygame.display.flip()

        clock.tick(30)

    pygame.quit()

if __name__ == '__main__':
    game_loop()