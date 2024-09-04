# # import pygame
 
# # # activate the pygame library .
# # pygame.init()
# # X = 600
# # Y = 600
 
# # # create the display surface object
# # # of specific dimension..e(X, Y).
# # scrn = pygame.display.set_mode((X, Y))
 
# # # set the pygame window name
# # pygame.display.set_caption('image')
 
# # # create a surface object, image is drawn on it.
# # imp = pygame.image.load("https://uploads.mangadex.org/covers/32d76d19-8a05-4db0-9fc2-e0b0648fe9d0/e90bdc47-c8b9-4df7-b2c0-17641b645ee1.jpg").convert()
 
# # # Using blit to copy content from one surface to other
# # scrn.blit(imp, (0, 0))
 
# # # paint screen one time
# # pygame.display.flip()
# # status = True
# # while (status):
 
# #   # iterate over the list of Event objects
# #   # that was returned by pygame.event.get() method.
# #     for i in pygame.event.get():
 
# #         # if event object type is QUIT
# #         # then quitting the pygame
# #         # and program both.
# #         if i.type == pygame.QUIT:
# #             status = False
 
# # # deactivates the pygame library
# # pygame.quit()




# import pygame
# from io import BytesIO
# import requests
# from PIL import Image

# # create image from URL
# rsp = requests.get("https://uploads.mangadex.org/covers/32d76d19-8a05-4db0-9fc2-e0b0648fe9d0/e90bdc47-c8b9-4df7-b2c0-17641b645ee1.jpg")
# pilimage = Image.open(BytesIO(rsp.content)).convert("RGBA")
# pgimg = pygame.image.fromstring(pilimage.tobytes(), pilimage.size, pilimage.mode)

# # show image
# pygame.init()
# display = pygame.display.set_mode((1980,1080))

# display.fill((255,255,255))
# display.blit(pgimg,(0,0))
# pygame.display.update()

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit(); exit()


# def main():
#     import assets.classesAndUtil.gameUtil as util
#     util.checkFetching()
    
# if __name__ == "_main_":
#     main()
    
import pygame

pygame.init()
WIDTH = HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont("Arial", 14)


def write(text, x, y, color="Coral",):
    text = font.render(text, 1, pygame.Color(color))
    text_rect = text.get_rect(center=(WIDTH//2, y))
    return text, text_rect

text, text_rect = write("Hello", 10, 10) # this will be centered anyhow, but at 10 height
loop = 1
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = 0
    screen.blit(text, text_rect)
    pygame.display.update()

pygame.quit()
    