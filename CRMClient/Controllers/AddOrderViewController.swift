//
//  AddOrderViewController.swift
//  CRMClient
//
//  Created by Nurzhan Ababakirov on 4/8/20.
//  Copyright © 2020 Nurzhan Ababakirov. All rights reserved.
//

import UIKit

class AddOrderViewController: UIViewController, UITextFieldDelegate, UIPickerViewDelegate, UIPickerViewDataSource {

    @IBOutlet weak var nameField: UITextField!
    @IBOutlet weak var typeOfCargoField: UITextField!
    @IBOutlet weak var typeOfCarField: UITextField!
    @IBOutlet weak var typeOfLoadField: UITextField!
    @IBOutlet weak var typeOfUnitsField: UITextField!
    @IBOutlet weak var priceClientField: UITextField!
    @IBOutlet weak var autoReleaseYearField: UITextField!
    @IBOutlet weak var holesField: UITextField!
    @IBOutlet weak var gapsField: UITextField!
    @IBOutlet weak var dryField: UITextField!
    @IBOutlet weak var patchField: UITextField!
    @IBOutlet weak var weightField: UITextField!
    @IBOutlet weak var widthField: UITextField!
    @IBOutlet weak var heightField: UITextField!
    @IBOutlet weak var lengthField: UITextField!
    @IBOutlet weak var unitField: UITextField!
    @IBOutlet weak var requirementsLoadingField: UITextField!
    @IBOutlet weak var addressField: UITextField!
    
    
    
    let cargo = ["Наволочные","Запалеченные","Общие","Режимный груз","Опасный груз"]
    let car = ["Тентованный полуприцеп (еврофура)","Jumbo","Автосцепка","Рефрижераторный фургон","Изотермический фургон","Контейнеровоз","Открытый бортовой полуприцеп"]
    let load = ["Задняя навалом","Задняя на паллетах","Задняя самоходом","Боковая навалом","Боковая на паллетах","Верхняя"]
    let units = ["Тонна","Килограмм"]
    let holes = ["Да","Нет"]
    let gaps = ["Да","Нет"]
    let dry = ["Да","Нет"]
    let patches = ["Да","Нет"]
    let volume = ["Метр","Сантиметр"]
    
    
    
    let pickerView = UIPickerView()
    var currentArr : [String] = []
    var activeTextField: UITextField!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        
        typeOfCargoField.delegate = self
        typeOfCarField.delegate = self
        typeOfLoadField.delegate = self
        typeOfUnitsField.delegate = self
        holesField.delegate = self
        gapsField.delegate = self
        dryField.delegate = self
        patchField.delegate = self
        unitField.delegate = self
        
        pickerView.delegate = self
        pickerView.dataSource = self
        
