### 📌 모델링 시퀀스 (Using XGBoostClassifier)
![image](https://github.com/user-attachments/assets/61e1f7f2-8b5b-4ade-a382-48ec4f2b8020)

<br/><br/>

### 📌 모델링 결과
<table style="margin: auto; border-collapse: collapse; text-align: center;">
    <thead>
        <tr>
            <th>Model</th>
            <th>AUC</th>
            <th>Data<br>(train(SMOTE),<br>test)</th>
            <th>ROC Curve</th>
            <th>Confusion Matrix</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>model</td>
            <td>0.8523</td>
            <td>8276, 1409</td> 
            <td>
                <img src="https://github.com/user-attachments/assets/3b86643f-3b63-4bc9-b1d5-6adf584c5a06" style="width: 300px; display: block; margin: auto;" alt="ROC Curve 1">
            </td>
            <td>
                <img src="https://github.com/user-attachments/assets/32afa08b-a3ad-442e-95f2-8ec4ce6f6b26" style="width: 300px; display: block; margin: auto;" alt="Confusion Matrix 1">
            </td>
        </tr>
        <tr>
            <td>P0_D0_model</td>
            <td>0.8313</td>
            <td>3434, 656</td> 
            <td>
                <img src="https://github.com/user-attachments/assets/c6a02814-5a3e-4e7d-8af1-a7760d565a24" style="width: 300px; display: block; margin: auto;" alt="ROC Curve 2">
            </td>
            <td>
                <img src="https://github.com/user-attachments/assets/5f07a26f-e293-44ba-b94e-d707d15bdf51" style="width: 300px; display: block; margin: auto;" alt="Confusion Matrix 2">
            </td>
        </tr>
        <tr>
            <td>P0_D1_model</td>
            <td>0.7712</td>
            <td>446, 73</td> 
            <td>
                <img src="https://github.com/user-attachments/assets/eec0d373-6567-4688-9a26-a9463167a8c8" style="width: 300px; display: block; margin: auto;" alt="ROC Curve 3">
            </td>
            <td>
                <img src="https://github.com/user-attachments/assets/f58562b9-1ef9-49dc-8908-ef041e14e0b0" style="width: 300px; display: block; margin: auto;" alt="Confusion Matrix 3">
            </td>
        </tr>
        <tr>
            <td>P1_D0_model</td>
            <td>0.8246</td>
            <td>1972, 331</td> 
            <td>
                <img src="https://github.com/user-attachments/assets/02255942-1fef-4e55-a717-3481e2659605" style="width: 300px; display: block; margin: auto;" alt="ROC Curve 4">
            </td>
            <td>
                <img src="https://github.com/user-attachments/assets/57c02ea9-fdc7-414f-857c-0fcb1fc18675" style="width: 300px; display: block; margin: auto;" alt="Confusion Matrix 4">
            </td>
        </tr>
        <tr>
            <td>P1_D1_model</td>
            <td>0.8072</td>
            <td>2388, 350</td> 
            <td>
                <img src="https://github.com/user-attachments/assets/90991a64-c9e4-4743-9acb-b491583410af" style="width: 300px; display: block; margin: auto;" alt="ROC Curve 5">
            </td>
            <td>
                <img src="https://github.com/user-attachments/assets/5da36d83-33a1-4485-bc01-0e4af9f032e8" style="width: 300px; display: block; margin: auto;" alt="Confusion Matrix 5">
            </td>
        </tr>
    </tbody>
</table>
