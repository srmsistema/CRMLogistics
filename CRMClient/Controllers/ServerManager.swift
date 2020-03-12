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
//
//    func postPhone(phone: String, _ completion: @escaping (User)-> Void, _ error: @escaping (String)-> Void) {
//        let parameters: [String: Any] = [
//            "phone": phone,
//        ]
//        let header = ["Content-Type": "application/json"]
//        self.post(url: "http://protected-peak-29297.herokuapp.com/login/", parameters: parameters, header: header, completion: { (data) in
//            do {
//                guard let data = data else {return}
//                let user = try JSONDecoder().decode(User.self, from: data)
//                DispatchQueue.main.async {
//                    completion(user)
//                }
//            } catch let err {
//                error(err.localizedDescription)
//            }
//        }, error: error)
//    }
//
//    func postUserInfo(token: String, userInfo: UserInfo, _ completion: @escaping (String)-> Void, _ error: @escaping (String)-> Void) {
//        let dicArray = userInfo.automobile.map {
//            $0.dictionaryRepresentation
//        }
//        let parameters: [String: Any] = [
//            "full_name": userInfo.full_name,
//            "address": userInfo.address,
//            "flat": userInfo.flat,
//            "floor": userInfo.floor,
//            "people": userInfo.people,
//            "owner_type": userInfo.owner_type,
//            "automobile": dicArray
//        ]
//        let header: [String: String] = [
//            "Content-Type": "application/json",
//            "Authorization": "Token \(token)"
//        ]
//        self.post(url: "http://protected-peak-29297.herokuapp.com/login/", parameters: parameters, header: header, completion: { (data) in
//            guard let data = data else {return}
//            DispatchQueue.main.async {
//                completion("\(data)")
//            }
//        }, error: error)
//    }
//
//    func getNewsList(token: String, _ completion: @escaping ([NewsCellStruct])-> Void, _ error: @escaping (String)-> Void) {
//        let header: [String: String] = [
//            "Content-Type": "application/json",
//            "Authorization": "Token \(token)"
//        ]
//        self.get(url: "http://protected-peak-29297.herokuapp.com/login/", header: header, completion: {
//            (data) in
//            do {
//                guard let data = data else {return}
//                let newsList = try JSONDecoder().decode([NewsCellStruct].self, from: data)
//                DispatchQueue.main.async {
//                    completion(newsList)
//                }
//            } catch let err {
//                error(err.localizedDescription)
//            }
//        }, error: error)
//    }
    
    
    func postSignUp(user: User, _ completion: @escaping (User)-> Void, _ error: @escaping (String)-> Void){
          let parameters: [String: Any] = [
            "first_name": user.first_name,
                    "email": "sardar@gmail.com",
                    "first_name": "Sardar",
                    "last_name": "Product",
                    "gender": "male",
                    "dateOfBirth": "2020-02-03",
                    "phone": "+996709070998",
                    "photo": null,
                    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MywiZXhwIjoxNTg4ODMyMTE1fQ.Gl5UEAfBhbt9h3S3jgwfO8jdBhOpJKjS7IQk9sY-bD8"
                ]
        let header: [String: String] = [
                    "Content-Type": "application/json",
                    //"Authorization": "Token \(token)"
                ]
        self.post(url: "http://protected-peak-29297.herokuapp.com/signup/", parameters: parameters, header: header, completion: { (data) in
           do {
                            guard let data = data else {return}
                            let user = try JSONDecoder().decode(User.self, from: data)
                            DispatchQueue.main.async {
                                completion(user)
                            }
                        } catch let err {
                            error(err.localizedDescription)
                        }
        }, error: { (error) in
            print(error)
        })
    }
    
}



