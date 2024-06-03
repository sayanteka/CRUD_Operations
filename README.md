# CRUD_Operations
 https://sayanteka-crud-operations-app-uawzae.streamlit.app/


![alt text](image.png)

![alt text](image-1.png)

If I keep on clicking up button, it reruns and the concept of counter doesn't work. It just prints 0 and 1.
So we have to store that in session state i.e. outside rerun block. So counter var will be a key in session state

# Diff between monolithic and microservices.
<img width="265" alt="image" src="https://github.com/sayanteka/CRUD_Operations/assets/66312084/fc44d6f8-5ee6-4638-afc0-7dd95683325a">

Suppose airbnb app has 3 components auth, payment, listings. problem with monolithic, if i change anything in authentication i need to redeploy again all units. Thus I have scaling issue. can't scale up indiviadual component. has to scale up every components. If I have developed any of the components with java then it has to be java for other components as well. advantage: Easier to develop and manage. 

<img width="484" alt="image" src="https://github.com/sayanteka/CRUD_Operations/assets/66312084/7bb93d06-dcfc-4cce-be00-31c17ab3449d">

Benefit of micro: Independent Deployment. Scaling up Benefit.

# Azure webapp deployment
cpu cores will commonly handle an avg of 220 to 250 users. 2 cpu cores=500 visitors.
Faster Ram faster processing speed.

# single tenant plus multi tenant.
single tenant apps are available in where they are registered. multi-tenant are available to users in both their home and other tenants.
For company users, tenant=company name. To add any individual add in azure active directory.
# apache kafka
<img width="437" alt="image" src="https://github.com/sayanteka/CRUD_Operations/assets/66312084/bdec407f-c9c0-4e37-b9a8-c5800d1aef3d">
https://www.youtube.com/watch?v=KerNf0NANMo
kafka=real time data processing
prodcer-kafkaserver-consumer

<img width="567" alt="image" src="https://github.com/sayanteka/CRUD_Operations/assets/66312084/dba46743-4638-48fc-8137-2991cc53ff90">

<img width="608" alt="image" src="https://github.com/sayanteka/CRUD_Operations/assets/66312084/f1f235be-9578-466e-b9c1-48280b04997b">


#single tenant vs multiple tenant

![Uploading image.png…]()


<img width="512" alt="image" src="https://github.com/sayanteka/CRUD_Operations/assets/66312084/647b7280-99c1-424c-8291-aabd7ca49ec5">





