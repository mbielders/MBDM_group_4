# EPA-simmodel

This project includes scripts for setting up and running sensitivity, scenario, and dike model analyses. The files included are `InitialSetup.py`, `Scenario.py`, `Sensitivity.py`, `dike_model_function.py`, `dike_model_simulation.py`, `dike_model_optimization.py`, `funs_dikes.py`, `funs_economy.py`, `funs_generate_network.py`, `funs_hydrostat.py`, `problem_formulation.py`, `Problem Formulations.ipynb`, and `EPAcourse_presentation.pptx`.

## Files

The set-up of the first three files will be explained in more details further below. 

### 1. InitialSetup.py
This script handles the initial setup for the project. It includes the necessary configurations and preparations needed before running any analyses.

### 2. Scenario.py
This script is responsible for defining and running different scenarios. It allows the user to specify various conditions and parameters to evaluate different outcomes.

### 3. Sensitivity.py
This script performs sensitivity analyses. It helps in understanding how the variation in input parameters can impact the results of the analysis.

### 4. dike_model_function.py
This script contains functions related to the dike model. It includes the core functions needed for dike modeling.

### 5. dike_model_simulation.py
This script simulates the dike model using the functions defined in `dike_model_function.py`.

### 6. dike_model_optimization.py
This script performs optimization on the dike model, aiming to find the best parameters that meet the defined objectives.

### 7. funs_dikes.py
This script contains additional utility functions related to dike analysis.

### 8. funs_economy.py
This script includes functions related to economic analysis within the project.

### 9. funs_generate_network.py
This script provides functions to generate network structures needed for the analysis.

### 10. funs_hydrostat.py
This script includes hydrological and statistical functions required for the analysis.

### 11. problem_formulation.py
This script defines the problem formulations for the analyses conducted within this project.

### 12. Problem Formulations.ipynb
This Jupyter Notebook contains interactive problem formulations for analysis and experimentation.

### 13. Problem formulation.py
This script version of `Problem Formulations.ipynb` provides an alternative approach for defining and running problem formulations.



## Explanation of Simulation and Analysis Files 1, 2 and 3

The code leverages the `ema_workbench` for exploratory modeling and analysis, as well as `pandas`, `matplotlib`, and `seaborn` for data handling and visualization.

The code consists of two main functions, one that runs the simulation and the second that analyses the results and shows the requested results. 


## Usage

- Ensure all scripts are in the same directory.
- Modify the scripts as necessary to fit your specific use case.

## Contact

For any questions or inquiries, please contact Group 4. The mails can be found through the Brightspace page of the course.