import pygame
pygame.init()

PLAYER = 'game_sprites/bird02.png'
BACKGROUND = 'game_sprites/bg.png'
PIPE = 'game_sprites/pillar0.png'



class Tools:
    GameSprites = {}
    GameSounds = {}
    GameSprites['background'] = pygame.image.load(BACKGROUND)
    GameSprites['player'] = pygame.image.load(PLAYER)
    GameSprites['message'] = pygame.image.load('game_sprites/welcome1.png')
    GameSprites['base'] = pygame.image.load('game_sprites/base2.png')
    GameSprites['pipe'] = (
        pygame.transform.rotate(pygame.image.load(PIPE), 180),
        pygame.image.load(PIPE)
    )

    GameSprites['numbers'] = (
        pygame.image.load('game_sprites/00.png'),
        pygame.image.load('game_sprites/01.png'),
        pygame.image.load('game_sprites/02.png'),
        pygame.image.load('game_sprites/03.png'),
        pygame.image.load('game_sprites/04.png'),
        pygame.image.load('game_sprites/05.png'),
        pygame.image.load('game_sprites/06.png'),
        pygame.image.load('game_sprites/07.png'),
        pygame.image.load('game_sprites/08.png'),
        pygame.image.load('game_sprites/09.png')
,
    )

    GameSounds['die'] = pygame.mixer.Sound('game_sounds/sfx_die.wav')
    GameSounds['hit'] = pygame.mixer.Sound('game_sounds/sfx_hit.wav')
    GameSounds['point'] = pygame.mixer.Sound('game_sounds/sfx_point.wav')
    GameSounds['swoosh'] = pygame.mixer.Sound('game_sounds/sfx_swooshing.wav')
    GameSounds['wing'] = pygame.mixer.Sound('game_sounds/sfx_wing.wav')