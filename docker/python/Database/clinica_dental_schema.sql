-- Borrar la base de datos existente
DROP DATABASE IF EXISTS clinica_dental;

-- Crear la base de datos
CREATE DATABASE clinica_dental;
USE clinica_dental;

-- Tabla de pacientes
CREATE TABLE pacientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    fecha_nacimiento DATE,
    telefono VARCHAR(20)
);

-- Tabla de doctores
CREATE TABLE doctores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    especialidad VARCHAR(255)
);

-- Tabla de citas
CREATE TABLE citas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    paciente_id INT,
    doctor_id INT,
    fecha_hora DATETIME,
    duracion_minutos INT,
    FOREIGN KEY (paciente_id) REFERENCES pacientes(id),
    FOREIGN KEY (doctor_id) REFERENCES doctores(id)
);

-- Tabla de notas clínicas
CREATE TABLE notas_clinicas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    paciente_id INT,
    doctor_id INT,
    fecha_hora DATETIME,
    texto TEXT,
    FOREIGN KEY (paciente_id) REFERENCES pacientes(id),
    FOREIGN KEY (doctor_id) REFERENCES doctores(id)
);

-- Tabla de correos electrónicos de pacientes
CREATE TABLE correos_pacientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    paciente_id INT,
    fecha_hora DATETIME,
    asunto VARCHAR(255),
    cuerpo TEXT,
    FOREIGN KEY (paciente_id) REFERENCES pacientes(id)
);

-- Tabla de preguntas frecuentes (FAQ)
CREATE TABLE faq (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pregunta TEXT,
    respuesta TEXT
);

-- Insertar datos de ejemplo en pacientes
INSERT INTO pacientes (nombre, apellido, fecha_nacimiento, telefono) VALUES
    ('Ana', 'García', '1985-03-15', '612345678'),
    ('Carlos', 'López', '1992-07-22', '698765432'),
    ('Laura', 'Martínez', '1978-11-01', '654321876'),
    ('Javier', 'Pérez', '1980-05-10', '612345679'),
    ('Sofía', 'Rodríguez', '1995-12-03', '698765433'),
    ('Miguel', 'Hernández', '1975-08-20', '654321877'),
    ('Isabel', 'Gómez', '1988-02-28', '612345680'),
    ('David', 'Sánchez', '1998-09-17', '698765434'),
    ('Elena', 'Ruiz', '1970-04-05', '654321878'),
    ('Pedro', 'Alonso', '1993-11-25', '612345681'),
    ('Marta', 'Jiménez', '1982-07-12', '698765435'),
    ('Jorge', 'Díaz', '1977-01-30', '654321879'),
    ('Carmen', 'Moreno', '1990-06-08', '612345682'),
    ('Raúl', 'Álvarez', '1997-10-23', '698765436'),
    ('Lucía', 'Romero', '1973-03-18', '654321880'),
    ('Alberto', 'Torres', '1986-09-01', '612345683'),
    ('Paula', 'Navarro', '1999-12-09', '698765437'),
    ('Daniel', 'Serrano', '1979-05-27', '654321881'),
    ('Silvia', 'Gutiérrez', '1991-08-14', '612345684'),
    ('Roberto', 'Ortega', '1971-02-02', '698765438'),
    ('Cristina', 'Castro', '1984-11-19', '654321882'),
    ('Antonio', 'Blanco', '1994-07-07', '612345685'),
    ('Nuria', 'Gil', '1983-04-24', '698765439'),
    ('Fernando', 'Vargas', '1976-12-31', '654321883'),
    ('Sara', 'Reyes', '1989-06-16', '612345686');

-- Insertar datos de ejemplo en doctores
INSERT INTO doctores (nombre, especialidad) VALUES
    ('Dr. Pérez', 'Odontología General'),
    ('Dra. Rodríguez', 'Ortodoncia'),
    ('Dr. Gómez', 'Periodoncia'),
    ('Dra. Sánchez', 'Endodoncia'),
    ('Dr. Ruiz', 'Implantología'),
    ('Dra. Alonso', 'Odontopediatría'),
    ('Dr. Jiménez', 'Cirugía Oral'),
    ('Dra. Díaz', 'Prostodoncia'),
    ('Dr. Moreno', 'Estética Dental'),
    ('Dra. Álvarez', 'Patología Oral'),
    ('Dr. Romero', 'Radiología Dental'),
    ('Dra. Torres', 'Medicina Bucal'),
    ('Dr. Navarro', 'Salud Pública Dental'),
    ('Dra. Serrano', 'Odontología Deportiva'),
    ('Dr. Gutiérrez', 'Odontología Geriátrica'),
    ('Dra. Ortega', 'Sedación Dental'),
    ('Dr. Castro', 'Odontología Forense'),
    ('Dra. Blanco', 'Odontología Hospitalaria'),
    ('Dr. Gil', 'Odontología del Sueño'),
    ('Dra. Vargas', 'Odontología Mínimamente Invasiva'),
    ('Dr. Reyes', 'Odontología Digital'),
    ('Dra. Herrera', 'Odontología Basada en Evidencia'),
    ('Dr. Martín', 'Odontología para Pacientes Especiales'),
    ('Dra. Soto', 'Odontología Holística'),
    ('Dr. Rubio', 'Odontología de Precisión');

