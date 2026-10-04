import argparse
from scenarios.runner import run_scenario

def main():
    parser = argparse.ArgumentParser(description="Run a scenario")
    parser.add_argument("--scenario", required=True, help="scenario")
    args = parser.parse_args()
    run_scenario(args.scenario)

if __name__ == "__main__":
    main()
