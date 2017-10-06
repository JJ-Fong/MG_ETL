select 
	b.mes_numero,
	a.modalidad_compra,
	count(nog) as cantidad,
	sum(monto) as monto
from (
	select distinct
		modalidad_compra,
		nog,
		sum(monto) as monto,
		fecha_adjudicada
	from fact_adjudicacion
	group by modalidad_compra, nog, fecha_adjudicada
) a
inner join dim_fecha b on a.fecha_adjudicada = b.id_fecha
group by b.mes_numero, a.modalidad_compra
order by b.mes_numero, a.modalidad_compra
