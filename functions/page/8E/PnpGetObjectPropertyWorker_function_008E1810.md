# PnpGetObjectPropertyWorker

- RVA: `0x008E1810`–`0x008E1D59` (길이 `1,353` bytes)
- VA: `0x00000001408E1810`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00085E50`
- 디코드: `330`개 명령, `1,353/1,353` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **16**; 고유 호출 대상: **13**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x008E191B` → [_PnpDispatchDevice](_PnpDispatchDevice_function_008E1D60.md) (function, `0x008E1D60`)
- `0x008E1932` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x008E1943` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x008E1979` → [_PnpDispatchDeviceInterface](_PnpDispatchDeviceInterface_function_008E0DB0.md) (function, `0x008E0DB0`)
- `0x008E1A4C` → [RtlStringCchPrintfExW](../../text/42/RtlStringCchPrintfExW_function_0042B390.md) (function, `0x0042B390`)
- `0x008E1AD4` → [RtlStringCchPrintfExW](../../text/42/RtlStringCchPrintfExW_function_0042B390.md) (function, `0x0042B390`)
- `0x008E1B1C` → [_RegRtlOpenKeyTransacted](_RegRtlOpenKeyTransacted_function_008EF810.md) (function, `0x008EF810`)
- `0x008E1B5D` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x008E1B72` → [PnpValidatePropertyData](../8F/PnpValidatePropertyData_function_008F7658.md) (function, `0x008F7658`)
- `0x008E1BA2` → [DrvDbDispatchDriverPackage](../93/DrvDbDispatchDriverPackage_function_009303A0.md) (function, `0x009303A0`)
- `0x008E1C17` → [PnpRegQueryValueIndirect](PnpRegQueryValueIndirect_function_008EE210.md) (function, `0x008EE210`)
- `0x008E1C76` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008E1CB6` → [PnpOpenObjectRegKey](PnpOpenObjectRegKey_function_008E15E8.md) (function, `0x008E15E8`)
- `0x008E1D08` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008E1D2F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008E1D4F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [PiDqPnPGetObjectPropertyInBestLocale](../8D/PiDqPnPGetObjectPropertyInBestLocale_function_008DEE10.md) at `0x008DF174`
- [PiDqPnPGetObjectProperty](../8D/PiDqPnPGetObjectProperty_function_008DFD90.md) at `0x008E0083`
- [PiPnpRtlInterfaceFilterCallback](PiPnpRtlInterfaceFilterCallback_function_008E4FC0.md) at `0x008E520A`
- [PiPnpRtlApplyMandatoryDeviceInterfaceFilters](PiPnpRtlApplyMandatoryDeviceInterfaceFilters_function_008E59D0.md) at `0x008E5BD6`
- [PiPnpRtlApplyMandatoryDeviceFilters](PiPnpRtlApplyMandatoryDeviceFilters_function_008E5E90.md) at `0x008E625C`
- [PiPnpRtlApplyMandatoryDeviceFilters](PiPnpRtlApplyMandatoryDeviceFilters_function_008E5E90.md) at `0x008E6322`
- [PiCMHandleIoctl](PiCMHandleIoctl_function_008EB880.md) at `0x008EBCF6`

