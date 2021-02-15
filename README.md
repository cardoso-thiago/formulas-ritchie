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
