# sub_00B2C5F4

- RVA: `0x00B2C5F4`–`0x00B2CB5B` (길이 `1,383` bytes)
- VA: `0x0000000140B2C5F4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009937C`
- 디코드: `357`개 명령, `1,383/1,383` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **21**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00B2C600` → [PiDevCfgParseVariableName](../../text/42/PiDevCfgParseVariableName_function_0042A6CC.md) (function, `0x0042A6CC`)
- `0x00B2C62C` → [PiDevCfgResolveVariable](../A8/PiDevCfgResolveVariable_function_00A81AB8.md) (function, `0x00A81AB8`)
- `0x00B2C6D6` → [PnpGetObjectProperty](../8E/PnpGetObjectProperty_function_008E2180.md) (function, `0x008E2180`)
- `0x00B2C6EE` → [PnpRegistryValueExists](../../text/5A/PnpRegistryValueExists_function_005A81A0.md) (function, `0x005A81A0`)
- `0x00B2C738` → [PnpValidateStringData](../../text/4B/PnpValidateStringData_function_004B7678.md) (function, `0x004B7678`)
- `0x00B2C74E` → [PiDevCfgParseVariableName](../../text/42/PiDevCfgParseVariableName_function_0042A6CC.md) (function, `0x0042A6CC`)
- `0x00B2C770` → [PiDevCfgResolveVariable](../A8/PiDevCfgResolveVariable_function_00A81AB8.md) (function, `0x00A81AB8`)
- `0x00B2C7C4` → [PiDevCfgResolveMultiSzValue](../AB/PiDevCfgResolveMultiSzValue_function_00AB6894.md) (function, `0x00AB6894`)
- `0x00B2C89E` → [PiDevCfgConvertPropertyFromValue](../73/PiDevCfgConvertPropertyFromValue_function_00732530.md) (function, `0x00732530`)
- `0x00B2C917` → [PiDevCfgSetObjectProperty](../A8/PiDevCfgSetObjectProperty_function_00A8DB50.md) (function, `0x00A8DB50`)
- `0x00B2C94C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00B2C96A` → [PiDevCfgParseVariableName](../../text/42/PiDevCfgParseVariableName_function_0042A6CC.md) (function, `0x0042A6CC`)
- `0x00B2C988` → [PiDevCfgResolveVariable](../A8/PiDevCfgResolveVariable_function_00A81AB8.md) (function, `0x00A81AB8`)
- `0x00B2C9B5` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00B2CA0A` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00B2CA45` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (function, `0x006AD310`)
- `0x00B2CA63` → [ZwSetSecurityObject](../../text/6B/ZwSetSecurityObject_function_006B0810.md) (function, `0x006B0810`)
- `0x00B2CAA4` → [ZwCreateKey](../../text/6A/ZwCreateKey_function_006AD470.md) (function, `0x006AD470`)
- `0x00B2CAED` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (function, `0x006AD310`)
- `0x00B2CB11` → [PiDevCfgPushCopyKeyEntry](../../text/4A/PiDevCfgPushCopyKeyEntry_function_004AFBA4.md) (function, `0x004AFBA4`)
- `0x00B2CB45` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00B2C6A2` → RVA `0x00E66398` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **14**
  - `0x00B2C600` → [PiDevCfgParseVariableName](../../text/42/PiDevCfgParseVariableName_function_0042A6CC.md) (`PAGE` → `.text`)
  - `0x00B2C6EE` → [PnpRegistryValueExists](../../text/5A/PnpRegistryValueExists_function_005A81A0.md) (`PAGE` → `.text`)
  - `0x00B2C738` → [PnpValidateStringData](../../text/4B/PnpValidateStringData_function_004B7678.md) (`PAGE` → `.text`)
  - `0x00B2C74E` → [PiDevCfgParseVariableName](../../text/42/PiDevCfgParseVariableName_function_0042A6CC.md) (`PAGE` → `.text`)
  - `0x00B2C94C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00B2C96A` → [PiDevCfgParseVariableName](../../text/42/PiDevCfgParseVariableName_function_0042A6CC.md) (`PAGE` → `.text`)
  - `0x00B2C9B5` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x00B2CA0A` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00B2CA45` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (`PAGE` → `.text`)
  - `0x00B2CA63` → [ZwSetSecurityObject](../../text/6B/ZwSetSecurityObject_function_006B0810.md) (`PAGE` → `.text`)
  - `0x00B2CAA4` → [ZwCreateKey](../../text/6A/ZwCreateKey_function_006AD470.md) (`PAGE` → `.text`)
  - `0x00B2CAED` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (`PAGE` → `.text`)
  - `0x00B2CB11` → [PiDevCfgPushCopyKeyEntry](../../text/4A/PiDevCfgPushCopyKeyEntry_function_004AFBA4.md) (`PAGE` → `.text`)
  - `0x00B2CB45` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **33**
  - `0x00B2C60D` → [PiDevCfgCopyDeviceKey + 0x1A0](../99/PiDevCfgCopyDeviceKey_function_00997374.md) (`tail-transfer`)
  - `0x00B2C617` → [PiDevCfgCopyDeviceKey + 0x369](../99/PiDevCfgCopyDeviceKey_function_00997374.md) (`tail-transfer`)
  - `0x00B2C643` → [PiDevCfgCopyDeviceKey + 0x369](../99/PiDevCfgCopyDeviceKey_function_00997374.md) (`tail-transfer`)
  - `0x00B2C650` → [PiDevCfgCopyDeviceKey + 0x369](../99/PiDevCfgCopyDeviceKey_function_00997374.md) (`tail-transfer`)
  - `0x00B2C672` → [PiDevCfgCopyDeviceKey + 0x1A0](../99/PiDevCfgCopyDeviceKey_function_00997374.md) (`tail-transfer`)
  - `0x00B2C67C` → [PiDevCfgCopyDeviceKey + 0x369](../99/PiDevCfgCopyDeviceKey_function_00997374.md) (`tail-transfer`)
  - `0x00B2C68B` → [PiDevCfgCopyDeviceKey + 0x1A0](../99/PiDevCfgCopyDeviceKey_function_00997374.md) (`tail-transfer`)
  - `0x00B2C70C` → [PiDevCfgCopyDeviceKey + 0x1DF](../99/PiDevCfgCopyDeviceKey_function_00997374.md) (`tail-transfer`)
  - `0x00B2C712` → [PiDevCfgCopyDeviceKey + 0x369](../99/PiDevCfgCopyDeviceKey_function_00997374.md) (`tail-transfer`)
  - `0x00B2C71B` → [PiDevCfgCopyDeviceKey + 0x369](../99/PiDevCfgCopyDeviceKey_function_00997374.md) (`tail-transfer`)
  - `0x00B2C721` → [PiDevCfgCopyDeviceKey + 0x1DF](../99/PiDevCfgCopyDeviceKey_function_00997374.md) (`tail-transfer`)
  - `0x00B2C72D` → [PiDevCfgCopyDeviceKey + 0x341](../99/PiDevCfgCopyDeviceKey_function_00997374.md) (`tail-transfer`)
  - `0x00B2C73F` → [PiDevCfgCopyDeviceKey + 0x23A](../99/PiDevCfgCopyDeviceKey_function_00997374.md) (`tail-transfer`)
  - `0x00B2C757` → [PiDevCfgCopyDeviceKey + 0x23A](../99/PiDevCfgCopyDeviceKey_function_00997374.md) (`tail-transfer`)
  - `0x00B2C7D4` → [PiDevCfgCopyDeviceKey + 0x434](../99/PiDevCfgCopyDeviceKey_function_00997374.md) (`tail-transfer`)
  - `0x00B2C7E0` → [PiDevCfgCopyDeviceKey + 0x254](../99/PiDevCfgCopyDeviceKey_function_00997374.md) (`tail-transfer`)
  - `0x00B2C801` → [PiDevCfgCopyDeviceKey + 0x254](../99/PiDevCfgCopyDeviceKey_function_00997374.md) (`tail-transfer`)
  - `0x00B2C814` → [PiDevCfgCopyDeviceKey + 0x254](../99/PiDevCfgCopyDeviceKey_function_00997374.md) (`tail-transfer`)
  - `0x00B2C81C` → [PiDevCfgCopyDeviceKey + 0x254](../99/PiDevCfgCopyDeviceKey_function_00997374.md) (`tail-transfer`)
  - `0x00B2C8CF` → [PiDevCfgCopyDeviceKey + 0x384](../99/PiDevCfgCopyDeviceKey_function_00997374.md) (`tail-transfer`)
  - `0x00B2C8DC` → [PiDevCfgCopyDeviceKey + 0x384](../99/PiDevCfgCopyDeviceKey_function_00997374.md) (`tail-transfer`)
  - `0x00B2C93C` → [PiDevCfgCopyDeviceKey + 0x384](../99/PiDevCfgCopyDeviceKey_function_00997374.md) (`tail-transfer`)
  - `0x00B2C958` → [PiDevCfgCopyDeviceKey + 0x384](../99/PiDevCfgCopyDeviceKey_function_00997374.md) (`tail-transfer`)
  - `0x00B2C973` → [PiDevCfgCopyDeviceKey + 0x540](../99/PiDevCfgCopyDeviceKey_function_00997374.md) (`tail-transfer`)
  - `0x00B2C9AB` → [PiDevCfgCopyDeviceKey + 0x540](../99/PiDevCfgCopyDeviceKey_function_00997374.md) (`tail-transfer`)
  - `0x00B2C9BF` → [PiDevCfgCopyDeviceKey + 0x61E](../99/PiDevCfgCopyDeviceKey_function_00997374.md) (`tail-transfer`)
  - `0x00B2C9E0` → [PiDevCfgCopyDeviceKey + 0x540](../99/PiDevCfgCopyDeviceKey_function_00997374.md) (`tail-transfer`)
  - `0x00B2C9F5` → [PiDevCfgCopyDeviceKey + 0x540](../99/PiDevCfgCopyDeviceKey_function_00997374.md) (`tail-transfer`)
  - `0x00B2C9FD` → [PiDevCfgCopyDeviceKey + 0x5FF](../99/PiDevCfgCopyDeviceKey_function_00997374.md) (`tail-transfer`)
  - `0x00B2CA6F` → [PiDevCfgCopyDeviceKey + 0x5FF](../99/PiDevCfgCopyDeviceKey_function_00997374.md) (`tail-transfer`)
  - `0x00B2CAAD` → [PiDevCfgCopyDeviceKey + 0x5FF](../99/PiDevCfgCopyDeviceKey_function_00997374.md) (`tail-transfer`)
  - `0x00B2CB4C` → [PiDevCfgCopyDeviceKey + 0x5FB](../99/PiDevCfgCopyDeviceKey_function_00997374.md) (`tail-transfer`)
  - `0x00B2CB56` → [PiDevCfgCopyDeviceKey + 0x2F7](../99/PiDevCfgCopyDeviceKey_function_00997374.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B2C5F4  4C 8D 44 24 74                  lea r8, [rsp + 0x74]
00B2C5F9  48 8B CE                        mov rcx, rsi
00B2C5FC  48 8D 55 30                     lea rdx, [rbp + 0x30]
00B2C600  E8 C7 E0 8F FF                  call 0x14042a6cc
00B2C605  8B 7C 24 74                     mov edi, dword ptr [rsp + 0x74]
00B2C609  33 D2                           xor edx, edx
00B2C60B  84 C0                           test al, al
00B2C60D  0F 84 01 AF E6 FF               je 0x140997514
00B2C613  0F BA E7 16                     bt edi, 0x16
00B2C617  0F 82 C0 B0 E6 FF               jb 0x1409976dd
00B2C61D  48 89 55 B0                     mov qword ptr [rbp - 0x50], rdx
00B2C621  4C 8D 45 B0                     lea r8, [rbp - 0x50]
00B2C625  48 8B 55 38                     mov rdx, qword ptr [rbp + 0x38]
00B2C629  48 8B CB                        mov rcx, rbx
00B2C62C  E8 87 54 F5 FF                  call 0x140a81ab8
00B2C631  33 D2                           xor edx, edx
00B2C633  85 C0                           test eax, eax
00B2C635  78 40                           js 0x140b2c677
00B2C637  48 8B 4D B0                     mov rcx, qword ptr [rbp - 0x50]
00B2C63B  8B 41 20                        mov eax, dword ptr [rcx + 0x20]
00B2C63E  FF C8                           dec eax
00B2C640  83 F8 01                        cmp eax, 1
00B2C643  0F 87 94 B0 E6 FF               ja 0x1409976dd
00B2C649  81 79 24 FE FF 00 00            cmp dword ptr [rcx + 0x24], 0xfffe
00B2C650  0F 87 87 B0 E6 FF               ja 0x1409976dd
00B2C656  48 8B 41 28                     mov rax, qword ptr [rcx + 0x28]
00B2C65A  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
00B2C65E  0F B7 41 24                     movzx eax, word ptr [rcx + 0x24]
00B2C662  66 83 E8 02                     sub ax, 2
00B2C666  66 89 45 C0                     mov word ptr [rbp - 0x40], ax
00B2C66A  0F B7 41 24                     movzx eax, word ptr [rcx + 0x24]
00B2C66E  66 89 45 C2                     mov word ptr [rbp - 0x3e], ax
00B2C672  E9 9D AE E6 FF                  jmp 0x140997514
00B2C677  3D 34 00 00 C0                  cmp eax, 0xc0000034
00B2C67C  0F 85 5B B0 E6 FF               jne 0x1409976dd
00B2C682  0F 28 45 30                     movaps xmm0, xmmword ptr [rbp + 0x30]
00B2C686  66 0F 7F 45 C0                  movdqa xmmword ptr [rbp - 0x40], xmm0
00B2C68B  E9 84 AE E6 FF                  jmp 0x140997514
00B2C690  4D 85 FF                        test r15, r15
00B2C693  74 50                           je 0x140b2c6e5
00B2C695  4C 8B 4C 24 68                  mov r9, qword ptr [rsp + 0x68]
00B2C69A  48 8D 45 A8                     lea rax, [rbp - 0x58]
00B2C69E  44 8B 45 D4                     mov r8d, dword ptr [rbp - 0x2c]
00B2C6A2  48 8B 0D EF 9C 33 00            mov rcx, qword ptr [rip + 0x339cef]
00B2C6A9  89 54 24 50                     mov dword ptr [rsp + 0x50], edx
00B2C6AD  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00B2C6B2  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00B2C6B7  89 54 24 40                     mov dword ptr [rsp + 0x40], edx
00B2C6BB  48 89 54 24 38                  mov qword ptr [rsp + 0x38], rdx
00B2C6C0  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00B2C6C5  48 8D 45 70                     lea rax, [rbp + 0x70]
00B2C6C9  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B2C6CE  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00B2C6D3  49 8B D7                        mov rdx, r15
00B2C6D6  E8 A5 5A DB FF                  call 0x1408e2180
00B2C6DB  3D 23 00 00 C0                  cmp eax, 0xc0000023
00B2C6E0  0F 94 C0                        sete al
00B2C6E3  EB 0E                           jmp 0x140b2c6f3
00B2C6E5  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00B2C6EA  48 8D 55 C0                     lea rdx, [rbp - 0x40]
00B2C6EE  E8 AD BA A7 FF                  call 0x1405a81a0
00B2C6F3  33 D2                           xor edx, edx
00B2C6F5  84 C0                           test al, al
00B2C6F7  74 1E                           je 0x140b2c717
00B2C6F9  0F BA E3 11                     bt ebx, 0x11
00B2C6FD  0F 93 C1                        setae cl
00B2C700  F6 85 00 01 00 00 01            test byte ptr [rbp + 0x100], 1
00B2C707  0F 95 C0                        setne al
00B2C70A  84 C8                           test al, cl
00B2C70C  0F 85 41 AE E6 FF               jne 0x140997553
00B2C712  E9 C6 AF E6 FF                  jmp 0x1409976dd
00B2C717  0F BA E3 10                     bt ebx, 0x10
00B2C71B  0F 82 BC AF E6 FF               jb 0x1409976dd
00B2C721  E9 2D AE E6 FF                  jmp 0x140997553
00B2C726  41 8D 46 FF                     lea eax, [r14 - 1]
00B2C72A  83 F8 01                        cmp eax, 1
00B2C72D  0F 87 82 AF E6 FF               ja 0x1409976b5
00B2C733  8B D7                           mov edx, edi
00B2C735  48 8B CE                        mov rcx, rsi
00B2C738  E8 3B AF 98 FF                  call 0x1404b7678
00B2C73D  84 C0                           test al, al
00B2C73F  0F 84 69 AE E6 FF               je 0x1409975ae
00B2C745  4C 8D 44 24 74                  lea r8, [rsp + 0x74]
00B2C74A  48 8D 55 30                     lea rdx, [rbp + 0x30]
00B2C74E  E8 79 DF 8F FF                  call 0x14042a6cc
00B2C753  33 D2                           xor edx, edx
00B2C755  84 C0                           test al, al
00B2C757  0F 84 51 AE E6 FF               je 0x1409975ae
00B2C75D  48 8B 75 38                     mov rsi, qword ptr [rbp + 0x38]
00B2C761  4C 8D 45 B0                     lea r8, [rbp - 0x50]
00B2C765  48 8B 4D 20                     mov rcx, qword ptr [rbp + 0x20]
00B2C769  48 89 55 B0                     mov qword ptr [rbp - 0x50], rdx
00B2C76D  48 8B D6                        mov rdx, rsi
00B2C770  E8 43 53 F5 FF                  call 0x140a81ab8
00B2C775  45 33 C0                        xor r8d, r8d
00B2C778  8B D8                           mov ebx, eax
00B2C77A  85 C0                           test eax, eax
00B2C77C  0F 88 84 00 00 00               js 0x140b2c806
00B2C782  44 8B 4C 24 74                  mov r9d, dword ptr [rsp + 0x74]
00B2C787  41 F7 C1 00 00 0C 00            test r9d, 0xc0000
00B2C78E  74 55                           je 0x140b2c7e5
00B2C790  48 8B 4D B0                     mov rcx, qword ptr [rbp - 0x50]
00B2C794  48 8D 45 B8                     lea rax, [rbp - 0x48]
00B2C798  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B2C79D  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00B2C7A2  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00B2C7A7  48 8B 45 C8                     mov rax, qword ptr [rbp - 0x38]
00B2C7AB  4C 8B 41 28                     mov r8, qword ptr [rcx + 0x28]
00B2C7AF  8B 51 24                        mov edx, dword ptr [rcx + 0x24]
00B2C7B2  8B 49 20                        mov ecx, dword ptr [rcx + 0x20]
00B2C7B5  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B2C7BA  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
00B2C7BF  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B2C7C4  E8 CB A0 F8 FF                  call 0x140ab6894
00B2C7C9  4C 8B 65 B8                     mov r12, qword ptr [rbp - 0x48]
00B2C7CD  45 33 C0                        xor r8d, r8d
00B2C7D0  8B D8                           mov ebx, eax
00B2C7D2  85 C0                           test eax, eax
00B2C7D4  0F 89 CE AF E6 FF               jns 0x1409977a8
00B2C7DA  41 8B F0                        mov esi, r8d
00B2C7DD  41 8B D8                        mov ebx, r8d
00B2C7E0  E9 E3 AD E6 FF                  jmp 0x1409975c8
00B2C7E5  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
00B2C7E9  8B 48 20                        mov ecx, dword ptr [rax + 0x20]
00B2C7EC  8B 78 24                        mov edi, dword ptr [rax + 0x24]
00B2C7EF  48 8B 70 28                     mov rsi, qword ptr [rax + 0x28]
00B2C7F3  8B C1                           mov eax, ecx
00B2C7F5  25 00 00 FF FF                  and eax, 0xffff0000
00B2C7FA  44 0F B7 F1                     movzx r14d, cx
00B2C7FE  44 0B F8                        or r15d, eax
00B2C801  E9 C2 AD E6 FF                  jmp 0x1409975c8
00B2C806  41 8B D8                        mov ebx, r8d
00B2C809  3D 34 00 00 C0                  cmp eax, 0xc0000034
00B2C80E  75 09                           jne 0x140b2c819
00B2C810  0F B7 7D 32                     movzx edi, word ptr [rbp + 0x32]
00B2C814  E9 AF AD E6 FF                  jmp 0x1409975c8
00B2C819  49 8B F0                        mov rsi, r8
00B2C81C  E9 A7 AD E6 FF                  jmp 0x1409975c8
00B2C821  85 C0                           test eax, eax
00B2C823  0F 85 90 00 00 00               jne 0x140b2c8b9
00B2C829  8B 45 D0                        mov eax, dword ptr [rbp - 0x30]
00B2C82C  83 F8 01                        cmp eax, 1
00B2C82F  75 4C                           jne 0x140b2c87d
00B2C831  41 8B C6                        mov eax, r14d
00B2C834  83 E8 01                        sub eax, 1
00B2C837  74 37                           je 0x140b2c870
00B2C839  83 E8 01                        sub eax, 1
00B2C83C  74 32                           je 0x140b2c870
00B2C83E  83 E8 01                        sub eax, 1
00B2C841  74 25                           je 0x140b2c868
00B2C843  83 E8 01                        sub eax, 1
00B2C846  74 18                           je 0x140b2c860
00B2C848  83 E8 03                        sub eax, 3
00B2C84B  74 0B                           je 0x140b2c858
00B2C84D  83 F8 04                        cmp eax, 4
00B2C850  75 16                           jne 0x140b2c868
00B2C852  44 8D 48 05                     lea r9d, [rax + 5]
00B2C856  EB 1E                           jmp 0x140b2c876
00B2C858  41 B9 12 20 00 00               mov r9d, 0x2012
00B2C85E  EB 16                           jmp 0x140b2c876
00B2C860  41 B9 07 00 00 00               mov r9d, 7
00B2C866  EB 0E                           jmp 0x140b2c876
00B2C868  41 B9 03 10 00 00               mov r9d, 0x1003
00B2C86E  EB 06                           jmp 0x140b2c876
00B2C870  41 B9 12 00 00 00               mov r9d, 0x12
00B2C876  44 89 4C 24 60                  mov dword ptr [rsp + 0x60], r9d
00B2C87B  EB 07                           jmp 0x140b2c884
00B2C87D  44 8B C8                        mov r9d, eax
00B2C880  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
00B2C884  48 8D 45 18                     lea rax, [rbp + 0x18]
00B2C888  4C 8B C6                        mov r8, rsi
00B2C88B  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B2C890  8B D7                           mov edx, edi
00B2C892  48 8D 45 A8                     lea rax, [rbp - 0x58]
00B2C896  41 8B CE                        mov ecx, r14d
00B2C899  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B2C89E  E8 8D 5C C0 FF                  call 0x140732530
00B2C8A3  48 8B 7D 18                     mov rdi, qword ptr [rbp + 0x18]
00B2C8A7  8B D8                           mov ebx, eax
00B2C8A9  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
00B2C8AD  45 33 C0                        xor r8d, r8d
00B2C8B0  8B 4D A8                        mov ecx, dword ptr [rbp - 0x58]
00B2C8B3  48 8B 55 E0                     mov rdx, qword ptr [rbp - 0x20]
00B2C8B7  EB 14                           jmp 0x140b2c8cd
00B2C8B9  41 8B C0                        mov eax, r8d
00B2C8BC  4C 89 45 18                     mov qword ptr [rbp + 0x18], r8
00B2C8C0  41 8B C8                        mov ecx, r8d
00B2C8C3  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
00B2C8C7  89 4D A8                        mov dword ptr [rbp - 0x58], ecx
00B2C8CA  49 8B F8                        mov rdi, r8
00B2C8CD  85 DB                           test ebx, ebx
00B2C8CF  0F 88 23 AE E6 FF               js 0x1409976f8
00B2C8D5  48 85 FF                        test rdi, rdi
00B2C8D8  75 08                           jne 0x140b2c8e2
00B2C8DA  85 C0                           test eax, eax
00B2C8DC  0F 85 16 AE E6 FF               jne 0x1409976f8
00B2C8E2  44 8B 4D D4                     mov r9d, dword ptr [rbp - 0x2c]
00B2C8E6  44 89 44 24 50                  mov dword ptr [rsp + 0x50], r8d
00B2C8EB  4C 8B C2                        mov r8, rdx
00B2C8EE  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
00B2C8F2  33 D2                           xor edx, edx
00B2C8F4  48 8B 0D 9D 9A 33 00            mov rcx, qword ptr [rip + 0x339a9d]
00B2C8FB  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
00B2C900  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00B2C904  48 8D 45 70                     lea rax, [rbp + 0x70]
00B2C908  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00B2C90D  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
00B2C912  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B2C917  E8 34 12 F6 FF                  call 0x140a8db50
00B2C91C  45 33 C0                        xor r8d, r8d
00B2C91F  8B D8                           mov ebx, eax
00B2C921  3D 22 00 00 C0                  cmp eax, 0xc0000022
00B2C926  74 0E                           je 0x140b2c936
00B2C928  44 39 44 24 60                  cmp dword ptr [rsp + 0x60], r8d
00B2C92D  75 0A                           jne 0x140b2c939
00B2C92F  3D 25 02 00 C0                  cmp eax, 0xc0000225
00B2C934  75 03                           jne 0x140b2c939
00B2C936  41 8B D8                        mov ebx, r8d
00B2C939  48 85 FF                        test rdi, rdi
00B2C93C  0F 84 B6 AD E6 FF               je 0x1409976f8
00B2C942  48 3B FE                        cmp rdi, rsi
00B2C945  74 0D                           je 0x140b2c954
00B2C947  33 D2                           xor edx, edx
00B2C949  48 8B CF                        mov rcx, rdi
00B2C94C  E8 1F 5F 05 00                  call 0x140b82870
00B2C951  45 33 C0                        xor r8d, r8d
00B2C954  4C 89 45 18                     mov qword ptr [rbp + 0x18], r8
00B2C958  E9 9B AD E6 FF                  jmp 0x1409976f8
00B2C95D  48 8B 4D 58                     mov rcx, qword ptr [rbp + 0x58]
00B2C961  4C 8D 44 24 74                  lea r8, [rsp + 0x74]
00B2C966  48 8D 55 30                     lea rdx, [rbp + 0x30]
00B2C96A  E8 5D DD 8F FF                  call 0x14042a6cc
00B2C96F  33 C9                           xor ecx, ecx
00B2C971  84 C0                           test al, al
00B2C973  0F 84 3B AF E6 FF               je 0x1409978b4
00B2C979  48 8B 55 38                     mov rdx, qword ptr [rbp + 0x38]
00B2C97D  4C 8D 45 B0                     lea r8, [rbp - 0x50]
00B2C981  48 89 4D B0                     mov qword ptr [rbp - 0x50], rcx
00B2C985  48 8B CB                        mov rcx, rbx
00B2C988  E8 2B 51 F5 FF                  call 0x140a81ab8
00B2C98D  33 DB                           xor ebx, ebx
00B2C98F  85 C0                           test eax, eax
00B2C991  78 52                           js 0x140b2c9e5
00B2C993  48 8B 4D B0                     mov rcx, qword ptr [rbp - 0x50]
00B2C997  8B 51 20                        mov edx, dword ptr [rcx + 0x20]
00B2C99A  8D 42 FF                        lea eax, [rdx - 1]
00B2C99D  83 F8 01                        cmp eax, 1
00B2C9A0  76 22                           jbe 0x140b2c9c4
00B2C9A2  83 FA 07                        cmp edx, 7
00B2C9A5  75 09                           jne 0x140b2c9b0
00B2C9A7  48 8B 79 28                     mov rdi, qword ptr [rcx + 0x28]
00B2C9AB  E9 04 AF E6 FF                  jmp 0x1409978b4
00B2C9B0  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
00B2C9B5  E8 F6 08 B8 FF                  call 0x1406ad2b0
00B2C9BA  48 89 5C 24 78                  mov qword ptr [rsp + 0x78], rbx
00B2C9BF  E9 CE AF E6 FF                  jmp 0x140997992
00B2C9C4  48 8B 41 28                     mov rax, qword ptr [rcx + 0x28]
00B2C9C8  48 89 45 48                     mov qword ptr [rbp + 0x48], rax
00B2C9CC  0F B7 41 24                     movzx eax, word ptr [rcx + 0x24]
00B2C9D0  66 83 E8 02                     sub ax, 2
00B2C9D4  66 89 45 40                     mov word ptr [rbp + 0x40], ax
00B2C9D8  0F B7 41 24                     movzx eax, word ptr [rcx + 0x24]
00B2C9DC  66 89 45 42                     mov word ptr [rbp + 0x42], ax
00B2C9E0  E9 CF AE E6 FF                  jmp 0x1409978b4
00B2C9E5  3D 34 00 00 C0                  cmp eax, 0xc0000034
00B2C9EA  75 C4                           jne 0x140b2c9b0
00B2C9EC  0F 28 45 30                     movaps xmm0, xmmword ptr [rbp + 0x30]
00B2C9F0  66 0F 7F 45 40                  movdqa xmmword ptr [rbp + 0x40], xmm0
00B2C9F5  E9 BA AE E6 FF                  jmp 0x1409978b4
00B2C9FA  66 39 17                        cmp word ptr [rdi], dx
00B2C9FD  0F 84 70 AF E6 FF               je 0x140997973
00B2CA03  48 8B D7                        mov rdx, rdi
00B2CA06  48 8D 4D 40                     lea rcx, [rbp + 0x40]
00B2CA0A  E8 71 DD 8F FF                  call 0x14042a780
00B2CA0F  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
00B2CA14  4C 8D 45 E8                     lea r8, [rbp - 0x18]
00B2CA18  33 C9                           xor ecx, ecx
00B2CA1A  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00B2CA1E  48 8D 45 40                     lea rax, [rbp + 0x40]
00B2CA22  48 89 4D 10                     mov qword ptr [rbp + 0x10], rcx
00B2CA26  BA 3F 00 0F 00                  mov edx, 0xf003f
00B2CA2B  48 89 45 F8                     mov qword ptr [rbp - 8], rax
00B2CA2F  48 8D 4D 80                     lea rcx, [rbp - 0x80]
00B2CA33  C7 45 E8 30 00 00 00            mov dword ptr [rbp - 0x18], 0x30
00B2CA3A  C7 45 00 40 02 00 00            mov dword ptr [rbp], 0x240
00B2CA41  4C 89 75 08                     mov qword ptr [rbp + 8], r14
00B2CA45  E8 C6 08 B8 FF                  call 0x1406ad310
00B2CA4A  33 D2                           xor edx, edx
00B2CA4C  8B D8                           mov ebx, eax
00B2CA4E  85 C0                           test eax, eax
00B2CA50  78 18                           js 0x140b2ca6a
00B2CA52  4D 85 F6                        test r14, r14
00B2CA55  74 5C                           je 0x140b2cab3
00B2CA57  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
00B2CA5B  4D 8B C6                        mov r8, r14
00B2CA5E  BA 04 00 00 00                  mov edx, 4
00B2CA63  E8 A8 3D B8 FF                  call 0x1406b0810
00B2CA68  EB 49                           jmp 0x140b2cab3
00B2CA6A  3D 34 00 00 C0                  cmp eax, 0xc0000034
00B2CA6F  0F 85 FE AE E6 FF               jne 0x140997973
00B2CA75  F7 44 24 74 00 00 01 00         test dword ptr [rsp + 0x74], 0x10000
00B2CA7D  74 07                           je 0x140b2ca86
00B2CA7F  8B DA                           mov ebx, edx
00B2CA81  E9 A1 00 00 00                  jmp 0x140b2cb27
00B2CA86  48 89 54 24 30                  mov qword ptr [rsp + 0x30], rdx
00B2CA8B  4C 8D 45 E8                     lea r8, [rbp - 0x18]
00B2CA8F  89 54 24 28                     mov dword ptr [rsp + 0x28], edx
00B2CA93  48 8D 4D 80                     lea rcx, [rbp - 0x80]
00B2CA97  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00B2CA9C  45 33 C9                        xor r9d, r9d
00B2CA9F  BA 3F 00 0F 00                  mov edx, 0xf003f
00B2CAA4  E8 C7 09 B8 FF                  call 0x1406ad470
00B2CAA9  8B D8                           mov ebx, eax
00B2CAAB  85 C0                           test eax, eax
00B2CAAD  0F 88 C0 AE E6 FF               js 0x140997973
00B2CAB3  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
00B2CAB8  48 85 D2                        test rdx, rdx
00B2CABB  75 40                           jne 0x140b2cafd
00B2CABD  48 8D 45 50                     lea rax, [rbp + 0x50]
00B2CAC1  C7 45 E8 30 00 00 00            mov dword ptr [rbp - 0x18], 0x30
00B2CAC8  0F 57 C0                        xorps xmm0, xmm0
00B2CACB  48 89 45 F8                     mov qword ptr [rbp - 8], rax
00B2CACF  4C 8D 45 E8                     lea r8, [rbp - 0x18]
00B2CAD3  4C 89 65 F0                     mov qword ptr [rbp - 0x10], r12
00B2CAD7  BA 19 00 02 00                  mov edx, 0x20019
00B2CADC  C7 45 00 40 02 00 00            mov dword ptr [rbp], 0x240
00B2CAE3  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
00B2CAE8  F3 0F 7F 45 08                  movdqu xmmword ptr [rbp + 8], xmm0
00B2CAED  E8 1E 08 B8 FF                  call 0x1406ad310
00B2CAF2  8B D8                           mov ebx, eax
00B2CAF4  85 C0                           test eax, eax
00B2CAF6  78 49                           js 0x140b2cb41
00B2CAF8  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
00B2CAFD  44 8B 8D 00 01 00 00            mov r9d, dword ptr [rbp + 0x100]
00B2CB04  4C 8B 45 80                     mov r8, qword ptr [rbp - 0x80]
00B2CB08  41 0F BA E9 1E                  bts r9d, 0x1e
00B2CB0D  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
00B2CB11  E8 8E 30 98 FF                  call 0x1404afba4
00B2CB16  33 D2                           xor edx, edx
00B2CB18  8B D8                           mov ebx, eax
00B2CB1A  85 C0                           test eax, eax
00B2CB1C  78 23                           js 0x140b2cb41
00B2CB1E  48 89 54 24 78                  mov qword ptr [rsp + 0x78], rdx
00B2CB23  48 89 55 80                     mov qword ptr [rbp - 0x80], rdx
00B2CB27  48 83 C8 FF                     or rax, 0xffffffffffffffff
00B2CB2B  48 FF C0                        inc rax
00B2CB2E  66 39 14 47                     cmp word ptr [rdi + rax*2], dx
00B2CB32  75 F7                           jne 0x140b2cb2b
00B2CB34  48 8D 3C 47                     lea rdi, [rdi + rax*2]
00B2CB38  48 83 C7 02                     add rdi, 2
00B2CB3C  E9 B9 FE FF FF                  jmp 0x140b2c9fa
00B2CB41  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
00B2CB45  E8 66 07 B8 FF                  call 0x1406ad2b0
00B2CB4A  33 D2                           xor edx, edx
00B2CB4C  E9 1E AE E6 FF                  jmp 0x14099796f
00B2CB51  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00B2CB56  E9 10 AB E6 FF                  jmp 0x14099766b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B2C5F4(void)
{
    __int64 result;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned int v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned int v_stack_p50;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p74;
    unsigned __int64 v_stack_p78;

    result = PiDevCfgParseVariableName(v_rsi, v_rbp + 48, v_stack_p74, a4);
    a2 = 0;
    *(unsigned __int64 *)(v_rbp - 80) = 0;
    result = PiDevCfgResolveVariable(v_rbx, *(unsigned __int64 *)(v_rbp + 56), v_rbp - 80, a4);
    a2 = 0;
    if (sign_flag) goto loc_00B2C677;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rbp - 80) + 32))) - 1);
    *(unsigned __int64 *)(v_rbp - 56) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 80) + 40);
    result = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rbp - 80) + 36)) - (2));
    *(unsigned __int16 *)(v_rbp - 64) = (unsigned __int16)(result);
    *(unsigned __int16 *)(v_rbp - 62) = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rbp - 80) + 36));