        typeOfCargoField.inputView = pickerView
        typeOfCarField.inputView = pickerView
        typeOfLoadField.inputView = pickerView
        typeOfUnitsField.inputView = pickerView
        holesField.inputView = pickerView
        gapsField.inputView = pickerView
        dryField.inputView = pickerView
        patchField.inputView = pickerView
        unitField.inputView = pickerView
        
    }
    
    @IBAction func saveInfo(_ sender: Any) {
        if typeOfCargoField.text != "" && typeOfCarField.text != "" && typeOfLoadField.text != "" && typeOfUnitsField.text != "" && priceClientField.text != "" && autoReleaseYearField.text != "" && weightField.text != "" && widthField.text != "" && heightField.text != "" && lengthField.text != "" && unitField.text != "" && addressField.text != "" && nameField.text != ""
        {
                        
            let typeOfCar = typeOfCarField.text!
            var numCar = 0
            switch typeOfCar {
            case "Тентованный полуприцеп (еврофура)":
                numCar = 1
            case "Jumbo":
                numCar = 2
            case "Автосцепка":
                numCar = 3
            case "Рефрижераторный фургон":
                numCar = 4
            case "Изотермический фургон":
                numCar = 5
            case "Контейнеровоз":
                numCar = 6
            case "Открытый бортовой полуприцеп":
                numCar = 7
                
            default: ()
            }
            
            let typeOfCargo = typeOfCargoField.text!
            var numCarGo = 0
            switch typeOfCargo {
            case "Наволочные":
                numCarGo = 1
            case "Запалеченные":
                numCarGo = 2
            case "Общие":
                numCarGo = 3
            case "Режимный груз":
                numCarGo = 4
            case "Опасный груз":
                numCarGo = 5
            default: ()
            }

            
            let typeOfLoad = typeOfLoadField.text!
            var numLoad = 0
            switch typeOfLoad {
            case "Задняя навалом":
                numLoad = 1
            case "Задняя на паллетах":
                numLoad = 2
            case "Задняя самоходом":
                numLoad = 3
            case "Боковая навалом":
                numLoad = 4
            case "Боковая на паллетах":
                numLoad = 5
            case "Верхняя":
                numLoad = 6
                
            default: ()
            }
            
            let noHoles = holesField.text!
            var numHoles = true
            switch noHoles {
            case "Да":
                numHoles = true
            case "Нет":
                numHoles = false
            default: ()
            }
            
            let noGaps = gapsField.text!
            var numGaps = true
            switch noGaps {
            case "Да":
                numHoles = true
            case "Нет":
                numHoles = false
            default: ()
            }
            
            let noDry = dryField.text!
            var numDry = true
            switch noDry {
            case "Да":
                numHoles = false
            case "Нет":
                numHoles = true
            default: ()
            }
            
            let noPatches = patchField.text!
            var numPatches = true
            switch noPatches {
            case "Да":
                numHoles = false
            case "Нет":
                numHoles = true
            default: ()
            }
            
            let typeOfVolume = unitField.text!
            var numVol = 0
            switch typeOfVolume {
            case "Метр":
                numVol = 1
            case "Сантиметр":
                numVol = 2
            default: ()
                }
            
            let typeOfUnits = typeOfUnitsField.text!
            var numUnit = 0
            switch typeOfUnits {
            case "Тонна":
                numUnit = 1
            case "Килограмм":
                numUnit = 2
                
            default: ()

            }
                        
            
            let name = nameField.text!
            let requirementsLoading = requirementsLoadingField.text!
            let priceClient = Int(priceClientField.text!)
            let autoReleaseYear = Int(autoReleaseYearField.text!)
            let weight = Int(weightField.text!)
            let width = Int(widthField.text!)
            let height = Int(heightField.text!)
            let length = Int(lengthField.text!)
            let address = addressField.text!
            
            let locationCargo = LocationCargo(address: address)
            let volume = Volume(width: width! , height: height!, length: length!, unit: numVol)
            let stateAwing = StateAwning(no_holes: numHoles, no_gaps: numGaps, dry: numDry, no_patches: numPatches)
            
            let createOrder = CreateOrder(name: name, price_client: priceClient!, requirements_loading: requirementsLoading, type_cargo: numCarGo, type_auto: numCar, auto_releaseyear: autoReleaseYear!, type_loading: numLoad, state_awning: stateAwing, weight: weight!, weight_measurementunit: numUnit, volume: volume, location_cargo: locationCargo)
            
            ServerManager.shared.postOrderInfo(token: UserDefaults.standard.value(forKey: "token") as! String,createOrder: createOrder, { (successMessage) in
                nextVC(identifier: "MainVC")
                print(successMessage)
            }) { (error) in
                createAlertError(title: "Ошибка", message: "Проверьте данные")
               print(error)
            }
            
        }
        func createAlert(title: String, message: String)
        {
            let alert = UIAlertController(title: title, message: message, preferredStyle: UIAlertController.Style.alert)
            
            alert.addAction(UIAlertAction(title: "Продолжить", style: UIAlertAction.Style.default, handler: {(action) in
                nextVC(identifier: "MainVC")
                alert.dismiss(animated: true, completion: nil)}))
            
            self.present(alert, animated: true, completion: nil)
        }
        
        func createAlertError(title: String, message: String)
           {
               let alert = UIAlertController(title: title, message: message, preferredStyle: UIAlertController.Style.alert)
               
               alert.addAction(UIAlertAction(title: "ОК", style: UIAlertAction.Style.default, handler: {(action) in
                alert.dismiss(animated: true, completion: nil)}))
               
               self.present(alert, animated: true, completion: nil)
               
               
           }


        func nextVC(identifier: String)
         {
                     let storyboard = UIStoryboard(name: "Main", bundle: nil)
                         let nextVC = storyboard.instantiateViewController(withIdentifier: identifier)
                     nextVC.modalPresentationStyle = .fullScreen
                         self.present(nextVC, animated: true, completion: nil)
         }
        
    }
    

    
    //MARK: Picker
    func textFieldShouldBeginEditing(_ textField: UITextField) -> Bool {
        activeTextField = textField
        
        switch textField {
        case typeOfCargoField:
            currentArr = cargo
        case typeOfCarField:
            currentArr = car
        case typeOfLoadField:
            currentArr = load
        case typeOfUnitsField:
            currentArr = units
        case holesField:
            currentArr = holes
        case gapsField:
            currentArr = gaps
        case dryField:
            currentArr = dry
        case patchField:
            currentArr = patches
        case unitField:
            currentArr = volume
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