-- Insertar datos de ejemplo en citas
INSERT INTO citas (paciente_id, doctor_id, fecha_hora, duracion_minutos) VALUES
    (1, 1, '2024-03-10 10:00:00', 30),
    (2, 2, '2024-03-10 11:00:00', 60),
    (3, 1, '2024-03-11 14:00:00', 45),
    (4, 3, '2024-03-12 10:30:00', 30),
    (5, 4, '2024-03-13 11:30:00', 60),
    (6, 5, '2024-03-14 15:00:00', 45),
    (7, 6, '2024-03-15 10:15:00', 30),
    (8, 7, '2024-03-16 11:15:00', 60),
    (9, 8, '2024-03-17 14:30:00', 45),
    (10, 9, '2024-03-18 10:45:00', 30),
    (11, 10, '2024-03-19 11:45:00', 60),
    (12, 11, '2024-03-20 15:30:00', 45),
    (13, 12, '2024-03-21 10:00:00', 30),
    (14, 13, '2024-03-22 11:00:00', 60),
    (15, 14, '2024-03-23 14:00:00', 45),
    (16, 15, '2024-03-24 10:30:00', 30),
    (17, 16, '2024-03-25 11:30:00', 60),
    (18, 17, '2024-03-26 15:00:00', 45),
    (19, 18, '2024-03-27 10:15:00', 30),
    (20, 19, '2024-03-28 11:15:00', 60),
    (21, 20, '2024-03-29 14:30:00', 45),
    (22, 21, '2024-03-30 10:45:00', 30),
    (23, 22, '2024-03-31 11:45:00', 60),
    (24, 23, '2024-04-01 15:30:00', 45),
    (25, 24, '2024-04-02 10:00:00', 30);

-- Insertar datos de ejemplo en notas_clinicas
INSERT INTO notas_clinicas (paciente_id, doctor_id, fecha_hora, texto) VALUES
    (1, 1, '2024-03-10 10:00:00', 'Paciente presenta dolor en la muela del juicio. Se recomienda radiografía.'),
    (2, 2, '2024-03-10 11:00:00', 'Ajuste de brackets realizado. Próxima cita en 6 semanas.'),
    (3, 1, '2024-03-11 14:00:00', 'Limpieza dental completa. Se observan pequeñas caries.'),
    (4, 3, '2024-03-12 10:30:00', 'Extracción de molar realizada con éxito. Paciente se recupera bien.'),
    (5, 4, '2024-03-13 11:30:00', 'Tratamiento de conducto en pieza 26. Se programa revisión en un mes.'),
    (6, 5, '2024-03-14 15:00:00', 'Colocación de implante en zona 46. Paciente muestra buena respuesta.'),
    (7, 6, '2024-03-15 10:15:00', 'Revisión de ortodoncia. Se ajustan arcos y ligaduras.'),
    (8, 7, '2024-03-16 11:15:00', 'Consulta de odontopediatría. Se realiza fluorización y sellado de fisuras.'),
    (9, 8, '2024-03-17 14:30:00', 'Cirugía de terceros molares. Paciente estable tras la intervención.'),
    (10, 9, '2024-03-18 10:45:00', 'Prótesis dental removible ajustada. Paciente satisfecho con el resultado.'),
    (11, 10, '2024-03-19 11:45:00', 'Diagnóstico de lesión en mucosa oral. Se toma muestra para biopsia.'),
    (12, 11, '2024-03-20 15:30:00', 'Análisis radiográfico completo. Se detectan anomalías en la articulación temporomandibular.'),
    (13, 12, '2024-03-21 10:00:00', 'Evaluación de riesgo de caries. Se recomiendan medidas preventivas.'),
    (14, 13, '2024-03-22 11:00:00', 'Consulta de odontología deportiva. Se confecciona protector bucal personalizado.'),
    (15, 14, '2024-03-23 14:00:00', 'Revisión de pacientes geriátricos. Se realizan ajustes en prótesis dentales.'),
    (16, 15, '2024-03-24 10:30:00', 'Sedación consciente para tratamiento dental. Paciente colaborador durante el procedimiento.'),
    (17, 16, '2024-03-25 11:30:00', 'Examen dental forense. Se documentan hallazgos para investigación.'),
    (18, 17, '2024-03-26 15:00:00', 'Consulta en entorno hospitalario. Se coordina tratamiento con otros especialistas.'),
    (19, 18, '2024-03-27 10:15:00', 'Tratamiento de apnea del sueño con dispositivo intraoral. Paciente refiere mejoría.'),
    (20, 19, '2024-03-28 11:15:00', 'Técnicas de odontología mínimamente invasiva aplicadas. Se preserva estructura dental.'),
    (21, 20, '2024-03-29 14:30:00', 'Diseño de sonrisa digital. Se simula resultado final del tratamiento.'),
    (22, 21, '2024-03-30 10:45:00', 'Revisión de evidencia científica para plan de tratamiento. Paciente informado sobre opciones.'),
    (23, 22, '2024-03-31 11:45:00', 'Atención dental para paciente con necesidades especiales. Se adapta el entorno y el protocolo.'),
    (24, 23, '2024-04-01 15:30:00', 'Enfoque holístico en la atención dental. Se consideran aspectos emocionales y nutricionales.'),
    (25, 24, '2024-04-02 10:00:00', 'Técnicas de odontología de precisión aplicadas. Se minimizan errores y se mejora el resultado.');

