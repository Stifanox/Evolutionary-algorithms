![logo.png](https://github.com/Stifanox/Evolutionary-algorithms/blob/bb34c6e17d6a08289dfba04dcb2d06733d1178d1/Resources/logo.png)
---
![](https://img.shields.io/badge/Politechnika-Krakowska-blue?style=flat)
![](https://img.shields.io/github/commit-activity/m/Stifanox/Evolutionary-algorithms?style=flat&color=009151)
![](https://img.shields.io/github/languages/top/Stifanox/Evolutionary-algorithms?style=flat&color=009151)

### This project implements genetic algorithms in Python.

# :star: Features
Feature|Details
---|---
Crossover|:heavy_check_mark: k-point, shuffle, discrete, uniform
Selection|:heavy_check_mark: top, roulette, tournament
Mutation|:heavy_check_mark: edge, single-point, two-point
Elitism|:heavy_check_mark: by percent, by count
Inversion|:heavy_check_mark: implemented
GUI|:heavy_check_mark: implemented (in Tkinter)
Plots|:heavy_check_mark: implemented (in Matplotlib)
File export|:heavy_check_mark: implemented

# :test_tube: Built-in functions
### The repository contains many built-in functions:
Hypersphere, Hyperellipsoid, Schwefel, Ackley, Michalewicz, Rastrigin, Rosenbrock, De Jong 3, De Jong 5, Martin And Gaddy, Griewank, Easom, Goldstein And Price, Picheny Goldstein And Price, Styblinski And Tang, Mc Cormick, Rana, Egg Holder, Keane, Schaffer 2, Himmelblau, Pits And Holes.

# :hammer_and_wrench: Prerequisites
In order to run this code, the end user must install the following list of programs and libraries:

* Python 3.10
* Matplotlib
* Numpy
* Scipy
* Multimethod
* Benchmark-functions

# :dna: Usage
After you have downloaded (or cloned) this repository, you can immediately begin to simulate the evolution by following these simple steps:
1. Select `main.py` and run it via Python interpreter.
2. Configuration window will pop up. You can set every parameter including, but not limited to the examined function, crossover type, selection type, and so on.
3. Click `Start evolution` button. Depending on the speed of your machine and selected settings, the evolution may take a while.
4. If you checked `Show chart` option previously, plots will be updated from time to time.
5. Once the simulation is complete, summary window will show the results.
6. You can now also view `EvolutionSave_` files, which contain statistics for every epoch.

# :movie_camera: Demonstration
![animation.gif](https://github.com/Stifanox/Evolutionary-algorithms/blob/bb34c6e17d6a08289dfba04dcb2d06733d1178d1/Resources/animation.gif)
