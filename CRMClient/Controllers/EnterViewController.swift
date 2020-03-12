//
//  EnterViewController.swift
//  CRMClient
//
//  Created by Nurzhan Ababakirov on 2/22/20.
//  Copyright © 2020 Nurzhan Ababakirov. All rights reserved.
//
import UIKit
import Foundation

class EnterViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    
    
    let user = User(username: "sar", password: "12313414", email:"sda", first_name: "", last_name: "", gender: "", dateOfBirth: "", phone: "", photo: "", token: "")
    }
    func post(){
        ServerManager.shared.postSignUp()
        
//    let url = URL(string: "https://polls.apiblueprint.org/login")!
//    var request = URLRequest(url: url)
//    request.httpMethod = "POST"
//    request.addValue("application/json", forHTTPHeaderField: "Content-Type")
//
//    request.httpBody = """
//    {
//        \"email\": \"altynai@gmail.com\",
//        \"username\": \"altynaibest\",
//    }
//    """.data(using: .utf8)
//
//    let task = URLSession.shared.dataTask(with: request) { data, response, error in
//      if let response = response {
//        print(response)
//
//        if let data = data, let body = String(data: data, encoding: .utf8) {
//          print(body)
//        }
//      } else {
//        print(error ?? "Unknown error")
//      }
//    }
//
//    task.resume()

    }
    
}

