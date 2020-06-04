from app import app



if __name__ == '__main__':
    port = 5000
    while True:
        try:
            app.run(host='localhost', port=port, debug=False)
        except:
            port+=1
        
