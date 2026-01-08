# This function computes the average of two quiz scores
# It displays whether the student passed or failed

from pyscript import document, display


def compute_average(e):
    # Get scores from input fields
    score1 = float(document.getElementById("score1").value)
    score2 = float(document.getElementById("score2").value)


# Calculate average
    average = (score1 + score2) / 2

# Determine pass/fail status
    if average >= 85:
        result = "✅ Passed"
    elif average <= 80:
        result = "❌ Failed"
    else:
        result = "❌ Failed"

    # Indicate what happens next
    document.getElementById("result").innerText = f"Average: {average:.2f}"
    document.getElementById("average").innerText = result