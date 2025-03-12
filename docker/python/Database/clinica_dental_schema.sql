-- Creación de la base de datos
CREATE DATABASE IF NOT EXISTS clinica_dental;
USE clinica_dental;

-- Tabla de pacientes (sin cambios)
CREATE TABLE IF NOT EXISTS pacientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    fecha_nacimiento DATE,
    telefono VARCHAR(20)
);

-- Tabla de doctores (sin cambios)
CREATE TABLE IF NOT EXISTS doctores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    especialidad VARCHAR(255)
);

-- Tabla de citas (sin cambios)
CREATE TABLE IF NOT EXISTS citas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    paciente_id INT,
    doctor_id INT,
    fecha_hora DATETIME,
    duracion_minutos INT,
    FOREIGN KEY (paciente_id) REFERENCES pacientes(id),
    FOREIGN KEY (doctor_id) REFERENCES doctores(id)
);

-- Tabla de notas clínicas
CREATE TABLE IF NOT EXISTS notas_clinicas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    paciente_id INT,
    doctor_id INT,
    fecha_hora DATETIME,
    texto TEXT,
    FOREIGN KEY (paciente_id) REFERENCES pacientes(id),
    FOREIGN KEY (doctor_id) REFERENCES doctores(id)
);

-- Tabla de correos electrónicos de pacientes
CREATE TABLE IF NOT EXISTS correos_pacientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    paciente_id INT,
    fecha_hora DATETIME,
    asunto VARCHAR(255),
    cuerpo TEXT,
    FOREIGN KEY (paciente_id) REFERENCES pacientes(id)
);

-- Tabla de preguntas frecuentes (FAQ) para el Chatbot
CREATE TABLE IF NOT EXISTS faq (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pregunta TEXT,
    respuesta TEXT
);

-- Insertar datos de ejemplo (sin cambios)
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

-- Insertar datos de ejemplo para notas clínicas
INSERT INTO notas_clinicas (paciente_id, doctor_id, fecha_hora, texto) VALUES
    (1, 1, '2024-03-10 10:00:00', 'Paciente presenta dolor en la muela del juicio. Se recomienda radiografía.'),
    (2, 2, '2024-03-10 11:00:00', 'Ajuste de brackets realizado. Próxima cita en 6 semanas.'),
    (3, 1, '2024-03-11 14:00:00', 'Limpieza dental completa. Se observan pequeñas caries.');

-- Insertar datos de ejemplo para correos electrónicos
INSERT INTO correos_pacientes (paciente_id, fecha_hora, asunto, cuerpo) VALUES
    (1, '2024-03-09 15:00:00', 'Consulta sobre cita', 'Hola, quería confirmar mi cita para mañana.'),
    (2, '2024-03-08 10:00:00', 'Dolor dental', 'Buenos días, tengo un fuerte dolor en la muela. ¿Puedo adelantar mi cita?'),
    (3, '2024-03-07 12:00:00', 'Información sobre blanqueamiento', 'Me gustaría saber más sobre el blanqueamiento dental que ofrecen.');

-- Insertar datos de ejemplo para FAQ
INSERT INTO faq (pregunta, respuesta) VALUES
    ('¿Cuáles son sus horarios de atención?', 'Atendemos de lunes a viernes de 9:00 a 18:00.'),
    ('¿Aceptan seguros dentales?', 'Sí, trabajamos con la mayoría de los seguros dentales.'),
    ('¿Cómo puedo cancelar mi cita?', 'Puede cancelar su cita llamando al 612345678 con 24 horas de antelación.');