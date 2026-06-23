from report import generate_report

sample = {

    "temperature":30,

    "humidity":62,

    "wind":5,

    "cloud":18,

    "dni":725,

    "power":3.08

}

file = generate_report(sample)

print(file)