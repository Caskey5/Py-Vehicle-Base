"""
+1. Kreiraj prazan rječnik koji predstavlja bazu vozila.

+2. Za svako vozilo:
    - Dodaj novi unos u rječnik.
    - Ključ neka bude jedinstveni broj (ID).
    - Vrijednost bude novi rječnik sa sljedećim ključevima:
        - 'tip'
        - 'proizvođač'
        - 'registarska oznaka'
        - 'godina prve registracije'
        - 'cijena u eur'

+3. Pripremi ispis:
    - Prvo ispiši naslovni red (naslove svih kolona), npr.:
        TIP | PROIZVOĐAČ | REGISTARSKA | GODINA | CIJENA
      (odvoji ih tabovima ili formatiraj da bude uredno)

+4. Prođi kroz rječnik s vozilima:
    - Za svaki ID i vozilo:
        - Ispiši ID, zatim TAB, zatim podatke iz rječnika vozila.
        - Prati isti redoslijed kolona kao u naslovu.

+5. Završeno!
===========================================================================
Nadodane stavke:

+6. (Napredno) Omogući unos vozila od strane korisnika
Ako želiš, možeš napraviti unos podataka za vozilo putem funkcije input().

+7. Kreiraj meni za korisnika :
    1. Lista svih vozila
    2. Dodaj novo vozilo
    3. Izlaz

"""

#1 - Kreiraj praznu listu koja predstavlja bazu vozila.
vehicle_base = []
id = 1

#2 - Dodaj vozila u bazu podataka s jedinstvenim ID-em kao kljucem vozila
vehicle_data = {   # Dodavanje prvog vozila sa ID-em 1
    'ID': id,
    'tip': 'Sedan',  
    'proizvođač': 'BMW',  
    'registarska oznaka': 'ZG-1234-AB',  
    'godina prve registracije': 2020,  
    'cijena u eur': 35000 
}
id += 1
vehicle_base.append(vehicle_data)

vehicle_data = {   # Dodavanje drugog vozila sa ID-em 2
    'ID': id,
    'tip': 'SUV',  
    'proizvođač': 'Audi',  
    'registarska oznaka': 'ST-5678-CD',  
    'godina prve registracije': 2019,
    'cijena u eur': 42000  
}
id += 1
vehicle_base.append(vehicle_data)

vehicle_data = {   # Dodavanje treceg vozila sa ID-em 3
    'ID': id,
    'tip': 'Hatchback', 
    'proizvođač': 'Volkswagen', 
    'registarska oznaka': 'RI-9012-EF',  
    'godina prve registracije': 2021,  
    'cijena u eur': 28000  
}
id += 1
vehicle_base.append(vehicle_data)

vehicle_data = {   # Dodavanje cetvrtog vozila sa ID-em 4
    'ID': id,
    'tip': 'Coupe',  
    'proizvođač': 'Mercedes-Benz',  
    'registarska oznaka': 'OS-3456-GH',    
    'godina prve registracije': 2022,  
    'cijena u eur': 55000  
}
id += 1
vehicle_base.append(vehicle_data)

#7 - Kreiraj meni za korisnika
while True:
    print()
    print()
    print()
    print("\n=== MENI ZA BAZU VOZILA ===")
    print("1. Lista svih vozila")
    print("2. Dodaj novo vozilo")
    print("3. Izlaz")
    print()    
 
    izbor = input("\nUnesite svoj izbor (1-3): ")
    
    if izbor == '1':
        print()
        print()
        print()
        print('\t\t\tLista svih vozila')
        print()
        # Lista svih vozila
        print(f"\n{'ID':<3} {'TIP':<12} {'PROIZVOĐAČ':<15} {'REGISTARSKA':<12} {'GODINA':<6} {'CIJENA':<8}")
        print("-" * 70)
        
        for all_vehicles in vehicle_base:
            vehicle_id = all_vehicles['ID']
            vehicle_type = all_vehicles['tip']
            producer = all_vehicles['proizvođač']
            registry = all_vehicles['registarska oznaka']
            year = all_vehicles['godina prve registracije']
            price = all_vehicles['cijena u eur']
            
            print(f"{vehicle_id:<3} {vehicle_type:<12} {producer:<15} {registry:<12} {year:<6} {price:<8}")
        
        print("-" * 70)

        
    elif izbor == '2':
        # Dodaj novo vozilo
        print()
        print()
        print(f"\n--- Dodavanje novog vozila (ID: {id}) ---")
        print()
        
        input_vehicle_data = {}
        input_vehicle_data['ID'] = id
        input_vehicle_data['tip'] = input('Unesite tip vozila: ')
        input_vehicle_data['proizvođač'] = input('Unesite proizvođača vozila: ')
        input_vehicle_data['registarska oznaka'] = input('Unesite registarsku oznaku vozila: ')
        input_vehicle_data['godina prve registracije'] = input('Unesite godinu prve registracije vozila: ')
        input_vehicle_data['cijena u eur'] = input('Unesite cijenu vozila (EUR): ')
        
        id += 1
        vehicle_base.append(input_vehicle_data)
        
        print(f"\n✓ Vozilo je uspješno dodano!")
        
    elif izbor == '3':
        # Izlaz
        print("\nHvala na korištenju baze vozila!")
        print()
        print()
        print("The End!")
        break
        
    else:
        print("\nNevažeći izbor! Molimo unesite 1, 2 ili 3.")