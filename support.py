from os import walk
import pygame

def import_folder(path):
    surface_list = []

    for _, _, img_file in walk(path):
        for image in img_file:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            image_surf = image_surf.subsurface((16,8,24,36))
            image_surf = pygame.transform.scale(image_surf, (48,64))
            surface_list.append(image_surf)

    return surface_list

def import_monster(path):
    surface_list = []

    for _, _, img_file in walk(path):
        for image in img_file:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            image_surf = pygame.transform.scale(image_surf, (48,64))
            surface_list.append(image_surf)

    return surface_list