loc_00B2C677:
    *(unsigned __int64 *)(v_rbp - 64) = v_xmm0;
}
```

## 5. (Beta) C Style

```c
void sub_00B2C5F4(void)
{
    int64_t result;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint32_t v_stack_p40;
    uint64_t v_stack_p48;
    uint32_t v_stack_p50;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p74;
    uint64_t v_stack_p78;

    result = PiDevCfgParseVariableName(local_rsi, local_rbp + 48, v_stack_p74, a4);
    a2 = 0;
    *(uint64_t *)(local_rbp - 0x50) = 0;
    result = PiDevCfgResolveVariable(local_rbx, *(uint64_t *)(local_rbp + 0x38), local_rbp - 80, a4);
    a2 = 0;
    if (sign_flag) goto loc_00B2C677;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rbp - 0x50) + 0x20))) - 1);
    *(uint64_t *)(local_rbp - 0x38) = *(uint64_t *)(*(uint64_t *)(local_rbp - 0x50) + 0x28);
    result = (uint16_t)((*(uint16_t *)(*(uint64_t *)(local_rbp - 0x50) + 0x24)) - (2));
    *(uint16_t *)(local_rbp - 0x40) = (uint16_t)(result);
    *(uint16_t *)(local_rbp - 0x3E) = (uint16_t)(*(uint16_t *)(*(uint64_t *)(local_rbp - 0x50) + 0x24));
loc_00B2C677:
    *(uint64_t *)(local_rbp - 0x40) = v_xmm0;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B2C5F4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
