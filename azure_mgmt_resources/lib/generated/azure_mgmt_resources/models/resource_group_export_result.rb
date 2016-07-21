# encoding: utf-8
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.

module Azure::ARM::Resources
  module Models
    #
    # Model object.
    #
    class ResourceGroupExportResult

      include MsRestAzure

      # @return The template content.
      attr_accessor :template

      # @return [ResourceManagementErrorWithDetails] The error.
      attr_accessor :error


      #
      # Mapper for ResourceGroupExportResult class as Ruby Hash.
      # This will be used for serialization/deserialization.
      #
      def self.mapper()
        {
          required: false,
          serialized_name: 'ResourceGroupExportResult',
          type: {
            name: 'Composite',
            class_name: 'ResourceGroupExportResult',
            model_properties: {
              template: {
                required: false,
                serialized_name: 'template',
                type: {
                  name: 'Object'
                }
              },
              error: {
                required: false,
                serialized_name: 'error',
                type: {
                  name: 'Composite',
                  class_name: 'ResourceManagementErrorWithDetails'
                }
              }
            }
          }
        }
      end
    end
  end
end
