#!/bin/bash

echo "🔍 Verificando claves SSH existentes..."
ls -al ~/.ssh

echo "✅ Si no ves 'id_ed25519.pub' o 'id_rsa.pub', generaremos una nueva clave."
read -p "¿Quieres generar una nueva clave SSH ahora? (s/n): " respuesta

if [[ "$respuesta" == "s" ]]; then
  echo "🛠 Generando nueva clave SSH..."
  ssh-keygen -t ed25519 -C "guscorzo2009@gmail.com"
fi

echo "🚀 Activando el agente SSH..."
eval "$(ssh-agent -s)"

echo "➕ Agregando la clave al agente..." 
ssh-add ~/.ssh/id_ed25519 2>/dev/null || ssh-add ~/.ssh/id_rsa

echo "📋 Tu clave pública es:" 
cat ~/.ssh/id_ed25519.pub 2>/dev/null || cat ~/.ssh/id_rsa.pub

echo "👉 Copia esta clave y agrégala en GitHub (Settings → SSH and GPG keys)."

echo "🔗 Probando conexión con GitHub..." 
ssh -T git@github.com

echo "🎉 Si ves el mensaje de bienvenida, ya puedes hacer:" 
echo "git push -u origin main"