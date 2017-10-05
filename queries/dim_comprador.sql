drop materialized view dim_comprador;
create materialized view dim_comprador as (
	select 
		concat(query.nit,'|',query.nombre) as id_comprador,
		query.*
	from (
		select
			upper(a.nit) as nit,
			concat(upper(a.municipio),'|',upper(a.departamento)) as id_ubicacion,
			case 
				when nit = '4251393' and then 
			upper(a.nombre) as nombre,
			upper(a.entidad_superior) as entidad_superior,
			case 
				when a.origen_fondos is null then 'NO ASIGNADO'
				else upper(origen_fondos)
			end origen_fondos
		from ( 
			select distinct *
			from raw_compradores
		) a
	) query
);
