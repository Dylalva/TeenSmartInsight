# Despliegue de TeenSmartInsight con Terraform

Este directorio contiene la configuración de Terraform para desplegar la aplicación TeenSmartInsight en AWS.

## Requisitos previos

1. Tener instalado [Terraform](https://www.terraform.io/downloads.html)
2. Tener una cuenta de AWS y credenciales configuradas

## Configuración de credenciales AWS

Antes de ejecutar Terraform, necesitas configurar tus credenciales de AWS. Tienes varias opciones:

### Opción 1: Archivo de credenciales AWS

Crea o edita el archivo `~/.aws/credentials`:

```
[default]
aws_access_key_id = TU_ACCESS_KEY
aws_secret_access_key = TU_SECRET_KEY
```

### Opción 2: Variables de entorno

Configura las siguientes variables de entorno:

```bash
export AWS_ACCESS_KEY_ID="TU_ACCESS_KEY"
export AWS_SECRET_ACCESS_KEY="TU_SECRET_KEY"
export AWS_REGION="us-east-2"
```

### Opción 3: Credenciales en el archivo main.tf

Descomenta y edita las líneas de `access_key` y `secret_key` en el archivo `main.tf` (no recomendado para repositorios públicos).

## Despliegue

1. Inicializa Terraform:
   ```bash
   terraform init
   ```

2. Verifica el plan de ejecución:
   ```bash
   terraform plan
   ```

3. Aplica la configuración:
   ```bash
   terraform apply
   ```

4. Confirma la operación escribiendo `yes` cuando se te solicite.

## Acceso a la aplicación

Una vez completado el despliegue, Terraform mostrará la IP pública de la instancia y el comando para conectarse por SSH.

## Destruir la infraestructura

Para eliminar todos los recursos creados:

```bash
terraform destroy
```