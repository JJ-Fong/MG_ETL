select * from (
select 'rc_dim_comp' as id, count(*)
from dim_comprador a
union
select 'rc_dim_compxdim_ubi' as id, count(*) 
from dim_comprador a
inner join dim_ubicacion b on a.id_ubicacion = b.id_ubicacion
) q 
order by q.id