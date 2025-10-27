{{ config(materialized='view') }}

with ranked as (
    select
        id                  as account_id,
        customer_id,
        account_type,
        balance,
        currency,
        created_at,
        row_number() over (
            partition by id
            order by created_at desc
        ) as rn
    from {{ source('raw', 'accounts') }}
)

select
    account_id,
    customer_id,
    account_type,
    balance,
    currency,
    created_at
from ranked
where rn = 1