CREATE TABLE pessoa (
    id INT NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(20) NOT NULL,
    nascimento DATE
)

INSERT INTO pessoa (nome, nascimento) VALUES ('Gabriel', '1997-11-02');

UPDATE pessoa SET nome='Gabriel andre' WHERE id=1;

DELETE FROM pessoa WHERE id=2;

SELECT * FROM pessoa ORDER BY nome;

SELECT * FROM pessoa ORDER BY nome DESC;

UPDATE pessoa SET GENERO='M' WHERE id=4;
UPDATE pessoa SET GENERO='M' WHERE id=6;

ALTER TABLE `pessoa` CHANGE `GENERO` `genero` VARCHAR(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL;

SELECT COUNT(id), genero FROM pessoa GROUP BY genero;

use teste;
SHOW DATABASE;
DROP DATABASE test;
DROP TABLE usuarios;