def weight_on_planets():
    epounds = float(input("What do you weigh on earth? "))

    mpounds = epounds * .38
    jpounds = epounds * 2.34


    print("\nOn Mars you would weigh", mpounds, "pounds.\nOn Jupiter you would weigh", jpounds, "pounds.")


if __name__ == '__main__':
    weight_on_planets()
