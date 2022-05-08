# robotics_challenge
Escenarios del challenge de robótica 

## Instrucciones de instalación

Para su instalación en el workspace de ROS se ha de ejecutar un script. Para ello ejecutaremos el siguiente comando:

```
rosrun robotics_challenge install.bash
```

## Como ejecutar el challenge en los diferentes escenarios:

El objetivo del challenge es que una vez dentro de la simulación, el robot pueda ir al punto indicado de destino sin que colisione y con una velocidad óptima.

Para ejecutar el challenge en los diferentes escenarios primero habrá que ejecutar el escenario deseado, esto se hará ejecutando el siguiente comando:
```
rosrun robotics_challenge robotics_challenge_1.bash 
```
Siendo robotics_challenge_1.bash el escenario 1 y teniendo hasta 4 escenarios. Por lo que se podrá ejecutar el escenario que se desee.

Una vez esté abierto nuestra simulación hay que llamar con roslaunch en el paquete rva_basic_tools al fichero lanzador_challenge.launch
En la llamada se le podrá pasar por parámetros el "goal_x" y el "goal_y" que definirán a dónde queremos mandar el robot.

Un ejemplo de la llamada sería: 
```
roslaunch rva_basic_tools lanzador_challenge.launch goal_x:=1 goal_y:=1
```
En este caso el robot se dirigirá hacia la posición x=1 y=1 del escenario que tengamos ejecutado.

## Lanzador_challenge.launch

Se trata del launcher de nuestro código, en nuestro caso ejecuta 4 módulos:
1. El primer módulo se trata del planificador de caminos, el cual ejecuta el planner_node.py que se nutre del AStar.py el cual ejecuta un algoritmo de A* para calcular el camino hacia el punto pasado por parámetro.
  
  -Parámtros:
    
    goal/x-->Será lo que indique la coordenada X del punto destino
    goal/y-->Será lo que indique la coordenada Y del punto destino

2. El segundo módulo es el scan_downsampler, este módulo sirve para controlar los puntos que queremos obtener del laser y una vez los obtenemos los pasamos a un marcador.
3. Es el módulo de contro a un punto (ControlGoal), sirve para indicar al robot que velocidad angular y lineal tiene que tener para llegar al punto destino.
4. Por último, el cuarto módulo es el módulo de control de colisiones (coll_avoidance) que mediante el método de campos potenciales evita que si se interpone un obstáculo entre el punto objetivo y el robot, el robot colisione.



