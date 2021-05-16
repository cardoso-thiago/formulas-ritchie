# Ritchie Formula Repo

![Rit banner](/docs/img/ritchie-banner.png)

## Documentação

Esse repositório contém fórmulas que podem ser executadas utilizando o [ritchie-cli](https://docs.ritchiecli.io).

## Usando as Fórmulas

```bash
 rit add repo
 Select your provider:
  > Github
    Gilab
 Repository name: {{some_repo_name}}
 Repository URL: {{this_repo_url}}
 Is a private repository?
    no
  > yes
 Personal access tokens: {{git_personal_token}}
 Select a tag version:
  > 1.0.1
    1.0.0
 Set the priority: 2
```

## Fórmulas Disponíveis nesse Repositório

* rit k8s secret: Gera um arquivo de Secret Opaque para o Kubernetes.
* rit gitlab wiki: Exibe uma lista de tópicos disponíveis em uma página do Gitlab Pages e abre a página correspondente ao tópico selecionado.
* rit stocks info: Exibe uma lista de 3 ações configuradas através de credenciais.
  * Dependência: [Yahoo Fin](http://theautomatic.net/yahoo_fin-documentation/) instalado
  * Deve ser adicionada uma nova credential com o nome `ticker` utilizando o comando `rit set credential`.
  * Executando o comando, você já pode adicionar até 5 tickers, no padrão `ticker1`, `ticker2`, etc.
  * Na execução da fórmula, caso não tenha completado com os 5 tickers, será solicitado o preenchimento das restantes, que podem ser deixados em branco.

> O padrão de nome do ticker segue o padrão do Yahoo Finance e geralmente possui um `.SA` no final. Você deve informar os tickers nesse formato. Para conferir os valores exatos, você pode consultar o site do [Yahoo Finance](https://finance.yahoo.com/).

* rit stocks info java: Versão em **Java** da fórmula `rit stocks info`. (Mais lento pra buildar, mais rápido pra executar)
* rit docker last version: Demonstração para obtenção da última versão de uma imagem docker no Docker Hub. Demonstração realizada com uma imagem do Alpine, que ignora a versão `latest` e pega a próxima versão da lista (que normalmente vai ser correspondente a última).
* rit spotify lyric: Pega o artista e nome da música em execução no Spotify Desktop e tenta abrir a página do [Genius](https://genius.com/) com a letra correspondente.