//
//  StatusViewController.swift
//  CRMClient
//
//  Created by Nurzhan Ababakirov on 3/3/20.
//  Copyright © 2020 Nurzhan Ababakirov. All rights reserved.
//

import UIKit

class StatusViewController:  UIViewController, UITextFieldDelegate, UIPickerViewDelegate, UIPickerViewDataSource {
    
    @IBOutlet weak var statusField: UITextField!
    
    let id = DriverOrderViewController()
    let statusT = DriverDetailsViewController()
    let status = ["Новая","Заключена", "Погрузка","Транспортировка","Выгрузка","Завершена","Отменена"]
    
    let pickerView = UIPickerView()
    var currentArr : [String] = []
    var activeTextField: UITextField!

    override func viewDidLoad() {
        super.viewDidLoad()
        
        statusField.delegate = self
        
        pickerView.delegate = self
        pickerView.dataSource = self
        
        statusField.inputView = pickerView
        
        
    }
    

    @IBAction func statusButton(_ sender: Any) {
    
                        if statusField.text != ""{
                        let typeOfStatus = statusField.text!
                        var numStatus = ""
                        switch typeOfStatus {
                        case "Новая":
                            numStatus = "Новая"
                        case "Заключена":
                            numStatus = "Заключена"
                        case "Погрузка":
                            numStatus = "Погрузка"
                        case "Транспортировка":
                            numStatus = "Транспортировка"
                        case "Выгрузка":
                            numStatus = "Выгрузка"
                        case "Завершена":
                            numStatus = "Завершена"
                        case "Отменена":
                            numStatus = "Отменена"

                        default: ()
                        }
                        
                        let statusOrder = OrderStatusStruct(orderStatus: numStatus)
                            print(statusOrder.orderStatus)
                        ServerManager.shared.putStatusOrder(token: UserDefaults.standard.value(forKey: "token") as! String, id: UserDefaults.standard.value(forKey: "id") as! Int, statusOrder: statusOrder, { (successMessage) in
                            print(successMessage)
                        }) { (error) in
                           print(error + "g")
                        }
                            DispatchQueue.main.async{
                                DriverDetailsViewController.self
                            }
                }
    }

        func textFieldShouldBeginEditing(_ textField: UITextField) -> Bool {
        activeTextField = textField
        
        switch textField {
        case statusField:
            currentArr = status
        default:
            print("Default")
        }
        pickerView.reloadAllComponents()
        return true
    }

    
    
    // Picker View
    func numberOfComponents(in pickerView: UIPickerView) -> Int {
        return 1
    }
    
    func pickerView(_ pickerView: UIPickerView, numberOfRowsInComponent component: Int) -> Int {
        return currentArr.count
    }
    
    func pickerView(_ pickerView: UIPickerView, titleForRow row: Int, forComponent component: Int) -> String? {
        return currentArr[row]
    }
    
    func pickerView(_ pickerView: UIPickerView, didSelectRow row: Int, inComponent component: Int) {
        print("Selected", currentArr[row])
        activeTextField.text = currentArr[row]
    }
}
