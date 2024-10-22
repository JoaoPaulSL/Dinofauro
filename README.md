Jogo do Dinofauro - Pygame
Este é um jogo inspirado no famoso jogo do dinossauro offline do Google Chrome, desenvolvido usando Python e a biblioteca Pygame. O jogador controla um dinossauro que deve saltar sobre cactos e evitar obstáculos aéreos, enquanto a dificuldade aumenta à medida que o jogo avança.

Funcionalidades
Controle simples com a barra de espaço para fazer o dinossauro pular.
Obstáculos variados, incluindo cactos e pássaros.
Aumento gradual da dificuldade à medida que a pontuação do jogador aumenta.
Sistema de pontuação e recorde, com exibição no topo da tela.
Tela de game over com opção de reiniciar o jogo pressionando a tecla "R".
Instalação e Execução
Pré-requisitos
Certifique-se de ter o Python e o Pygame instalados em seu ambiente. Se você ainda não tem o Pygame instalado, execute o seguinte comando para instalá-lo:

pip install pygame

Como executar o jogo
Clone este repositório ou faça o download do código-fonte.
Navegue até o diretório do jogo.
Execute o arquivo main.py com o Python:

Estrutura do Projeto
O projeto está organizado da seguinte forma:

├── img/                    # Diretório com imagens do jogo
│   ├── background.png       # Imagem de fundo
│   ├── cactus.png           # Imagem do obstáculo (cacto)
│   ├── cactus2.png          # Imagem do obstáculo (variação de cacto)
│   ├── cactus3.png          # Imagem do obstáculo (variação de cacto)
│   ├── cactus4.png          # Imagem do obstáculo aéreo (pássaro)
│   ├── inossouro.png        # Imagem do personagem principal (dinossauro)
├── settings.py              # Arquivo com configurações gerais (largura, altura da tela, etc.)
├── dino.py                  # Classe que implementa a lógica do dinossauro
├── obstacle.py              # Classe que implementa a lógica dos obstáculos
├── game.py                  # Lógica principal do jogo
├── main.py                  # Arquivo principal que inicializa e executa o jogo
└── README.md                # Este arquivo com informações sobre o projeto

Controles
Barra de Espaço: Faz o dinossauro pular.
Tecla R: Reinicia o jogo após o game over.
Objetivo
O objetivo do jogo é evitar os obstáculos, como cactos e pássaros, enquanto acumula pontos. O jogo se torna progressivamente mais difícil à medida que o jogador acumula pontos, com os obstáculos se movendo mais rápido.

Melhorias Futuras
Algumas possíveis melhorias que podem ser implementadas no futuro:

Adição de níveis de dificuldade selecionáveis.
Introdução de diferentes personagens jogáveis.
Animação para o dinossauro e obstáculos.
Efeitos sonoros para os saltos e colisões.
Contribuição
Se você deseja contribuir com o projeto, fique à vontade para abrir uma pull request ou enviar sugestões através de issues.

Licença
Este projeto é de código aberto e está disponível sob a licença MIT.
