import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from ema_workbench import (Scenario, Policy, MultiprocessingEvaluator)
from ema_workbench.em_framework.samplers import sample_levers, sample_uncertainties
from problem_formulation import get_model_for_problem_formulation
from ema_workbench.util import ema_logging

ema_logging.log_to_stderr(ema_logging.INFO)


def run_scenario_discovery():
    # Load the model
    model, steps = get_model_for_problem_formulation(2)

    # Generate multiple scenarios for scenario discovery
    n_scenarios = 100
    scenarios = sample_uncertainties(model, n_scenarios)

    # Sample lever values
    lever_samples = list(sample_levers(model, n_scenarios))

    # Define policies with varied RfR and DikeIncrease levers
    policies = [Policy(f'policy_{i}', **sample) for i, sample in enumerate(lever_samples)]

    # Run experiments using MultiprocessingEvaluator
    with MultiprocessingEvaluator(model) as evaluator:
        experiments, outcomes = evaluator.perform_experiments(scenarios=scenarios, policies=policies)

    return experiments, outcomes


def analyze_scenario_discovery(experiments, outcomes):
    # Convert experiments to DataFrame
    experiments_df = pd.DataFrame.from_dict(experiments)
    outcomes_df = pd.DataFrame.from_dict(outcomes)

    # Combine experiments and outcomes into one DataFrame
    df = pd.concat([experiments_df, outcomes_df], axis=1)

    # Perform k-means clustering on the outcomes
    kmeans = KMeans(n_clusters=3)
    df['Cluster'] = kmeans.fit_predict(outcomes_df)

    # Analyze the clusters
    cluster_centers = kmeans.cluster_centers_
    print("Cluster Centers:")
    print(cluster_centers)

    # Visualize the clusters
    sns.pairplot(df, hue='Cluster',
                 vars=['Expected Annual Damage', 'Dike Investment Costs', 'RfR Investment Costs', 'Evacuation Costs',
                       'Expected Number of Deaths'])
    plt.suptitle('Scenario Discovery Clusters')
    plt.savefig('Scenario.png', format='png', dpi=1000, bbox_inches='tight')
    plt.show()

    # Summarize the key characteristics of each cluster
    cluster_summary = df.groupby('Cluster').mean()
    print("Cluster Summary:")
    print(cluster_summary)


if __name__ == "__main__":
    experiments, outcomes = run_scenario_discovery()
    analyze_scenario_discovery(experiments, outcomes)
