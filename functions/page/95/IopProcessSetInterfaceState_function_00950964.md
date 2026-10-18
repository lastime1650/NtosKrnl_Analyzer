# IopProcessSetInterfaceState

- RVA: `0x00950964`–`0x00950F1D` (길이 `1,465` bytes)
- VA: `0x0000000140950964`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00091C78`
- 디코드: `372`개 명령, `1,465/1,465` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **35**; 고유 호출 대상: **30**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x00950A68` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00950A84` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00950AA0` → [CmGetDeviceInterfaceClassGuid](../8F/CmGetDeviceInterfaceClassGuid_function_008F3380.md) (function, `0x008F3380`)
- `0x00950AB6` → [IopBuildGlobalSymbolicLinkString](IopBuildGlobalSymbolicLinkString_function_00951530.md) (function, `0x00951530`)
- `0x00950AD7` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00950B31` → [PnpGetObjectProperty](../8E/PnpGetObjectProperty_function_008E2180.md) (function, `0x008E2180`)
- `0x00950B54` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x00950B66` → [PnpUnicodeStringToWstrFree](../8F/PnpUnicodeStringToWstrFree_function_008F59F0.md) (function, `0x008F59F0`)
- `0x00950B78` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00950B87` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00950B96` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00950BA3` → [PiDmObjectRelease](../8E/PiDmObjectRelease_function_008E4F70.md) (function, `0x008E4F70`)
- `0x00950BB1` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00950C1C` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00950C2E` → [PiDmAddCacheReferenceForObject](PiDmAddCacheReferenceForObject_function_00950FB4.md) (function, `0x00950FB4`)
- `0x00950C45` → [CmpLockSiloKeyLockTrackerExclusive](../8F/CmpLockSiloKeyLockTrackerExclusive_function_008F9EF8.md) (function, `0x008F9EF8`)
- `0x00950C9A` → [ZwOpenSymbolicLinkObject](../../text/6A/ZwOpenSymbolicLinkObject_function_006AF7F0.md) (function, `0x006AF7F0`)
- `0x00950CB8` → [ZwCreateSymbolicLinkObject](../../text/6A/ZwCreateSymbolicLinkObject_function_006AE9D0.md) (function, `0x006AE9D0`)
- `0x00950CCB` → [PiDmObjectReleaseLock](../8E/PiDmObjectReleaseLock_function_008E5584.md) (function, `0x008E5584`)
- `0x00950D01` → [PnpSetDeviceClassChange](PnpSetDeviceClassChange_function_009517B0.md) (function, `0x009517B0`)
- `0x00950D09` → [PnpRaiseNtPlugPlayInterfacePropertyChangeEvent](PnpRaiseNtPlugPlayInterfacePropertyChangeEvent_function_00951D54.md) (function, `0x00951D54`)
- `0x00950D22` → [PiDmRemoveCacheReferenceForObject](PiDmRemoveCacheReferenceForObject_function_00950F24.md) (function, `0x00950F24`)
- `0x00950D3C` → [PiDmObjectManagerAcquireSharedLock](PiDmObjectManagerAcquireSharedLock_function_009511A0.md) (function, `0x009511A0`)
- `0x00950D4B` → [PiDmLookupObject](PiDmLookupObject_function_00951360.md) (function, `0x00951360`)
- `0x00950D70` → [PiDmObjectManagerReleaseLock](PiDmObjectManagerReleaseLock_function_0095111C.md) (function, `0x0095111C`)
- `0x00950D7C` → [CmpLockSiloKeyLockTrackerExclusive](../8F/CmpLockSiloKeyLockTrackerExclusive_function_008F9EF8.md) (function, `0x008F9EF8`)
- `0x00950D8D` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00950DD8` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (function, `0x00463960`)
- `0x00950DF0` → [PnpDeviceObjectFromDeviceInstanceWithTag](../8E/PnpDeviceObjectFromDeviceInstanceWithTag_function_008E7490.md) (function, `0x008E7490`)
- `0x00950E55` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00950E80` → [IoGetDeviceProperty](../8F/IoGetDeviceProperty_function_008FA720.md) (function, `0x008FA720`)
- `0x00950EA7` → [PipCanEnableInterfaces](PipCanEnableInterfaces_function_00951E70.md) (function, `0x00951E70`)
- `0x00950EE8` → [PiRemoveDeferredSetInterfaceState](../AA/PiRemoveDeferredSetInterfaceState_function_00AAE03C.md) (function, `0x00AAE03C`)
- `0x00950F02` → [PiDeferSetInterfaceState](../AA/PiDeferSetInterfaceState_function_00AA6FA4.md) (function, `0x00AA6FA4`)
- `0x00950F13` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [IopDoDeferredSetInterfaceState](../94/IopDoDeferredSetInterfaceState_function_0094EF68.md) at `0x0094EFD2`
- [IoSetDeviceInterfaceState](IoSetDeviceInterfaceState_function_00950740.md) at `0x00950778`

### Static image references
- `0x00950987` → RVA `0x00E0A740` (`.data`; read)
- `0x00950B19` → RVA `0x00011490` (`.rdata`; read)
- `0x00950B2A` → RVA `0x00E66398` (`.data`; read)
- `0x00950C78` → RVA `0x00FD9AA8` (`PAGEDATA`; read)
- `0x00950CE3` → RVA `0x000122D8` (`.rdata`; read)
- `0x00950CEF` → RVA `0x00013E30` (`.rdata`; read)
- `0x00950D35` → RVA `0x00F8B7A0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **15**
  - `0x00950A68` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00950A84` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00950AD7` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00950B54` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x00950B78` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00950B87` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00950B96` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00950BB1` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00950C1C` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00950C9A` → [ZwOpenSymbolicLinkObject](../../text/6A/ZwOpenSymbolicLinkObject_function_006AF7F0.md) (`PAGE` → `.text`)
  - `0x00950CB8` → [ZwCreateSymbolicLinkObject](../../text/6A/ZwCreateSymbolicLinkObject_function_006AE9D0.md) (`PAGE` → `.text`)
  - `0x00950D8D` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x00950DD8` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (`PAGE` → `.text`)
  - `0x00950E55` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00950F13` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00950964  48 8B C4                        mov rax, rsp
00950967  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
0095096B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0095096F  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00950973  55                              push rbp
00950974  41 54                           push r12
00950976  41 55                           push r13
00950978  41 56                           push r14
0095097A  41 57                           push r15
0095097C  48 8D 68 C8                     lea rbp, [rax - 0x38]
00950980  48 81 EC 10 01 00 00            sub rsp, 0x110
00950987  48 8B 05 B2 9D 4B 00            mov rax, qword ptr [rip + 0x4b9db2]
0095098E  48 33 C4                        xor rax, rsp
00950991  48 89 45 00                     mov qword ptr [rbp], rax
00950995  33 DB                           xor ebx, ebx
00950997  44 88 44 24 63                  mov byte ptr [rsp + 0x63], r8b
0095099C  0F 57 C0                        xorps xmm0, xmm0
0095099F  88 54 24 61                     mov byte ptr [rsp + 0x61], dl
009509A3  33 C0                           xor eax, eax
009509A5  89 5C 24 64                     mov dword ptr [rsp + 0x64], ebx
009509A9  48 89 5C 24 70                  mov qword ptr [rsp + 0x70], rbx
009509AE  0F 57 C9                        xorps xmm1, xmm1
009509B1  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
009509B5  4C 8B F9                        mov r15, rcx
009509B8  89 45 C8                        mov dword ptr [rbp - 0x38], eax
009509BB  44 8B F3                        mov r14d, ebx
009509BE  89 5C 24 68                     mov dword ptr [rsp + 0x68], ebx
009509C2  44 8B E3                        mov r12d, ebx
009509C5  89 5C 24 78                     mov dword ptr [rsp + 0x78], ebx
009509C9  8B FB                           mov edi, ebx
009509CB  88 5C 24 62                     mov byte ptr [rsp + 0x62], bl
009509CF  44 8B EB                        mov r13d, ebx
009509D2  88 5C 24 60                     mov byte ptr [rsp + 0x60], bl
009509D6  8B F3                           mov esi, ebx
009509D8  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
009509DC  0F 11 4D 90                     movups xmmword ptr [rbp - 0x70], xmm1
009509E0  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
009509E4  0F 11 45 A0                     movups xmmword ptr [rbp - 0x60], xmm0
009509E8  0F 11 45 B0                     movups xmmword ptr [rbp - 0x50], xmm0
009509EC  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
009509F0  48 85 C9                        test rcx, rcx
009509F3  0F 84 E9 01 00 00               je 0x140950be2
009509F9  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
009509FD  48 85 C9                        test rcx, rcx
00950A00  0F 84 DC 01 00 00               je 0x140950be2
00950A06  41 0F B7 17                     movzx edx, word ptr [r15]
00950A0A  66 85 D2                        test dx, dx
00950A0D  0F 84 CF 01 00 00               je 0x140950be2
00950A13  45 0F B7 47 02                  movzx r8d, word ptr [r15 + 2]
00950A18  44 8D 4B 02                     lea r9d, [rbx + 2]
00950A1C  66 45 3B C1                     cmp r8w, r9w
00950A20  72 77                           jb 0x140950a99
00950A22  66 41 3B D0                     cmp dx, r8w
00950A26  0F 87 B6 01 00 00               ja 0x140950be2
00950A2C  66 39 19                        cmp word ptr [rcx], bx
00950A2F  0F 84 CE 01 00 00               je 0x140950c03
00950A35  66 41 3B D0                     cmp dx, r8w
00950A39  75 10                           jne 0x140950a4b
00950A3B  8B C2                           mov eax, edx
00950A3D  48 D1 E8                        shr rax, 1
00950A40  66 39 5C 41 FE                  cmp word ptr [rcx + rax*2 - 2], bx
00950A45  0F 84 B8 01 00 00               je 0x140950c03
00950A4B  49 8B C0                        mov rax, r8
00950A4E  49 2B C1                        sub rax, r9
00950A51  48 3B D0                        cmp rdx, rax
00950A54  0F 86 92 01 00 00               jbe 0x140950bec
00950A5A  49 03 D1                        add rdx, r9
00950A5D  B9 00 01 00 00                  mov ecx, 0x100
00950A62  41 B8 50 70 73 75               mov r8d, 0x75737050
00950A68  E8 83 16 23 00                  call 0x140b820f0
00950A6D  48 8B D8                        mov rbx, rax
00950A70  48 85 C0                        test rax, rax
00950A73  0F 84 5F 01 00 00               je 0x140950bd8
00950A79  45 0F B7 07                     movzx r8d, word ptr [r15]
00950A7D  48 8B C8                        mov rcx, rax
00950A80  49 8B 57 08                     mov rdx, qword ptr [r15 + 8]
00950A84  E8 B7 5D D7 FF                  call 0x1406c6840
00950A89  41 0F B7 07                     movzx eax, word ptr [r15]
00950A8D  48 8B F3                        mov rsi, rbx
00950A90  48 D1 E8                        shr rax, 1
00950A93  33 C9                           xor ecx, ecx
00950A95  66 89 0C 43                     mov word ptr [rbx + rax*2], cx
00950A99  4C 8D 45 F0                     lea r8, [rbp - 0x10]
00950A9D  48 8B D6                        mov rdx, rsi
00950AA0  E8 DB 28 FA FF                  call 0x1408f3380
00950AA5  8B D8                           mov ebx, eax
00950AA7  85 C0                           test eax, eax
00950AA9  0F 88 9C 00 00 00               js 0x140950b4b
00950AAF  48 8D 55 90                     lea rdx, [rbp - 0x70]
00950AB3  49 8B CF                        mov rcx, r15
00950AB6  E8 75 0A 00 00                  call 0x140951530
00950ABB  8B D8                           mov ebx, eax
00950ABD  85 C0                           test eax, eax
00950ABF  0F 88 86 00 00 00               js 0x140950b4b
00950AC5  BB 90 01 00 00                  mov ebx, 0x190
00950ACA  41 B8 50 70 20 20               mov r8d, 0x20207050
00950AD0  8B D3                           mov edx, ebx
00950AD2  B9 00 01 00 00                  mov ecx, 0x100
00950AD7  E8 14 16 23 00                  call 0x140b820f0
00950ADC  33 C9                           xor ecx, ecx
00950ADE  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
00950AE2  4C 8B F0                        mov r14, rax
00950AE5  48 85 C0                        test rax, rax
00950AE8  0F 84 EA 00 00 00               je 0x140950bd8
00950AEE  89 4C 24 50                     mov dword ptr [rsp + 0x50], ecx
00950AF2  48 8D 44 24 78                  lea rax, [rsp + 0x78]
00950AF7  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00950AFC  44 8D 41 03                     lea r8d, [rcx + 3]
00950B00  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
00950B04  48 8D 44 24 68                  lea rax, [rsp + 0x68]
00950B09  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
00950B0E  45 33 C9                        xor r9d, r9d
00950B11  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00950B16  48 8B D6                        mov rdx, rsi
00950B19  48 8D 05 70 09 6C FF            lea rax, [rip - 0x93f690]
00950B20  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00950B25  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00950B2A  48 8B 0D 67 58 51 00            mov rcx, qword ptr [rip + 0x515867]
00950B31  E8 4A 16 F9 FF                  call 0x1408e2180
00950B36  8B D8                           mov ebx, eax
00950B38  3D 25 02 00 C0                  cmp eax, 0xc0000225
00950B3D  0F 84 C8 00 00 00               je 0x140950c0b
00950B43  85 C0                           test eax, eax
00950B45  0F 89 7B 02 00 00               jns 0x140950dc6
00950B4B  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
00950B4F  48 85 C9                        test rcx, rcx
00950B52  74 0C                           je 0x140950b60
00950B54  E8 F7 1C 23 00                  call 0x140b82850
00950B59  0F 57 C0                        xorps xmm0, xmm0
00950B5C  0F 11 45 90                     movups xmmword ptr [rbp - 0x70], xmm0
00950B60  49 8B D7                        mov rdx, r15
00950B63  48 8B CE                        mov rcx, rsi
00950B66  E8 85 4E FA FF                  call 0x1408f59f0
00950B6B  4D 85 ED                        test r13, r13
00950B6E  74 0D                           je 0x140950b7d
00950B70  BA 50 6E 70 49                  mov edx, 0x49706e50
00950B75  49 8B CD                        mov rcx, r13
00950B78  E8 63 6D 9A FF                  call 0x1402f78e0
00950B7D  4D 85 E4                        test r12, r12
00950B80  74 0A                           je 0x140950b8c
00950B82  33 D2                           xor edx, edx
00950B84  49 8B CC                        mov rcx, r12
00950B87  E8 E4 1C 23 00                  call 0x140b82870
00950B8C  4D 85 F6                        test r14, r14
00950B8F  74 0A                           je 0x140950b9b
00950B91  33 D2                           xor edx, edx
00950B93  49 8B CE                        mov rcx, r14
00950B96  E8 D5 1C 23 00                  call 0x140b82870
00950B9B  48 85 FF                        test rdi, rdi
00950B9E  74 08                           je 0x140950ba8
00950BA0  48 8B CF                        mov rcx, rdi
00950BA3  E8 C8 43 F9 FF                  call 0x1408e4f70
00950BA8  8B C3                           mov eax, ebx
00950BAA  48 8B 4D 00                     mov rcx, qword ptr [rbp]
00950BAE  48 33 CC                        xor rcx, rsp
00950BB1  E8 8A BA D5 FF                  call 0x1406ac640
00950BB6  4C 8D 9C 24 10 01 00 00         lea r11, [rsp + 0x110]
00950BBE  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00950BC2  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00950BC6  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00950BCA  49 8B E3                        mov rsp, r11
00950BCD  41 5F                           pop r15
00950BCF  41 5E                           pop r14
00950BD1  41 5D                           pop r13
00950BD3  41 5C                           pop r12
00950BD5  5D                              pop rbp
00950BD6  C3                              ret
00950BD7  CC                              int3
00950BD8  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00950BDD  E9 69 FF FF FF                  jmp 0x140950b4b
00950BE2  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00950BE7  E9 5F FF FF FF                  jmp 0x140950b4b
00950BEC  48 8B C2                        mov rax, rdx
00950BEF  48 D1 E8                        shr rax, 1
00950BF2  66 39 5C 41 FE                  cmp word ptr [rcx + rax*2 - 2], bx
00950BF7  74 0A                           je 0x140950c03
00950BF9  66 39 1C 41                     cmp word ptr [rcx + rax*2], bx
00950BFD  0F 85 57 FE FF FF               jne 0x140950a5a
00950C03  48 8B F1                        mov rsi, rcx
00950C06  E9 8E FE FF FF                  jmp 0x140950a99
00950C0B  BB 10 00 00 C0                  mov ebx, 0xc0000010
00950C10  E9 36 FF FF FF                  jmp 0x140950b4b
00950C15  49 8B D4                        mov rdx, r12
00950C18  48 8D 4D E0                     lea rcx, [rbp - 0x20]
00950C1C  E8 5F 9B AD FF                  call 0x14042a780
00950C21  4C 8D 44 24 70                  lea r8, [rsp + 0x70]
00950C26  48 8B D6                        mov rdx, rsi
00950C29  B9 03 00 00 00                  mov ecx, 3
00950C2E  E8 81 03 00 00                  call 0x140950fb4
00950C33  48 8B 7C 24 70                  mov rdi, qword ptr [rsp + 0x70]
00950C38  8B D8                           mov ebx, eax
00950C3A  85 C0                           test eax, eax
00950C3C  0F 88 09 FF FF FF               js 0x140950b4b
00950C42  48 8B CF                        mov rcx, rdi
00950C45  E8 AE 92 FA FF                  call 0x1408f9ef8
00950C4A  8B 47 20                        mov eax, dword ptr [rdi + 0x20]
00950C4D  A8 01                           test al, 1
00950C4F  0F 84 6A 01 00 00               je 0x140950dbf
00950C55  4C 8D 77 28                     lea r14, [rdi + 0x28]
00950C59  45 33 ED                        xor r13d, r13d
00950C5C  4D 39 2E                        cmp qword ptr [r14], r13
00950C5F  0F 85 C7 00 00 00               jne 0x140950d2c
00950C65  48 8D 45 90                     lea rax, [rbp - 0x70]
00950C69  C7 45 A0 30 00 00 00            mov dword ptr [rbp - 0x60], 0x30
00950C70  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
00950C74  4C 8D 45 A0                     lea r8, [rbp - 0x60]
00950C78  48 8B 05 29 8E 68 00            mov rax, qword ptr [rip + 0x688e29]
00950C7F  BA 01 00 0F 00                  mov edx, 0xf0001
00950C84  49 8B CE                        mov rcx, r14
00950C87  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00950C8B  4C 89 6D A8                     mov qword ptr [rbp - 0x58], r13
00950C8F  C7 45 B8 40 02 00 00            mov dword ptr [rbp - 0x48], 0x240
00950C96  4C 89 6D C8                     mov qword ptr [rbp - 0x38], r13
00950C9A  E8 51 EB D5 FF                  call 0x1406af7f0
00950C9F  8B D8                           mov ebx, eax
00950CA1  3D 34 00 00 C0                  cmp eax, 0xc0000034
00950CA6  75 17                           jne 0x140950cbf
00950CA8  4C 8D 4D E0                     lea r9, [rbp - 0x20]
00950CAC  BA 01 00 0F 00                  mov edx, 0xf0001
00950CB1  4C 8D 45 A0                     lea r8, [rbp - 0x60]
00950CB5  49 8B CE                        mov rcx, r14
00950CB8  E8 13 DD D5 FF                  call 0x1406ae9d0
00950CBD  8B D8                           mov ebx, eax
00950CBF  85 DB                           test ebx, ebx
00950CC1  78 05                           js 0x140950cc8
00950CC3  C6 44 24 62 01                  mov byte ptr [rsp + 0x62], 1
00950CC8  48 8B CF                        mov rcx, rdi
00950CCB  E8 B4 48 F9 FF                  call 0x1408e5584
00950CD0  4C 8B 75 80                     mov r14, qword ptr [rbp - 0x80]
00950CD4  33 C0                           xor eax, eax
00950CD6  4C 8B 6D 88                     mov r13, qword ptr [rbp - 0x78]
00950CDA  38 44 24 62                     cmp byte ptr [rsp + 0x62], al
00950CDE  74 2E                           je 0x140950d0e
00950CE0  45 33 C0                        xor r8d, r8d
00950CE3  48 8D 05 EE 15 6C FF            lea rax, [rip - 0x93ea12]
00950CEA  44 38 44 24 61                  cmp byte ptr [rsp + 0x61], r8b
00950CEF  48 8D 0D 3A 31 6C FF            lea rcx, [rip - 0x93cec6]
00950CF6  4D 8B C7                        mov r8, r15
00950CF9  48 8D 55 F0                     lea rdx, [rbp - 0x10]
00950CFD  48 0F 44 C8                     cmove rcx, rax
00950D01  E8 AA 0A 00 00                  call 0x1409517b0
00950D06  48 8B D6                        mov rdx, rsi
00950D09  E8 46 10 00 00                  call 0x140951d54
00950D0E  8A 44 24 60                     mov al, byte ptr [rsp + 0x60]
00950D12  84 C0                           test al, al
00950D14  0F 84 31 FE FF FF               je 0x140950b4b
00950D1A  48 8B D6                        mov rdx, rsi
00950D1D  B9 03 00 00 00                  mov ecx, 3
00950D22  E8 FD 01 00 00                  call 0x140950f24
00950D27  E9 1F FE FF FF                  jmp 0x140950b4b
00950D2C  BB 00 00 00 40                  mov ebx, 0x40000000
00950D31  EB 68                           jmp 0x140950d9b
00950D33  8B D9                           mov ebx, ecx
00950D35  48 8D 0D 64 AA 63 00            lea rcx, [rip + 0x63aa64]
00950D3C  E8 5F 04 00 00                  call 0x1409511a0
00950D41  48 8B D6                        mov rdx, rsi
00950D44  48 8D 0D 55 AA 63 00            lea rcx, [rip + 0x63aa55]
00950D4B  E8 10 06 00 00                  call 0x140951360
00950D50  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00950D55  48 8B F8                        mov rdi, rax
00950D58  4C 8B F0                        mov r14, rax
00950D5B  48 85 C0                        test rax, rax
00950D5E  74 58                           je 0x140950db8
00950D60  F0 FF 47 08                     lock inc dword ptr [rdi + 8]
00950D64  48 8B 7C 24 70                  mov rdi, qword ptr [rsp + 0x70]
00950D69  48 8D 0D 30 AA 63 00            lea rcx, [rip + 0x63aa30]
00950D70  E8 A7 03 00 00                  call 0x14095111c
00950D75  85 DB                           test ebx, ebx
00950D77  78 2C                           js 0x140950da5
00950D79  48 8B CF                        mov rcx, rdi
00950D7C  E8 77 91 FA FF                  call 0x1408f9ef8
00950D81  49 8B 4E 28                     mov rcx, qword ptr [r14 + 0x28]
00950D85  45 33 ED                        xor r13d, r13d
00950D88  48 85 C9                        test rcx, rcx
00950D8B  74 21                           je 0x140950dae
00950D8D  E8 1E C5 D5 FF                  call 0x1406ad2b0
00950D92  4D 89 6E 28                     mov qword ptr [r14 + 0x28], r13
00950D96  C6 44 24 62 01                  mov byte ptr [rsp + 0x62], 1
00950D9B  C6 44 24 60 01                  mov byte ptr [rsp + 0x60], 1
00950DA0  E9 23 FF FF FF                  jmp 0x140950cc8
00950DA5  4C 8B 75 80                     mov r14, qword ptr [rbp - 0x80]
00950DA9  E9 9D FD FF FF                  jmp 0x140950b4b
00950DAE  BB 34 00 00 C0                  mov ebx, 0xc0000034
00950DB3  E9 10 FF FF FF                  jmp 0x140950cc8
00950DB8  BB 34 00 00 C0                  mov ebx, 0xc0000034
00950DBD  EB AA                           jmp 0x140950d69
00950DBF  BB 34 00 00 C0                  mov ebx, 0xc0000034
00950DC4  EB D5                           jmp 0x140950d9b
00950DC6  83 7C 24 68 12                  cmp dword ptr [rsp + 0x68], 0x12
00950DCB  0F 85 3A FE FF FF               jne 0x140950c0b
00950DD1  49 8B D6                        mov rdx, r14
00950DD4  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00950DD8  E8 83 2B B1 FF                  call 0x140463960
00950DDD  8B D8                           mov ebx, eax
00950DDF  85 C0                           test eax, eax
00950DE1  0F 88 64 FD FF FF               js 0x140950b4b
00950DE7  BA 50 6E 70 49                  mov edx, 0x49706e50
00950DEC  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00950DF0  E8 9B 66 F9 FF                  call 0x1408e7490
00950DF5  8A 54 24 61                     mov dl, byte ptr [rsp + 0x61]
00950DF9  33 C9                           xor ecx, ecx
00950DFB  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
00950DFF  4C 8B E8                        mov r13, rax
00950E02  48 85 C0                        test rax, rax
00950E05  0F 84 E7 00 00 00               je 0x140950ef2
00950E0B  48 8B 80 38 01 00 00            mov rax, qword ptr [rax + 0x138]
00950E12  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
00950E16  4C 8B C1                        mov r8, rcx
00950E19  84 D2                           test dl, dl
00950E1B  0F 85 86 00 00 00               jne 0x140950ea7
00950E21  33 C9                           xor ecx, ecx
00950E23  38 4C 24 63                     cmp byte ptr [rsp + 0x63], cl
00950E27  0F 85 92 00 00 00               jne 0x140950ebf
00950E2D  84 D2                           test dl, dl
00950E2F  0F 84 FE FE FF FF               je 0x140950d33
00950E35  C7 44 24 64 00 02 00 00         mov dword ptr [rsp + 0x64], 0x200
00950E3D  4D 85 E4                        test r12, r12
00950E40  0F 85 C8 00 00 00               jne 0x140950f0e
00950E46  8B 54 24 64                     mov edx, dword ptr [rsp + 0x64]
00950E4A  B9 00 01 00 00                  mov ecx, 0x100
00950E4F  41 B8 50 70 20 20               mov r8d, 0x20207050
00950E55  E8 96 12 23 00                  call 0x140b820f0
00950E5A  4C 8B E0                        mov r12, rax
00950E5D  48 85 C0                        test rax, rax
00950E60  0F 84 72 FD FF FF               je 0x140950bd8
00950E66  44 8B 44 24 64                  mov r8d, dword ptr [rsp + 0x64]
00950E6B  48 8D 44 24 64                  lea rax, [rsp + 0x64]
00950E70  4D 8B CC                        mov r9, r12
00950E73  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00950E78  BA 0B 00 00 00                  mov edx, 0xb
00950E7D  49 8B CD                        mov rcx, r13
00950E80  E8 9B 98 FA FF                  call 0x1408fa720
00950E85  8B D8                           mov ebx, eax
00950E87  3D 23 00 00 C0                  cmp eax, 0xc0000023
00950E8C  74 AF                           je 0x140950e3d
00950E8E  33 C9                           xor ecx, ecx
00950E90  85 C0                           test eax, eax
00950E92  0F 88 B3 FC FF FF               js 0x140950b4b
00950E98  39 4C 24 64                     cmp dword ptr [rsp + 0x64], ecx
00950E9C  0F 84 A9 FC FF FF               je 0x140950b4b
00950EA2  E9 6E FD FF FF                  jmp 0x140950c15
00950EA7  E8 C4 0F 00 00                  call 0x140951e70
00950EAC  33 C9                           xor ecx, ecx
00950EAE  84 C0                           test al, al
00950EB0  0F 84 55 FD FF FF               je 0x140950c0b
00950EB6  8A 54 24 61                     mov dl, byte ptr [rsp + 0x61]
00950EBA  E9 64 FF FF FF                  jmp 0x140950e23
00950EBF  4D 85 C0                        test r8, r8
00950EC2  0F 84 65 FF FF FF               je 0x140950e2d
00950EC8  49 8B 85 38 01 00 00            mov rax, qword ptr [r13 + 0x138]
00950ECF  8B 48 20                        mov ecx, dword ptr [rax + 0x20]
00950ED2  F6 C1 10                        test cl, 0x10
00950ED5  75 07                           jne 0x140950ede
00950ED7  33 C9                           xor ecx, ecx
00950ED9  E9 4F FF FF FF                  jmp 0x140950e2d
00950EDE  84 D2                           test dl, dl
00950EE0  49 8B C8                        mov rcx, r8
00950EE3  49 8B D7                        mov rdx, r15
00950EE6  75 1A                           jne 0x140950f02
00950EE8  E8 4F D1 15 00                  call 0x140aae03c
00950EED  E9 59 FC FF FF                  jmp 0x140950b4b
00950EF2  84 D2                           test dl, dl
00950EF4  0F 85 11 FD FF FF               jne 0x140950c0b
00950EFA  4C 8B C1                        mov r8, rcx
00950EFD  E9 21 FF FF FF                  jmp 0x140950e23
00950F02  E8 9D 60 15 00                  call 0x140aa6fa4
00950F07  8B D8                           mov ebx, eax
00950F09  E9 3D FC FF FF                  jmp 0x140950b4b
00950F0E  33 D2                           xor edx, edx
00950F10  49 8B CC                        mov rcx, r12
00950F13  E8 58 19 23 00                  call 0x140b82870
00950F18  E9 29 FF FF FF                  jmp 0x140950e46
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopProcessSetInterfaceState(__int64 a1, unsigned __int8 a2, unsigned __int8 a3)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_mA0;
    unsigned int v_stack_mA8;
    unsigned int v_stack_mAC;
    unsigned __int8 v_stack_mAD;
    unsigned __int8 v_stack_mAE;
    unsigned __int8 v_stack_mAF;
    unsigned __int8 v_stack_mB0;
    unsigned int v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned int v_stack_mD0;
    unsigned int v_stack_mD4;
    unsigned __int8 v_stack_mD5;
    unsigned __int8 v_stack_mD6;
    unsigned __int8 v_stack_mD7;
    unsigned __int8 v_stack_mD8;
    unsigned int v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned int v_stack_mF8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (272);
    result = (*(unsigned __int64 *)(v_rip + 4955570)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 56) = result;
    v_rbx = 0;
    v_stack_mD5 = a3;
    v_stack_mD7 = a2;
    result = 0;
    v_stack_mD4 = 0;
    v_stack_mC8 = 0;
    *(unsigned __int64 *)(v_rsp - 56 - 64) = 0;
    *(unsigned int *)(v_rsp - 56 - 56) = 0;
    v_stack_mD0 = 0;
    v_stack_mC0 = 0;
    v_stack_mD6 = 0;
    v_stack_mD8 = 0;
    *(unsigned __int64 *)(v_rsp - 56 - 32) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 56 - 112) = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 56 - 16) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 56 - 96) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 56 - 80) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 56 - 48) = v_xmm0;
    if (a1 == 0) goto loc_00950BE2;
    if (*(unsigned __int64 *)(a1 + 8) == 0) goto loc_00950BE2;
    if ((unsigned __int16)(*(unsigned __int16 *)(a1)) == 0) goto loc_00950BE2;
    if (((unsigned __int16)(*(unsigned __int16 *)(a1 + 2))) < ((unsigned __int16)(v_rbx + 2))) goto loc_00950A99;
    if (((unsigned __int16)(*(unsigned __int16 *)(a1))) > ((unsigned __int16)(*(unsigned __int16 *)(a1 + 2)))) goto loc_00950BE2;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8))) == 0) goto loc_00950C03;
    if (((unsigned __int16)(*(unsigned __int16 *)(a1))) != ((unsigned __int16)(*(unsigned __int16 *)(a1 + 2)))) goto loc_00950A4B;
    result = ((unsigned int)((unsigned int)(*(unsigned __int16 *)(a1)))) >> (1);
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + result * 2 - 2)) == 0) goto loc_00950C03;
loc_00950A4B:
    result = (*(unsigned __int16 *)(a1 + 2)) - (v_rbx + 2);
    if ((*(unsigned __int16 *)(a1)) <= result) goto loc_00950BEC;
loc_00950A5A:
    a2 = (*(unsigned __int16 *)(a1)) + (v_rbx + 2);
    result = ExAllocatePool2(256, a2, (unsigned int)(0x75737050ULL), v_rbx + 2);
    if (result == 0) goto loc_00950BD8;
    result = memcpy(result, *(unsigned __int64 *)(a1 + 8), *(unsigned __int16 *)(a1), v_rbx + 2);
    result = (*(unsigned __int16 *)(a1)) >> (1);
    a1 = 0;
    *(unsigned __int16 *)(result + result * 2) = 0;
loc_00950A99:
    result = CmGetDeviceInterfaceClassGuid(a1, result, v_rsp - 56 - 16, v_rbx + 2);
    if (sign_flag) goto loc_00950B4B;
    result = IopBuildGlobalSymbolicLinkString(0, v_rsp - 56 - 112, v_rsp - 56 - 16, v_rbx + 2);
    if (sign_flag) goto loc_00950B4B;
    result = ExAllocatePool2(256, 400, (unsigned int)(0x20207050ULL), v_rbx + 2);
    a1 = 0;
    *(unsigned __int64 *)(v_rsp - 56 - 128) = result;
    if (result == 0) goto loc_00950BD8;
    v_stack_mE8 = 0;
    v_stack_mF0 = v_stack_mC0;
    v_stack_mF8 = 400;
    v_stack_m100 = result;
    a4 = 0;
    v_stack_m108 = v_stack_mD0;
    v_stack_m110 = v_rip - 9696912;
    v_stack_m118 = 0;
    result = PnpGetObjectProperty(*(unsigned __int64 *)(v_rip + 5331047), result, a1 + 3, a4);
    if (((unsigned int)(result)) == 0xC0000225ULL) goto loc_00950C0B;
    if (!sign_flag) goto loc_00950DC6;
loc_00950B4B:
    if (*(unsigned __int64 *)(v_rsp - 56 - 104) != 0) {
        result = ExFreePool(*(unsigned __int64 *)(v_rsp - 56 - 104), result, a1 + 3, a4);
        *(unsigned __int64 *)(v_rsp - 56 - 112) = v_xmm0;
    }
    result = PnpUnicodeStringToWstrFree(result, 0, a1 + 3, a4);
    if (0 != 0) {
        a2 = 0x49706E50ULL;
        a1 = 0;
        result = ObfDereferenceObjectWithTag(a1, a2, a1 + 3, a4);
    }
    if (0 != 0) {
        a2 = 0;
        a1 = 0;
        result = ExFreePoolWithTag(a1, a2, a1 + 3, a4);
    }
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, a1 + 3, a4);
    }
    if (0 != 0) {
        a1 = 0;
        result = PiDmObjectRelease(a1, a2, a1 + 3, a4);
    }
    a1 = (*(unsigned __int64 *)(v_rsp - 56)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a1 + 3, a4);
    return result;
loc_00950BD8:
    goto loc_00950B4B;
loc_00950BE2:
    goto loc_00950B4B;
loc_00950BEC:
    result = (0) >> (1);
    if ((*(unsigned __int16 *)(a1 + result * 2 - 2)) == ((unsigned __int16)((unsigned int)(0xC000000DULL)))) goto loc_00950C03;
    if ((*(unsigned __int16 *)(a1 + result * 2)) != ((unsigned __int16)((unsigned int)(0xC000000DULL)))) goto loc_00950A5A;
loc_00950C03:
    goto loc_00950A99;
loc_00950C0B:
    goto loc_00950B4B;
loc_00950C15:
    result = RtlInitUnicodeString(v_rsp - 56 - 32, 0, a1 + 3, a4);
    result = PiDmAddCacheReferenceForObject(3, a1, v_stack_mA0, a4);
    if (sign_flag) goto loc_00950B4B;
    result = CmpLockSiloKeyLockTrackerExclusive(v_stack_mA0, a1, v_stack_mA0, a4);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_mA0 + 32)))) & (1)) == 0) goto loc_00950DBF;
    v_r13 = 0;
    if ((*(unsigned __int64 *)(v_stack_mA0 + 40)) != 0) goto loc_00950D2C;
    *(unsigned int *)(v_rsp - 56 - 96) = 48;
    *(unsigned __int64 *)(v_rsp - 56 - 80) = v_rsp - 56 - 112;
    *(unsigned __int64 *)(v_rsp - 56 - 64) = *(unsigned __int64 *)(v_rip + 6852137);
    *(unsigned __int64 *)(v_rsp - 56 - 88) = 0;
    *(unsigned int *)(v_rsp - 56 - 72) = 576;
    *(unsigned __int64 *)(v_rsp - 56 - 56) = 0;
    result = ZwOpenSymbolicLinkObject(v_stack_mA0 + 40, (unsigned int)(0xF0001ULL), v_rsp - 56 - 96, a4);
    v_rbx = (unsigned int)((unsigned int)(result));
    if (((unsigned int)(result)) == 0xC0000034ULL) {
        a4 = v_rsp - 56 - 32;
        a2 = 0xF0001ULL;
        a3 = v_rsp - 56 - 96;
        a1 = v_stack_mA0 + 40;
        result = ZwCreateSymbolicLinkObject(a1, a2, a3, a4);
        v_rbx = (unsigned int)(result);
    }
    if (!(sign_flag)) {
        v_stack_mAE = 1;
    }
    result = PiDmObjectReleaseLock(v_stack_mA0, a2, a3, a4);
    result = 0;
    if (v_stack_mAE != 0) {
        a3 = 0;
        result = v_rip - 9693714;
        a1 = v_rip - 9686726;
        a3 = a1;
        a2 = v_rsp - 56 - 16;
        if (v_stack_mAF == 0) { a1 = result; }
        result = PnpSetDeviceClassChange(a1, a2, a3, a4);
        a2 = a1;
        result = PnpRaiseNtPlugPlayInterfacePropertyChangeEvent(a1, a2, a3, a4);
    }
    if ((unsigned __int8)(v_stack_mB0) == 0) goto loc_00950B4B;
    result = PiDmRemoveCacheReferenceForObject(3, a1, a3, a4);
    goto loc_00950B4B;
loc_00950D2C:
    goto loc_00950D9B;
loc_00950D33:
    result = PiDmObjectManagerAcquireSharedLock(v_rip + 6531684, a1, a3, a4);
    result = PiDmLookupObject(v_rip + 6531669, a1, a3, a4);
    v_stack_mA0 = result;
    if (result == 0) goto loc_00950DB8;
loc_00950D69:
    result = PiDmObjectManagerReleaseLock(v_rip + 6531632, a1, a3, a4);
    if (sign_flag) goto loc_00950DA5;
    result = CmpLockSiloKeyLockTrackerExclusive(v_stack_mA0, a1, a3, a4);
    v_r13 = 0;
    if (*(unsigned __int64 *)(result + 40) == 0) goto loc_00950DAE;
    result = ZwClose(*(unsigned __int64 *)(result + 40), a1, a3, a4);
    *(unsigned __int64 *)(result + 40) = 0;
    v_stack_mAE = 1;
loc_00950D9B:
    v_stack_mB0 = 1;
    goto loc_00950CC8;
loc_00950DA5:
    goto loc_00950B4B;
loc_00950DAE:
    goto loc_00950CC8;
loc_00950DB8:
    goto loc_00950D69;
loc_00950DBF:
    goto loc_00950D9B;
loc_00950DC6:
    if (v_stack_mA8 != 18) goto loc_00950C0B;
    result = RtlInitUnicodeStringEx(v_rsp - 56 - 48, *(unsigned __int64 *)(v_rsp - 56 - 128), a3, a4);
    if (sign_flag) goto loc_00950B4B;
    result = PnpDeviceObjectFromDeviceInstanceWithTag(v_rsp - 56 - 48, (unsigned int)(0x49706E50ULL), a3, a4);
    a1 = 0;
    *(unsigned __int64 *)(v_rsp - 56 - 120) = result;
    if (result == 0) goto loc_00950EF2;
    if ((unsigned __int8)(v_stack_mAF) != 0) goto loc_00950EA7;
    a1 = 0;
loc_00950E23:
    if (v_stack_mAD != 0) goto loc_00950EBF;
loc_00950E2D:
    if ((unsigned __int8)(v_stack_mAF) == 0) goto loc_00950D33;
    v_stack_mAC = 512;
loc_00950E3D:
    if (0 != 0) goto loc_00950F0E;
loc_00950E46:
    result = ExAllocatePool2(256, (unsigned int)(v_stack_mAC), (unsigned int)(0x20207050ULL), a4);
    if (result == 0) goto loc_00950BD8;
    v_stack_mF0 = v_stack_mAC;
    result = IoGetDeviceProperty(result, 11, (unsigned int)(v_stack_mAC), result);
    if (((unsigned int)(result)) == 0xC0000023ULL) goto loc_00950E3D;
    a1 = 0;
    if (sign_flag) goto loc_00950B4B;
    if (v_stack_mAC == 0) goto loc_00950B4B;
    goto loc_00950C15;
loc_00950EA7:
    result = PipCanEnableInterfaces(a1, 11, (unsigned int)(v_stack_mAC), result);
    a1 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_00950C0B;
    goto loc_00950E23;
loc_00950EBF:
    if ((unsigned int)(v_stack_mAC) == 0) goto loc_00950E2D;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 312) + 32)))) & (16)) != 0) goto loc_00950EDE;
    a1 = 0;
    goto loc_00950E2D;
loc_00950EDE:
    if ((unsigned __int8)(v_stack_mAF) != 0) goto loc_00950F02;
    result = PiRemoveDeferredSetInterfaceState((unsigned int)(v_stack_mAC), 0, (unsigned int)(v_stack_mAC), result);
    goto loc_00950B4B;
loc_00950EF2:
    if (0 != 0) goto loc_00950C0B;
    goto loc_00950E23;
loc_00950F02:
    result = PiDeferSetInterfaceState((unsigned int)(v_stack_mAC), 0, (unsigned int)(v_stack_mAC), result);
    goto loc_00950B4B;
loc_00950F0E:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, (unsigned int)(v_stack_mAC), result);
    goto loc_00950E46;
}
```

