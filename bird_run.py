DATA_PATH = ""
import os
import sys
import time
from ecoscape_utilities import BirdRun
from ecoscape_connectivity import compute_connectivity, half_cauchy
from ecoscape_connectivity.util import read_transmission_csv

def run_birds(run_name=None, use_cauchy=True, use_permeability=True, num_simulations=1000):

    if run_name is None:
        run_name = f"Run_cauchy:{use_cauchy}_permeability:{use_permeability}_num_simulations:{num_simulations}"

    bird_run = BirdRun(DATA_PATH)

    bird_states = {
        "stejay": ["US-AZ", "US-CA", "US-CO", "US-ID", "US-MT", "US-NM", "US-NV", "US-OR", "US-UT",  "US-WA", "US-WY"]}
    bird_names = {
        "stejay": "Steller's Jay"
    }
    if use_cauchy:
        bird_dispersal = {
            "stejay": half_cauchy(22, 22 * 4), # 6.7 Km
         }
    else:
        bird_dispersal = {
            "stejay": 22, # 6.7 Km
        }

    birds = []

    for bird, states in bird_states.items():
        for state in states:
            birds.append(bird_run.get_bird_run(
                bird, bird_names.get(bird), state=state, run_name=run_name))

    start_t = time.time()
    for bird in birds:
        print("Computing:", bird.name, "in", bird.state)

        # Creates output folder, if missing.
        # bird_run.createdir_for_file(bird.repopulation_fn)
        # bird_run.createdir_for_file(bird.gradient_fn)

        transmission_d = read_transmission_csv(bird.transmission_fn) if use_permeability else {}

        t0 = time.time()
        compute_connectivity(
            habitat_fn=bird.habitat_fn,
            landcover_fn=bird.terrain_fn,
            connectivity_fn=bird.repopulation_fn,
            permeability_dict=transmission_d,
            dispersal=bird_dispersal[bird.nickname],
            num_simulations=num_simulations,
            single_tile=True
        )

        print("Processed", bird.name, "in", bird.state, "in", time.time() - t0, "seconds")
    print("Total time:", time.time() - start_t)

run_birds(use_cauchy=True, use_permeability=True, num_simulations=1000)
run_birds(use_cauchy=False, use_permeability=True, num_simulations=1000)
run_birds(use_cauchy=True, use_permeability=False, num_simulations=1000)
