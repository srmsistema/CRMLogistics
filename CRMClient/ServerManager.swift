//
//  ServerManager.swift
//  CRMClient
//
//  Created by Nurzhan Ababakirov on 3/5/20.
//  Copyright © 2020 Nurzhan Ababakirov. All rights reserved.
//

import UIKit
import Alamofire

class ServerManager: HTTPRequestManager  {
    
    class var shared: ServerManager {
        struct Static {
            static let instance = ServerManager()
        }
        return Static.instance
    }
}

extension ServerManager {
    
    
    func postUserInfo(userInfo: UserInfo, _ completion: @escaping (User)-> Void, _ error: @escaping (String)-> Void) {
        
        let parameters: [String: Any] = [
            "username": userInfo.username,
            "email": userInfo.email,
            "password": userInfo.password
        ]
        
        let header: [String: String] = [
                    "Content-Type": "application/json"
                ]
        self.post(url: "https://protected-peak-29297.herokuapp.com/signup/", parameters: parameters, header: header, completion: { (data) in
           do {
                            guard let data = data else {return}
                            let user = try JSONDecoder().decode(User.self, from: data)
                            DispatchQueue.main.async {
                                completion(user)
                            }
                        } catch let err {
                            error(err.localizedDescription)
                        }
        }, error: error)
    }
    
    func postSignIn(loginInfo: LogInfo, _ completion: @escaping (TokInfo)-> Void, _ error: @escaping (String)-> Void){
        let parameters: [String: Any] = [
            "username": loginInfo.username,
            "password": loginInfo.password
        ]
        
        let header: [String: String] = [
            "Content-Type": "application/json"
        ]
        
        self.post(url: "http://protected-peak-29297.herokuapp.com/login/", parameters: parameters, header: header, completion: { (data) in
            do {
                                    guard let data = data else {return}
                                    let tokInfo = try JSONDecoder().decode(TokInfo.self, from: data)
                                    DispatchQueue.main.async {
                                        completion(tokInfo)
                                    }
                                } catch let err {
                                        error("\(err.localizedDescription) + I am cool")
                                    }
                    }, error: error)
                }
}