## 5. (Beta) C Style

```c
int64_t IopProcessSetInterfaceState(void *Arg1, uint8_t Arg2, uint8_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m28;
    uint64_t v_stack_mA0;
    uint32_t v_stack_mA8;
    uint32_t v_stack_mAC;
    uint8_t v_stack_mAD;
    uint8_t v_stack_mAE;
    uint8_t v_stack_mAF;
    uint8_t v_stack_mB0;
    uint32_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint32_t v_stack_mD0;
    uint32_t v_stack_mD4;
    uint8_t v_stack_mD5;
    uint8_t v_stack_mD6;
    uint8_t v_stack_mD7;
    uint8_t v_stack_mD8;
    uint32_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint32_t v_stack_mF8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (272);
    result = (*(uint64_t *)(v_rip + 0x4B9DB2)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x38) = result;
    local_rbx = 0;
    v_stack_mD5 = Arg3;
    v_stack_mD7 = Arg2;
    result = 0;
    v_stack_mD4 = 0;
    v_stack_mC8 = 0;
    *(uint64_t *)(local_rsp - 0x38 - 0x40) = 0;
    *(uint32_t *)(local_rsp - 0x38 - 0x38) = 0;
    v_stack_mD0 = 0;
    v_stack_mC0 = 0;
    v_stack_mD6 = 0;
    v_stack_mD8 = 0;
    *(uint64_t *)(local_rsp - 0x38 - 0x20) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x38 - 0x70) = v_xmm1;
    *(uint64_t *)(local_rsp - 0x38 - 0x10) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x38 - 0x60) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x38 - 0x50) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x38 - 0x30) = v_xmm0;
    if (Arg1 == NULL) goto loc_00950BE2;
    if (*(uint64_t *)(arg1 + 0x8) == 0) goto loc_00950BE2;
    if ((uint16_t)(*(uint16_t *)(arg1)) == 0) goto loc_00950BE2;
    if (((uint16_t)(*(uint16_t *)(arg1 + 0x2))) < ((uint16_t)(local_rbx + 2))) goto loc_00950A99;
    if (((uint16_t)(*(uint16_t *)(arg1))) > ((uint16_t)(*(uint16_t *)(arg1 + 0x2)))) goto loc_00950BE2;
    if ((*(uint16_t *)(*(uint64_t *)(arg1 + 0x8))) == 0) goto loc_00950C03;
    if (((uint16_t)(*(uint16_t *)(arg1))) != ((uint16_t)(*(uint16_t *)(arg1 + 0x2)))) goto loc_00950A4B;
    result = ((uint32_t)((uint32_t)(*(uint16_t *)(arg1)))) >> (1);
    if ((*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + result * 2 - 0x2)) == 0) goto loc_00950C03;
loc_00950A4B:
    result = (*(uint16_t *)(arg1 + 0x2)) - (local_rbx + 2);
    if ((*(uint16_t *)(arg1)) <= result) goto loc_00950BEC;
loc_00950A5A:
    Arg2 = (*(uint16_t *)(arg1)) + (local_rbx + 2);
    result = ExAllocatePool2(256, Arg2, (uint32_t)(0x75737050ULL), local_rbx + 2);
    if (result == 0) goto loc_00950BD8;
    result = memcpy(result, *(uint64_t *)(arg1 + 0x8), *(uint16_t *)(arg1), local_rbx + 2);
    result = (*(uint16_t *)(arg1)) >> (1);
    Arg1 = 0;
    *(uint16_t *)(result + result * 2) = 0;
loc_00950A99:
    result = CmGetDeviceInterfaceClassGuid(Arg1, result, local_rsp - 56 - 16, local_rbx + 2);
    if (sign_flag) goto loc_00950B4B;
    result = IopBuildGlobalSymbolicLinkString(0, local_rsp - 56 - 112, local_rsp - 56 - 16, local_rbx + 2);
    if (sign_flag) goto loc_00950B4B;
    result = ExAllocatePool2(256, 400, (uint32_t)(0x20207050ULL), local_rbx + 2);
    Arg1 = 0;
    *(uint64_t *)(local_rsp - 0x38 - 0x80) = result;
    if (result == 0) goto loc_00950BD8;
    v_stack_mE8 = 0;
    v_stack_mF0 = v_stack_mC0;
    v_stack_mF8 = 400;
    v_stack_m100 = result;
    a4 = 0;
    v_stack_m108 = v_stack_mD0;
    v_stack_m110 = v_rip - 9696912;
    v_stack_m118 = 0;
    result = PnpGetObjectProperty(*(uint64_t *)(v_rip + 0x515867), result, Arg1 + 3, a4);
    if (((uint32_t)(result)) == 0xC0000225ULL) goto loc_00950C0B;
    if (!sign_flag) goto loc_00950DC6;
loc_00950B4B:
    if (*(uint64_t *)(local_rsp - 0x38 - 0x68) != 0) {
        result = ExFreePool(*(uint64_t *)(local_rsp - 0x38 - 0x68), result, Arg1 + 3, a4);
        *(uint64_t *)(local_rsp - 0x38 - 0x70) = v_xmm0;
    }
    result = PnpUnicodeStringToWstrFree(result, 0, Arg1 + 3, a4);
    if (0 != 0) {
        Arg2 = 0x49706E50ULL;
        Arg1 = 0;
        result = ObfDereferenceObjectWithTag(Arg1, Arg2, Arg1 + 3, a4);
    }
    if (0 != 0) {
        Arg2 = 0;
        Arg1 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg1 + 3, a4);
    }
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg1 + 3, a4);
    }
    if (0 != 0) {
        Arg1 = 0;
        result = PiDmObjectRelease(Arg1, Arg2, Arg1 + 3, a4);
    }
    Arg1 = (*(uint64_t *)(local_rsp - 0x38)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg1 + 3, a4);
    return result;
loc_00950BD8:
    goto loc_00950B4B;
loc_00950BE2:
    goto loc_00950B4B;
loc_00950BEC:
    result = (0) >> (1);
    if ((*(uint16_t *)(arg1 + result * 2 - 0x2)) == ((uint16_t)((uint32_t)(0xC000000DULL)))) goto loc_00950C03;
    if ((*(uint16_t *)(arg1 + result * 2)) != ((uint16_t)((uint32_t)(0xC000000DULL)))) goto loc_00950A5A;
loc_00950C03:
    goto loc_00950A99;
loc_00950C0B:
    goto loc_00950B4B;
loc_00950C15:
    result = RtlInitUnicodeString(local_rsp - 56 - 32, 0, Arg1 + 3, a4);
    result = PiDmAddCacheReferenceForObject(3, Arg1, v_stack_mA0, a4);
    if (sign_flag) goto loc_00950B4B;
    result = CmpLockSiloKeyLockTrackerExclusive(v_stack_mA0, Arg1, v_stack_mA0, a4);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_mA0 + 0x20)))) & (1)) == 0) goto loc_00950DBF;
    local_r13 = 0;
    if ((*(uint64_t *)(v_stack_mA0 + 0x28)) != 0) goto loc_00950D2C;
    *(uint32_t *)(local_rsp - 0x38 - 0x60) = 48;
    *(uint64_t *)(local_rsp - 0x38 - 0x50) = local_rsp - 56 - 112;
    *(uint64_t *)(local_rsp - 0x38 - 0x40) = *(uint64_t *)(v_rip + 0x688E29);
    *(uint64_t *)(local_rsp - 0x38 - 0x58) = 0;
    *(uint32_t *)(local_rsp - 0x38 - 0x48) = 576;
    *(uint64_t *)(local_rsp - 0x38 - 0x38) = 0;
    result = ZwOpenSymbolicLinkObject(v_stack_mA0 + 40, (uint32_t)(0xF0001ULL), local_rsp - 56 - 96, a4);
    local_rbx = (uint32_t)((uint32_t)(result));
    if (((uint32_t)(result)) == 0xC0000034ULL) {
        a4 = local_rsp - 56 - 32;
        Arg2 = 0xF0001ULL;
        Arg3 = local_rsp - 56 - 96;
        Arg1 = v_stack_mA0 + 40;
        result = ZwCreateSymbolicLinkObject(Arg1, Arg2, Arg3, a4);
        local_rbx = (uint32_t)(result);
    }
    if (!(sign_flag)) {
        v_stack_mAE = 1;
    }
    result = PiDmObjectReleaseLock(v_stack_mA0, Arg2, Arg3, a4);
    result = 0;
    if (v_stack_mAE != 0) {
        Arg3 = 0;
        result = v_rip - 9693714;
        Arg1 = v_rip - 9686726;
        Arg3 = Arg1;
        Arg2 = local_rsp - 56 - 16;
        if (v_stack_mAF == 0) { Arg1 = result; }
        result = PnpSetDeviceClassChange(Arg1, Arg2, Arg3, a4);
        Arg2 = Arg1;
        result = PnpRaiseNtPlugPlayInterfacePropertyChangeEvent(Arg1, Arg2, Arg3, a4);
    }
    if ((uint8_t)(v_stack_mB0) == 0) goto loc_00950B4B;
    result = PiDmRemoveCacheReferenceForObject(3, Arg1, Arg3, a4);
    goto loc_00950B4B;
loc_00950D2C:
    goto loc_00950D9B;
loc_00950D33:
    result = PiDmObjectManagerAcquireSharedLock(v_rip + 6531684, Arg1, Arg3, a4);
    result = PiDmLookupObject(v_rip + 6531669, Arg1, Arg3, a4);
    v_stack_mA0 = result;
    if (result == 0) goto loc_00950DB8;
loc_00950D69:
    result = PiDmObjectManagerReleaseLock(v_rip + 6531632, Arg1, Arg3, a4);
    if (sign_flag) goto loc_00950DA5;
    result = CmpLockSiloKeyLockTrackerExclusive(v_stack_mA0, Arg1, Arg3, a4);
    local_r13 = 0;
    if (*(uint64_t *)(result + 0x28) == 0) goto loc_00950DAE;
    result = ZwClose(*(uint64_t *)(result + 0x28), Arg1, Arg3, a4);
    *(uint64_t *)(result + 0x28) = 0;
    v_stack_mAE = 1;
loc_00950D9B:
    v_stack_mB0 = 1;
    goto loc_00950CC8;
loc_00950DA5:
    goto loc_00950B4B;
loc_00950DAE:
    goto loc_00950CC8;
loc_00950DB8:
    goto loc_00950D69;
loc_00950DBF:
    goto loc_00950D9B;
loc_00950DC6:
    if (v_stack_mA8 != 18) goto loc_00950C0B;
    result = RtlInitUnicodeStringEx(local_rsp - 56 - 48, *(uint64_t *)(local_rsp - 0x38 - 0x80), Arg3, a4);
    if (sign_flag) goto loc_00950B4B;
    result = PnpDeviceObjectFromDeviceInstanceWithTag(local_rsp - 56 - 48, (uint32_t)(0x49706E50ULL), Arg3, a4);
    Arg1 = 0;
    *(uint64_t *)(local_rsp - 0x38 - 0x78) = result;
    if (result == 0) goto loc_00950EF2;
    if ((uint8_t)(v_stack_mAF) != 0) goto loc_00950EA7;
    Arg1 = 0;
loc_00950E23:
    if (v_stack_mAD != 0) goto loc_00950EBF;
loc_00950E2D:
    if ((uint8_t)(v_stack_mAF) == 0) goto loc_00950D33;
    v_stack_mAC = 512;
loc_00950E3D:
    if (0 != 0) goto loc_00950F0E;
loc_00950E46:
    result = ExAllocatePool2(256, (uint32_t)(v_stack_mAC), (uint32_t)(0x20207050ULL), a4);
    if (result == 0) goto loc_00950BD8;
    v_stack_mF0 = v_stack_mAC;
    result = IoGetDeviceProperty(result, 11, (uint32_t)(v_stack_mAC), result);
    if (((uint32_t)(result)) == 0xC0000023ULL) goto loc_00950E3D;
    Arg1 = 0;
    if (sign_flag) goto loc_00950B4B;
    if (v_stack_mAC == 0) goto loc_00950B4B;
    goto loc_00950C15;
loc_00950EA7:
    result = PipCanEnableInterfaces(Arg1, 11, (uint32_t)(v_stack_mAC), result);
    Arg1 = 0;
    if ((uint8_t)(result) == 0) goto loc_00950C0B;
    goto loc_00950E23;
loc_00950EBF:
    if ((uint32_t)(v_stack_mAC) == 0) goto loc_00950E2D;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x138) + 0x20)))) & (16)) != 0) goto loc_00950EDE;
    Arg1 = 0;
    goto loc_00950E2D;
loc_00950EDE:
    if ((uint8_t)(v_stack_mAF) != 0) goto loc_00950F02;
    result = PiRemoveDeferredSetInterfaceState((uint32_t)(v_stack_mAC), 0, (uint32_t)(v_stack_mAC), result);
    goto loc_00950B4B;
loc_00950EF2:
    if (0 != 0) goto loc_00950C0B;
    goto loc_00950E23;
loc_00950F02:
    result = PiDeferSetInterfaceState((uint32_t)(v_stack_mAC), 0, (uint32_t)(v_stack_mAC), result);
    goto loc_00950B4B;
loc_00950F0E:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, (uint32_t)(v_stack_mAC), result);
    goto loc_00950E46;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `16` | `R` |
| `Arg1` | `+ 0x2` | `16` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00950964&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
