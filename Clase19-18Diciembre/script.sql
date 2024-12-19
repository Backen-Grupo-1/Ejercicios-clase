-- CREACIÓN TABLAS
create table Hotel (
    id_hotel SERIAL primary key,
    nombre varchar(50),
    ubicacion varchar(50)
);

create table Habitacion (
    id_habitacion SERIAL primary key,
    id_hotel integer references Hotel (id_hotel),
    numero integer,
    precio_por_noche decimal(10, 2)
);

create table Reserva (
    id_reserva SERIAL primary key,
    id_habitacion integer references Habitacion (id_habitacion),
    fecha_reserva date,
    duracion integer
);

-- INSERTAR DATOS

insert into
    Hotel (nombre, ubicacion)
values ('Hotel Sol', 'Playa'),
    ('Hotel Luna', 'Montaña');

insert into
    Habitacion (
        id_hotel,
        numero,
        precio_por_noche
    )
values (1, 101, 100.00),
    (1, 102, 120.00),
    (2, 201, 80.00),
    (2, 202, 95.00);

insert into
    Reserva (
        id_habitacion,
        fecha_reserva,
        duracion
    )
values (1, '2024-12-01', 3),
    (2, '2024-12-02', 2),
    (3, '2024-12-03', 1);

-- CONSULTAS

select nombre, ubicacion from hotel h;

select * from habitacion h;
-- id_habitacion, id_hotel, numero, precio_por_noche

select id_habitacion, numero
from habitacion
where
    precio_por_noche > 90;

select sum(duracion) from reserva r;

-- • Incrementa en $10.00 el precio de todas las habitaciones que pertenecen al “Hotel Sol”.
update habitacion set precio_por_noche = precio_por_noche + 10 where id_hotel = 1

-- • El “Hotel Luna” ahora está ubicado en “Bosque”.
update hotel set ubicacion= 'Bosque' where id_hotel = 2

-- • Extiende la duración de la reserva de la habitación 101 en 2 días.
update reserva set duracion = duracion + 2 where id_habitacion = 1

-- • Borra la reserva hecha en la habitación 102.
delete from reserva where id_habitacion= 2
-- • Borra todas las habitaciones cuyo precio por noche supere $120.00.
delete from habitacion where precio_por_noche > 120

-- • Agrega una columna“estado” (tipo BOOLEAN) a la tabla“Habitacion” para indicar si la habitación está disponible o no. Establece un valor por defecto en TRUE.
alter table habitacion add column estado boolean default true

-- • Cambia el tipo de dato de la columna“duracion” en la table “Reserva” para que acepte decimales (por ejemplo, para medios días).
alter table reserva alter column duracion type decimal (5,2)