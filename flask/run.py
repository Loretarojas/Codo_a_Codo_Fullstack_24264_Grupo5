from app import create_app

# Crear una instancia de la aplicación
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
