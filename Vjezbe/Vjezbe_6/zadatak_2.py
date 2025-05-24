from harmonic_oscillator import HarmonicOscillator

h = HarmonicOscillator(0.1, 10, 0.3, 0)

koraci = [0.05, 0.01, 0.001]
periodi = {}

for korak in koraci:
    pt = h.period_titranja(korak)
    periodi[korak] = pt

for korak in periodi:
    print(f"Period titranja je {periodi[korak]} za korak {korak}")