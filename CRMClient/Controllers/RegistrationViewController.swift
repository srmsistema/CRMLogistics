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
    @IBOutlet weak var checkField: UITextField!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        nameField.text = ""
        emailField.text = ""
        passwordField.text = ""
        checkField.text = ""
    }
    
    
    @IBAction func saveInfo(_ sender: Any) {
        if nameField.text != "" && emailField.text != "" && passwordField.text != "" && checkField.text != ""{
            let name = nameField.text!
            let email = emailField.text!
            let password = passwordField.text!
            let password_check = checkField.text!
            print(name, email, password)
            let userInfo = UserInfo(username: name, email: email, password: password)
            
            ServerManager.shared.postUserInfo(userInfo: userInfo, { (user) in
                UserDefaults.standard.set(user.token, forKey: "token")
                print(UserDefaults.standard.value(forKey: "token") as! String)
                }, {
                    (error) in
                    print("h ", error)
            })
                
        }
        
    }
    

}

