==========================
CFN Kafka - ACLs Provider
==========================

AWS CFN Provider for Kafka ACLs

How to use
==========

Using AWS Private registry resource
------------------------------------

The original plan with this project was to use a new Resource published in AWS Private Registry and have CFN templates
such as

.. code-block:: yaml

    Resources:
      NewACL:
        Type: EWS::Kafka::ACL
        Properties:
	BootstrapServers: str
	Policies: [ Policy ]


However, due to the fact that AWS hosts the functions which are used then to create the resources in their own account,
there is no access to clusters which are located inside a VPC unless you provide with public access.

If you aim to use that and deploy it to your account, refer to the docs/README.md which is generated through the
cloudformation SDK for properties, and return values.

Using a lambda function + Custom resource
-------------------------------------------

Due to the limitation mentioned above (VPC), I adapted the project to use a very similar format of definition to stay consistent,
but this time to use that resource, you will be creating the Lambda function yourselves, in your VPC if you so need to, and will be able to
use it as follows:

.. code-block:: yaml

    Resources:
      NewACL:
        Type: Custom::KafkaACL
        Properties:
          ServiceToken: !Sub "arn:${AWS::Partition}:lambda:${AWS::Region}:${AWS::AccountId}:function:kafka-acl-provider
          BootstrapServers: my-cluster-endpoint.internal
	  Policies: [ Policy ]


Features
==========

CRUD support for Kafka topics against a kafka cluster.

Credits
========

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