-- Insertar datos de ejemplo en correos_pacientes
INSERT INTO correos_pacientes (paciente_id, fecha_hora, asunto, cuerpo) VALUES
    (1, '2024-03-09 15:00:00', 'Consulta sobre cita', 'Hola, quería confirmar mi cita para mañana.'),
    (2, '2024-03-08 10:00:00', 'Dolor dental', 'Buenos días, tengo un fuerte dolor en la muela. ¿Puedo adelantar mi cita?'),
    (3, '2024-03-07 12:00:00', 'Información sobre blanqueamiento', 'Me gustaría saber más sobre el blanqueamiento dental que ofrecen.'),
    (4, '2024-03-06 14:00:00', 'Resultados de radiografía', '¿Podrían enviarme los resultados de mi radiografía?'),
    (5, '2024-03-05 14:00:00', 'Consulta sobre precios', '¿Cuál es el precio de una limpieza dental?'),
    (6, '2024-03-04 11:00:00', 'Cambio de cita', 'Necesito cambiar mi cita del próximo lunes.'),
    (7, '2024-03-03 16:00:00', 'Información sobre seguros', '¿Trabajan con seguros dentales de Adeslas?'),
    (8, '2024-03-02 10:00:00', 'Recomendación de dentífrico', '¿Qué dentífrico recomiendan para sensibilidad dental?'),
    (9, '2024-03-01 12:00:00', 'Dolor post-extracción', 'Tengo dolor después de la extracción de una muela. ¿Qué puedo hacer?'),
    (10, '2024-02-29 14:00:00', 'Consulta sobre ortodoncia', '¿Cuánto dura un tratamiento de ortodoncia?'),
    (11, '2024-02-28 11:00:00', 'Información sobre implantes', '¿Qué tipos de implantes ofrecen?'),
    (12, '2024-02-27 16:00:00', 'Consulta sobre prótesis', '¿Cuánto cuesta una prótesis dental removible?'),
    (13, '2024-02-26 10:00:00', 'Recomendación de enjuague bucal', '¿Qué enjuague bucal recomiendan para encías sensibles?'),
    (14, '2024-02-25 12:00:00', 'Dolor de mandíbula', 'Tengo dolor en la mandíbula. ¿Podría ser bruxismo?'),
    (15, '2024-02-24 14:00:00', 'Consulta sobre periodoncia', '¿Qué es la periodoncia?'),
    (16, '2024-02-23 11:00:00', 'Información sobre endodoncia', '¿Duele un tratamiento de endodoncia?'),
    (17, '2024-02-22 16:00:00', 'Consulta sobre cirugía oral', '¿Qué tipo de cirugías orales realizan?'),
    (18, '2024-02-21 10:00:00', 'Recomendación de cepillo dental', '¿Qué tipo de cepillo dental recomiendan?'),
    (19, '2024-02-20 12:00:00', 'Dolor en encías', 'Tengo dolor en las encías. ¿Podría ser gingivitis?'),
    (20, '2024-02-19 14:00:00', 'Consulta sobre odontopediatría', '¿A qué edad debo llevar a mi hijo al dentista?'),
    (21, '2024-02-18 11:00:00', 'Información sobre estética dental', '¿Qué tratamientos de estética dental ofrecen?'),
    (22, '2024-02-17 16:00:00', 'Consulta sobre radiología dental', '¿Qué tipo de radiografías dentales realizan?'),
    (23, '2024-02-16 10:00:00', 'Recomendación de hilo dental', '¿Qué tipo de hilo dental recomiendan?'),
    (24, '2024-02-15 12:00:00', 'Dolor al masticar', 'Tengo dolor al masticar. ¿Podría ser una caries?'),
    (25, '2024-02-14 14:00:00', 'Consulta sobre medicina bucal', '¿Qué es la medicina bucal?');