### Static image references
- `0x008E182C` → RVA `0x00E0A740` (`.data`; read)
- `0x008E18DC` → RVA `0x008E1D60` (`_PnpDispatchDevice`; read)
- `0x008E195D` → RVA `0x008E0DB0` (`_PnpDispatchDeviceInterface`; read)
- `0x008E1A38` → RVA `0x00B0D8D0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x008E1AAE` → RVA `0x00AFCD40` (` ?? ::NNGAKEGL::`string'`; read)
- `0x008E1AC0` → RVA `0x00AFD430` (` ?? ::NNGAKEGL::`string'`; read)
- `0x008E1B86` → RVA `0x009303A0` (`DrvDbDispatchDriverPackage`; read)
- `0x008E1CD2` → RVA `0x008EE210` (`PnpRegQueryValueIndirect`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **9**
  - `0x008E1932` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x008E1943` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x008E1A4C` → [RtlStringCchPrintfExW](../../text/42/RtlStringCchPrintfExW_function_0042B390.md) (`PAGE` → `.text`)
  - `0x008E1AD4` → [RtlStringCchPrintfExW](../../text/42/RtlStringCchPrintfExW_function_0042B390.md) (`PAGE` → `.text`)
  - `0x008E1B5D` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x008E1C76` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008E1D08` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008E1D2F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008E1D4F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008E1810  40 55                           push rbp
008E1812  53                              push rbx
008E1813  56                              push rsi
008E1814  57                              push rdi
008E1815  41 54                           push r12
008E1817  41 55                           push r13
008E1819  41 56                           push r14
008E181B  41 57                           push r15
008E181D  48 8D AC 24 38 FF FF FF         lea rbp, [rsp - 0xc8]
008E1825  48 81 EC D8 01 00 00            sub rsp, 0x1d8
008E182C  48 8B 05 0D 8F 52 00            mov rax, qword ptr [rip + 0x528f0d]
008E1833  48 33 C4                        xor rax, rsp
008E1836  48 89 85 B0 00 00 00            mov qword ptr [rbp + 0xb0], rax
008E183D  4C 8B 9D 30 01 00 00            mov r11, qword ptr [rbp + 0x130]
008E1844  45 33 FF                        xor r15d, r15d
008E1847  4C 8B AD 38 01 00 00            mov r13, qword ptr [rbp + 0x138]
008E184E  4D 8B D1                        mov r10, r9
008E1851  4C 8B A5 48 01 00 00            mov r12, qword ptr [rbp + 0x148]
008E1858  4C 8B F1                        mov r14, rcx
008E185B  4C 89 4D B0                     mov qword ptr [rbp - 0x50], r9
008E185F  48 8B F2                        mov rsi, rdx
008E1862  4C 8B 8D 40 01 00 00            mov r9, qword ptr [rbp + 0x140]
008E1869  49 63 F8                        movsxd rdi, r8d
008E186C  4C 8B 85 58 01 00 00            mov r8, qword ptr [rbp + 0x158]
008E1873  48 89 4D C8                     mov qword ptr [rbp - 0x38], rcx
008E1877  8B 8D 60 01 00 00               mov ecx, dword ptr [rbp + 0x160]
008E187D  4C 89 4D 98                     mov qword ptr [rbp - 0x68], r9
008E1881  4C 89 45 88                     mov qword ptr [rbp - 0x78], r8
008E1885  4C 89 5D B8                     mov qword ptr [rbp - 0x48], r11
008E1889  4C 89 7D C0                     mov qword ptr [rbp - 0x40], r15
008E188D  66 85 C9                        test cx, cx
008E1890  0F 85 F9 03 00 00               jne 0x1408e1c8f
008E1896  4D 85 E4                        test r12, r12
008E1899  0F 84 DF 02 00 00               je 0x1408e1b7e
008E189F  8B 95 50 01 00 00               mov edx, dword ptr [rbp + 0x150]
008E18A5  85 D2                           test edx, edx
008E18A7  4D 0F 44 E7                     cmove r12, r15
008E18AB  8D 47 FF                        lea eax, [rdi - 1]
008E18AE  45 89 39                        mov dword ptr [r9], r15d
008E18B1  89 55 A4                        mov dword ptr [rbp - 0x5c], edx
008E18B4  45 89 38                        mov dword ptr [r8], r15d
008E18B7  44 89 7D FC                     mov dword ptr [rbp - 4], r15d
008E18BB  44 89 7D 0C                     mov dword ptr [rbp + 0xc], r15d
008E18BF  83 F8 0A                        cmp eax, 0xa
008E18C2  0F 87 FD 02 00 00               ja 0x1408e1bc5
008E18C8  49 8B 84 FE 28 01 00 00         mov rax, qword ptr [r14 + rdi*8 + 0x128]
008E18D0  48 85 C0                        test rax, rax
008E18D3  0F 84 39 04 00 00               je 0x1408e1d12
008E18D9  89 4D 08                        mov dword ptr [rbp + 8], ecx
008E18DC  48 8D 0D 7D 04 00 00            lea rcx, [rip + 0x47d]
008E18E3  4C 89 4D E8                     mov qword ptr [rbp - 0x18], r9
008E18E7  41 B9 08 00 00 00               mov r9d, 8
008E18ED  89 55 F8                        mov dword ptr [rbp - 8], edx
008E18F0  48 8B D6                        mov rdx, rsi
008E18F3  4C 89 45 00                     mov qword ptr [rbp], r8
008E18F7  44 8B C7                        mov r8d, edi
008E18FA  4C 89 55 D0                     mov qword ptr [rbp - 0x30], r10
008E18FE  4C 89 5D D8                     mov qword ptr [rbp - 0x28], r11
008E1902  4C 89 6D E0                     mov qword ptr [rbp - 0x20], r13
008E1906  4C 89 65 F0                     mov qword ptr [rbp - 0x10], r12
008E190A  48 3B C1                        cmp rax, rcx
008E190D  75 4E                           jne 0x1408e195d
008E190F  48 8D 45 D0                     lea rax, [rbp - 0x30]
008E1913  49 8B CE                        mov rcx, r14
008E1916  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008E191B  E8 40 04 00 00                  call 0x1408e1d60
008E1920  8B D8                           mov ebx, eax
008E1922  3D 16 00 00 C0                  cmp eax, 0xc0000016
008E1927  74 57                           je 0x1408e1980
008E1929  48 8B 4D C0                     mov rcx, qword ptr [rbp - 0x40]
008E192D  48 85 C9                        test rcx, rcx
008E1930  74 05                           je 0x1408e1937
008E1932  E8 79 B9 DC FF                  call 0x1406ad2b0
008E1937  8B C3                           mov eax, ebx
008E1939  48 8B 8D B0 00 00 00            mov rcx, qword ptr [rbp + 0xb0]
008E1940  48 33 CC                        xor rcx, rsp
008E1943  E8 F8 AC DC FF                  call 0x1406ac640
008E1948  48 81 C4 D8 01 00 00            add rsp, 0x1d8
008E194F  41 5F                           pop r15
008E1951  41 5E                           pop r14
008E1953  41 5D                           pop r13
008E1955  41 5C                           pop r12
008E1957  5F                              pop rdi
008E1958  5E                              pop rsi
008E1959  5B                              pop rbx
008E195A  5D                              pop rbp
008E195B  C3                              ret
008E195C  CC                              int3
008E195D  48 8D 0D 4C F4 FF FF            lea rcx, [rip - 0xbb4]
008E1964  48 3B C1                        cmp rax, rcx
008E1967  0F 85 19 02 00 00               jne 0x1408e1b86
008E196D  48 8D 45 D0                     lea rax, [rbp - 0x30]
008E1971  49 8B CE                        mov rcx, r14
008E1974  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008E1979  E8 32 F4 FF FF                  call 0x1408e0db0
008E197E  EB A0                           jmp 0x1408e1920
008E1980  4C 39 7D B0                     cmp qword ptr [rbp - 0x50], r15
008E1984  0F 84 0F 03 00 00               je 0x1408e1c99
008E198A  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
008E198E  4C 89 7D A8                     mov qword ptr [rbp - 0x58], r15
008E1992  44 89 7D A0                     mov dword ptr [rbp - 0x60], r15d
008E1996  44 89 7D 90                     mov dword ptr [rbp - 0x70], r15d
008E199A  44 89 38                        mov dword ptr [rax], r15d
008E199D  48 8B 45 88                     mov rax, qword ptr [rbp - 0x78]
008E19A1  44 88 7D 80                     mov byte ptr [rbp - 0x80], r15b
008E19A5  44 89 38                        mov dword ptr [rax], r15d
008E19A8  48 8B 45 B8                     mov rax, qword ptr [rbp - 0x48]
008E19AC  48 85 C0                        test rax, rax
008E19AF  0F 85 F7 01 00 00               jne 0x1408e1bac
008E19B5  41 8B 45 10                     mov eax, dword ptr [r13 + 0x10]
008E19B9  41 0F B6 4D 0F                  movzx ecx, byte ptr [r13 + 0xf]
008E19BE  41 0F B6 55 0E                  movzx edx, byte ptr [r13 + 0xe]
008E19C3  45 0F B6 45 0D                  movzx r8d, byte ptr [r13 + 0xd]
008E19C8  45 0F B6 4D 0C                  movzx r9d, byte ptr [r13 + 0xc]
008E19CD  45 0F B6 55 0B                  movzx r10d, byte ptr [r13 + 0xb]
008E19D2  45 0F B6 5D 0A                  movzx r11d, byte ptr [r13 + 0xa]
008E19D7  41 0F B6 5D 09                  movzx ebx, byte ptr [r13 + 9]
008E19DC  41 0F B6 7D 08                  movzx edi, byte ptr [r13 + 8]
008E19E1  41 0F B7 75 06                  movzx esi, word ptr [r13 + 6]
008E19E6  45 0F B7 75 04                  movzx r14d, word ptr [r13 + 4]
008E19EB  89 84 24 88 00 00 00            mov dword ptr [rsp + 0x88], eax
008E19F2  41 8B 45 00                     mov eax, dword ptr [r13]
008E19F6  89 8C 24 80 00 00 00            mov dword ptr [rsp + 0x80], ecx
008E19FD  48 8D 4D D0                     lea rcx, [rbp - 0x30]
008E1A01  89 54 24 78                     mov dword ptr [rsp + 0x78], edx
008E1A05  44 89 44 24 70                  mov dword ptr [rsp + 0x70], r8d
008E1A0A  45 33 C0                        xor r8d, r8d
008E1A0D  44 89 4C 24 68                  mov dword ptr [rsp + 0x68], r9d
008E1A12  45 33 C9                        xor r9d, r9d
008E1A15  44 89 54 24 60                  mov dword ptr [rsp + 0x60], r10d
008E1A1A  44 89 5C 24 58                  mov dword ptr [rsp + 0x58], r11d
008E1A1F  89 5C 24 50                     mov dword ptr [rsp + 0x50], ebx
008E1A23  89 7C 24 48                     mov dword ptr [rsp + 0x48], edi
008E1A27  41 8D 51 30                     lea edx, [r9 + 0x30]
008E1A2B  89 74 24 40                     mov dword ptr [rsp + 0x40], esi
008E1A2F  44 89 74 24 38                  mov dword ptr [rsp + 0x38], r14d
008E1A34  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
008E1A38  48 8D 05 91 BE 22 00            lea rax, [rip + 0x22be91]
008E1A3F  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008E1A44  C7 44 24 20 00 08 00 00         mov dword ptr [rsp + 0x20], 0x800
008E1A4C  E8 3F 99 B4 FF                  call 0x14042b390
008E1A51  8B D8                           mov ebx, eax
008E1A53  85 C0                           test eax, eax
008E1A55  0F 88 F1 00 00 00               js 0x1408e1b4c
008E1A5B  BF 00 02 00 00                  mov edi, 0x200
008E1A60  4C 89 7D A8                     mov qword ptr [rbp - 0x58], r15
008E1A64  8B CF                           mov ecx, edi
008E1A66  48 8D 45 D0                     lea rax, [rbp - 0x30]
008E1A6A  66 0F 1F 44 00 00               nop word ptr [rax + rax]
008E1A70  66 44 39 38                     cmp word ptr [rax], r15w
008E1A74  74 14                           je 0x1408e1a8a
008E1A76  48 83 C0 02                     add rax, 2
008E1A7A  48 83 E9 01                     sub rcx, 1
008E1A7E  75 F0                           jne 0x1408e1a70
008E1A80  BB 0D 00 00 C0                  mov ebx, 0xc000000d
008E1A85  E9 C2 00 00 00                  jmp 0x1408e1b4c
008E1A8A  48 2B F9                        sub rdi, rcx
008E1A8D  48 83 FF 30                     cmp rdi, 0x30
008E1A91  0F 83 85 02 00 00               jae 0x1408e1d1c
008E1A97  48 8D 5D 30                     lea rbx, [rbp + 0x30]
008E1A9B  BF 3B 00 00 00                  mov edi, 0x3b
008E1AA0  48 8D 45 D0                     lea rax, [rbp - 0x30]
008E1AA4  8B D7                           mov edx, edi
008E1AA6  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
008E1AAB  45 33 C9                        xor r9d, r9d
008E1AAE  48 8D 05 8B B2 21 00            lea rax, [rip + 0x21b28b]
008E1AB5  45 33 C0                        xor r8d, r8d
008E1AB8  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008E1ABD  48 8B CB                        mov rcx, rbx
008E1AC0  48 8D 05 69 B9 21 00            lea rax, [rip + 0x21b969]
008E1AC7  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008E1ACC  C7 44 24 20 00 08 00 00         mov dword ptr [rsp + 0x20], 0x800
008E1AD4  E8 B7 98 B4 FF                  call 0x14042b390
008E1AD9  48 8B 75 C8                     mov rsi, qword ptr [rbp - 0x38]
008E1ADD  8B F8                           mov edi, eax
008E1ADF  41 BD 34 00 00 C0               mov r13d, 0xc0000034
008E1AE5  85 C0                           test eax, eax
008E1AE7  78 43                           js 0x1408e1b2c
008E1AE9  48 85 F6                        test rsi, rsi
008E1AEC  74 10                           je 0x1408e1afe
008E1AEE  48 8B 86 E0 00 00 00            mov rax, qword ptr [rsi + 0xe0]
008E1AF5  48 85 C0                        test rax, rax
008E1AF8  74 04                           je 0x1408e1afe
008E1AFA  4C 8B 78 08                     mov r15, qword ptr [rax + 8]
008E1AFE  48 8B 4D B0                     mov rcx, qword ptr [rbp - 0x50]
008E1B02  48 8D 45 A8                     lea rax, [rbp - 0x58]
008E1B06  4C 89 7C 24 28                  mov qword ptr [rsp + 0x28], r15
008E1B0B  41 B9 01 00 00 00               mov r9d, 1
008E1B11  45 33 C0                        xor r8d, r8d
008E1B14  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008E1B19  48 8B D3                        mov rdx, rbx
008E1B1C  E8 EF DC 00 00                  call 0x1408ef810
008E1B21  3D 7C 01 00 C0                  cmp eax, 0xc000017c
008E1B26  8B F8                           mov edi, eax
008E1B28  41 0F 44 FD                     cmove edi, r13d
008E1B2C  48 85 DB                        test rbx, rbx
008E1B2F  74 0D                           je 0x1408e1b3e
008E1B31  48 8D 45 30                     lea rax, [rbp + 0x30]
008E1B35  48 3B D8                        cmp rbx, rax
008E1B38  0F 85 0C 02 00 00               jne 0x1408e1d4a
008E1B3E  41 3B FD                        cmp edi, r13d
008E1B41  0F 85 88 00 00 00               jne 0x1408e1bcf
008E1B47  BB 25 02 00 C0                  mov ebx, 0xc0000225
008E1B4C  4C 8B 7D 98                     mov r15, qword ptr [rbp - 0x68]
008E1B50  48 8B 75 88                     mov rsi, qword ptr [rbp - 0x78]
008E1B54  48 8B 4D A8                     mov rcx, qword ptr [rbp - 0x58]
008E1B58  48 85 C9                        test rcx, rcx
008E1B5B  74 05                           je 0x1408e1b62
008E1B5D  E8 4E B7 DC FF                  call 0x1406ad2b0
008E1B62  85 DB                           test ebx, ebx
008E1B64  0F 88 BF FD FF FF               js 0x1408e1929
008E1B6A  45 8B 07                        mov r8d, dword ptr [r15]
008E1B6D  49 8B CC                        mov rcx, r12
008E1B70  8B 16                           mov edx, dword ptr [rsi]
008E1B72  E8 E1 5A 01 00                  call 0x1408f7658
008E1B77  8B D8                           mov ebx, eax
008E1B79  E9 AB FD FF FF                  jmp 0x1408e1929
008E1B7E  41 8B D7                        mov edx, r15d
008E1B81  E9 25 FD FF FF                  jmp 0x1408e18ab
008E1B86  48 8D 0D 13 E8 04 00            lea rcx, [rip + 0x4e813]
008E1B8D  48 3B C1                        cmp rax, rcx
008E1B90  0F 85 D4 00 00 00               jne 0x1408e1c6a
008E1B96  48 8D 45 D0                     lea rax, [rbp - 0x30]
008E1B9A  49 8B CE                        mov rcx, r14
008E1B9D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008E1BA2  E8 F9 E7 04 00                  call 0x1409303a0
008E1BA7  E9 74 FD FF FF                  jmp 0x1408e1920
008E1BAC  B9 55 00 00 00                  mov ecx, 0x55
008E1BB1  66 44 39 38                     cmp word ptr [rax], r15w
008E1BB5  0F 84 FA FD FF FF               je 0x1408e19b5
008E1BBB  48 83 C0 02                     add rax, 2
008E1BBF  48 83 E9 01                     sub rcx, 1
008E1BC3  75 EC                           jne 0x1408e1bb1
008E1BC5  BB 0D 00 00 C0                  mov ebx, 0xc000000d
008E1BCA  E9 5A FD FF FF                  jmp 0x1408e1929
008E1BCF  8B DF                           mov ebx, edi
008E1BD1  85 FF                           test edi, edi
008E1BD3  0F 88 73 FF FF FF               js 0x1408e1b4c
008E1BD9  48 8B 86 08 02 00 00            mov rax, qword ptr [rsi + 0x208]
008E1BE0  44 8B 75 A4                     mov r14d, dword ptr [rbp - 0x5c]
008E1BE4  44 89 75 90                     mov dword ptr [rbp - 0x70], r14d
008E1BE8  48 85 C0                        test rax, rax
008E1BEB  0F 85 E1 00 00 00               jne 0x1408e1cd2
008E1BF1  4C 8B 45 B8                     mov r8, qword ptr [rbp - 0x48]
008E1BF5  48 8D 45 80                     lea rax, [rbp - 0x80]
008E1BF9  48 8B 55 A8                     mov rdx, qword ptr [rbp - 0x58]
008E1BFD  4C 8D 4D A0                     lea r9, [rbp - 0x60]
008E1C01  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008E1C06  48 8B CE                        mov rcx, rsi
008E1C09  48 8D 45 90                     lea rax, [rbp - 0x70]
008E1C0D  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008E1C12  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
008E1C17  E8 F4 C5 00 00                  call 0x1408ee210
008E1C1C  8B C8                           mov ecx, eax
008E1C1E  41 3B C5                        cmp eax, r13d
008E1C21  0F 84 20 FF FF FF               je 0x1408e1b47
008E1C27  3D 7C 01 00 C0                  cmp eax, 0xc000017c
008E1C2C  0F 84 15 FF FF FF               je 0x1408e1b47
008E1C32  85 C0                           test eax, eax
008E1C34  75 4A                           jne 0x1408e1c80
008E1C36  0F B7 45 A0                     movzx eax, word ptr [rbp - 0x60]
008E1C3A  4C 8B 7D 98                     mov r15, qword ptr [rbp - 0x68]
008E1C3E  41 89 07                        mov dword ptr [r15], eax
008E1C41  83 F8 01                        cmp eax, 1
008E1C44  0F 84 06 FF FF FF               je 0x1408e1b50
008E1C4A  48 8B 75 88                     mov rsi, qword ptr [rbp - 0x78]
008E1C4E  8B 45 90                        mov eax, dword ptr [rbp - 0x70]
008E1C51  89 06                           mov dword ptr [rsi], eax
008E1C53  85 C9                           test ecx, ecx
008E1C55  75 09                           jne 0x1408e1c60
008E1C57  45 85 F6                        test r14d, r14d
008E1C5A  0F 85 F4 FE FF FF               jne 0x1408e1b54
008E1C60  BB 23 00 00 C0                  mov ebx, 0xc0000023
008E1C65  E9 EA FE FF FF                  jmp 0x1408e1b54
008E1C6A  48 8D 4D D0                     lea rcx, [rbp - 0x30]
008E1C6E  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
008E1C73  49 8B CE                        mov rcx, r14
008E1C76  E8 55 8E DD FF                  call 0x1406baad0
008E1C7B  E9 A0 FC FF FF                  jmp 0x1408e1920
008E1C80  81 F9 23 00 00 C0               cmp ecx, 0xc0000023
008E1C86  74 AE                           je 0x1408e1c36
008E1C88  8B D9                           mov ebx, ecx
008E1C8A  E9 BD FE FF FF                  jmp 0x1408e1b4c
008E1C8F  B8 0D 00 00 C0                  mov eax, 0xc000000d
008E1C94  E9 A0 FC FF FF                  jmp 0x1408e1939
008E1C99  48 8D 45 C0                     lea rax, [rbp - 0x40]
008E1C9D  41 B9 01 00 00 02               mov r9d, 0x2000001
008E1CA3  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008E1CA8  44 8B C7                        mov r8d, edi
008E1CAB  48 8B D6                        mov rdx, rsi
008E1CAE  44 88 7C 24 20                  mov byte ptr [rsp + 0x20], r15b
008E1CB3  49 8B CE                        mov rcx, r14
008E1CB6  E8 2D F9 FF FF                  call 0x1408e15e8
008E1CBB  8B D8                           mov ebx, eax
008E1CBD  85 C0                           test eax, eax
008E1CBF  0F 88 64 FC FF FF               js 0x1408e1929
008E1CC5  48 8B 45 C0                     mov rax, qword ptr [rbp - 0x40]
008E1CC9  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
008E1CCD  E9 B8 FC FF FF                  jmp 0x1408e198a
008E1CD2  48 8D 0D 37 C5 00 00            lea rcx, [rip + 0xc537]
008E1CD9  48 3B C1                        cmp rax, rcx
008E1CDC  0F 84 0F FF FF FF               je 0x1408e1bf1
008E1CE2  4C 8B 45 B8                     mov r8, qword ptr [rbp - 0x48]
008E1CE6  48 8D 4D 80                     lea rcx, [rbp - 0x80]
008E1CEA  48 8B 55 A8                     mov rdx, qword ptr [rbp - 0x58]
008E1CEE  4C 8D 4D A0                     lea r9, [rbp - 0x60]
008E1CF2  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
008E1CF7  48 8D 4D 90                     lea rcx, [rbp - 0x70]
008E1CFB  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
008E1D00  48 8B CE                        mov rcx, rsi
008E1D03  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
008E1D08  E8 C3 8D DD FF                  call 0x1406baad0
008E1D0D  E9 0A FF FF FF                  jmp 0x1408e1c1c
008E1D12  BB 02 00 00 C0                  mov ebx, 0xc0000002
008E1D17  E9 0D FC FF FF                  jmp 0x1408e1929
008E1D1C  83 C7 0C                        add edi, 0xc
008E1D1F  B9 00 01 00 00                  mov ecx, 0x100
008E1D24  8B D7                           mov edx, edi
008E1D26  41 B8 50 4E 50 52               mov r8d, 0x52504e50
008E1D2C  48 03 D2                        add rdx, rdx
008E1D2F  E8 BC 03 2A 00                  call 0x140b820f0
008E1D34  48 8B D8                        mov rbx, rax
008E1D37  48 85 C0                        test rax, rax
008E1D3A  0F 85 60 FD FF FF               jne 0x1408e1aa0
008E1D40  BB 17 00 00 C0                  mov ebx, 0xc0000017
008E1D45  E9 02 FE FF FF                  jmp 0x1408e1b4c
008E1D4A  33 D2                           xor edx, edx
008E1D4C  48 8B CB                        mov rcx, rbx
008E1D4F  E8 1C 0B 2A 00                  call 0x140b82870
008E1D54  E9 E5 FD FF FF                  jmp 0x1408e1b3e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PnpGetObjectPropertyWorker(__int64 a1, __int64 a2, int a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, unsigned int a9, __int64 a10, unsigned int a11)
{
    __int64 result;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned int v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned int v_stack_m10C;
    unsigned int v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned int v_stack_m164;
    unsigned int v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned int v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int8 v_stack_m188;
    unsigned __int64 v_stack_m1F8;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_mD8;
    unsigned int v_stack_mFC;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p30;
    unsigned int v_stack_p38;
    unsigned int v_stack_p40;
    unsigned int v_stack_p48;
    unsigned int v_stack_p50;
    unsigned int v_stack_p58;
    unsigned int v_stack_p60;
    unsigned int v_stack_p68;
    unsigned int v_stack_p70;
    unsigned int v_stack_p78;
    unsigned int v_stack_p80;
    unsigned int v_stack_p88;

    v_rsp = (v_rsp) - (472);
    result = (*(unsigned __int64 *)(v_rip + 5410573)) ^ (v_rsp);
    v_stack_m58 = result;
    v_r15 = 0;
    v_stack_m158 = a4;
    v_stack_m140 = a1;
    v_stack_m170 = a7;
    v_stack_m180 = a10;
    v_stack_m150 = a5;
    v_stack_m148 = 0;
    if ((unsigned __int16)((unsigned int)(a11)) != 0) goto loc_008E1C8F;
    if (a8 == 0) goto loc_008E1B7E;
    if ((unsigned int)((unsigned int)(a9)) == 0) { a8 = 0; }
loc_008E18AB:
    *(unsigned int *)(a7) = 0;
    v_stack_m164 = (unsigned int)((unsigned int)(a9));
    *(unsigned int *)(a10) = 0;
    v_stack_m10C = 0;
    v_stack_mFC = 0;
    if (((unsigned int)((int)(a3) - 1)) > 10) goto loc_008E1BC5;
    if (*(unsigned __int64 *)(a1 + (int)(a3) * 8 + 296) == 0) goto loc_008E1D12;
    v_stack_m100 = (unsigned int)((unsigned int)(a11));
    v_stack_m120 = a7;
    v_stack_m110 = (unsigned int)((unsigned int)(a9));
    v_stack_m108 = a10;
    v_stack_m138 = a4;
    v_stack_m130 = a5;
    v_stack_m128 = a6;
    v_stack_m118 = a8;
    if ((*(unsigned __int64 *)(a1 + (int)(a3) * 8 + 296)) != (v_rip + 1149)) goto loc_008E195D;
    v_stack_m1F8 = v_stack_m138;
    result = _PnpDispatchDevice(a1, a2, (unsigned int)((unsigned int)((int)(a3))), 8);
loc_008E1920:
    if (((unsigned int)(result)) == 0xC0000016ULL) goto loc_008E1980;
loc_008E1929:
    if (v_stack_m148 != 0) {
        result = ZwClose(v_stack_m148, a2, (unsigned int)((unsigned int)((int)(a3))), 8);
    }
loc_008E1939:
    a1 = (v_stack_m58) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, (unsigned int)((unsigned int)((int)(a3))), 8);
    v_rsp = (v_rsp) + (472);
    return result;
loc_008E195D:
    if (result != (v_rip - 2996)) goto loc_008E1B86;
    v_stack_p20 = v_stack_m138;
    result = _PnpDispatchDeviceInterface(a1, a2, (unsigned int)((unsigned int)((int)(a3))), 8);
    goto loc_008E1920;
loc_008E1980:
    if (v_stack_m158 == 0) goto loc_008E1C99;
loc_008E198A:
    v_stack_m160 = 0;
    v_stack_m168 = 0;
    v_stack_m178 = 0;
    *(unsigned int *)(v_stack_m170) = 0;
    v_stack_m188 = 0;
    *(unsigned int *)(v_stack_m180) = 0;
    if (v_stack_m150 != 0) goto loc_008E1BAC;
loc_008E19B5:
    v_stack_p88 = (unsigned int)((unsigned int)(*(unsigned int *)(a6 + 16)));
    v_stack_p80 = (unsigned int)(*(unsigned __int8 *)(a6 + 15));
    v_stack_p78 = (unsigned int)(*(unsigned __int8 *)(a6 + 14));
    v_stack_p70 = (unsigned int)(*(unsigned __int8 *)(a6 + 13));
    a3 = 0;
    v_stack_p68 = (unsigned int)(*(unsigned __int8 *)(a6 + 12));
    a4 = 0;
    v_stack_p60 = (unsigned int)(*(unsigned __int8 *)(a6 + 11));
    v_stack_p58 = (unsigned int)(*(unsigned __int8 *)(a6 + 10));
    v_stack_p50 = (unsigned int)(*(unsigned __int8 *)(a6 + 9));
    v_stack_p48 = (unsigned int)(*(unsigned __int8 *)(a6 + 8));
    v_stack_p40 = (unsigned int)(*(unsigned __int16 *)(a6 + 6));
    v_stack_p38 = (unsigned int)(*(unsigned __int16 *)(a6 + 4));
    v_stack_p30 = (unsigned int)((unsigned int)(*(unsigned int *)(a6)));
    v_stack_p28 = v_rip + 2277009;
    v_stack_p20 = 0x800ULL;
    result = RtlStringCchPrintfExW(v_stack_m138, a4 + 48, a3, a4);
    if (sign_flag) goto loc_008E1B4C;
    v_stack_m160 = 0;
loc_008E1A70:
    if ((*(unsigned __int16 *)(v_stack_m138)) == 0) goto loc_008E1A8A;
    result = (v_stack_m138) + (2);
    a1 = (512) - (1);
    if (condition_is_not_equal) goto loc_008E1A70;
    goto loc_008E1B4C;
loc_008E1A8A:
    v_rdi = (512) - (a1);
    if (v_rdi >= 48) goto loc_008E1D1C;
loc_008E1AA0:
    v_stack_p38 = v_stack_m138;
    a4 = 0;
    a3 = 0;
    v_stack_p30 = v_rip + 2208395;
    v_stack_p28 = v_rip + 2210153;
    v_stack_p20 = 0x800ULL;
    result = RtlStringCchPrintfExW(v_stack_mD8, 59, a3, a4);
    if (sign_flag) goto loc_008E1B2C;
    if (v_stack_m140 == 0) goto loc_008E1AFE;
    if (*(unsigned __int64 *)(v_stack_m140 + 224) != 0) {
        v_r15 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m140 + 224) + 8);
    }
    v_stack_p28 = v_r15;
    a3 = 0;
    v_stack_p20 = v_stack_m160;
    result = _RegRtlOpenKeyTransacted(v_stack_m158, v_stack_mD8, a3, 1);
    v_rdi = (unsigned int)((unsigned int)(result));
    if (((unsigned int)(result)) == 0xC000017CULL) { v_rdi = (unsigned int)((unsigned int)(0xC0000034ULL)); }
loc_008E1B2C:
    if (v_stack_mD8 == 0) goto loc_008E1B3E;
    if (v_stack_mD8 != v_stack_mD8) goto loc_008E1D4A;
loc_008E1B3E:
    if (((unsigned int)(v_rdi)) != ((unsigned int)((unsigned int)(0xC0000034ULL)))) goto loc_008E1BCF;
loc_008E1B47:
loc_008E1B4C:
loc_008E1B50:
loc_008E1B54:
    result = v_stack_mD8;
    if (v_stack_m160 != 0) {
        result = ZwClose(v_stack_m160, v_stack_mD8, a3, 1);
    }
    if (sign_flag) goto loc_008E1929;
    result = PnpValidatePropertyData(a8, (unsigned int)(*(unsigned int *)(v_stack_m180)), (unsigned int)(*(unsigned int *)(v_stack_m170)), 1);
    goto loc_008E1929;
loc_008E1B7E:
    goto loc_008E18AB;
loc_008E1B86:
    if (result != (v_rip + 321555)) goto loc_008E1C6A;
    v_stack_p20 = v_stack_m138;
    result = DrvDbDispatchDriverPackage(*(unsigned __int16 *)(a6 + 4), (unsigned int)((unsigned int)(v_stack_m170)), (unsigned int)(*(unsigned int *)(v_stack_m170)), 1);
    goto loc_008E1920;
loc_008E1BAC:
loc_008E1BB1:
    if ((*(unsigned __int16 *)(result)) == ((unsigned __int16)(v_stack_m170))) goto loc_008E19B5;
    result = (result) + (2);
    a1 = (85) - (1);
    if (condition_is_not_equal) goto loc_008E1BB1;
loc_008E1BC5:
    goto loc_008E1929;
loc_008E1BCF:
    if (sign_flag) goto loc_008E1B4C;
    v_stack_m178 = (unsigned int)((unsigned int)(v_stack_m164));
    if (*(unsigned __int64 *)(v_stack_m180 + 520) != 0) goto loc_008E1CD2;
loc_008E1BF1:
    v_stack_p30 = v_stack_m188;
    v_stack_p28 = v_stack_m178;
    v_stack_p20 = a8;
    result = PnpRegQueryValueIndirect(v_stack_m180, v_stack_m160, v_stack_m150, v_stack_m168);
loc_008E1C1C:
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0xC0000034ULL)))) goto loc_008E1B47;
    if (((unsigned int)(result)) == 0xC000017CULL) goto loc_008E1B47;
    if ((unsigned int)(result) != 0) goto loc_008E1C80;
