//
//  EnterViewController.swift
//  CRMClient
//
//  Created by Nurzhan Ababakirov on 2/22/20.
//  Copyright © 2020 Nurzhan Ababakirov. All rights reserved.
//
import UIKit
import Foundation

class DriverSignInViewController: UIViewController {

    @IBOutlet weak var nameField: UITextField!
    @IBOutlet weak var passwordField: UITextField!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        nameField.text = ""
        passwordField.text = ""
    }
    
    @IBAction func saveInfo(_ sender: Any){
            if nameField.text != "" && passwordField.text != "" {
                let name = nameField.text!
                let password = passwordField.text!
                print(name, password)
                let loginInfo = LogInfo(username: name, password: password)
                
                 ServerManager.shared.postSignIn(loginInfo: loginInfo, { (successMessage) in
                              print(successMessage)
                           self.nextVC(identifier: "DriverVC")
                           }) { (error) in
                            self.createAlert(title: "Ошибка", message: "Неправильный логин или пароль")
                              print(error)
                           }
                    
            }
            
        }
     func nextVC(identifier: String) {
           let storyboard = UIStoryboard(name: "Main", bundle: nil)
               let nextVC = storyboard.instantiateViewController(withIdentifier: identifier)
           nextVC.modalPresentationStyle = .fullScreen
               self.present(nextVC, animated: true, completion: nil)
       }
    func createAlert(title: String, message: String)
       {
           let alert = UIAlertController(title: title, message: message, preferredStyle: UIAlertController.Style.alert)
           
           alert.addAction(UIAlertAction(title: "ОК", style: UIAlertAction.Style.default, handler: {(action) in alert.dismiss(animated: true, completion: nil)}))
               self.present(alert, animated: true, completion: nil)
           
           
       }

    }

