select * from (
select 'rc_dim_prov' as id, count(*) 
from dim_proveedor
union 
select 'rc_dim_provxdim_ubi' as id, count(*) 
from dim_proveedor a
inner join dim_ubicacion b on a.id_ubicacion = b.id_ubicacion
union
select 'rc_dim_provxdim_fecha' as id, count(*) 
from dim_proveedor a
inner join dim_fecha b on a.fecha_inscripcion_rm = b.id_fecha
) q 
order by q.id