loc_008E1C36:
    *(unsigned int *)(v_stack_m170) = (unsigned int)(v_stack_m168);
    if (((unsigned int)(v_stack_m168)) == 1) goto loc_008E1B50;
    *(unsigned int *)(v_stack_m180) = (unsigned int)((unsigned int)(v_stack_m178));
    if ((unsigned int)((unsigned int)((unsigned int)(result))) != 0) goto loc_008E1C60;
    if ((unsigned int)((unsigned int)(v_stack_m164)) != 0) goto loc_008E1B54;
loc_008E1C60:
    goto loc_008E1B54;
loc_008E1C6A:
    v_stack_p20 = v_stack_m138;
    result = guard_dispatch_icall((unsigned int)(v_stack_m164), v_stack_m160, v_stack_m150, v_stack_m168);
    goto loc_008E1920;
loc_008E1C80:
    if (((unsigned int)((unsigned int)(v_stack_m164))) == 0xC0000023ULL) goto loc_008E1C36;
    goto loc_008E1B4C;
loc_008E1C8F:
    goto loc_008E1939;
loc_008E1C99:
    v_stack_p28 = v_stack_m148;
    v_stack_p20 = (unsigned __int8)(v_stack_m170);
    result = PnpOpenObjectRegKey((unsigned int)(v_stack_m164), v_stack_m180, (unsigned int)((unsigned int)(v_rdi)), (unsigned int)(0x2000001ULL));
    if (sign_flag) goto loc_008E1929;
    v_stack_m158 = v_stack_m148;
    goto loc_008E198A;
