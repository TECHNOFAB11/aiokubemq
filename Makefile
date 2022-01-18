
.PHONY: protoc
protoc:
	python -m grpc_tools.protoc --grpc_python_out=aiokubemq/proto --python_out=aiokubemq/proto --mypy_out=aiokubemq/proto -I=. kubemq.proto
	cd aiokubemq/proto && sed -i 's/^\(import.*pb2\)/from . \1/g' *.py
	# needed because the imports are stupid and broken
