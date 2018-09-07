from datetime import datetime

if __name__ == "__main__":
dia = datetime.now().day
mes = datetime.now().month
ano = datetime.now().year
print(str(dia)+'/'+str(mes)+'/'+str(ano))
