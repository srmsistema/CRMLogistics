//
//  CreateAccountViewController.swift
//  CRMClient
//
//  Created by Nurzhan Ababakirov on 2/22/20.
//  Copyright © 2020 Nurzhan Ababakirov. All rights reserved.
//

import UIKit

class RegistrationViewController: UIViewController {

    @IBOutlet weak var nameField: UITextField!
    @IBOutlet weak var emailField: UITextField!
    @IBOutlet weak var passwordField: UITextField!
    @IBOutlet weak var firstNameField: UITextField!
    @IBOutlet weak var lastNameField: UITextField!
    @IBOutlet weak var dateOfBirthField: UITextField!
    @IBOutlet weak var numberField: UITextField!
    @IBOutlet weak var genderField: UITextField!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        nameField.text = ""
        emailField.text = ""
        passwordField.text = ""
        firstNameField.text = ""
        lastNameField.text = ""
        numberField.text = ""
        genderField.text = ""
        dateOfBirthField.text = ""

    }
    
    
    @IBAction func saveInfo(_ sender: Any) {
        if nameField.text != "" && emailField.text != "" && passwordField.text != "" && firstNameField.text != "" && lastNameField.text != "" && numberField.text != "" && genderField.text != "" && dateOfBirthField.text != ""{
            
            let name = nameField.text!
            let email = emailField.text!
            let password = passwordField.text!
            let firstName = firstNameField.text!
            let lastName = lastNameField.text!
            let phone = numberField.text!
            let dateOfBirth = dateOfBirthField.text!
            let gender = genderField.text!
    
            
            print(name, email, password, firstName, lastName, phone, dateOfBirth, gender)
            
            let user = User(username: name, email: email, password: password)
            let userInfo = UserInfo(user: user, first_name: firstName, last_name: lastName, gender: gender, dateOfBirth: dateOfBirth, phone: phone)
            
            print(userInfo.user.username)
            
            ServerManager.shared.postUserInfo(userInfo: userInfo, { (user) in
                
                print(user)
                UserDefaults.standard.set(user.user.token, forKey: "token")
                print(UserDefaults.standard.value(forKey: "token") as! String)
                createAlert(title: "Поздравляем!", message: "Вы зарегистрировались! Нажмите 'Продолжить', чтобы войти")
                }, {
                    (error) in
                    createAlertError(title: "Ошибка!", message: "Проверьте правильность полей")
                    print(error, "IAM")
            })
            
            
            
    func createAlert(title: String, message: String)
    {
        let alert = UIAlertController(title: title, message: message, preferredStyle: UIAlertController.Style.alert)
        
        alert.addAction(UIAlertAction(title: "Продолжить", style: UIAlertAction.Style.default, handler: {(action) in
            nextVC(identifier: "LoginVC")
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
    }
}
