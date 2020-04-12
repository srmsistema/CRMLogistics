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
    
  func postUserInfo(userInfo: UserInfo, _ completion: @escaping (TokenInfo)-> Void, _ error: @escaping (String)-> Void) {
        let user: [String: Any] = [
            "username": userInfo.user.username,
            "password": userInfo.user.password,
            "email": userInfo.user.email
    
        ]
        let parameters: [String: Any] = [
            "user": user,
            "first_name": userInfo.first_name,
            "last_name": userInfo.last_name,
            "gender": userInfo.gender,
            "dateOfBirth": userInfo.dateOfBirth,
            "phone": userInfo.phone,
            
        ]
        print(parameters)
        
        let header: [String: String] = [
                    "Content-Type": "application/json"
                ]
    self.post(url: "https://crmlogistics.herokuapp.com/signup/", parameters: parameters, header: header, completion: { (data) in
           do {
                            guard let data = data else {return}
                            print(data)
                            let user = try JSONDecoder().decode(TokenInfo.self, from: data)
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
        
        self.post(url: "https://crmlogistics.herokuapp.com/login/", parameters: parameters, header: header, completion: { (data) in
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
    
     
    func getUserInfo(userInfo: UserInfo, _ completion: @escaping (UserInfo) -> Void, _ error: @escaping (String) -> Void){
        let header: [String: String] = [
            "Content-Type": "application/json"
        ]
        self.get(url: "http://protected-peak-29297.herokuapp.com/users/", header: header, completion: {
            (data) in
            do {
                guard let data = data else {return}
                let userInfo = try JSONDecoder().decode(UserInfo.self, from: data)
                DispatchQueue.main.async {
                    completion(userInfo)
                }
            } catch let err {
                       error(err.localizedDescription)
                   }
               }, error: error)
    }
    
    func postOrderInfo(token: String, createOrder: CreateOrder,_ completion: @escaping(CreateOrder)-> Void,_ error: @escaping (String)-> Void){
        
        let volume: [String: Any] = [
            "width": createOrder.volume.width,
            "height": createOrder.volume.height,
            "length": createOrder.volume.length,
            "unit": createOrder.volume.unit
        
        ]
        
        let locationCargo: [String: Any] = [
            "address": createOrder.location_cargo.address
        ]
        
        let stateAwning: [String: Any] = [
            "noHoles": createOrder.state_awning.no_holes,
            "noGaps": createOrder.state_awning.no_gaps,
            "dry": createOrder.state_awning.dry,
            "noPatches": createOrder.state_awning.no_patches
        ]
        
        let parameters: [String: Any] = [
            "name": createOrder.name,
            "priceClient": createOrder.price_client,
            "requirementsLoading": createOrder.requirements_loading,
            "typeCargo": createOrder.type_cargo,
            "typeAuto": createOrder.type_auto,
            "autoReleaseYear": createOrder.auto_releaseyear,
            "typeLoading": createOrder.type_loading,
            "stateAwning": stateAwning,
            "weight": createOrder.weight,
            "weightMeasurementUnit": createOrder.weight_measurementunit,
            "volume": volume,
            "locationCargo": locationCargo
            ]
        
        
    print(parameters)
        let header: [String: String] = [
            "Content-Type": "application/json",
            "Authorization": "Bearer \(token)"
            
            ]
       
    self.post(url: "http://crmlogistics.herokuapp.com/order/create/", parameters: parameters, header: header, completion: {(data) in
            print(data ?? "success")
        }, error: error)
    }
}



