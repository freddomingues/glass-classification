# -*- coding: utf-8 -*-
"""
@author: fred_
"""

import numpy as np
from flask import Flask, request, render_template
import pickle
import os

app = Flask(__name__)
nb_model = pickle.load(open('naive_bayes_model.sav', 'rb'))
lr_model = pickle.load(open('logistic_regression_model.sav', 'rb'))
svm_model = pickle.load(open('svm_model.sav','rb'))

glassesFolder = os.path.join('static','glasses')

app.config['UPLOAD_FOLDER'] = glassesFolder

@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/indexRL')
def lr():
    return render_template('indexRL.html')

@app.route('/indexSVM')
def svm():
    return render_template('indexSVM.html')

@app.route('/predictNB', methods=['GET','POST'])
def predict_nb():
    RI = float(request.form['inputRI'])
    Na = float(request.form['inputNa'])
    Mg = float(request.form['inputMg'])
    Al = float(request.form['inputAl'])
    Si = float(request.form['inputSi'])
    K = float(request.form['inputK'])
    Ca = float(request.form['inputCa'])
    Ba = float(request.form['inputBa'])
    Fe = float(request.form['inputFe'])
    novo_registro = [[RI, Na, Mg, Al, Si, K, Ca, Ba, Fe]]
    novo_registro = np.asarray(novo_registro)
    
    resposta_nb = nb_model.predict(novo_registro)
    
    if resposta_nb == 1:
        glass = os.path.join(app.config['UPLOAD_FOLDER'],'class1.jpg')
        return render_template('index.html', 
                               prediction_text_nb ='Resultado: Vidro Processado para Construções', 
                               img_nb = glass)
    elif resposta_nb == 2:
        glass = os.path.join(app.config['UPLOAD_FOLDER'],'class2.jpg')
        return render_template('index.html', 
                               prediction_text_nb ='Resultado: Vidro Não-Processado para Construções',
                               img_nb = glass)
    elif resposta_nb == 3:
        glass = os.path.join(app.config['UPLOAD_FOLDER'],'class3.jpg')
        return render_template('index.html', 
                               prediction_text_nb ='Resultado: Vidro Processado para Veículos',
                               img_nb = glass)
    elif resposta_nb == 4:
        glass = os.path.join(app.config['UPLOAD_FOLDER'],'class4.jpg')
        return render_template('index.html', 
                               prediction_text_nb ='Resultado: Vidro Não-Processado para Veículos',
                               img_nb = glass)
    elif resposta_nb == 5:
        glass = os.path.join(app.config['UPLOAD_FOLDER'],'class5.jpg')
        return render_template('index.html', 
                               prediction_text_nb ='Resultado: Vidro para potes',
                               img_nb = glass)
    elif resposta_nb == 6:
        glass = os.path.join(app.config['UPLOAD_FOLDER'],'class6.jpg')
        return render_template('index.html', 
                               prediction_text_nb ='Resultado: Vidro para Louças',
                               img_nb = glass)
    elif resposta_nb == 7:  
        glass = os.path.join(app.config['UPLOAD_FOLDER'],'class7.jpg')
        return render_template('index.html', 
                               prediction_text_nb ='Resultado: Vidro para Faróis de Carros',
                               img_nb = glass)
    else:
        return render_template('index.html', prediction_text_nb ='Resultado: ')

