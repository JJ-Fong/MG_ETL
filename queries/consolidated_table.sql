create materialized view consolidated_table as (
select
	a.id_adjudicacion as id_adjudicacion,
	a.nog as nog,
	a.categoria as categoria,
	a.descripcion as descripcion,
	a.monto as monto,
	a.fecha_publicada as fecha_publicada,
	a.fecha_presentacion_ofertas as fecha_presentacion_ofertas,
	a.fecha_cierre_ofertas as fecha_cierre_ofertas,
	a.fecha_adjudicada as fecha_adjudicada,
	a.tipo_ofertas as tipo_ofertas, 
	a.modalidad_compra as modalidad_compra,
	b.nit as nit_proveedor,
	d.municipio as municipio_proveedor,
	d.departamento as departamento_proveedor,
	b.nombre as nombre_proveedor,
	b.actividad_economica as actividad_economica_proveedor,
	b.tipo as tipo_proveedor,
	b.fecha_inscripcion_rm as fecha_inscripcion_rm_proveedor, 
	c.nit as nit_comprador, 
	e.municipio as municipio_comprador,
	e.departamento as departamento_comprador, 
	c.nombre as nombre_comprador,
	c.entidad_superior as entidad_superior_comprador, 
	c.origen_fondos as origen_fondos_comprador
from fact_adjudicacion a
inner join dim_proveedor b on a.id_proveedor = b.id_proveedor
inner join dim_comprador c on a.id_comprador = c.id_comprador
inner join dim_ubicacion d on b.id_ubicacion = d.id_ubicacion
inner join dim_ubicacion e on c.id_ubicacion = e.id_ubicacion
) 