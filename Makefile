.DEFAULT: install

.PHONY: install
install:
	poetry run pre-commit install --hook-type pre-commit --hook-type commit-msg

.PHONY: certs
certs:
	mkcert -cert-file certs/localhost-cert.pem -key-file certs/localhost-key.pem localhost 127.0.0.1 ::1

.PHONY: configure
configure:
	poetry run cli configure

.PHONY: server
server:
	poetry run server

.PHONY: dev
dev:
	poetry run cli serve
