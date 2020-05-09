//
//  ServerManager.swift
//  CRMClient
//
//  Created by Nurzhan Ababakirov on 3/5/20.
//  Copyright © 2020 Nurzhan Ababakirov. All rights reserved.

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
    
     
    func getProfileInfo(token: String, _ completion: @escaping ([Profile]) -> Void, _ error: @escaping (String) -> Void){
        let header: [String: String] = [
            "Authorization": "Bearer \(token)"
        ]
       self.get(url: "http://crmlogistics.herokuapp.com/clients/", header: header, completion: {
            (data) in
            do {
                guard let data = data else {return}
                let profileInfo = try JSONDecoder().decode([Profile].self, from: data)
                DispatchQueue.main.async {
                    completion(profileInfo)
                }
            } catch let err {
                       error(err.localizedDescription)
                   }
               }, error: error)
    }
    
    func getDriverProfileInfo(token: String, _ completion: @escaping (DriverProfileStruct) -> Void, _ error: @escaping (String) -> Void){
        let header: [String: String] = [
            "Authorization": "Bearer \(token)"
        ]
       self.get(url: "https://crmlogistics.herokuapp.com/drivers/profile", header: header, completion: {
            (data) in
            do {
                guard let data = data else {return}
                let profileInfo = try JSONDecoder().decode(DriverProfileStruct.self, from: data)
                DispatchQueue.main.async {
                    completion(profileInfo)
                }
            } catch let err {
                       error(err.localizedDescription)
                   }
               }, error: error)
    }
    
    func putStatusOrder(token: String, id: Int, statusOrder: OrderStatusStruct,_ completion: @escaping(OrderStatusStruct)-> Void,_ error: @escaping (String)-> Void){
        let parameters: [String: Any] = [
            "orderStatus": statusOrder.orderStatus
        ]
        
        let header: [String: String] = [
            "Authorization": "Bearer \(token)"
            ]
        
        self.put(url: "http://crmlogistics.herokuapp.com/order/update/\(id)", parameters: parameters, header: header, completion: {(data) in

                   print(data ?? "success")
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
    
        func getOrderList(token: String, _ completion: @escaping ([OrderStruct]) -> Void, _ error: @escaping (String) -> Void){
        let header: [String: String] = [
            "Authorization": "Bearer \(token)"
        ]
        self.get(url: "https://crmlogistics.herokuapp.com/order/", header: header, completion: {
            (data) in
            do {
                guard let data = data else {return}
                let orderList = try JSONDecoder().decode([OrderStruct].self, from: data)
                DispatchQueue.main.async {
                    completion(orderList)
                }
            } catch let err {
                       error(err.localizedDescription)
                   }
               }, error: error)
        }
        func getDriverMyOrderList(token: String, _ completion: @escaping ([DriverOrderStruct]) -> Void, _ error: @escaping (String) -> Void){
        let header: [String: String] = [
            "Authorization": "Bearer \(token)"
        ]
        self.get(url: "https://crmlogistics.herokuapp.com/drivers/order", header: header, completion: {
            (data) in
            do {
                guard let data = data else {return}
                let orderList = try JSONDecoder().decode([DriverOrderStruct].self, from: data)
                DispatchQueue.main.async {
                    completion(orderList)
                }
            } catch let err {
                       error(err.localizedDescription)
                   }
               }, error: error)
        }
    
        func getDriverOrderList(token: String, _ completion: @escaping ([DriverOrderStruct]) -> Void, _ error: @escaping (String) -> Void){
        let header: [String: String] = [
            "Authorization": "Bearer \(token)"
        ]
        self.get(url: "https://crmlogistics.herokuapp.com/order/", header: header, completion: {
            (data) in
            do {
                guard let data = data else {return}
                let orderList = try JSONDecoder().decode([DriverOrderStruct].self, from: data)
                DispatchQueue.main.async {
                    completion(orderList)
                }
            } catch let err {
                       error(err.localizedDescription)
                   }
               }, error: error)
        }
    
        func postDriverSignIn(loginInfo: LogInfo, _ completion: @escaping (TokInfo)-> Void, _ error: @escaping (String)-> Void){
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
}



 