loc_008E1CD2:
    if (v_stack_m148 == (v_rip + 50487)) goto loc_008E1BF1;
    v_stack_p30 = v_stack_m188;
    v_stack_p28 = v_stack_m178;
    v_stack_p20 = a8;
    result = guard_dispatch_icall(v_stack_m180, v_stack_m160, v_stack_m150, v_stack_m168);
    goto loc_008E1C1C;
loc_008E1D12:
    goto loc_008E1929;
loc_008E1D1C:
    v_rdi = (unsigned int)((v_rdi) + (12));
    a2 = ((unsigned int)((unsigned int)(v_rdi))) + ((unsigned int)((unsigned int)(v_rdi)));
    result = ExAllocatePool2(256, a2, (unsigned int)(0x52504E50ULL), v_stack_m168);
    if (result != 0) goto loc_008E1AA0;
    goto loc_008E1B4C;
loc_008E1D4A:
    a2 = 0;
    result = ExFreePoolWithTag((unsigned int)(0xC0000017ULL), a2, (unsigned int)(0x52504E50ULL), v_stack_m168);
    goto loc_008E1B3E;
}
```

## 5. (Beta) C Style

```c
int64_t PnpGetObjectPropertyWorker(void *Arg1, int64_t Arg2, void *Arg3, int64_t Arg4, int64_t Arg5, void *Arg6, void *Arg7, int64_t Arg8, uint32_t Arg9, void *Arg10, uint32_t Arg11)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg6 = (uint8_t *)Arg6;
    uint8_t *arg7 = (uint8_t *)Arg7;
    uint8_t *arg10 = (uint8_t *)Arg10;

    int64_t result;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsp;
    uint32_t v_stack_m100;
    uint64_t v_stack_m108;
    uint32_t v_stack_m10C;
    uint32_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint32_t v_stack_m164;
    uint32_t v_stack_m168;
    uint64_t v_stack_m170;
    uint32_t v_stack_m178;
    uint64_t v_stack_m180;
    uint8_t v_stack_m188;
    uint64_t v_stack_m1F8;
    uint64_t v_stack_m58;
    uint64_t v_stack_mD8;
    uint32_t v_stack_mFC;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint32_t v_stack_p30;
    uint32_t v_stack_p38;
    uint32_t v_stack_p40;
    uint32_t v_stack_p48;
    uint32_t v_stack_p50;
    uint32_t v_stack_p58;
    uint32_t v_stack_p60;
    uint32_t v_stack_p68;
    uint32_t v_stack_p70;
    uint32_t v_stack_p78;
    uint32_t v_stack_p80;
    uint32_t v_stack_p88;

    local_rsp = (local_rsp) - (472);
    result = (*(uint64_t *)(v_rip + 0x528F0D)) ^ (local_rsp);
    v_stack_m58 = result;
    local_r15 = 0;
    v_stack_m158 = Arg4;
    v_stack_m140 = Arg1;
    v_stack_m170 = Arg7;
    v_stack_m180 = Arg10;
    v_stack_m150 = Arg5;
    v_stack_m148 = 0;
    if ((uint16_t)((uint32_t)(Arg11)) != 0) goto loc_008E1C8F;
    if (Arg8 == 0) goto loc_008E1B7E;
    if ((uint32_t)((uint32_t)(Arg9)) == 0) { Arg8 = 0; }
