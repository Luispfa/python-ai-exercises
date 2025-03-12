-- Creación de la base de datos
CREATE DATABASE IF NOT EXISTS clinica_dental;
USE clinica_dental;

-- Tabla de pacientes
CREATE TABLE IF NOT EXISTS pacientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    fecha_nacimiento DATE,
    telefono VARCHAR(20)
);

-- Tabla de doctores
CREATE TABLE IF NOT EXISTS doctores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    especialidad VARCHAR(255)
);

-- Tabla de citas
CREATE TABLE IF NOT EXISTS citas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    paciente_id INT,
    doctor_id INT,
    fecha_hora DATETIME,
    duracion_minutos INT,
    FOREIGN KEY (paciente_id) REFERENCES pacientes(id),
    FOREIGN KEY (doctor_id) REFERENCES doctores(id)
);

-- Insertar datos de ejemplo
INSERT INTO pacientes (nombre, apellido, fecha_nacimiento, telefono) VALUES
    ('Ana', 'García', '1985-03-15', '612345678'),
    ('Carlos', 'López', '1992-07-22', '698765432'),
    ('Laura', 'Martínez', '1978-11-01', '654321876');

INSERT INTO doctores (nombre, especialidad) VALUES
    ('Dr. Pérez', 'Odontología General'),
    ('Dra. Rodríguez', 'Ortodoncia');

INSERT INTO citas (paciente_id, doctor_id, fecha_hora, duracion_minutos) VALUES
    (1, 1, '2024-03-10 10:00:00', 30),
    (2, 2, '2024-03-10 11:00:00', 60),
    (3, 1, '2024-03-11 14:00:00', 45);