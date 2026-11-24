Name:		python-comfyui-workflow-templates-media-assets-03
Version:	0.1.2
Release:	1
Summary:	Workflow template preview assets for ComfyUI
License:	MIT
Group:		Development/Python
URL:		https://github.com/Comfy-Org/workflow_templates
Source0:	https://files.pythonhosted.org/packages/source/c/comfyui-workflow-templates-media-assets-03/comfyui_workflow_templates_media_assets_03-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)

%description
Third preview-asset bundle for the ComfyUI workflow templates.
These are upstream media assets, not model weights.
comfyui-workflow-templates 0.11.118 requires this package.

%files
%{py_sitedir}/comfyui_workflow_templates_media_assets_03
%{py_sitedir}/comfyui_workflow_templates_media_assets_03-*.*-info
