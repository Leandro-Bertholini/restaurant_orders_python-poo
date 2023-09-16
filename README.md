# `Projeto Restaurant Orders - Python com P.O.O.`

## Visão Geral
Este projeto, que faz parte do módulo ciência da computação em um curso de desenvolvimento web ao qual cursei, teve como objetivo aplicar os conceitos de **POO**(Programação Orientada a Objetos) e trabalhar com **Set**, **Hashmap** e **Dict** usando como linguagem o **Python** e seu framework de testes **Pytest**.
Foi criado um programa que, de maneira simples, possa gerar seus cardápios considerando possíveis restrições alimentares e também a disponibilidade dos ingredientes em estoque.

## Habilidades exercitadas
- Praticar o conceito de Hashmaps através das estruturas de dados Dict e Set do Python;
- Praticar os conhecimentos de testes de software;
- Praticar os conhecimentos de orientação a objetos.

## Tecnologias Utilizadas
- Python
- pytest
- Flake8
- VS Code

<details>
<summary> 🗄️ Execução Local do Projeto:</summary><br>

Para executar, clone esse repositório com o comando:

    git clone git@github.com:Leandro-Bertholini/restaurant_orders_python-poo.git

Entre na pasta do projeto e crie o ambiente virtual:

    python3 -m venv .venv source .venv/bin/activate


Ative o ambiente virtual:

    source .venv/bin/activate

Instale as dependências no ambiente virtual:

    python3 -m pip install -r dev-requirements.txt

**OBS:** Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente. Quando precisar desativar o ambiente virtual, execute o comando deactivate. Lembre-se de ativar novamente quando voltar a trabalhar no projeto.

***Para Executar os Testes***:

    Para executar os testes certifique-se de que você está com o ambiente virtual ativado.

    python3 -m pytest
</details>

<details>
  <summary>
    <b>👀 De olho na dica - Como rodar a aplicação?</b>
  </summary>

Para ver a aplicação rodando com as funcionalidades implementadas, use o comando a seguir no terminal com o ambiente virtual ativado:

```bash
python3 -m uvicorn app:app
```

Acesse a rota `/docs` para ver a [documentação](http://127.0.0.1:8000/docs) gerada pelo FastAPI!

</details>


## Requisitos desenvolvidos:

<details>
<summary><strong>Fase 1:</strong></summary><br>

Foi implementada a classe `Ingredient` que se encontra no módulo `src/models/ingredient.py`. Um objeto desta classe contém o nome e restrições alimentares do ingrediente como atributos. Ela foi testada no módulo `tests/ingredient/test_ingredient.py`, onde os testes devem garantir que:

- a classe pode ser instanciada corretamente de acordo com a assinatura esperada;
- o atributo conjunto `restrictions` é populado como esperado;
- o método mágico `__repr__` funcione como esperado;
- o método mágico `__eq__` funcione como esperado;
- o método mágico `__hash__` funcione como esperado.
- Para estes testes, em que esperemos a falha, o requisito será aprovado quando a resposta do Pytest for XFAIL(Expected Fail), ao invés de PASSED.
</details>

<details>
<summary><strong>Fase 2:</strong></summary><br>

Foi implementada a classe `Dish` que se encontra no módulo `src/models/dish.py`. Uma instância desta classe possui atributos representando o nome, o preço e a receita do prato. Ela é testada no módulo `tests/dish/test_dish.py`, onde os testes devem garantir que:

- a classe pode ser instanciada corretamente de acordo com a assinatura esperada;
- os métodos da classe, inclusive os métodos mágicos, funcionem como esperado;
- o dicionário de receita do prato devolve a quantidade correta de um ingrediente;
- são levantados erros ao criar pratos inválidos;
- Para estes testes, em que esperemos a falha, o requisito será aprovado quando a resposta do Pytest for XFAIL(Expected Fail), ao invés de PASSED.
</details>

<details>
<summary><strong>Fase 3:</strong></summary><br>

Foi implementado a classe `MenuData` que fará todo o mapeamento de pratos e ingredientes baseado nos arquivo csv disponibilizado. Ela se encontra no módulo `src/services/menu_data.py`. Ao longo da implementação foi garantido que:

- a classe, ao ser instanciada, recebe o caminho para o arquivo csv no parâmetro `source_path`;

- a classe fará a leitura do arquivo csv e baseado em seu conteúdo fará as devidas instanciações de pratos e ingredientes;

- a classe contenha o atributo `dishes` que deverá ser um _set_ com todos os pratos devidamente instanciados;

- cada um dos pratos contenha sua respectiva receita, isto é, seus ingredientes e quantidades, bem como seu preço.
</details>

<details>
<summary><strong>Fase 4:</strong></summary><br>

Foi implementado o método `get_main_menu` dentro da classe `MenuBuilder` que se encontra no arquivo `src/services/menu_builder.py`. O método tem como parâmetro opcional uma restrição que deve ser levada em conta na hora de gerar o cardápio.
o retorno deste método deve ser do tipo `List[Dict]`. Assim, é necessário que o método retorne uma lista de dicionários que contenham as chaves dish_name, ingredients, price e restrictions que se referem, respectivamente, ao `nome` do prato, `ingredientes` que o compõem, seu `preço` no cardápio e `restrições` daquele mesmo prato.

</details>

<details>
<summary><strong>Fase 5:</strong></summary><br>

Neste requisito, o primeiro dos métodos trabalhados `(check_recipe_availability)` deve checar se a receita passada como parâmetro está ou não disponível para consumo, para isso, deve retornar False caso um ingrediente da receita não exista no estoque ou caso não exista quantidade suficiente destes ingredientes em estoque e True caso o prato esteja disponível para consumo. O segundo método `(consume_recipe)` também recebe uma receita como parâmetro, mas deve subtrair a quantidade de ingredientes usados na receita do total disponível em estoque. Vale lembrar que a subtração só deve acontecer caso a receita esteja disponível para consumo, caso contrário, deverá ser levantada uma exceção `ValueError`.
</details>


<details>
<summary><strong>Fase 6:</strong></summary><br>

Minha tarefa nesta fase, foi complementar a implementação do método `get_main_menu`, que está na classe `MenuBuilder`, para considerar a disponibilidade em estoque dos ingredientes do prato além das restrições alimentares. Assim, o Restaurante 🍝 🦐 Chapa Quente 🍛 🥘 possuirá a ferramenta capaz de gerar cardápios dinâmicos considerando restrições alimentares e disponibilidade em estoque. 
</details>


### Criação do Projeto:

- Trybe - Curso de Desenvolvimento Web


###  ☝ Desenvolvimento da Aplicação:

- Leandro Bertholini




