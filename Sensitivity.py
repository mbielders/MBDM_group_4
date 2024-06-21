import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from ema_workbench import (Scenario, Policy, MultiprocessingEvaluator, perform_experiments)
from ema_workbench.em_framework.samplers import sample_uncertainties
from problem_formulation import get_model_for_problem_formulation
from ema_workbench.analysis import feature_scoring
from ema_workbench.util import ema_logging

ema_logging.log_to_stderr(ema_logging.INFO)


def run_sensitivity_analysis():
    # Load the model
    model, steps = get_model_for_problem_formulation(2)

    # Generate multiple scenarios for sensitivity analysis
    n_scenarios = 500
    scenarios = sample_uncertainties(model, n_scenarios)

    # Define a policy (using the same zero policy as before)
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

    # Run experiments using MultiprocessingEvaluator
    with MultiprocessingEvaluator(model) as evaluator:
        experiments, outcomes = evaluator.perform_experiments(scenarios=scenarios, policies=[policy0])

    return experiments, outcomes


def analyze_sensitivity(experiments, outcomes):
    # Convert results to DataFrame
    df = pd.DataFrame.from_dict(outcomes)

    # Perform feature scoring to identify important variables
    scores = feature_scoring.get_feature_scores_all(experiments, outcomes)

    # Display feature scores
    print(scores)

    # Plot feature scores for 'Expected Annual Damage'
    sns.set(style="whitegrid")
    plt.figure(figsize=(20, 10))
    sns.barplot(x=scores.index, y=scores['Expected Annual Damage'])
    plt.title('Sensitivity Analysis: Feature Scores for Expected Annual Damage')
    plt.xticks(rotation=45, ha='right')
    plt.xlabel('Uncertainty and Policy Levers')
    plt.ylabel('Feature Score')
    plt.tight_layout()
    plt.savefig('Sensitivity.pdf', format='pdf', dpi=300, bbox_inches='tight')
    plt.show()



if __name__ == "__main__":
    experiments, outcomes = run_sensitivity_analysis()
    analyze_sensitivity(experiments, outcomes)
