from travel import create_app

if __name__ == '__main__':
    app = create_app()
    app.secret_key = 'somerandomvalue'
    app.run(debug = True)
