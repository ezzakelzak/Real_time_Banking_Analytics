{{ config(materialized='view') }}

with ranked as (
    select
        id              as customer_id,
        first_name,
        last_name,
        email,
        created_at,
        row_number() over (
            partition by id
            order by created_at desc
        ) as rn
    from {{ source('raw', 'customers') }}
)

select
    customer_id,
    first_name,
    last_name,
    email,
    created_at
from ranked
where rn = 1