loc_008E18AB:
    *(uint32_t *)(arg7) = 0;
    v_stack_m164 = (uint32_t)((uint32_t)(Arg9));
    *(uint32_t *)(arg10) = 0;
    v_stack_m10C = 0;
    v_stack_mFC = 0;
    if (((uint32_t)((int32_t)(Arg3) - 1)) > 10) goto loc_008E1BC5;
    if (*(uint64_t *)(arg1 + (int32_t)(arg3) * 8 + 0x128) == 0) goto loc_008E1D12;
    v_stack_m100 = (uint32_t)((uint32_t)(Arg11));
    v_stack_m120 = Arg7;
    v_stack_m110 = (uint32_t)((uint32_t)(Arg9));
    v_stack_m108 = Arg10;
    v_stack_m138 = Arg4;
    v_stack_m130 = Arg5;
    v_stack_m128 = Arg6;
    v_stack_m118 = Arg8;
    if ((*(uint64_t *)(arg1 + (int32_t)(arg3) * 8 + 0x128)) != (v_rip + 1149)) goto loc_008E195D;
    v_stack_m1F8 = v_stack_m138;
    result = _PnpDispatchDevice(Arg1, Arg2, (uint32_t)((uint32_t)((int32_t)(Arg3))), 8);
loc_008E1920:
    if (((uint32_t)(result)) == 0xC0000016ULL) goto loc_008E1980;
