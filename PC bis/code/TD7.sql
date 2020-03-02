select count(id_vol) from vol where jour = 2016-05-02 and heure < 12:00;
select id_vol from vol join aeroport on vol.destination = aeroport.id_aero where aeroport.ville = "Paris" and vol.jour = 2016-05-02;
select id
from vol as v1 join vol as v2 on v1.id_vol = v2.id_vol
where v1.depart = v2.arrivee and v1.arrivee = v2.depart and v1.niveau = v2.niveau;
