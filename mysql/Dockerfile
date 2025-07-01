FROM mysql:8.0

# Set environment variables for MySQL root user
ENV MYSQL_ROOT_PASSWORD=rootpass
ENV MYSQL_DATABASE=appdb
ENV MYSQL_USER=user
ENV MYSQL_PASSWORD=password

# Copy initialization SQL script
COPY init.sql /docker-entrypoint-initdb.d/
