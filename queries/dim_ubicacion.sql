create view dim_ubicacion as (
	select distinct 
		case
			when ((a.municipio is null) or (a.departamento is null)) then 'NO ASIGNADO'
			else concat(upper(a.municipio),'|',upper(a.departamento)) 
		end id_ubicacion,
		case
			when ((a.municipio is null) or (a.departamento is null)) then 'NO ASIGNADO'
			else upper(a.municipio)
		end municipio,
		case 
			when ((a.municipio is null) or (a.departamento is null)) then 'NO ASIGNADO'
			else upper(a.departamento)
		end departamento
	from (
		select distinct
			municipio,
			departamento
		from raw_compradores_test1
		union
		select distinct
			municipio,
			departamento
		from raw_proveedores_test1
	) a
)