loc_008E1929:
    if (v_stack_m148 != 0) {
        result = ZwClose(v_stack_m148, Arg2, (uint32_t)((uint32_t)((int32_t)(Arg3))), 8);
    }
loc_008E1939:
    Arg1 = (v_stack_m58) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, (uint32_t)((uint32_t)((int32_t)(Arg3))), 8);
    local_rsp = (local_rsp) + (472);
    return result;
loc_008E195D:
    if (result != (v_rip - 2996)) goto loc_008E1B86;
    v_stack_p20 = v_stack_m138;
    result = _PnpDispatchDeviceInterface(Arg1, Arg2, (uint32_t)((uint32_t)((int32_t)(Arg3))), 8);
    goto loc_008E1920;
loc_008E1980:
    if (v_stack_m158 == 0) goto loc_008E1C99;
loc_008E198A:
    v_stack_m160 = 0;
    v_stack_m168 = 0;
    v_stack_m178 = 0;
    *(uint32_t *)(v_stack_m170) = 0;
    v_stack_m188 = 0;
    *(uint32_t *)(v_stack_m180) = 0;
    if (v_stack_m150 != 0) goto loc_008E1BAC;
loc_008E19B5:
    v_stack_p88 = (uint32_t)((uint32_t)(*(uint32_t *)(arg6 + 0x10)));
    v_stack_p80 = (uint32_t)(*(uint8_t *)(arg6 + 0xF));
    v_stack_p78 = (uint32_t)(*(uint8_t *)(arg6 + 0xE));
    v_stack_p70 = (uint32_t)(*(uint8_t *)(arg6 + 0xD));
    Arg3 = 0;
    v_stack_p68 = (uint32_t)(*(uint8_t *)(arg6 + 0xC));
    Arg4 = 0;
    v_stack_p60 = (uint32_t)(*(uint8_t *)(arg6 + 0xB));
    v_stack_p58 = (uint32_t)(*(uint8_t *)(arg6 + 0xA));
    v_stack_p50 = (uint32_t)(*(uint8_t *)(arg6 + 0x9));
    v_stack_p48 = (uint32_t)(*(uint8_t *)(arg6 + 0x8));
    v_stack_p40 = (uint32_t)(*(uint16_t *)(arg6 + 0x6));
    v_stack_p38 = (uint32_t)(*(uint16_t *)(arg6 + 0x4));
    v_stack_p30 = (uint32_t)((uint32_t)(*(uint32_t *)(arg6)));
    v_stack_p28 = v_rip + 2277009;
    v_stack_p20 = 0x800ULL;
    result = RtlStringCchPrintfExW(v_stack_m138, Arg4 + 48, Arg3, Arg4);
    if (sign_flag) goto loc_008E1B4C;
    v_stack_m160 = 0;
