<#assign jpath=handlers("JsonHandler")>
<#assign dataset=providers(type="FileProvider", file="/Users/salva/Dropbox/cogito/cogito_wrapper_module/repository/projects/files/project.json")>

@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix data: <http://data.cogito.iot.linkeddata.es/resources/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix facility: <https://cogito.iot.linkeddata.es/def/facility#> .

data:Project_[=jpath.filter('$.project_id', dataset)]
    a facility:Project ;
    facility:hasName "[=jpath.filter('$.project_name', dataset)]"^^<http://www.w3.org/2001/XMLSchema#string> ;
    facility:hasDescription "[=jpath.filter('$.project_description', dataset)]"^^<http://www.w3.org/2001/XMLSchema#string> ;
    facility:projectID "[=jpath.filter('$.project_id', dataset)]"^^<http://www.w3.org/2001/XMLSchema#string> .