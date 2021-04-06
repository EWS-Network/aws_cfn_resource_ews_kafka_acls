# EWS::Kafka::ACL Policy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#resource" title="Resource">Resource</a>" : <i>String</i>,
    "<a href="#patterntype" title="PatternType">PatternType</a>" : <i>String</i>,
    "<a href="#principal" title="Principal">Principal</a>" : <i>String</i>,
    "<a href="#resourcetype" title="ResourceType">ResourceType</a>" : <i>String</i>,
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#effect" title="Effect">Effect</a>" : <i>String</i>,
    "<a href="#host" title="Host">Host</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#resource" title="Resource">Resource</a>: <i>String</i>
<a href="#patterntype" title="PatternType">PatternType</a>: <i>String</i>
<a href="#principal" title="Principal">Principal</a>: <i>String</i>
<a href="#resourcetype" title="ResourceType">ResourceType</a>: <i>String</i>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#effect" title="Effect">Effect</a>: <i>String</i>
<a href="#host" title="Host">Host</a>: <i>String</i>
</pre>

## Properties

#### Resource

Name of the resource to apply the ACL for

_Required_: Yes

_Type_: String

_Pattern_: <code>^[a-zA-Z0-9_.-]+$</code>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PatternType

Pattern type

_Required_: No

_Type_: String

_Allowed Values_: <code>LITERAL</code> | <code>PREFIXED</code> | <code>MATCH</code>

_Pattern_: <code>^[A-Z]+$</code>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Principal

Kafka user to apply the ACLs for.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceType

Kafka user to apply the ACLs for.

_Required_: Yes

_Type_: String

_Allowed Values_: <code>CLUSTER</code> | <code>DELEGATION_TOKEN</code> | <code>GROUP</code> | <code>TOPIC</code> | <code>TRANSACTIONAL_ID</code>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Action

Access action allowed.

_Required_: Yes

_Type_: String

_Allowed Values_: <code>ALL</code> | <code>READ</code> | <code>WRITE</code> | <code>CREATE</code> | <code>DELETE</code> | <code>ALTER</code> | <code>DESCRIBE</code> | <code>CLUSTER_ACTION</code> | <code>DESCRIBE_CONFIGS</code> | <code>ALTER_CONFIGS</code> | <code>IDEMPOTENT_WRITE</code>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Effect

Effect for the ACL.

_Required_: Yes

_Type_: String

_Allowed Values_: <code>DENY</code> | <code>ALLOW</code>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Host

Specify the host for the ACL. Defaults to '*'

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

