create view fact_adjudicacion as (
	select 
		concat(query.categoria,'|',query.id_proveedor,'|',query.id_comprador,'|',query.nog) as id_adjudicacion, 
		query.*
	from (
		select 
			upper(a.nit_comprador) as id_comprador, 
			upper(a.nit_proveedor) as id_proveedor,
	 		a.nog,
			a.fecha_publicada,
			a.fecha_presentacion_ofertas,
			a.fecha_cierre_ofertas,
			a.fecha_adjudicada,
			upper(categoria) as categoria, 
			monto as monto,
			upper(descripcion) as descripcion, 
			upper(tipo_ofertas) as tipo_ofertas,
			upper(modalidad_compra) as modalidad_compra
		from (
			select distinct
			*
			from raw_adjudicaciones_test1
		) a
	) query
)