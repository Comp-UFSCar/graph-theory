__author__ = 'Thales'
import datetime

def write_simulation(data, uk12=True, wg59=True, usair97=True):

    uk12_data = ""
    wg59_data = ""
    usair97_data = ""

    if uk12 is True:
        # Gera relatorio para grafo UK12
        uk12_data += \
            "Grafo UK12:\n" \
            "\na) Sementes utilizadas: " + str(data['uk12']['a']['seeds'])+ "\n"

        for i in data['uk12']['a']['seeds']:
            uk12_data += "\t\t" + str(i) + " = " + str(len(data['uk12']['a']['nodelist'][i])) +\
                         " vertices conectados\n\t\t\tVertices: " + str(data['uk12']['a']['nodelist'][i]) + "\n\n"

        uk12_data += "\t\tVertice\tLabel\tPi\tLambda\n"
        for i in data['uk12']['grafo'].nodes():
            uk12_data += "\t\t" + str(i) + "\t" +\
                         str(data['uk12']['lbl'][i]) +"\t" +\
                         str(data['uk12']['a']['pi'][i]) + "\t" +\
                         str(data['uk12']['a']['lambda'][i]) + "\n"

        uk12_data += \
            "\nb) Sementes utilizadas: " + str(data['uk12']['b']['seeds'])+ "\n"

        for i in data['uk12']['b']['seeds']:
            uk12_data += "\t\t" + str(i) + " = " + str(len(data['uk12']['b']['nodelist'][i])) +\
                         " vertices conectados\n\t\t\tVertices: " + str(data['uk12']['b']['nodelist'][i]) + "\n\n"

        uk12_data += "\t\tVertice\tLabel\tPi\tLambda\n"
        for i in data['uk12']['grafo'].nodes():
            uk12_data += "\t\t" + str(i) + "\t" +\
                         str(data['uk12']['lbl'][i]) +"\t" +\
                         str(data['uk12']['b']['pi'][i]) + "\t" +\
                         str(data['uk12']['b']['lambda'][i]) + "\n"

        # Escreve todos os relatorio no arquivo '/generated-data/simulation_results_uk12'
        try:
            f = open('../generated-data/uk12_simulation_results.txt', "w")
            f.write("Simulacao gerada em\t"+ str(datetime.datetime.today()) + "\n\n")
            f.write(uk12_data)
            f.close()
        except IOError:
            print "Erro na escrita do arquivo de simulacao"


    if wg59 is True:
        # Gera relatorio para grafo WG59
        wg59_data += \
            "Grafo WG59:\n" \
            "\na) Sementes utilizadas: " + str(data['wg59']['a']['seeds'])+ "\n"

        for i in data['wg59']['a']['seeds']:
            wg59_data += "\t\t" + str(i) + " = " + str(len(data['wg59']['a']['nodelist'][i])) +\
                         " vertices conectados\n\t\t\tVertices: " + str(data['wg59']['a']['nodelist'][i]) + "\n\n"

        wg59_data += "\t\tVertice\tLabel\tPi\tLambda\n"
        for i in data['wg59']['grafo'].nodes():
            wg59_data += "\t\t" + str(i) + "\t" +\
                         str(data['wg59']['lbl'][i]) +"\t" +\
                         str(data['wg59']['a']['pi'][i]) + "\t" +\
                         str(data['wg59']['a']['lambda'][i]) + "\n"

        wg59_data += \
            "\nb) Sementes utilizadas: " + str(data['wg59']['b']['seeds'])+ "\n"

        for i in data['wg59']['b']['seeds']:
            wg59_data += "\t\t" + str(i) + " = " + str(len(data['wg59']['b']['nodelist'][i])) +\
                         " vertices conectados\n\t\t\tVertices: " + str(data['wg59']['b']['nodelist'][i]) + "\n\n"

        wg59_data += "\t\tVertice\tLabel\tPi\tLambda\n"
        for i in data['wg59']['grafo'].nodes():
            wg59_data += "\t\t" + str(i) + "\t" +\
                         str(data['wg59']['lbl'][i]) +"\t" +\
                         str(data['wg59']['b']['pi'][i]) + "\t" +\
                         str(data['wg59']['b']['lambda'][i]) + "\n"

        # Escreve todos os relatorio no arquivo '/generated-data/simulation_results_wg59'
        try:
            f = open('../generated-data/wg59_simulation_results.txt', "w")
            f.write("Simulacao gerada em\t"+ str(datetime.datetime.today()) + "\n\n")
            f.write(wg59_data)
            f.close()
        except IOError:
            print "Erro na escrita do arquivo de simulacao"

    if usair97 is True:

        # Gera relatorio para grafo USAir97
        usair97_data += \
            "Grafo USAir97:\n" \
            "\na) Sementes utilizadas: " + str(data['usair97']['a']['seeds'])+ "\n"

        for i in data['usair97']['a']['seeds']:
            usair97_data += "\t\t" + str(i) + " = " + str(len(data['usair97']['a']['nodelist'][i])) +\
                         " vertices conectados\n\t\t\tVertices: " + str(data['usair97']['a']['nodelist'][i]) + "\n\n"

        usair97_data += "\t\tVertice\tLabel\tPi\tLambda\n"
        for i in data['usair97']['grafo'].nodes():
            usair97_data += "\t\t" + str(i) + "\t" +\
                         str(data['usair97']['lbl'][i]) +"\t" +\
                         str(data['usair97']['a']['pi'][i]) + "\t" +\
                         str(data['usair97']['a']['lambda'][i]) + "\n"

        usair97_data += \
            "\nb) Sementes utilizadas: " + str(data['usair97']['b']['seeds'])+ "\n"

        for i in data['usair97']['b']['seeds']:
            usair97_data += "\t\t" + str(i) + " = " + str(len(data['usair97']['b']['nodelist'][i])) +\
                         " vertices conectados\n\t\t\tVertices: " + str(data['usair97']['b']['nodelist'][i]) + "\n\n"

        usair97_data += "\t\tVertice\tLabel\tPi\tLambda\n"
        for i in data['usair97']['grafo'].nodes():
            usair97_data += "\t\t" + str(i) + "\t" +\
                         str(data['usair97']['lbl'][i]) +"\t" +\
                         str(data['usair97']['b']['pi'][i]) + "\t" +\
                         str(data['usair97']['b']['lambda'][i]) + "\n"

        # Escreve todos os relatorio no arquivo '/generated-data/simulation_results_usair97'
        try:
            f = open('../generated-data/usair97_simulation_results.txt', "w")
            f.write("Simulacao gerada em\t"+ str(datetime.datetime.today()) + "\n\n")
            f.write(usair97_data)
            f.close()
        except IOError:
            print "Erro na escrita do arquivo de simulacao"