@app.route('/predictRL',methods=['GET','POST'])
def predict_rl():
    RI = float(request.form['inputRI'])
    Na = float(request.form['inputNa'])
    Mg = float(request.form['inputMg'])
    Al = float(request.form['inputAl'])
    Si = float(request.form['inputSi'])
    K = float(request.form['inputK'])
    Ca = float(request.form['inputCa'])
    Ba = float(request.form['inputBa'])
    Fe = float(request.form['inputFe'])
    novo_registro = [[RI, Na, Mg, Al, Si, K, Ca, Ba, Fe]]
    novo_registro = np.asarray(novo_registro)
    
    resposta_rl = lr_model.predict(novo_registro)
    
    if resposta_rl == 1:
        glass = os.path.join(app.config['UPLOAD_FOLDER'],'class1.jpg')
        return render_template('indexRL.html', 
                               prediction_text_rl ='Resultado: Vidro Processado para Construções', 
                               img_rl = glass)
    elif resposta_rl == 2:
        glass = os.path.join(app.config['UPLOAD_FOLDER'],'class2.jpg')
        return render_template('indexRL.html', 
                               prediction_text_rl ='Resultado: Vidro Não-Processado para Construções',
                               img_rl = glass)
    elif resposta_rl == 3:
        glass = os.path.join(app.config['UPLOAD_FOLDER'],'class3.jpg')
        return render_template('indexRL.html', 
                               prediction_text_rl ='Resultado: Vidro Processado para Veículos',
                               img_rl = glass)
    elif resposta_rl == 4:
        glass = os.path.join(app.config['UPLOAD_FOLDER'],'class4.jpg')
        return render_template('indexRL.html', 
                               prediction_text_rl ='Resultado: Vidro Não-Processado para Veículos',
                               img_rl = glass)
    elif resposta_rl == 5:
        glass = os.path.join(app.config['UPLOAD_FOLDER'],'class5.jpg')
        return render_template('indexRL.html', 
                               prediction_text_rl ='Resultado: Vidro para potes',
                               img_rl = glass)
    elif resposta_rl == 6:
        glass = os.path.join(app.config['UPLOAD_FOLDER'],'class6.jpg')
        return render_template('indexRL.html', 
                               prediction_text_rl ='Resultado: Vidro para Louças',
                               img_rl = glass)
    elif resposta_rl == 7:
        glass = os.path.join(app.config['UPLOAD_FOLDER'],'class7.jpg')
        return render_template('indexRL.html', 
                               prediction_text_rl ='Resultado: Vidro para Faróis de Carros',
                               img_rl = glass)
    else:
        return render_template('indexRL.html', prediction_text_rl ='Resultado: ')
    

@app.route('/predictSVM',methods=['GET','POST'])
def predict_svm():
    RI = float(request.form['inputRI'])
    Na = float(request.form['inputNa'])
    Mg = float(request.form['inputMg'])
    Al = float(request.form['inputAl'])
    Si = float(request.form['inputSi'])
    K = float(request.form['inputK'])
    Ca = float(request.form['inputCa'])
    Ba = float(request.form['inputBa'])
    Fe = float(request.form['inputFe'])
    novo_registro = [[RI, Na, Mg, Al, Si, K, Ca, Ba, Fe]]
    novo_registro = np.asarray(novo_registro)
    
    resposta_svm = svm_model.predict(novo_registro)
    
    if resposta_svm == 1:
        glass = os.path.join(app.config['UPLOAD_FOLDER'],'class1.jpg')
        return render_template('indexSVM.html', 
                               prediction_text_svm ='Resultado: Vidro Processado para Construções', 
                               img_svm = glass)
    elif resposta_svm == 2:
        glass = os.path.join(app.config['UPLOAD_FOLDER'],'class2.jpg')
        return render_template('indexSVM.html', 
                               prediction_text_svm ='Resultado: Vidro Não-Processado para Construções',
                               img_svm = glass)
    elif resposta_svm == 3:
        glass = os.path.join(app.config['UPLOAD_FOLDER'],'class3.jpg')
        return render_template('indexSVM.html', 
                               prediction_text_svm ='Resultado: Vidro Processado para Veículos',
                               img_svm = glass)
    elif resposta_svm == 4:
        glass = os.path.join(app.config['UPLOAD_FOLDER'],'class4.jpg')
        return render_template('indexSVM.html', 
                               prediction_text_svm ='Resultado: Vidro Não-Processado para Veículos',
                               img_svm = glass)
    elif resposta_svm == 5:
        glass = os.path.join(app.config['UPLOAD_FOLDER'],'class5.jpg')
        return render_template('indexSVM.html', 
                               prediction_text_svm ='Resultado: Vidro para potes',
                               img_svm = glass)
    elif resposta_svm == 6:
        glass = os.path.join(app.config['UPLOAD_FOLDER'],'class6.jpg')
        return render_template('indexSVM.html', 
                               prediction_text_svm ='Resultado: Vidro para Louças',
                               img_svm = glass)
    elif resposta_svm == 7:
        glass = os.path.join(app.config['UPLOAD_FOLDER'],'class7.jpg')
        return render_template('indexSVM.html', 
                               prediction_text_svm ='Resultado: Vidro para Faróis de Carros',
                               img_svm = glass)
    else:
        return render_template('indexSVM.html', 
                               prediction_text_svm ='Resultado: ')
    

if __name__ == "__main__":
    app.run(debug=False)
    #http_server = WSGIServer(('', 5000), app)
    #http_server.serve_forever()
