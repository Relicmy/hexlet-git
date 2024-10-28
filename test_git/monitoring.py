def monitoring(*args, **kwargs):
    if args:
        print("Параметры переданы")
    else:
        print("Параметры не переданы")
        
        

if __name__ == "__main__":
    monitoring(True)