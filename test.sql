CREATE TABLE raw_adjudicaciones_test1 (
	categoria varchar(256),
	status varchar(256), 
	monto float, 
	nog varchar(256),
	nit_proveedor varchar(256),
	nit_comprador varchar(256),
	descripcion varchar(2048),
	fecha_publicada date,
	modalidad_compra varchar(256),
	tipo_ofertas varchar(256),
	fecha_presentacion_ofertas varchar(256),
	nombre_comprador varchar(256),
	unidades varchar(256),
	fecha_adjudicada date,
	fecha_cierre_ofertas date
)

CREATE TABLE raw_proveedores_test1 (
	departamento varchar(256),
	rep_legal varchar(256), 
	municipio varchar(256),
	tipo varchar(256),
	inscripcion_rm date,
	nombre varchar(256),
	activ_economica varchar(256),
	nit varchar(256)
)

CREATE TABLE  raw_compradores_test1(
	entidad_superior varchar(256),
	departamento varchar(256), 
	origen_fondos varchar(256),
	nombre varchar(256),
	municipio varchar(256),
	nit varchar(256)
)