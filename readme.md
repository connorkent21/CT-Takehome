# CT Take Home Assignment

This project is a backend API that makes use of Django + Graphql to provide an interface for managing Crypto wallets and associated addresses + transactions. I decided to go with GraphQL since it is both a very convenient way of querying an API but also makes it very easy to test the API without a client application via http://localhost:8000/graphql/.

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

AddAddressInput: { input: { walletId: ID!, addressString: String! } }



mutation RemoveAddress($input: RemoveAddressInput!) {
  removeAddress(input: $input) {
    ok
  }
}

RemoveAddressInput: { input: { addressId: ID! } }



mutation SyncTransactions($input: SyncTransactionsInput!) {
  syncTransactions(input: $input) {
    ok
  }
}

SyncTransactionsInput: { input: { walletId: ID! } }

```

## Testing (Unit Tests)

```
make test
```
