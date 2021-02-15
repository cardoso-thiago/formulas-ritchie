# Ritchie Formula

## Comando

```bash
rit k8s secret
```

## Descrição

Gera o arquivo para criação de um [Secrets](https://kubernetes.io/docs/concepts/configuration/secret/) para o Kubernetes. O secret gerado é do tipo [Opaque](https://kubernetes.io/docs/concepts/configuration/secret/#opaque-secrets) e adiciona um usuário e senha solicitados na execução da fórmula.

> A fórmula utiliza **Python**, portanto é uma dependência para a sua execução. Por esse motivo, a fórmula não possui disponibilidade para execução com o parâmetro `--docker` do Ritchie, pois com a dependência resolvida, a fórmula deve funcionar em qualquer plataforma na execução local.