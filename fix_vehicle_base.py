""""
1. Kreiraj prazan rječnik koji predstavlja bazu vozila.

2. Za svako vozilo:
    - Dodaj novi unos u rječnik.
    - Ključ neka bude jedinstveni broj (ID).
    - Vrijednost bude novi rječnik sa sljedećim ključevima:
        - 'tip'
        - 'proizvođač'
        - 'registarska oznaka'
        - 'godina prve registracije'
        - 'cijena u eur'

3. Pripremi ispis:
    - Prvo ispiši naslovni red (naslove svih kolona), npr.:
        TIP | PROIZVOĐAČ | REGISTARSKA | GODINA | CIJENA
      (odvoji ih tabovima ili formatiraj da bude uredno)

4. Prođi kroz rječnik s vozilima:
    - Za svaki ID i vozilo:
        - Ispiši ID, zatim TAB, zatim podatke iz rječnika vozila.
        - Prati isti redoslijed kolona kao u naslovu.

5. Završeno!


*Ako zapneš u 4. koraku (kako ispisati podatke iz unutarnjeg rječnika u pravilnom redoslijedu),
pokušaj prvo ručno navesti redoslijed ključeva koje želiš ispisivati.

"""

#1 - Kreiraj prazan rječnik koji predstavlja bazu vozila
vehicle_base = {}

#2 - Dodajte vozila u bazu podataka s jedinstvenim ID-om kao ključem i detaljima vozila kao ugniježđenim rječnikom
# Svaki unos vozila sadrži: tip, proizvođača, registarsku oznaku, godinu registracije i cijenu u EUR


# Dodavanje prvog vozila s ID-om 1
vehicle_base[1] = {
    'tip': 'Sedan',  
    'proizvođač': 'BMW', 
    'registarska oznaka': 'ZG-1234-AB', 
    'godina prve registracije': 2020,  
    'cijena u eur': 35000  
}

# Dodavanje prvog vozila s ID-om 2
vehicle_base[2] = {
    'tip': 'SUV',  
    'proizvođač': 'Audi', 
    'registarska oznaka': 'ST-5678-CD',  
    'godina prve registracije': 2019,  
    'cijena u eur': 42000  
}

# Dodavanje prvog vozila s ID-om 3
vehicle_base[3] = {
    'tip': 'Hatchback',  
    'proizvođač': 'Volkswagen',  
    'registarska oznaka': 'RI-9012-EF',   
    'godina prve registracije': 2021,  
    'cijena u eur': 28000  
}

# Dodavanje prvog vozila s ID-om 4
vehicle_base[4] = {
    'tip': 'Coupe',  
    'proizvođač': 'Mercedes-Benz',  
    'registarska oznaka': 'OS-3456-GH', 
    'godina prve registracije': 2022,  
    'cijena u eur': 55000 
}

#3 - Pripremi i ispišite zaglavlje retka s naslovima stupaca
print(f"{'ID':<3} {'TIP':<12} {'PROIZVOĐAČ':<15} {'REGISTARSKA':<12} {'GODINA':<6} {'CIJENA':<8}")
print("-" * 70) 


#4 - Prodi kroz rječnik vozila i ispisi podatke za svako vozilo
# Definiraj redoslijed ključeva
key_order = ['tip', 'proizvođač', 'registarska oznaka', 'godina prve registracije', 'cijena u eur']


# Prođi kroz svaki ID vozila i podatke o vozilu
for vehicle_id, vehicle_data in vehicle_base.items():
    tip = vehicle_data['tip']
    proizvodjac = vehicle_data['proizvođač']
    registarska = vehicle_data['registarska oznaka']
    godina = vehicle_data['godina prve registracije']
    cijena = vehicle_data['cijena u eur']
    

# Ispis
    print(f"{vehicle_id:<3} {tip:<12} {proizvodjac:<15} {registarska:<12} {godina:<6} {cijena:<8}")

#5 - Zavrseno!
print("\nBaza vozila je uspješno kreirana i ispisana!") 

