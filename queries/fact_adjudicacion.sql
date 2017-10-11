drop materialized view fact_adjudicacion; 
create materialized view fact_adjudicacion as (
	select 
		concat(query.categoria,'|',query.id_proveedor,'|',query.id_comprador,'|',query.nog) as id_adjudicacion, 
		query.*
	from (
		select 
			case 
				when nog in ('4734157','4747577') then concat(upper(a.nit_comprador),'|OFICINA MUNICIPAL DE PLANIFICACIÓN')
				else concat(upper(a.nit_comprador),'|',upper(a.nombre_comprador)) 
			end id_comprador, 
			upper(a.nit_proveedor) as id_proveedor,
	 		a.nog,
			date_part('year',a.fecha_publicada)*10000+date_part('month',a.fecha_publicada)*100+date_part('day',a.fecha_publicada) as fecha_publicada,
			case
				when (a.fecha_presentacion_ofertas is null) and (not a.fecha_publicada is null) then date_part('year',a.fecha_publicada)*10000+date_part('month',a.fecha_publicada)*100+date_part('day',a.fecha_publicada)
				when nog = '287075' then 20160710
				when nog ='155322' then 20160525
				when nog ='510912' then 20071018
				else date_part('year',a.fecha_presentacion_ofertas)*10000+date_part('month',a.fecha_presentacion_ofertas)*100+date_part('day',a.fecha_presentacion_ofertas) 
			end fecha_presentacion_ofertas,
			case 
				when a.fecha_cierre_ofertas is null then 
				else date_part('year',a.fecha_cierre_ofertas)*10000+date_part('month',a.fecha_cierre_ofertas)*100+date_part('day',a.fecha_cierre_ofertas)
			end fecha_cierre_ofertas,
			case 
				when nog ='667048' then 20160414
				when nog ='287075' then 20160822
				when nog ='155322' then 20160525
				when nog ='479268' then 20160822
				when nog ='510912' then 20160530
				when nog in('788783','165131','96520','96504','165158','96490') then 20160523
				when nog ='788805' then 20160906
				else date_part('year',a.fecha_adjudicada)*10000+date_part('month',a.fecha_adjudicada)*100+date_part('day',a.fecha_adjudicada) 
			end fecha_adjudicada,
			upper(categoria) as categoria, 
			monto as monto,
			upper(descripcion) as descripcion, 
			case 
				when nog in ('510912','287075','155322','479268') then 'SÓLO EN PAPEL.'
				when nog in ('5290163') then 'SÓLO ELECTRÓNICAS.'
				else upper(tipo_ofertas) 
			end tipo_ofertas,
			upper(modalidad_compra) as modalidad_compra
		from (
			select distinct
			*
			from raw_adjudicaciones
		) a
	) query
)