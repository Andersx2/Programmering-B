from matplotlib import pyplot as plt

def f(x):
    """Holder på den ønskede funktion"""
    return x**2-9
def df(x):
    """Holder på den ønskede funktion differentieret"""
    return 2*x

def newton(f, df, x, acc):
    """ Tager en funktion: f, f', et startgæt af nulpunkt og den ønskede nøjagtigehed.
        Retunerer det fundne nulpunktet"""
    while abs(f(x)) > acc:
        #   x = x - f(x) / df(x)
        x = x - float(f(x)/df(x))
        print(x)
        plt.scatter(x, f(x), s=50)
    return x


if __name__ == "__main__":
    print("Endelige svar: " + str(newton(f, df, 1000, acc=0.0001)))
    plt.xlabel("x-akse")
    plt.ylabel("y-akse")
    plt.title("Nulpunktssøgning med Newtons metode")
    plt.show()