loc_008E1A70:
    if ((*(uint16_t *)(v_stack_m138)) == 0) goto loc_008E1A8A;
    result = (v_stack_m138) + (2);
    Arg1 = (512) - (1);
    if (condition_is_not_equal) goto loc_008E1A70;
    goto loc_008E1B4C;
loc_008E1A8A:
    local_rdi = (512) - (Arg1);
    if (local_rdi >= 48) goto loc_008E1D1C;
loc_008E1AA0:
    v_stack_p38 = v_stack_m138;
    Arg4 = 0;
    Arg3 = 0;
    v_stack_p30 = v_rip + 2208395;
    v_stack_p28 = v_rip + 2210153;
    v_stack_p20 = 0x800ULL;
    result = RtlStringCchPrintfExW(v_stack_mD8, 59, Arg3, Arg4);
    if (sign_flag) goto loc_008E1B2C;
    if (v_stack_m140 == 0) goto loc_008E1AFE;
    if (*(uint64_t *)(v_stack_m140 + 0xE0) != 0) {
        local_r15 = *(uint64_t *)(*(uint64_t *)(v_stack_m140 + 0xE0) + 0x8);
    }
    v_stack_p28 = local_r15;
    Arg3 = 0;
    v_stack_p20 = v_stack_m160;
    result = _RegRtlOpenKeyTransacted(v_stack_m158, v_stack_mD8, Arg3, 1);
    local_rdi = (uint32_t)((uint32_t)(result));
    if (((uint32_t)(result)) == 0xC000017CULL) { local_rdi = (uint32_t)((uint32_t)(0xC0000034ULL)); }
