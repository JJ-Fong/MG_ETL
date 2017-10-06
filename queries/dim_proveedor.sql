drop materialized view dim_proveedor;
create materialized view dim_proveedor as (
	select 
		query.nit as id_proveedor,
		query.*
	from (
		select distinct
			upper(a.nit) as nit,
			case
				when (a.nit = '82864012') then concat('MIXCO|',upper(a.departamento))
				when (a.municipio is null) or (a.departamento is null) then 'NO ASIGNADO'
				else concat(upper(a.municipio),'|',upper(a.departamento))
			end id_ubicacion,
			upper(a.nombre) as nombre,
			case
				when (nit = '16906888') then 'CONSTRUCTORES'
				when (nit = '54262348') then 'VENTA AL POR MENOR DE OTROS PRODUCTOS EN ALMACENES ESPECIALIZADOS'
				else upper(a.activ_economica) 
			end actividad_economica,
			upper(a.tipo) as tipo, 
			case
				when (a.nit = '85949019') then 20140411
 				when (inscripcion_rm is null) then 15000101
				else date_part('year',a.inscripcion_rm)*10000+date_part('month',a.inscripcion_rm)*100+date_part('day',a.inscripcion_rm) 
			end fecha_inscripcion_rm
		from (
			select distinct
				*
			from raw_proveedores
		) a
	) query 
)