{{ config(materialized='view') }}

SELECT
    id                      AS transaction_id,
    account_id,
    amount,
    txn_type                AS transaction_type,
    related_account_id,
    status,
    created_at              AS transaction_time
FROM {{ source('raw', 'transactions') }}