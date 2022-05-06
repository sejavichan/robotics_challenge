rosrun rqt_graph rqt_graph
# robotics_challenge
Robotic challenge scenarios for the Robotics and Advanced subject of UPO's Software Engineering Grade

## Installation instructions

This branch has been specifically adapted to the ROS Melodic and Noetic distributions. It has been tested in Ubuntu 18.04 and Ubuntu 20.04, respectively.

We provide you with a useful installation script that you can use for easily installing it into a ROS workspace. To use it you have to specify the target catkin workspace where the node should be installed. To do this you can use:

```
rosrun robotics_challenge install.bash
```

## How to use the challenge

The goal of the challenge is to setup the simulation environment in which your path tracking, path planning and collision avoidance modules should be used in order to guide the Turtlebot robot to a goal destination.

This configuration includes the setup of:

* A gazebo world file that has the environment where the robot is placed on.
* The spawn of a Turtlebot robot equipped with a LASER sensor and a RGBD camera.
* The localization module (AMCL) and the map that should be used as the frame to determine the navigation goals.

A convenient bash script is available for each scenario (1-3). Example:

```
$  rosrun robotics_challenge robotics_challenge_1.bash
```

## Instrucciones para ejecutar el challenge en los diferentes escenarios:

Para ejecutar el challenge en los diferentes escenarios primero habrá que ejecutar el escenario deseado, esto se hará accediendo a la ruta dentro de nuestro workspace:
catkin_ws/src/robotics_challenge/scripts

Una vez dentro de la ruta anterior, se ejecutará el comando 
```
./robotics_challenge_1.bash 
```
Siendo robotics_challenge_1.bash el escenario 1 y teniendo hasta 4 escenarios. Por lo que se podrá ejecutar el escenario que queramos.

Una vez esté abierto nuestro escenario hay que llamar con roslaunch en el paquete rva_basic_tools al fichero lanzador_challenge.launch
En la llamada se le podrá pasar por parámetros el "goal_x" y el "goal_y" que definirán a dónde queremos mandar el robot.

Un ejemplo de la llamada sería: 
```
roslaunch rva_basic_tools lanzador_challenge.launch goal_x:=1 goal_y:=1
```
En este caso para el escenario 1 el robot se dirigirá hacia la posición x=1 y=1 del escenario que tengamos ejecutado.

## Lanzador_challenge.launch

Se trata del launcher de nuestro código, en nuestro caso ejecuta 4 módulos:
1. El primer módulo se trata del planificador de caminos, el cual ejecuta el planner_node.py que se nutre del AStar.py el cual ejecuta un algoritmo de A* para calcular el camino hacia el punto pasado por parámetro.
2. El segundo módulo es el scan_downsampler, este módulo sirve para controlar los puntos que queremos obtener del laser y una vez los obtenemos los pasamos a un marcador.
3. Es el módulo de contro a un punto (ControlGoal), sirve para indicar al robot que velocidad angular y lineal tiene que tener para llegar al punto destino.
4. Por último, el cuarto módulo es el módulo de control de colisiones (coll_avoidance) que mediante el método de campos potenciales evita que si se interpone un obstáculo entre el punto objetivo y el robot, el robot colisione.