loc_008E1B2C:
    if (v_stack_mD8 == 0) goto loc_008E1B3E;
    if (v_stack_mD8 != v_stack_mD8) goto loc_008E1D4A;
loc_008E1B3E:
    if (((uint32_t)(local_rdi)) != ((uint32_t)((uint32_t)(0xC0000034ULL)))) goto loc_008E1BCF;
loc_008E1B47:
loc_008E1B4C:
loc_008E1B50:
loc_008E1B54:
    result = v_stack_mD8;
    if (v_stack_m160 != 0) {
        result = ZwClose(v_stack_m160, v_stack_mD8, Arg3, 1);
    }
    if (sign_flag) goto loc_008E1929;
    result = PnpValidatePropertyData(Arg8, (uint32_t)(*(uint32_t *)(v_stack_m180)), (uint32_t)(*(uint32_t *)(v_stack_m170)), 1);
    goto loc_008E1929;
loc_008E1B7E:
    goto loc_008E18AB;
loc_008E1B86:
    if (result != (v_rip + 321555)) goto loc_008E1C6A;
    v_stack_p20 = v_stack_m138;
    result = DrvDbDispatchDriverPackage(*(uint16_t *)(arg6 + 0x4), (uint32_t)((uint32_t)(v_stack_m170)), (uint32_t)(*(uint32_t *)(v_stack_m170)), 1);
    goto loc_008E1920;
loc_008E1BAC:
loc_008E1BB1:
    if ((*(uint16_t *)(result)) == ((uint16_t)(v_stack_m170))) goto loc_008E19B5;
    result = (result) + (2);
    Arg1 = (85) - (1);
    if (condition_is_not_equal) goto loc_008E1BB1;
loc_008E1BC5:
    goto loc_008E1929;
loc_008E1BCF:
    if (sign_flag) goto loc_008E1B4C;
    v_stack_m178 = (uint32_t)((uint32_t)(v_stack_m164));
    if (*(uint64_t *)(v_stack_m180 + 0x208) != 0) goto loc_008E1CD2;
loc_008E1BF1:
    v_stack_p30 = v_stack_m188;
    v_stack_p28 = v_stack_m178;
    v_stack_p20 = Arg8;
    result = PnpRegQueryValueIndirect(v_stack_m180, v_stack_m160, v_stack_m150, v_stack_m168);
loc_008E1C1C:
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0xC0000034ULL)))) goto loc_008E1B47;
    if (((uint32_t)(result)) == 0xC000017CULL) goto loc_008E1B47;
    if ((uint32_t)(result) != 0) goto loc_008E1C80;
loc_008E1C36:
    *(uint32_t *)(v_stack_m170) = (uint32_t)(v_stack_m168);
    if (((uint32_t)(v_stack_m168)) == 1) goto loc_008E1B50;
    *(uint32_t *)(v_stack_m180) = (uint32_t)((uint32_t)(v_stack_m178));
    if ((uint32_t)((uint32_t)((uint32_t)(result))) != 0) goto loc_008E1C60;
    if ((uint32_t)((uint32_t)(v_stack_m164)) != 0) goto loc_008E1B54;
loc_008E1C60:
    goto loc_008E1B54;
loc_008E1C6A:
    v_stack_p20 = v_stack_m138;
    result = guard_dispatch_icall((uint32_t)(v_stack_m164), v_stack_m160, v_stack_m150, v_stack_m168);
    goto loc_008E1920;
loc_008E1C80:
    if (((uint32_t)((uint32_t)(v_stack_m164))) == 0xC0000023ULL) goto loc_008E1C36;
    goto loc_008E1B4C;
loc_008E1C8F:
    goto loc_008E1939;
loc_008E1C99:
    v_stack_p28 = v_stack_m148;
    v_stack_p20 = (uint8_t)(v_stack_m170);
    result = PnpOpenObjectRegKey((uint32_t)(v_stack_m164), v_stack_m180, (uint32_t)((uint32_t)(local_rdi)), (uint32_t)(0x2000001ULL));
    if (sign_flag) goto loc_008E1929;
    v_stack_m158 = v_stack_m148;
    goto loc_008E198A;
loc_008E1CD2:
    if (v_stack_m148 == (v_rip + 50487)) goto loc_008E1BF1;
    v_stack_p30 = v_stack_m188;
    v_stack_p28 = v_stack_m178;
    v_stack_p20 = Arg8;
    result = guard_dispatch_icall(v_stack_m180, v_stack_m160, v_stack_m150, v_stack_m168);
    goto loc_008E1C1C;
loc_008E1D12:
    goto loc_008E1929;
loc_008E1D1C:
    local_rdi = (uint32_t)((local_rdi) + (12));
    Arg2 = ((uint32_t)((uint32_t)(local_rdi))) + ((uint32_t)((uint32_t)(local_rdi)));
    result = ExAllocatePool2(256, Arg2, (uint32_t)(0x52504E50ULL), v_stack_m168);
    if (result != 0) goto loc_008E1AA0;
    goto loc_008E1B4C;
loc_008E1D4A:
    Arg2 = 0;
    result = ExFreePoolWithTag((uint32_t)(0xC0000017ULL), Arg2, (uint32_t)(0x52504E50ULL), v_stack_m168);
    goto loc_008E1B3E;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x128 + rdi*8` | `64` | `R` |
| `Arg3` | `- 0x1` | `32` | `R` |
| `Arg6` | `+ 0x0` | `32` | `R` |
| `Arg6` | `+ 0x4` | `16` | `R` |
| `Arg6` | `+ 0x6` | `16` | `R` |
| `Arg6` | `+ 0x8` | `8` | `R` |
| `Arg6` | `+ 0x9` | `8` | `R` |
| `Arg6` | `+ 0xA` | `8` | `R` |
| `Arg6` | `+ 0xB` | `8` | `R` |
| `Arg6` | `+ 0xC` | `8` | `R` |
| `Arg6` | `+ 0xD` | `8` | `R` |
| `Arg6` | `+ 0xE` | `8` | `R` |
| `Arg6` | `+ 0xF` | `8` | `R` |
| `Arg6` | `+ 0x10` | `32` | `R` |
| `Arg7` | `+ 0x0` | `32` | `W` |
| `Arg10` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008E1810&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