-- Insertar datos de ejemplo en faq
INSERT INTO faq (pregunta, respuesta) VALUES
    ('¿Cuáles son sus horarios de atención?', 'Atendemos de lunes a viernes de 9:00 a 18:00.'),
    ('¿Aceptan seguros dentales?', 'Sí, trabajamos con la mayoría de los seguros dentales.'),
    ('¿Cómo puedo cancelar mi cita?', 'Puede cancelar su cita llamando al 612345678 con 24 horas de antelación.'),
    ('¿Cuál es el precio de una limpieza dental?', 'El precio de una limpieza dental es de 50 euros.'),
    ('¿Qué dentífrico recomiendan para sensibilidad dental?', 'Recomendamos dentífricos con flúor y nitrato de potasio.'),
    ('¿Cuánto dura un tratamiento de ortodoncia?', 'Un tratamiento de ortodoncia suele durar entre 18 y 24 meses.'),
    ('¿Qué tipos de implantes ofrecen?', 'Ofrecemos implantes de titanio y de zirconio.'),
    ('¿Cuánto cuesta una prótesis dental removible?', 'El precio de una prótesis dental removible varía según el material y el diseño.'),
    ('¿Qué enjuague bucal recomiendan para encías sensibles?', 'Recomendamos enjuagues bucales con clorhexidina o aceites esenciales.'),
    ('¿Podría ser bruxismo?', 'El dolor de mandíbula puede ser un síntoma de bruxismo. Le recomendamos que consulte a un especialista.'),
    ('¿Qué es la periodoncia?', 'La periodoncia es la especialidad que se encarga de la prevención y tratamiento de las enfermedades de las encías.'),
    ('¿Duele un tratamiento de endodoncia?', 'Un tratamiento de endodoncia se realiza con anestesia local, por lo que no debería doler.'),
    ('¿Qué tipo de cirugías orales realizan?', 'Realizamos extracciones, implantes, injertos óseos y otros procedimientos quirúrgicos.'),
    ('¿Qué tipo de cepillo dental recomiendan?', 'Recomendamos cepillos dentales con cerdas suaves o medias.'),
    ('¿Podría ser gingivitis?', 'El dolor en las encías puede ser un síntoma de gingivitis. Le recomendamos que consulte a un especialista.'),
    ('¿A qué edad debo llevar a mi hijo al dentista?', 'Se recomienda llevar a los niños al dentista a partir de los 6 meses de edad.'),
    ('¿Qué tratamientos de estética dental ofrecen?', 'Ofrecemos blanqueamiento dental, carillas de porcelana, coronas y otros tratamientos de estética dental.'),
    ('¿Qué tipo de radiografías dentales realizan?', 'Realizamos radiografías panorámicas, periapicales y cefalométricas.'),
    ('¿Qué tipo de hilo dental recomiendan?', 'Recomendamos hilo dental con cera o sin cera, según las preferencias del paciente.'),
    ('¿Podría ser una caries?', 'El dolor al masticar puede ser un síntoma de caries. Le recomendamos que consulte a un especialista.'),
    ('¿Qué es la medicina bucal?', 'La medicina bucal es la especialidad que se encarga del diagnóstico y tratamiento de las enfermedades de la mucosa oral.'),
    ('¿Realizan tratamientos de ortodoncia invisible?', 'Sí, realizamos tratamientos de ortodoncia invisible con alineadores transparentes.'),
    ('¿Qué es el bruxismo?', 'El bruxismo es el hábito involuntario de apretar o rechinar los dientes, generalmente durante la noche.'),
    ('¿Cómo puedo saber si tengo mal aliento?', 'El mal aliento puede ser causado por diversos factores, como la higiene bucal deficiente o enfermedades de las encías. Le recomendamos que consulte a un especialista.'),
    ('¿Qué es la odontología preventiva?', 'La odontología preventiva se centra en la prevención de las enfermedades bucodentales a través de la higiene bucal, la dieta y las revisiones periódicas.');