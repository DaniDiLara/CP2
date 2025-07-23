# Define la imagen del contenedor
FROM docker.io/library/nginx:alpine

# Copiamos el contenido web
COPY index.html /usr/share/nginx/html/index.html

# Copiamos certificado y clave autofirmados
COPY nginx.crt /etc/nginx/nginx.crt
COPY nginx.key /etc/nginx/nginx.key

# Copiamos configuración de nginx
COPY default.conf /etc/nginx/conf.d/default.conf

# Copiamos contenido inicial destinado al volumen persistente
COPY images /usr/share/nginx/html/images

# Instalamos el paquete de utilidades necesarias para htpasswd
RUN apk add --no-cache apache2-utils

# Creamos el archivo con usuario y contraseña
RUN htpasswd -bc /etc/nginx/.htpasswd dani 1234

# El contenedor escucha por el puerto 443
EXPOSE 443
