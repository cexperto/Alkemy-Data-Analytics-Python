CREATE DATABASE culture
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1;

-- create table informacion
CREATE TABLE IF NOT EXISTS public.informacion
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY,
    index integer,
    cod_localidad bigint,
    id_provincia bigint,
    id_departamento bigint,
    categoria text COLLATE pg_catalog."default",
    provincia text COLLATE pg_catalog."default",
    localidad text COLLATE pg_catalog."default",
    nombre text COLLATE pg_catalog."default",
    domicilio text COLLATE pg_catalog."default",
    codigo_postal text COLLATE pg_catalog."default",
    numero_de_telefono text COLLATE pg_catalog."default",
    mail text COLLATE pg_catalog."default",
    web text COLLATE pg_catalog."default",
    fecha_de_carga date,
    CONSTRAINT informacion_pkey PRIMARY KEY (id)
)


-- crete table conjuntos
CREATE TABLE IF NOT EXISTS public.conjuntos
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY,
    index text COLLATE pg_catalog."default",
    cantidad bigint,
    fecha_de_carga date,
    CONSTRAINT conjuntos_pkey PRIMARY KEY (id)
)


-- create table informacioncines

CREATE TABLE IF NOT EXISTS public.informacioncines
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY,
    "Provincia" character varying COLLATE pg_catalog."default",
    "Pantallas" integer,
    "Butacas" integer,
    "espacio_INCAA" integer,
    fecha_de_carga date,
    CONSTRAINT informacioncines_pkey PRIMARY KEY (id)
)
