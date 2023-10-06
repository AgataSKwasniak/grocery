chleb = 6.50
sok = 4.00
paczek = 5.50

a = int(input("Ile kupujesz chleba ? "))
b = int(input("Ile kupujesz soków ? "))
c = int(input("Ile kupujesz pączków ? "))

print(f"Twoje zamówienie to: "
                f"\n1. chlebów - {a} - razem: {chleb*a}"
                f"\n2. soków - {b} - razem: {sok*b}"
                f"\n3. paczków - {c} - razem: {paczek*c}"
                f"\nRazem do zapłaty: {(chleb*a)+(sok*b)+(paczek*c)}")


print("Druga opcja zapisania:")
x = 6.50 #chleb
y = 4.00 #sok
z = 5.50 #paczek

a = int(input("Ile kupujesz chleba ? "))
b = int(input("Ile kupujesz soków ? "))
c = int(input("Ile kupujesz pączków ? "))

suma = x*a + y*b + z*c

print(f"Twoje zamówienie to: "
                f"\n1. chlebów - {a} - razem: {x*a}"
                f"\n2. soków - {b} - razem: {y*b}"
                f"\n3. paczków - {c} - razem: {z*c}"
                f"\nRazem do zapłaty: {suma}")


