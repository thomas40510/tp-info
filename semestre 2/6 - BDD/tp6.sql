/*select titre,auteur from stock where entrep�t="A2" and nbEx<2;
select idClient,nom as "last name", pr�nom as "first name", adresse as "address" from client;
select commande.ISBN,titre from commande join stock on commande.ISBN = stock.ISBN where nbEx=0 ;
select commande.ISBN,titre from commande 
	join stock 
	on commande.ISBN = stock.ISBN 
where entrep�t="B2" and commande.status="� exp�dier";

select nom, pr�nom, adresse from client 
join commande on commande.idClient = client.idClient
where commande.status="� exp�dier";

select nom, pr�nom, adresse from client 
join commande on commande.idClient = client.idClient 
join stock on stock.ISBN = commande.ISBN
where commande.status="� exp�dier" and stock.nbEx=0;

select distinct c1.ISBN from commande as c1 
join commande as c2 on c2.idClient = c1.idClient
where c2.ISBN=952977 and c1.ISBN!=952977;

select distinct stock.titre, stock.auteur from stock 
join commande as c1 on c1.ISBN = stock.ISBN
join commande as c2 on c2.idClient = c1.idClient
where c2.ISBN=(select ISBN from stock where titre="Real mathematical analysis") 
and c1.ISBN!=(select ISBN from stock where titre="Real mathematical analysis") ;*/

select nom, pr�nom from client 
join commande on commande.idClient = client.idClient 
join stock on stock.ISBN = commande.ISBN
where stock.auteur = "Saunders MacLane"  and status ="� exp�dier" or status = "envoy�"
group by client.idClient having count(*)>2