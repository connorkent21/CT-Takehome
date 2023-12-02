# CT Take Home Assignment

## Getting Started

from root directory:

```
pipenv install
pipenv shell

cd base

make migrate
make run
```

## Seeding initial User + Wallet

```
make run_command COMMAND="seed_db"
```

## Testing GQL Endpoints

Navigate to http://localhost:8000/graphql/

### Queries

```
query GetAddresses {
  addresses{
    edges {
      node {
        id
        balance
        transactions {
          id
        }
      }
    }
  }
}

query GetAddress($id: ID!) {
  address(id: $id) {
    id
    balance
  }
}

query GetTransactions {
  transactions {
    edges {
      node {
        id
        transactionHash
      }
    }
  }
}

query GetTransaction($id: ID!) {
  transaction(id: $id) {
    id
    transactionHash
  }
}

query GetUsers {
  users {
    edges {
      node {
        id
        firstName
        lastName
      }
    }
  }
}

query GetWallets{
  wallets {
    edges {
      node {
        id
      }
    }
  }
}
```

### Mutations

```
mutation AddAddress($input: AddAddressInput!) {
  addAddress(input: $input) {
    address {
      id
      balance
    }
  }
}

mutation RemoveAddress($input: RemoveAddressInput!) {
  removeAddress(input: $input) {
    ok
  }
}

mutation SyncTransactions($input: SyncTransactionsInput!) {
  syncTransactions(input: $input) {
    ok
  }
}
```

## Testing (Unit Tests)

```
make test
```
