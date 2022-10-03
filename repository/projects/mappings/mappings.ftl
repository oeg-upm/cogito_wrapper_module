<#assign jpath=handlers("JsonHandler")>
<#assign dataset=providers("FileProvider", { "file" : "/usr/src/app/repository/projects/files/project.json" })>

@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix data: <http://data.cogito.iot.linkeddata.es/resources/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix facility: <https://cogito.iot.linkeddata.es/def/facility#> .
@prefix project: <http://data.cogito.iot.linkeddata.es/resources/project/> .

data:Project_[=jpath.filter('$.project_id', dataset)]
    a facility:Project ;
    facility:hasName "[=jpath.filter('$.project_name', dataset)]"^^<http://www.w3.org/2001/XMLSchema#string> ;
    facility:hasDescription "[=jpath.filter('$.project_description', dataset)]"^^<http://www.w3.org/2001/XMLSchema#string> ;
    facility:projectID "[=jpath.filter('$.project_id', dataset)]"^^<http://www.w3.org/2001/XMLSchema#string> .

project:[=jpath.filter('$.project_id', dataset)]
    a facility:Project ;
    facility:hasName "[=jpath.filter('$.project_name', dataset)]"^^<http://www.w3.org/2001/XMLSchema#string> ;
    facility:hasDescription "[=jpath.filter('$.project_description', dataset)]"^^<http://www.w3.org/2001/XMLSchema#string> ;
    facility:projectID "[=jpath.filter('$.project_id', dataset)]"^^<http://www.w3.org/2001/XMLSchema#string> .

data:Project_[=jpath.filter('$.project_id', dataset)] owl:sameAs  project:[=jpath.filter('$.project_id', dataset)] .
project:[=jpath.filter('$.project_id', dataset)] owl:sameAs data:Project_[=jpath.filter('$.project_id', dataset)] .