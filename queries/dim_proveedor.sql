drop view dim_proveedor;
create materialized view dim_proveedor as (
	select 
		query.nit as id_proveedor,
		query.*
	from (
		select
			upper(a.nit) as nit,
			case
				when (a.municipio is null) or (a.departamento is null) then 'NO ASIGNADO'
				else concat(upper(a.municipio),'|',upper(a.departamento))
			end id_ubicacion,
			upper(a.nombre) as nombre,
			case
				when (a.rep_legal is null) then 'NO ASIGNADO'
				else upper(a.rep_legal)
			end representante_legal,
			upper(a.activ_economica) as actividad_economica,
			upper(a.tipo) as tipo, 
			case
				when (inscripcion_rm is null) then '1900-01-01'
				else inscripcion_rm
			end fecha_inscripcion_rm
		from (
			select distinct
				*
			from raw_proveedores
		) a
	) query 
)