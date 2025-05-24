import matplotlib.pyplot as plt

class HarmonicOscillator:
    def __init__(self, m, k, x, v):
        self.m = m
        self.k = k
        self.x = x
        self.v = v
        self.poz = []
        self.brzine = []
        self.akc = []
        self.koraci = []
    
    def oscillate(self, vrijeme, korak=0.01):
        i = 0
        x = self.x
        v = self.v
        a = -(self.k / self.m) * x

        self.poz.append(x)
        self.brzine.append(v)
        self.akc.append(a)
        self.koraci.append(0)
        while i < vrijeme:
            a = -(self.k / self.m) * x
            v = v + a * korak
            x = x + v * korak
            self.poz.append(x)
            self.brzine.append(v)
            self.akc.append(a)
            i += korak
            self.koraci.append(i)
    
    def reset(self):
        self.poz = []
        self.brzine = []
        self.akc = []
        self.koraci = []

    def period_titranja(self, korak=0.01):
        trenutno_t = 2
        period = None
        while period == None:
            self.oscillate(trenutno_t, korak)

            pocetna = None
            krajnja = None
            for i in range(len(self.poz) - 1):
                if self.poz[i + 1] < self.poz[i]:
                    if self.poz[i] >= 0 and self.poz[i + 1] < 0:
                        if pocetna == None:
                            pocetna = self.koraci[i]
                        else:
                            krajnja = self.koraci[i]
                            break

            if pocetna == None or krajnja == None:
                trenutno_t += 1
                self.reset()
                continue    

            period = krajnja - pocetna

        self.reset()
        return period

    def plot_trajectory(self):
        plt.figure(figsize=(10, 4))

        plt.subplot(1, 3, 1)
        plt.plot(self.koraci, self.poz)
        plt.xlabel("t (s)")
        plt.ylabel("x (m)")
        plt.title("x - t graf")
        plt.ylim(min(self.poz) - 0.1, max(self.poz) + 0.1)

        plt.subplot(1, 3, 2)
        plt.plot(self.koraci, self.brzine)
        plt.xlabel("t (s)")
        plt.ylabel("v (m/s)")
        plt.title("v - t graf")
        plt.ylim(min(self.brzine) - 0.1, max(self.brzine) + 0.1)

        plt.subplot(1, 3, 3)
        plt.plot(self.koraci, self.akc)
        plt.xlabel("t (s)")
        plt.ylabel("a (m / s ** 2)")
        plt.title("a - t graf")
        plt.ylim(min(self.akc) - 0.1, max(self.akc) + 0.1)

        plt.tight_layout()
        plt.show()