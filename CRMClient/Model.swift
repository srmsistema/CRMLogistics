//
//  Model.swift
//  CRMClient
//
//  Created by Nurzhan Ababakirov on 3/8/20.
//  Copyright © 2020 Nurzhan Ababakirov. All rights reserved.
//

import Foundation

struct User: Codable {
    let username, email, first_name: String
    let last_name, gender, dateOfBirth, phone: String
    let photo: String
    let token:String
}

struct UserInfo: Codable {
    let username, email, password: String
}

struct LogInfo: Codable {
    let username, password: String
}

struct TokInfo: Codable {
    let username, token: String
}



