# Hypertro.py: Em Busca do Shape 🏋️

### Criado com ❤️ e 💉 por:

✨[Amanda Arruda - amms2](https://github.com/amandaarruda)

✨[Letícia Pedrosa - lblp](https://github.com/leticiapedrosa)

✨[Paulo Rafael - prba](https://github.com/paulorbaguiar)

✨[Peterson Melo - pjfm](https://github.com/PetersonNave)

✨[Victor Matias - vcms](https://github.com/victorrmatiass)

✨[Renato Serrano - rmsa](https://github.com/renatomsa)

✨[Sthefany Cabral - sgsc](https://github.com/StheCabral)

---

### Conhecendo o conceito do nosso jogo:
Em "Hypertro.py: Em Busca do Shape" você guiará o Carianinho em sua jornada no mundo da academia! Ele começa assim, franzino... É um ectomorfo nato e seu percurso exigirá dedicação!

![cariani_easy](https://user-images.githubusercontent.com/66084295/200189269-5f8b1c69-0b86-470d-87ba-d860063ee30a.png)

Você deverá ajudá-lo a coletar os seguintes itens para que ele alcance a hipertrofia: Anilhas, halteres, batatas-doces, creatina e a clássica proteína, indispensável!

Colete pelo menos 5 de cada um dos elementos, tenha cuidado para não perder nenhum e você já não será mais um iniciante! Vamos partir para o nível médio!

![cariani_medium](https://user-images.githubusercontent.com/66084295/200189464-b7b39859-4147-4ff3-876b-f01164fb7411.png)

Nosso Carianinho já está mais forte e, com seus bíceps mais evidentes, já começa a postar o clássico "Tá pago!💪" nas redes socias!

Um segredo: caso você perca pontos de vida ao não coletar algum dos itens, será possível contar com uma ajudinha extra para recuperá-los! 💉

Mas não se esqueça, quanto mais natural, melhor, sempre! Então, tente não perder nossos preciosos elementos enquanto coleta 10 de cada.


A dificuldade está aumentando e se tornará cada vez mais devagar alcançar a crescente quantidade de itens que você precisa!

Carianinho já percorreu uma longa estrada e, após muito esforço, seu shape está quase pronto para a competição, dê uma olhada:

![cariani_hard](https://user-images.githubusercontent.com/66084295/200189884-a93d85f4-ad58-4461-84f1-60edd389d756.png)

Não desista agora, seu apoio foi fundamental até aqui! É só coletar 30 itens de cada e estaremos prontos!


### Por trás do nome:

Nossa ideia é criar um trocadilho com o nome "hipertrofia" em inglês *(hypertrophy)* e a linguagem utilizada para o desenvolvimento do jogo: Python. Nosso objetivo é, como indica o subtítulo, alcançar o shape!

### Organização do código:

Para uma prática mais limpa, optamos por modularizar o jogo da seguinte forma:
* Screen Win Lose (Direciona o usuário de acordo com o resultado e permite que o jogo possa ser reiniciado)
* Dificuldade (Busca ajustar o jogo de acordo com a dificuldade selecionada)
* Assets (Pasta que contém os elementos visuais do jogo)
* Main (Por último, mas não menos importante, o arquivo main define a mecânica do jogo e permite a integração entre as funções e classes de cada módulo)

Utilizando programação orientada a objetos, criamos as seguintes classes:
* ItemsClasses (Pasta que contém as classes com os nossos elementos: seringa, anilha, halter, batata-doce, frango, creatina)
* Mochila (Para coletar os elementos)
* Sounds (Para administrar as trilhas sonoras durante os seguintes momentos: início, durante o jogo, vitória e perda)
* Placar (Responsável por contabilizar os pontos)
* Player (Direciona o Carianinho na tela e evolui o personagem de acordo com o nível)
* Item (Determina a queda dos itens do jogo, aplicando a gravidade de maneira adequada)
* Quadrante (Gera um range adequado para que os elementos caiam de maneira a ser capturados)
* Start Screen (É a entrada do nosso jogo, direciona o jogador para o menu)
* Controlador de vida (Administra os corações e contabiliza o dano quando se deixa de coletar um elemento)
* Button (Controla os botões do jogo)

### Ferramentas, Bibliotecas e Frameworks:
Utilizamos o Python como ferramenta para o desenvolvimento do jogo e a biblioteca Pygame, além da IDE Visual Studio Code. Optamos por essa combinação devido a familiaridade dos integrantes com elas, bem como pelo direcionamento em sala de aula.

Além disso, para os elementos artísticos do jogo, utilizamos os aplicativos Procreate e 8bit Painter por serem mais intuitivos e agregarem uma boa qualidade às artes.

### Estrutura da equipe:

Todos os integrantes participaram da concepção do jogo, bem como ajudaram ao longo do processo no polimento da ideia.

Funções específicas:

* Amanda Arruda: Incrementar a jogabilidade e os níveis, corrigir bugs, design da tela inicial, dos elementos e dos Carianinhos, redação do relatório.
* Letícia Pedrosa: Corrigir bugs e melhorar a integração do personagem com os níveis.
* Paulo Rafael: Design do background, de elementos e da tela de vitória e integração com o usuário.
* Peterson Melo: Desenvolvimento da mecânica do jogo e da divisão em classes, do controle dos elementos coletados, da adequação dos quadrantes e curadoria musical.
* Victor Matias: Desenvolvimento do placar, da mecânica dos níveis e divisão em classes, do controle de dificuldade, do menu e curadoria musical.
* Renato Serrano: Implementação da tela de game over e ajustes finos do layout.
* Sthefany Cabral: Correção de bugs, criação dos slides e organização ágil da equipe através do Notion.

### Conceitos que foram apresentados durante a disciplina e utilizados no projeto:

Para a estrutura lógica básica do jogo, utilizamos, assim como aprendemos em sala, operadores lógicos, comandos condicionais e laços de repetição. Além disso, para a implementação dos objetos coletáveis, foi preciso utilizar conceitos de listas, tuplas e dicionários. Por fim, utilizamos a modularização, a programação orientada a objetos e funções.

### Desafios e aprendizados:

Nosso maior desafio não-técnico foi, sem dúvida, conciliar o desenvolvimento do jogo com as demandas das demais matérias, especialmente num período do semestre com provas mais frequentes, como foi o caso. Em relação a dificuldades técnicas, a programação orientada a objetos foi a maior delas, além da aplicação dos comandos específicos do Pygame, uma vez que nem todos os integrantes estavam familiarizados com eles.

Entretanto, apesar de todos terem contribuido no código, a experiência do desenvolvimento do jogo foi algo extremamente proveitoso para que descobríssemos naturalmente certas áreas de afinidadade dentro da programação, o que foi muito útil para a finalização da disciplina com um olhar mais apurado em relação aos nossos gostos. Além disso, nosso trabalho em grupo foi respeitoso em relação às demandas de cada um dos integrantes e bastante divertido, uma vez que uniu o nosso interesse em comum -a prática de exercícios físicos- com um estilo de jogo mais lúdico. 

Por fim, também conseguimos realizar um projeto acima das nossas expectativas em relação a ideia original, uma vez que incrementamos os níveis, tivemos diferentes skins do personagem principal, um elemento coletável que auxilia no ganho de vida e outros ajustes finos que não havíamos planejado inicialmente. Concluimos o projeto extremamente satisfeitos com o nosso resultado.


### Link para nossa apresentação:
[Clique aqui para ver nossos slides!](https://www.canva.com/design/DAFRCiJ0ajY/ToPnFaAKSfZouJJjDC9wtQ/view?utm_content=DAFRCiJ0ajY&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)
---

## Galeria do jogo📸:

**Tela inicial▶️**

![image](https://user-images.githubusercontent.com/66084295/200207841-7a708f92-44d1-4c08-a093-e2569a9cf356.png)

**Menu🎮**

![image](https://user-images.githubusercontent.com/66084295/200207965-6799dd58-03a5-43ff-ad75-3ea8aea6cbb7.png)

### Níveis⚡

**Easy👌**

![image](https://user-images.githubusercontent.com/66084295/200208051-eb745aaf-81a3-4da3-9884-37fb7576dd22.png)

**Medium😎**

![image](https://user-images.githubusercontent.com/66084295/200208142-4e2e3416-1d09-44b8-a54d-de6ffa699f9c.png)

**Hard🔥**

![image](https://user-images.githubusercontent.com/66084295/200208321-b11005dc-b6a7-4a66-afca-2229d4dc0571.png)

**Tela de Vitória🏆**

![image](https://user-images.githubusercontent.com/66084295/200208936-ee13505a-4857-4daa-a4b1-fa3befdcd874.png)

**Tela de Game Over❌**

![image](https://user-images.githubusercontent.com/66084295/200208422-8af82916-e5eb-4bb8-ab10-b18edf5a2a9c.png)
