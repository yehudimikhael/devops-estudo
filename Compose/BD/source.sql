GRANT ALL PRIVILEGES ON inscricao.* TO 'noc'@'%';
CREATE TABLE IF NOT EXISTS competidores(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), phone VARCHAR(15), vehicle VARCHAR(15))
INSERT INTO competidores(name, phone, vehicle)values ('Fred', '(21)12345678', 'Hilux')
INSERT INTO competidores(name, phone, vehicle)values ('Vilma', '(22)9876367', 'L200')
INSERT INTO competidores(name, phone, vehicle)values ('Carlos', '(23)9993871', 'Ranger')

