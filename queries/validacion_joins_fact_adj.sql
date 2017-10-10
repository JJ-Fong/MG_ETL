select * from (
	select 'rc_fact_adj' as id, count(*) as cont
	from fact_adjudicacion a
	union
	select 'rc_fact_adjxdim_prov' as id, count(*) as cont
	from fact_adjudicacion a
	inner join dim_proveedor b on a.id_proveedor = b.id_proveedor
	union
	select 'rc_fact_adjxdim_comp' as id, count(*) as cont
	from fact_adjudicacion a
	inner join dim_comprador b on a.id_comprador = b.id_comprador
	union
	select 'rc_fact_adj_fecha_adjxdim_fecha' as id, count(*) as cont
	from fact_adjudicacion a
	inner join dim_fecha b on a.fecha_adjudicada = b.id_fecha
	union
	select 'rc_fact_adj_fecha_publicadaxdim_fecha' as id, count(*) as cont
	from fact_adjudicacion a
	inner join dim_fecha b on a.fecha_publicada = b.id_fecha
	union
	select 'rc_fact_adj_fecha_presentacion_ofertasxdim_fecha' as id, count(*) as cont
	from fact_adjudicacion a
	inner join dim_fecha b on a.fecha_presentacion_ofertas = b.id_fecha
	union
	select 'rc_fact_adj_fecha_cierrexdim_fecha' as id, count(*) as cont
	from fact_adjudicacion a
	inner join dim_fecha b on a.fecha_cierre_ofertas = b.id_fecha
) q
order by q.id