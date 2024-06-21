import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from ema_workbench import Scenario, Policy, MultiprocessingEvaluator
from ema_workbench.em_framework.samplers import sample_uncertainties
from problem_formulation import get_model_for_problem_formulation
from ema_workbench.util import ema_logging

ema_logging.log_to_stderr(ema_logging.INFO)

def run_simulation():
    # Load the model
    model, steps = get_model_for_problem_formulation(2)

    # Define a reference scenario
    reference_values = {
        "Bmax": 175,
        "Brate": 1.5,
        "pfail": 0.5,
        "discount rate 0": 3.5,
        "discount rate 1": 3.5,
        "discount rate 2": 3.5,
        "ID flood wave shape": 4
    }
    scen1 = {key.name: reference_values[key.name.split('_')[-1]] if '_' in key.name else reference_values[key.name] for
             key in model.uncertainties}
    ref_scenario = Scenario("reference", **scen1)

    # Define a policy
    zero_policy = {
        "DaysToThreat": 0,
        "DikeIncrease 0": 0,
        "DikeIncrease 1": 0,
        "DikeIncrease 2": 0,
        "RfR 0": 0,
        "RfR 1": 0,
        "RfR 2": 0
    }
    pol0 = {key.name: zero_policy[key.name.split('_')[-1]] for key in model.levers}
    policy0 = Policy("Policy 0", **pol0)

    # Generate multiple scenarios
    n_scenarios = 50
    scenarios = sample_uncertainties(model, n_scenarios)

    # Run experiments using MultiprocessingEvaluator
    with MultiprocessingEvaluator(model) as evaluator:
        experiments, outcomes = evaluator.perform_experiments(scenarios=scenarios, policies=[policy0])

    # Convert results to DataFrame
    results = pd.DataFrame.from_dict(outcomes)

    return results

def analyze_results(results):
    # Display summary statistics
    summary = results.describe()
    print(summary)

    # Print the columns to verify the correct names
    print("Columns in the results DataFrame:", results.columns)

    # Adjust column name for plotting
    column_to_plot = 'Expected Annual Damage'  # Adjust based on your requirements

    # Calculate mean value
    mean_value = results[column_to_plot].mean()

    # Plot example results
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=results, x=results.index, y=column_to_plot)
    plt.axhline(y=mean_value, color='green', linestyle='-', label=f'Mean: {mean_value:.2e}')
    plt.title('Expected Annual Damage Over Time')
    plt.xlabel('Experiment Index')
    plt.ylabel(column_to_plot)
    plt.legend()
    plt.savefig('InitialSetup.pdf', format='pdf', dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    results = run_simulation()
    analyze_results(results)
