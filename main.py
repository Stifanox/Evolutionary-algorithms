from GUI.ApplicationGUI import ApplicationGUI
from Evolution.EvolutionBuilder import EvolutionBuilder
from threading import Thread


def startEvo(appGUI: ApplicationGUI):
    appParams = appGUI.getParameters()
    evolution = EvolutionBuilder(appParams) \
        .setSelection(appParams.selectionType, appParams.selectionNumOrPercent,
                      appParams.selectionArgument) \
        .setElitism(appParams.elitismType, appParams.elitismArgument, appParams.toMaximize) \
        .setInverse(appParams.useInversion, appParams.inversionProbability) \
        .setMutation(appParams.mutationType, appParams.mutationProbability) \
        .setMaximize(appParams.toMaximize) \
        .setShowChart(appParams.showChart) \
        .setCrossover(appParams.crossoverType, appParams.crossoverArgument) \
        .buildEvolution(appParams.specimenCount, appParams.epochCount, appParams.chromosomePrecision)

    Thread(target=evolution.startEvolution, args=[appGUI.renderPlot, appGUI.showResult], daemon=True).start()


def quitProgram(appGUI: ApplicationGUI):
    appGUI.quit()
    appGUI.destroy()


if __name__ == '__main__':
    app = ApplicationGUI(lambda: startEvo(app))
    app.protocol("WM_DELETE_WINDOW", lambda: quitProgram(app))
    app.mainloop()
