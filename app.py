from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

startups = []
batalhas = []
todas_startups = []
vencedores_rodada = []
batalhas_concluidas = set()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        slogan = request.form['slogan']
        ano = request.form['ano']
        startup = {
            'nome': nome,
            'slogan': slogan,
            'ano': ano,
            'pontuacao': 70,
            'eventos': {
                'pitch': 0,
                'bug': 0,
                'tracao': 0,
                'investidor': 0,
                'fake_news': 0
            }
        }
        startups.append(startup)
        todas_startups.append(startup.copy())
        return redirect(url_for('cadastro'))
    return render_template('cadastro.html', startups=startups)

@app.route('/batalhas')
def batalhas_rodada():
    global startups, batalhas

    if not batalhas:
        if len(startups) not in [4, 8]:
            return "Número inválido de startups. Cadastre exatamente 4 ou 8 startups para iniciar o torneio."

    if len(startups) % 2 != 0:
        return "Erro: número ímpar de startups na rodada."

    random.shuffle(startups)
    batalhas = [(startups[i], startups[i+1]) for i in range(0, len(startups), 2)]
    return render_template('batalhas.html', batalhas=batalhas, batalhas_concluidas=batalhas_concluidas)



@app.route('/evento/<int:indice>', methods=['GET', 'POST'])
def evento(indice):
    global batalhas, batalhas_concluidas

    if indice in batalhas_concluidas:
        return redirect(url_for('batalhas_rodada'))

    startup1 = batalhas[indice][0]
    startup2 = batalhas[indice][1]

    eventos_disponiveis = {
        "pitch": 6,
        "bug": -4,
        "tracao": 3,
        "investidor": -6,
        "fake_news": -8
    }

    if request.method == 'POST':
        pontos1 = 0
        pontos2 = 0

        for evento, valor in eventos_disponiveis.items():
            if request.form.get(f"{evento}_1"):
                pontos1 += valor
                startup1["eventos"][evento] += 1
            if request.form.get(f"{evento}_2"):
                pontos2 += valor
                startup2["eventos"][evento] += 1

        startup1["pontuacao"] += pontos1
        startup2["pontuacao"] += pontos2

        if pontos1 > pontos2:
            startup1["pontuacao"] += 30
            vencedor = startup1["nome"]
            vencedores_rodada.append(startup1)
        elif pontos2 > pontos1:
            startup2["pontuacao"] += 30
            vencedor = startup2["nome"]
            vencedores_rodada.append(startup2)
        else:
            escolha = random.choice([1, 2])
            if escolha == 1:
                startup1["pontuacao"] += 2 + 30
                vencedor = f"{startup1['nome']} (Shark Fight 🦈)"
                vencedores_rodada.append(startup1)
            else:
                startup2["pontuacao"] += 2 + 30
                vencedor = f"{startup2['nome']} (Shark Fight 🦈)"
                vencedores_rodada.append(startup2)

        batalhas_concluidas.add(indice)
        return render_template('resultado.html', vencedor=vencedor, startup1=startup1, startup2=startup2)

    return render_template('evento.html', startup1=startup1, startup2=startup2, indice=indice)

@app.route('/nova-rodada', methods=['POST'])
def nova_rodada():
    global startups, batalhas, vencedores_rodada, batalhas_concluidas

    startups = vencedores_rodada.copy()
    vencedores_rodada.clear()
    batalhas_concluidas.clear()

    if len(startups) < 2:
        return redirect(url_for('ranking'))

    random.shuffle(startups)
    batalhas = [(startups[i], startups[i+1]) for i in range(0, len(startups), 2)]
    return redirect(url_for('batalhas_rodada'))

@app.route('/ranking')
def ranking():
    startups_ordenadas = sorted(todas_startups, key=lambda x: x['pontuacao'], reverse=True)
    return render_template("ranking.html", startups=startups_ordenadas)

@app.route('/reset-total')
def reset_total():
    global startups, batalhas, vencedores_rodada, batalhas_concluidas, todas_startups
    startups.clear()
    batalhas.clear()
    vencedores_rodada.clear()
    batalhas_concluidas.clear()
    todas_startups.clear()
    return redirect(url_for('index'))

@app.route('/reset')
def reset():
    global startups, batalhas, vencedores_rodada, batalhas_concluidas
    startups = [s.copy() for s in todas_startups]
    batalhas.clear()
    vencedores_rodada.clear()
    batalhas_concluidas.clear()
    return redirect(url_for('batalhas_rodada'))
if __name__ == '__main__':
    app.run(debug=True)
