drop materialized view dim_fecha; 
create materialized view dim_fecha as (
	select distinct
		date_part('year', a.fecha)*10000+date_part('month',a.fecha)*100+date_part('day',a.fecha) as id_fecha,
		a.fecha as fecha, 
		date_part('year', a.fecha) as ano,
		date_part('month', a.fecha) as mes_numero,
		case
			when (date_part('month', a.fecha) = 1) then 'ENERO'
			when (date_part('month', a.fecha) = 2) then 'FEBRERO'
			when (date_part('month', a.fecha) = 3) then 'MARZO'
			when (date_part('month', a.fecha) = 4) then 'ABRIL'
			when (date_part('month', a.fecha) = 5) then 'MAYO'
			when (date_part('month', a.fecha) = 6) then 'JUNIO'
			when (date_part('month', a.fecha) = 7) then 'JULIO' 
			when (date_part('month', a.fecha) = 8) then 'AGOSTO' 
			when (date_part('month', a.fecha) = 9) then 'SEPTIEMBRE' 
			when (date_part('month', a.fecha) = 10) then 'OCTUBRE' 
			when (date_part('month', a.fecha) = 11) then 'NOVIEMBRE' 
			when (date_part('month', a.fecha) = 12) then 'DICIEMBRE' 
		end mes_nombre, 
		case 
			when (date_part('month', a.fecha) = 1) then 'ENE' 
			when (date_part('month', a.fecha) = 2) then 'FEB' 
			when (date_part('month', a.fecha) = 3) then 'MAR' 
			when (date_part('month', a.fecha) = 4) then 'ABR' 
			when (date_part('month', a.fecha) = 5) then 'MAY' 
			when (date_part('month', a.fecha) = 6) then 'JUN' 
			when (date_part('month', a.fecha) = 7) then 'JUL' 
			when (date_part('month', a.fecha) = 8) then 'AGO' 
			when (date_part('month', a.fecha) = 9) then 'SEP' 
			when (date_part('month', a.fecha) = 10) then 'OCT' 
			when (date_part('month', a.fecha) = 11) then 'NOV' 
			when (date_part('month', a.fecha) = 12) then 'DIC' 
		end mes_nombre_corto, 
	--	as ano_mes,
		date_part('day', a.fecha) as dia_numero,
		case
			when extract(dow from a.fecha) = 0 then 'DOMINGO'
			when extract(dow from a.fecha) = 1 then 'LUNES'
			when extract(dow from a.fecha) = 2 then 'MARTES'
			when extract(dow from a.fecha) = 3 then 'MIERCOLES'
			when extract(dow from a.fecha) = 4 then 'JUEVES'
			when extract(dow from a.fecha) = 5 then 'VIERNES'
			when extract(dow from a.fecha) = 6 then 'SABADO'
		end dia_nombre,
		case
			when extract(dow from a.fecha) = 0 then 'DOM'
			when extract(dow from a.fecha) = 1 then 'LUN'
			when extract(dow from a.fecha) = 2 then 'MAR'
			when extract(dow from a.fecha) = 3 then 'MIE'
			when extract(dow from a.fecha) = 4 then 'JUE'
			when extract(dow from a.fecha) = 5 then 'VIE'
			when extract(dow from a.fecha) = 6 then 'SAB'
		end dia_nombre_corto,
		case 
			when extract(dow from a.fecha) = 0 then 7
			else extract(dow from a.fecha) 
		end dia_semana
	from (
		select fecha_publicada as fecha from raw_adjudicaciones where not (fecha_publicada is null)
		union
		select fecha_adjudicada as fecha from raw_adjudicaciones where not (fecha_adjudicada is null)
		union 
		select fecha_cierre_ofertas as fecha from raw_adjudicaciones where not (fecha_cierre_ofertas is null)
		union
		select fecha_presentacion_ofertas as fecha from raw_adjudicaciones where not (fecha_presentacion_ofertas is null)
		union
		select inscripcion_rm as fecha from raw_proveedores where not (inscripcion_rm is null)
	) a
)