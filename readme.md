# Sobre 📚

Este projeto foi desenvolvido como parte de um teste prático que avalia o conhecimento em Django.

## Especificações 👀

- **Python:** 3.10.12
- **Django:** 4.2.7
- **Poetry:** 1.1.12

## Configuração do Ambiente Virtual 🐍

Recomendado o uso de ambientes virtuais para garantir que as dependências do projeto sejam isoladas.
Você pode criar um ambiente virtual usando a ferramenta Poetry. Certifique-se de ter o Poetry instalado e execute os seguintes comandos:

```bash
poetry install
```

Isso instalará todas as dependências listadas no arquivo pyproject.toml.

## Executando o Projeto 🚀

Antes de iniciar o projeto, você precisará aplicar as migrações do banco de dados. Execute o seguinte comando:
```bash
python manage.py migrate
```
Agora é só iniciar o servidor de desenvolvimento:

```bash
python manage.py runserver
```
O projeto estará disponível em http://localhost:8000/.

## Endpoints da API 🌐
A API deste projeto fornece endpoints para gerenciar as Task e Person:

-  /person/: [retorna todas as pessoas criadas.]
-  /task/: [retorna todas as tasks criadas.]
Consulte a documentação da API para obter detalhes sobre como usar cada endpoint.

## Documentação da API 📖
A documentação da API é gerada automaticamente usando o Django rest framework. Para acessar a documentação, inicie o servidor e vá para http://localhost:8000/api/.

