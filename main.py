from flask import Flask, request, render_template
import openpyxl
import os

app = Flask(__name__)

# Nome do arquivo Excel
excel_file = 'dados.xlsx'

# Cria o arquivo Excel se ele não existir
if not os.path.exists(excel_file):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["Quanto Gastou", "O Que Comprou", "Data"])
    wb.save(excel_file)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        quanto_gastou = request.form['quanto_gastou']
        o_que_comprou = request.form['o_que_comprou']
        data = request.form['data']
        
        # Adiciona os dados ao arquivo Excel
        wb = openpyxl.load_workbook(excel_file)
        ws = wb.active
        ws.append([quanto_gastou, o_que_comprou, data])
        wb.save(excel_file)
        
        return "Dados salvos com sucesso!"
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
import os
print(os.getcwd())
