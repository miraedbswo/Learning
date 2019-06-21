# TerraForm

테라폼(Terraform)은 **HashiCorp**에서 개발한 오픈소스 **IaC(Infrastructure as code)** 소프트웨어다. 

개발자는 테라폼에서 제공하는 HCL(Hashicorp Configuration Language)라는 고수준 설정 언어(high-level configuration language) 혹은 json 를 이용해서 데이터센터 인프라스트럭처를 정의할 수 있다. 

하지만 HCL을 사용하는 것을 권장함.

테라폼은 Amazon Web Service, IBM Cloud, Google Cloud Platform, Linode, Microsoft Azure, Oracle Cloud Infrastructure, VMware vSphere, OpenStack 등의 인프라스트럭처 제공자를 지원한다.

------



## 내가 테라폼을 선택한 이유

사실 지금까지 내가 Infrastructure as Code를 사용 할 필요가 없다고 생각했다. 

기숙사 지원 시스템을 만들면서, 같이 서비스를 구축해가는 선배들이 하나 둘 씩 졸업해가면서, 새로운 신입생이 왔을 때 내가 직접적으로 기술을 전수해 줄 수 없을 지도 모르겠다고 생각했다. 이 기회를 통해 Infra를 코드로 관리하고, 직접적으로 기술을 전수하지 않아도 누구든지 이 프로젝트를 되맡아 할 수 있도록 구축하는 것이 좋다고 생각했다.

문서화를 완벽하게 하여 이미 구축해둔 기숙사 시스템을 어떻게 구축했는지 하나 하나 설명하고 전수하는 것도 좋겠지만, 

그게 코드로 보는 것만큼 직관적일까?



저자는, 코드가 말보다 인프라에 대한 높은 수준의 설명을 해 줄 수 있다고 생각한다.

