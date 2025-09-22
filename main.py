from pyscript import document

def compute_average(e):
    s1 = document.getElementById("score1").value
    s2 = document.getElementById("score2").value

    s1 = float(s1) if s1 else 0
    s2 = float(s2) if s2 else 0

    avg = (s1 + s2) / 2
    status = "Passed" if avg >= 75 else "Failed"

    msg = f"Average: {avg:.2f}\nResult: {status}"

    result_div = document.getElementById("result")
    result_div.innerText = msg

    # clear previous classes
    result_div.classList.remove("pass", "fail")

    # apply new class
    if status == "Passed":
        result_div.classList.add("pass")
    else:
        result_div.classList.add("fail")
