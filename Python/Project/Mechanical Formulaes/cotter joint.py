from math import sqrt, pi, ceil

print("Enter load in tension and compression")
P = float(input())
print("Enter factor of safety")
Nf = float(input())

# todo: Socket and Spigot
print("Enter Yield strength in tension for Socket and Spigot")
Sytss = float(input())
stss = Sytss / Nf
print(f"Sigma tension for spigot and socket = {stss} N/mm^2")

print("Enter Yield strength percentage in compression for Socket and Spigot")
Sycss = float(input())
scss = (Sytss * Sycss) / Nf
print(f"Sigma Compression for Spigot and Socket = {scss} N/mm^2")

print("Enter Yield strength percentage in shear for Socket and Spigot")
Sysss = float(input())
tss = (Sytss * Sysss) / Nf
print(f"Sigma Shear for Spigot and Socket = {tss} N/mm^2")

# Cotter
print("Enter Yield strength in tension for Cotter")
Sytc = float(input())
stc = Sytc / Nf
print(f"Sigma tension in cotter = {stc} N/mm^2")

scc = (Sytc * Sycss) / Nf
print(f"Sigma compression in cotter = {scc} N/mm^2")

tc = (Sytc * Sysss) / Nf
print(f"Sigma Shear for cotter = {tc} N/mm^2")

d = ceil(sqrt((P / stss) * (4 / pi))) + 4
print("\nDiameter of Rod(d) = ", d)

t = ceil(0.3 * d)
print("Thickness of cotter(t) = ", t)

l1 = (t * (4 / pi)) / 2
l2 = sqrt((-l1) ** 2 + 4 * (P / stss) * (4 / pi)) / 2
l3 = [l1 - l2, l1 + l2]
d1s = max(l3)
d1c = P / (scc * t)
d1 = ceil(max([d1s, d1c]))
print("Diameter of Spigot(d1) = ", d1)

d2 = ceil(sqrt((4 * P) / (pi * scss) + d1 ** 2))
print("Diameter of Spigot collar(d2) = ", d2)

t1 = ceil(P / (pi * d1 * tss))
print("Thickness of Spigot collar(t1) = ", t1)

a = ceil(P / (2 * d1 * tss))
print("Distance from end of slot to end of spigot(a) = ", a)

h1 = (4 * t) / pi
h2 = sqrt(h1 ** 2 + 4 * ((d1 ** 2) - ((d1 * t) * (4 / pi)) + (P / stss) * (4 / pi)))
D1 = max([(h1 + h2) / 2, (h1 - h2) / 2])
print("Outside diameter of socket(D1) = ", ceil(D1))

D2 = (P / (scc * t)) + d1
print('Diameter of socket collar(D2) = ', ceil(D2))

c = P / (2 * tss * (D2 - d1))
print("Thickness of socket(c) = ", ceil(c))

b1 = P / (2 * t * tc)
b2 = sqrt((6*((D2/2)*(((D2-d1)/6)+(d1/4))))/(t*stc))
b = max([b1, b2])
print("Width of cotter(b) = ", ceil(b))
