import random



scorePlayer = 0
scoreCPU = 0
choixPlayer = ''
choixCPU = ''

def choisir(choixPlayer):

    choixPlayer = input("\n 1: Pierre \n 2: Papier \n 3: Ciseaux \n Votre choix (1/2/3) : ")

    while(choixPlayer not in "123"):

        print("\n Votre choix n'est pas valide. Veuillez réessayer \n")
        choixPlayer = input(" 1: Pierre \n 2: Papier \n 3: Ciseaux \n Votre choix (1/2/3) : ")

    return convertir(int(choixPlayer))

def convertir(choix):
    if(choix == 1):
        resultat = 'Pierre'
    elif choix == 2:
        resultat = 'Papier'
    else:
        resultat = 'Ciseaux'
    return resultat

def comparer():
    
    global choixCPU, choixPlayer, scorePlayer, scoreCPU

    if(choixPlayer != choixCPU):
        
        if(choixPlayer=="Papier" and choixCPU =="Pierre"):
            scorePlayer += 1
        
        elif (choixPlayer=="Papier" and choixCPU =="Ciseaux"):
            scoreCPU += 1
        
        elif (choixPlayer == "Pierre" and choixCPU == "Papier"):
            scoreCPU += 1
        
        elif (choixPlayer=="Pierre" and choixCPU == "Ciseaux"):
            scorePlayer+=1
        
        elif (choixPlayer == "Ciseaux" and choixCPU == "Pierre"):
            scoreCPU+=1
        else:
            scorePlayer+=1

def main():

    global choixPlayer, choixCPU
    print("Bienvenu sur le pierre-papier-ciseaux. Le premier qui atteint un score de 2 gagne")
    
    while(scorePlayer < 5 and scoreCPU < 5):

        choixPlayer = choisir(choixPlayer)
        choixCPU = convertir(random.randrange(3))
        
        comparer()
        
        print('')
        print("Votre choix : " + choixPlayer +" vs choix CPU: " +choixCPU)
        print("Votre score : " + str(scorePlayer) + " vs score CPU : " + str(scoreCPU))

    if(scoreCPU <scorePlayer):
        print("Bravo ! Vous avez gagné")
    else:
        print("Désolé, vous êtes nuls")
main()