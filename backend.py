from app import app



if __name__ == '__main__':
    port = 5011
    while True:
        try:
            app.run(host='localhost', port=port, debug=False)
        except:
            port+=1
        
