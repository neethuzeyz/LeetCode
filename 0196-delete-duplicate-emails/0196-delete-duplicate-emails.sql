
DELETE FROM Person
USING Person p2
WHERE Person.Email = p2.Email 
  AND Person.id > p2.id;