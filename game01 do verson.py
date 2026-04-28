import pygame 

# Iniciando o Pygame 
pygame. int()

# Definindo o tamanho da janela 
LARGURA, ALTURA = 720, 720 
tela = pygame.display.set_mode((LARGURA, ALTURA)) 
pygame.DISPLAY.SET_CAPTION("Nome da janela") 

# Loop principal do jogo 
rodando = True 
while rodando: 
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT: 
            rodando = False 

            # Atualizar a tela 
            pygame.display.flip() 

# Finaliza o Pygame 
pygame.quit() 
