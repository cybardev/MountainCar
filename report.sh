#!/usr/bin/env bash
# ------------------------------------------------ #
#                                                  #
#         Test the Mountain Car simulation         #
#      and generate reports in markdown format     #
#                                                  #
# ------------------------------------------------ #

# -------------- required variables -------------- #

PROGRAM="MountainCar"

states=("5" "10" "20" "100")
alphas=("0.01" "0.1" "0.5")

# --------------- utility functions -------------- #

function lb() {
    echo ""
}

function hr() {
    lb
    [[ -n "$1" ]] && echo "$1" || echo "---"
    lb
}

function observation() {
    echo "**Observation**: Goal was reached after -K reward."
    hr
}

# ------------------------------------------------ #
#
# run program with different parameters and generate results for each
#
# ------------------------------------------------ #

mkdir "tmp"

for state in ${states[@]}; do
    echo "Starting program with state $state"
    python3 "./$PROGRAM.py" -s "$state" >> "tmp/results_s$state.md" &
    lb
done

for alpha in ${alphas[@]}; do
    echo "Starting program with alpha $alpha"
    python3 "./$PROGRAM.py" -a "$alpha" >> "tmp/results_a$alpha.md" &
    lb
done

# allow all results to be generated
echo "waiting for all simulations to complete..."
wait
echo "Simulations complete. Generating report..."

# ------------------------------------------------ #
#
# aggregate individual results into a single report
#
# ------------------------------------------------ #

function report_gen() {
    REPORT_LINES=15

    echo "# $PROGRAM Report"
    lb
    echo "**Author**: Sheikh Saad Abdullah"
    lb
    echo "## Varying states between 5, 10, 20, 100 with fixed alpha of 0.1"
    hr

    for state in ${states[@]}; do
        head -n $REPORT_LINES "tmp/results_s$state.md"
        hr "..."
        tail -n $REPORT_LINES "tmp/results_s$state.md"
        observation
    done

    echo "## Varying alpha between 0.01, 0.1, 0.5 with fixed state of 10"
    hr

    for alpha in ${alphas[@]}; do
        head -n $REPORT_LINES "tmp/results_a$alpha.md"
        hr "..."
        tail -n $REPORT_LINES "tmp/results_a$alpha.md"
        observation
    done
}

report_gen > "$PROGRAM.md"
echo "Report generated. Cleaning up..."

# ----------------- cleaning up ------------------ #

[[ -d "./tmp" ]] && rm -rf "./tmp"
echo "All Done!"

# --------------------- END ---------------------- #

