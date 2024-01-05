# Telegram Bot Template

Template for creating Telegram bots.

## Local Installation

While the production environment can be hosted on an external server, a local development environment is also recommended for testing the bot. It is crucial not to share the same bot token for production and development. It is recommended that each team member creates their own development bot.

To install locally, you need to have _docker_, _python3.10_, and _poetry_ installed.

## Configuration

To configure the required variables locally, copy the following file:

    cp .env.dist .env

Then, configure the `BOT_TOKEN` and `SECRET_TOKEN` variables. The `WEBHOOK_HOST` variable is only necessary if an external server is being used.

## Database

A PostgreSQL database is required, and it can be set up using Docker:

    docker compose up -d

If using a different database, configure the `DATABASE_URL` variable in the `.env` file.

To set up the schema, run:

    make configure

### Settings Class

A Settings class is included that allows storing values in a table. You can specify the associated chat (chat), the name of the data (key), and its value (value). If you want data that exists for any chat, you can use 0 (zero) as the chat identifier.

## Execution

### Locally

The first step is to install the dependencies:

    poetry install

Then, you can start the service in polling mode:

    make serve

The bot should now be able to respond.

### Commands

The bot supports the following commands. If anything else is sent, the bot will respond in echo mode (returns what is sent to it).

#### Command `/start`

Returns a greeting message.

#### Command `/save DATA`

Saves the specified data in the database.

#### Command `/load`

Returns the saved data.

## References

For obtaining open APIs, you can refer to the following GitHub repository:

* [https://github.com/toddmotto/public-apis](https://github.com/toddmotto/public-apis)
