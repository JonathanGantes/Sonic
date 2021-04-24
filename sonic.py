import retro
import csv

#Abriendo el csv con los movimientos y luego lo pasamos a una lista
with open('Movimiento2.csv', newline='') as f:
    reader = csv.reader(f)
    movimientos = list(reader)

env = retro.make('SonicTheHedgehog-Genesis', 'GreenHillZone.Act1')

env.reset()

done = False
x=0
while not done:
    env.render()

    action = movimientos[x]
    ob, rew, done, info = env.step(action)
    print("Action ", action, "Reward ", rew)
    x=x+1
