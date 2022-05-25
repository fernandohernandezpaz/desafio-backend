create table capacitaciones_guia
(
    id          integer      not null
        primary key,
    nombre      text not null,
    descripcion text         not null,
    fecha_guia  text         not null,
    portada     text not null,
    blob        blob,
    orden       integer not null
);

create table catalogos_ciclo
(
    id     integer     not null
        primary key,
    nombre text not null
);

create table catalogos_cultivo
(
    id     integer     not null
        primary key,
    nombre text not null
);

create table catalogos_cultivo_ciclos
(
    id         integer not null
        primary key,
    cultivo_id integer not null,
    ciclo_id   integer not null
);

create table catalogos_pais
(
    id     integer     not null
        primary key,
    nombre text not null
);

create table catalogos_departamento
(
    id      integer     not null
        primary key,
    nombre  text not null,
    pais_id integer     not null
);

create table catalogos_sexo
(
    id     integer     not null
        primary key,
    nombre text not null
);

create table formularios_modulo
(
    id     integer     not null
        primary key,
    nombre text not null
);

create table formularios_formulario
(
    id             integer      not null
        primary key,
    nombre         text not null,
    descripcion    text,
    autoevaluacion integer,
    indice         integer,
    modulo_id      integer      not null
);

create table capacitaciones_capituloguia
(
    id           integer      not null
        primary key,
    nombre       text not null,
    introduccion text         not null,
    objetivo     text,
    foto         text not null,
    blob         blob,
    orden        integer not null,
    guia_id      integer      not null
);

create table capacitaciones_temacapituloguia
(
    id          integer      not null
        primary key,
    titulo      text not null,
    descripcion text         not null,
    orden       integer not null,
    foto        text not null,
    blob        blob,
    capitulo_id integer      not null
);

create table capacitaciones_fototema
(
    id      integer      not null
        primary key,
    titulo  text not null,
    foto    text not null,
    blob    blob,
    orden   integer not null,
    tema_id integer      not null
);

create table capacitaciones_videotema
(
    id        integer      not null
        primary key,
    titulo    text not null,
    video     text,
    url       text,
    principal integer         not null,
    tema_id   integer      not null,
    blob      blob
);

create table formularios_matriz
(
    id            integer      not null
        primary key,
    nombre        text not null,
    descripcion   text,
    orden         integer,
    formulario_id integer      not null
);

create table formularios_tipoobjeto
(
    id     integer     not null
        primary key,
    nombre text not null
);

create table formularios_cuestionario
(
    id             integer  not null
        primary key,
    objeto         bigint   not null,
    fecha          text not null,
    tipo_objeto_id integer  not null
);

create table formularios_tipopregunta
(
    id     integer     not null
        primary key,
    nombre text not null
);

create table formularios_pregunta
(
    id               integer      not null
        primary key,
    nombre           text not null,
    descripcion      text,
    indice           integer,
    modulo_id        integer      not null,
    tipo_pregunta_id integer      not null
);

create table formularios_cuestionariodetalle
(
    id              integer      not null
        primary key,
    respuesta       text not null,
    archivo         text not null,
    acertada        integer         not null,
    cuestionario_id integer      not null,
    pregunta_id     integer      not null
);

create table formularios_cuestionariodetallematrizpregunta
(
    id              integer      not null
        primary key,
    fila            integer not null,
    respuesta       text not null,
    archivo         text,
    blob            blob,
    acertada        integer,
    ciclo_cierre    integer,
    indice_matriz   integer     not null,
    cuestionario_id integer      not null,
    cultivo_id      integer,
    matriz_id       integer      not null,
    pregunta_id     integer      not null
);

create table formularios_formulariopregunta
(
    id            integer not null
        primary key,
    formulario_id integer not null,
    pregunta_id   integer not null,
    tema_id       integer,
    pregunta_padre_id   integer
);

create table formularios_matrizpregunta
(
    id          integer not null
        primary key,
    columna     integer not null,
    matriz_id   integer not null,
    pregunta_id integer not null
);

create table formularios_respuesta
(
    id          integer      not null
        primary key,
    nombre      text not null,
    descripcion text,
    acertada    integer         not null,
    pregunta_id integer      not null
);

create table mercado_categoria
(
    id     integer     not null
        primary key,
    nombre text not null
);

create table mercado_cobertura
(
    id     integer     not null
        primary key,
    nombre text not null,
    orden  integer not null
);

create table mercado_directorio
(
    id           integer      not null
        primary key,
    nombre       text not null,
    descripcion  text         not null,
    contacto     text not null,
    telefono     integer not null,
    correo       text not null,
    logo         text not null,
    blob         blob,
    web          text not null,
    cobertura_id integer      not null,
    pais_id      integer      not null,
    es_aliado_estrategico        integer         not null
);

create table mercado_directorio_categorias
(
    directorio_id integer not null,
    categoria_id  integer not null
);

create table mercado_servicio
(
    id     integer     not null
        primary key,
    nombre text not null
);

create table if not exists mercado_directorio_servicios
(
    directorio_id    integer    not    null,
    servicio_id    integer    not    null
);

create table if not exists recursos_categoriadocumento
(
    id  integer  not null        primary key,
    nombre text not null
);

create table if not exists recursos_tematica
(
    id  integer  not null        primary key,
    nombre text not null
);

create table if not exists recursos_documento
(
    id    integer  not null        primary key,
    nombre text  not null,
    descripcion text not null,
    portada text not null,
    blob blob,
    fecha text not null,
    enlace text not null,
    categoria_id integer not null,
    tematica_id integer not null
);

create table if not exists recursos_video
(
    id  integer  not null        primary key,
    nombre text not null,
    descripcion text not null,
    video text,
    embed text,
    url text,
    tematica_id integer not null,
    blob blob
);

create table if not exists recursos_categoriaenlace
(
    id  integer  not null        primary key,
    nombre text   not null
);

create table if not exists recursos_enlace
(
    id  integer  not null        primary key,
    nombre text not null,
    descripcion text not null,
    categoria_id integer not null,
    url text
);

create table if not exists capacitaciones_audiotema
(
    id integer not null primary key,
    titulo text not null,
    audio text not null,
    blob blob,
    tema_id integer not null
);

create table capacitaciones_capituloguia_formularios
(
    id              integer not null        primary key,
    capituloguia_id integer not null,
    formulario_id   integer not null
);

create table capacitaciones_descargablestema
(
    id      integer not null        primary key,
    titulo  text not null,
    archivo text not null,
    blob    blob,
    tema_id integer      not null
);

create table users_gruposredessociales
(
    id         integer not null        primary key,
    nombre     text not null,
    url        text not null,
    plataforma text  not null,
    pais_id    integer not null
);
