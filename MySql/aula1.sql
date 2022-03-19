CREATE TABLE pessoa (
    id INT NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(20) NOT NULL,
    nascimento DATE
)

INSERT INTO pessoa (nome, nascimento) VALUES ('Gabriel', '02-11-1997')
INSERT INTO pessoa (nome, nascimento) VALUES ('Andre', '11-02-1997')
