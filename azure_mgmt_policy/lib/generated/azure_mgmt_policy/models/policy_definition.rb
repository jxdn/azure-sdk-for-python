# encoding: utf-8
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.

module Azure::ARM::Policy
  module Models
    #
    # The policy definition.
    #
    class PolicyDefinition

      include MsRestAzure

      # @return [PolicyType] Gets or sets policy definition policy type.
      # Possible values include: 'NotSpecified', 'BuiltIn', 'Custom'
      attr_accessor :policy_type

      # @return [String] Gets or sets the policy definition display name.
      attr_accessor :display_name

      # @return [String] Gets or sets the policy definition description.
      attr_accessor :description

      # @return Gets or sets the policy rule.
      attr_accessor :policy_rule

      # @return [String] Gets or sets the Id of the policy definition.
      attr_accessor :id

      # @return [String] Gets or sets the name of the policy definition.
      attr_accessor :name


      #
      # Mapper for PolicyDefinition class as Ruby Hash.
      # This will be used for serialization/deserialization.
      #
      def self.mapper()
        {
          required: false,
          serialized_name: 'PolicyDefinition',
          type: {
            name: 'Composite',
            class_name: 'PolicyDefinition',
            model_properties: {
              policy_type: {
                required: false,
                serialized_name: 'properties.policyType',
                type: {
                  name: 'String'
                }
              },
              display_name: {
                required: false,
                serialized_name: 'properties.displayName',
                type: {
                  name: 'String'
                }
              },
              description: {
                required: false,
                serialized_name: 'properties.description',
                type: {
                  name: 'String'
                }
              },
              policy_rule: {
                required: false,
                serialized_name: 'properties.policyRule',
                type: {
                  name: 'Object'
                }
              },
              id: {
                required: false,
                serialized_name: 'id',
                type: {
                  name: 'String'
                }
              },
              name: {
                required: false,
                serialized_name: 'name',
                type: {
                  name: 'String'
                }
              }
            }
          }
        }
      end
    end
  end
end
