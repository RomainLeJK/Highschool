from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/tri', methods=['POST'])
def resultat_insertion():
    resultat = request.form
    adresse = resultat['choix_tri']
    tab = json.loads(resultat['valeur_tableau'])  # Transforme la liste JSON au format str en list python
    etapes = ""
    tableau = tab.copy()  # Permet de conserver le tableau original

    if adresse == "tri_par_insertion":
        for i in range(1, len(tab)):
            clé = tab[i]
            j = i - 1
            # Décale les éléments plus grands que `clé`
            while j >= 0 and tab[j] > clé:
                tab[j + 1] = tab[j]
                j -= 1
            # Insère `clé` à la bonne position
            etapes += f"Etape n°{i}.1 : {tab} \n"
            tab[j + 1] = clé
            etapes += f"Etape n°{i}.2 : {tab} \n"

        return render_template('tri_insertion.html', tableau_etapes=etapes, tableau=tableau)

    elif adresse == "tri_par_selection":
        for i in range(len(tab)):  # i : valeur tout à gauche des valeurs non-triées
            min = i  # Part du principe que i est la plus petite valeur
            for j in range(i + 1, len(tab)):  # Parcourt toutes les valeurs non triées
                if tab[j] < tab[min]:  # Si une valeur et celle d’après ne sont pas dans le bon ordre
                    min = j  # Définit le nouveau minimum
            if min != i:  # Si le minimum n’est pas tout à gauche, on inverse
                tab[i], tab[min] = tab[min], tab[i]
            etapes += f"Etape n°{i + 1} : {tab} \n"

        return render_template('tri_selection.html', tableau_etapes=etapes, tableau=tableau)

app.run(debug=True)
