# IoBuildPoDeviceNotifyList

- RVA: `0x00B78B0C`–`0x00B79197` (길이 `1,675` bytes)
- VA: `0x0000000140B78B0C`
- 실행 섹션: `PAGELK`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000AF498`
- 디코드: `455`개 명령, `1,675/1,675` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **19**; 고유 호출 대상: **13**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00B78B60` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00B78C05` → [IoGetAttachedDeviceReference](../../text/41/IoGetAttachedDeviceReference_function_0041D940.md) (function, `0x0041D940`)
- `0x00B78C12` → [IopCaptureObjectName](IopCaptureObjectName_function_00B791A0.md) (function, `0x00B791A0`)
- `0x00B78C1F` → [IopCaptureObjectName](IopCaptureObjectName_function_00B791A0.md) (function, `0x00B791A0`)
- `0x00B78C2C` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x00B78C3D` → [IopCheckDeviceFlags](IopCheckDeviceFlags_function_00B79250.md) (function, `0x00B79250`)
- `0x00B78E66` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x00B78E82` → [IoGetLowerDeviceObjectWithTag](../../text/27/IoGetLowerDeviceObjectWithTag_function_00272660.md) (function, `0x00272660`)
- `0x00B78E92` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00B78FCD` → [IopIsNotifyInBroadcast](IopIsNotifyInBroadcast_function_00B792CC.md) (function, `0x00B792CC`)
- `0x00B79006` → [IopIsNotifyInBroadcast](IopIsNotifyInBroadcast_function_00B792CC.md) (function, `0x00B792CC`)
- `0x00B79083` → [IopIsNotifyInBroadcast](IopIsNotifyInBroadcast_function_00B792CC.md) (function, `0x00B792CC`)
- `0x00B79099` → [IopFreePoDeviceNotifyListHead](IopFreePoDeviceNotifyListHead_function_00B79300.md) (function, `0x00B79300`)
- `0x00B790D9` → [PnpPowerStateTransitionWatchdogPushRecord](../../page/A9/PnpPowerStateTransitionWatchdogPushRecord_function_00A95CCC.md) (function, `0x00A95CCC`)
- `0x00B790E0` → [PnpLockDeviceActionQueue](../../text/4A/PnpLockDeviceActionQueue_function_004A4388.md) (function, `0x004A4388`)
- `0x00B790ED` → [PnpPowerStateTransitionWatchdogPopRecord](../../page/AD/PnpPowerStateTransitionWatchdogPopRecord_function_00AD19E4.md) (function, `0x00AD19E4`)
- `0x00B79106` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00B79113` → [IopCheckDeviceFlags](IopCheckDeviceFlags_function_00B79250.md) (function, `0x00B79250`)
- `0x00B79178` → [IopIsNotifyInBroadcast](IopIsNotifyInBroadcast_function_00B792CC.md) (function, `0x00B792CC`)

### Direct callers
- [PopBuildDeviceNotifyList](PopBuildDeviceNotifyList_function_00B789E8.md) at `0x00B78A87`

### Static image references
- `0x00B78BAA` → RVA `0x00F8C438` (`.data`; read)
- `0x00B790A3` → RVA `0x00F8C418` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **10**
  - `0x00B78B60` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGELK` → `.text`)
  - `0x00B78C05` → [IoGetAttachedDeviceReference](../../text/41/IoGetAttachedDeviceReference_function_0041D940.md) (`PAGELK` → `.text`)
  - `0x00B78C2C` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGELK` → `.text`)
  - `0x00B78E66` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (`PAGELK` → `.text`)
  - `0x00B78E82` → [IoGetLowerDeviceObjectWithTag](../../text/27/IoGetLowerDeviceObjectWithTag_function_00272660.md) (`PAGELK` → `.text`)
  - `0x00B78E92` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGELK` → `.text`)
  - `0x00B790D9` → [PnpPowerStateTransitionWatchdogPushRecord](../../page/A9/PnpPowerStateTransitionWatchdogPushRecord_function_00A95CCC.md) (`PAGELK` → `PAGE`)
  - `0x00B790E0` → [PnpLockDeviceActionQueue](../../text/4A/PnpLockDeviceActionQueue_function_004A4388.md) (`PAGELK` → `.text`)
  - `0x00B790ED` → [PnpPowerStateTransitionWatchdogPopRecord](../../page/AD/PnpPowerStateTransitionWatchdogPopRecord_function_00AD19E4.md) (`PAGELK` → `PAGE`)
  - `0x00B79106` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGELK` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x00B790D3` → [sub_00B8075E](../B8/Unknown_function_00B8075E.md) (`tail-transfer`)
  - `0x00B7917F` → [sub_00B8075E + 0xB](../B8/Unknown_function_00B8075E.md) (`tail-transfer`)
  - `0x00B79189` → [sub_00B8075E + 0xB](../B8/Unknown_function_00B8075E.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B78B0C  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00B78B11  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
00B78B16  48 89 7C 24 18                  mov qword ptr [rsp + 0x18], rdi
00B78B1B  55                              push rbp
00B78B1C  41 56                           push r14
00B78B1E  41 57                           push r15
00B78B20  48 8B EC                        mov rbp, rsp
00B78B23  48 83 EC 40                     sub rsp, 0x40
00B78B27  48 8D 45 E0                     lea rax, [rbp - 0x20]
00B78B2B  8B FA                           mov edi, edx
00B78B2D  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
00B78B31  48 8D 45 E0                     lea rax, [rbp - 0x20]
00B78B35  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
00B78B39  48 8D 45 F0                     lea rax, [rbp - 0x10]
00B78B3D  48 89 45 F8                     mov qword ptr [rbp - 8], rax
00B78B41  48 8D 45 F0                     lea rax, [rbp - 0x10]
00B78B45  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00B78B49  4C 8B F9                        mov r15, rcx
00B78B4C  F6 C2 01                        test dl, 1
00B78B4F  0F 84 7A 05 00 00               je 0x140b790cf
00B78B55  33 D2                           xor edx, edx
00B78B57  41 B8 80 01 00 00               mov r8d, 0x180
00B78B5D  49 8B CF                        mov rcx, r15
00B78B60  E8 DB E0 B4 FF                  call 0x1406c6c40
00B78B65  49 8D 4F 30                     lea rcx, [r15 + 0x30]
00B78B69  41 89 BF 78 01 00 00            mov dword ptr [r15 + 0x178], edi
00B78B70  BA 05 00 00 00                  mov edx, 5
00B78B75  48 8D 41 E8                     lea rax, [rcx - 0x18]
00B78B79  48 89 41 F0                     mov qword ptr [rcx - 0x10], rax
00B78B7D  48 89 00                        mov qword ptr [rax], rax
00B78B80  48 8D 41 F8                     lea rax, [rcx - 8]
00B78B84  48 89 01                        mov qword ptr [rcx], rax
00B78B87  48 89 00                        mov qword ptr [rax], rax
00B78B8A  48 8D 41 08                     lea rax, [rcx + 8]
00B78B8E  48 89 41 10                     mov qword ptr [rcx + 0x10], rax
00B78B92  48 89 00                        mov qword ptr [rax], rax
00B78B95  48 8D 41 18                     lea rax, [rcx + 0x18]
00B78B99  48 89 41 20                     mov qword ptr [rcx + 0x20], rax
00B78B9D  48 8D 49 48                     lea rcx, [rcx + 0x48]
00B78BA1  48 89 00                        mov qword ptr [rax], rax
00B78BA4  48 83 EA 01                     sub rdx, 1
00B78BA8  75 CB                           jne 0x140b78b75
00B78BAA  48 8B 1D 87 38 41 00            mov rbx, qword ptr [rip + 0x413887]
00B78BB1  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00B78BB5  EB 07                           jmp 0x140b78bbe
00B78BB7  48 8B D8                        mov rbx, rax
00B78BBA  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00B78BBE  48 85 C0                        test rax, rax
00B78BC1  75 F4                           jne 0x140b78bb7
00B78BC3  EB 0C                           jmp 0x140b78bd1
00B78BC5  48 8B D8                        mov rbx, rax
00B78BC8  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00B78BCC  48 85 C0                        test rax, rax
00B78BCF  75 F4                           jne 0x140b78bc5
00B78BD1  48 3B 1D 60 38 41 00            cmp rbx, qword ptr [rip + 0x413860]
00B78BD8  0F 84 D0 00 00 00               je 0x140b78cae
00B78BDE  48 8D BB A0 00 00 00            lea rdi, [rbx + 0xa0]
00B78BE5  83 67 58 00                     and dword ptr [rdi + 0x58], 0
00B78BE9  83 67 5C 00                     and dword ptr [rdi + 0x5c], 0
00B78BED  83 67 60 00                     and dword ptr [rdi + 0x60], 0
00B78BF1  83 67 64 00                     and dword ptr [rdi + 0x64], 0
00B78BF5  C6 47 38 00                     mov byte ptr [rdi + 0x38], 0
00B78BF9  48 8B 43 20                     mov rax, qword ptr [rbx + 0x20]
00B78BFD  48 89 47 40                     mov qword ptr [rdi + 0x40], rax
00B78C01  48 8B 4B 20                     mov rcx, qword ptr [rbx + 0x20]
00B78C05  E8 36 4D 8A FF                  call 0x14041d940
00B78C0A  48 89 47 30                     mov qword ptr [rdi + 0x30], rax
00B78C0E  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00B78C12  E8 89 05 00 00                  call 0x140b791a0
00B78C17  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
00B78C1B  48 89 47 50                     mov qword ptr [rdi + 0x50], rax
00B78C1F  E8 7C 05 00 00                  call 0x140b791a0
00B78C24  48 8B 4F 40                     mov rcx, qword ptr [rdi + 0x40]
00B78C28  48 89 47 48                     mov qword ptr [rdi + 0x48], rax
00B78C2C  E8 EF 6D 69 FF                  call 0x14020fa20
00B78C31  BA 00 20 00 00                  mov edx, 0x2000
00B78C36  C6 47 38 00                     mov byte ptr [rdi + 0x38], 0
00B78C3A  48 8B CF                        mov rcx, rdi
00B78C3D  E8 0E 06 00 00                  call 0x140b79250
00B78C42  84 C0                           test al, al
00B78C44  74 04                           je 0x140b78c4a
00B78C46  80 4F 38 02                     or byte ptr [rdi + 0x38], 2
00B78C4A  48 8B 05 E7 37 41 00            mov rax, qword ptr [rip + 0x4137e7]
00B78C51  48 8D 4B 10                     lea rcx, [rbx + 0x10]
00B78C55  48 39 01                        cmp qword ptr [rcx], rax
00B78C58  74 11                           je 0x140b78c6b
00B78C5A  48 8B 1B                        mov rbx, qword ptr [rbx]
00B78C5D  48 85 DB                        test rbx, rbx
00B78C60  74 30                           je 0x140b78c92
00B78C62  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00B78C66  E9 61 FF FF FF                  jmp 0x140b78bcc
00B78C6B  83 BB C0 01 00 00 00            cmp dword ptr [rbx + 0x1c0], 0
00B78C72  74 E6                           je 0x140b78c5a
00B78C74  8B 83 8C 01 00 00               mov eax, dword ptr [rbx + 0x18c]
00B78C7A  A8 04                           test al, 4
00B78C7C  75 DC                           jne 0x140b78c5a
00B78C7E  48 8B 45 E8                     mov rax, qword ptr [rbp - 0x18]
00B78C82  48 8D 55 E0                     lea rdx, [rbp - 0x20]
00B78C86  48 39 10                        cmp qword ptr [rax], rdx
00B78C89  74 0F                           je 0x140b78c9a
00B78C8B  B9 03 00 00 00                  mov ecx, 3
00B78C90  CD 29                           int 0x29
00B78C92  48 8B 19                        mov rbx, qword ptr [rcx]
00B78C95  E9 37 FF FF FF                  jmp 0x140b78bd1
00B78C9A  48 89 47 08                     mov qword ptr [rdi + 8], rax
00B78C9E  48 8D 55 E0                     lea rdx, [rbp - 0x20]
00B78CA2  48 89 17                        mov qword ptr [rdi], rdx
00B78CA5  48 89 38                        mov qword ptr [rax], rdi
00B78CA8  48 89 7D E8                     mov qword ptr [rbp - 0x18], rdi
00B78CAC  EB AC                           jmp 0x140b78c5a
00B78CAE  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
00B78CB2  48 8D 4D E0                     lea rcx, [rbp - 0x20]
00B78CB6  48 3B C1                        cmp rax, rcx
00B78CB9  74 67                           je 0x140b78d22
00B78CBB  48 8D 4D E0                     lea rcx, [rbp - 0x20]
00B78CBF  48 39 48 08                     cmp qword ptr [rax + 8], rcx
00B78CC3  75 C6                           jne 0x140b78c8b
00B78CC5  48 8B 08                        mov rcx, qword ptr [rax]
00B78CC8  48 39 41 08                     cmp qword ptr [rcx + 8], rax
00B78CCC  75 BD                           jne 0x140b78c8b
00B78CCE  48 89 4D E0                     mov qword ptr [rbp - 0x20], rcx
00B78CD2  48 8D 55 E0                     lea rdx, [rbp - 0x20]
00B78CD6  48 89 51 08                     mov qword ptr [rcx + 8], rdx
00B78CDA  48 8D 90 60 FF FF FF            lea rdx, [rax - 0xa0]
00B78CE1  80 48 38 01                     or byte ptr [rax + 0x38], 1
00B78CE5  48 8B C2                        mov rax, rdx
00B78CE8  48 8B 4A 08                     mov rcx, qword ptr [rdx + 8]
00B78CEC  EB 07                           jmp 0x140b78cf5
00B78CEE  48 8B C1                        mov rax, rcx
00B78CF1  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
00B78CF5  48 85 C9                        test rcx, rcx
00B78CF8  75 F4                           jne 0x140b78cee
00B78CFA  EB 0C                           jmp 0x140b78d08
00B78CFC  48 8B C1                        mov rax, rcx
00B78CFF  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
00B78D03  48 85 C9                        test rcx, rcx
00B78D06  75 F4                           jne 0x140b78cfc
00B78D08  48 3B C2                        cmp rax, rdx
00B78D0B  74 A1                           je 0x140b78cae
00B78D0D  80 88 D8 00 00 00 01            or byte ptr [rax + 0xd8], 1
00B78D14  48 8B 08                        mov rcx, qword ptr [rax]
00B78D17  48 85 C9                        test rcx, rcx
00B78D1A  75 E0                           jne 0x140b78cfc
00B78D1C  48 8B 40 10                     mov rax, qword ptr [rax + 0x10]
00B78D20  EB E6                           jmp 0x140b78d08
00B78D22  48 8B 15 0F 37 41 00            mov rdx, qword ptr [rip + 0x41370f]
00B78D29  45 32 D2                        xor r10b, r10b
00B78D2C  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
00B78D30  EB 07                           jmp 0x140b78d39
00B78D32  48 8B D0                        mov rdx, rax
00B78D35  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00B78D39  48 85 C0                        test rax, rax
00B78D3C  75 F4                           jne 0x140b78d32
00B78D3E  EB 14                           jmp 0x140b78d54
00B78D40  48 8B 02                        mov rax, qword ptr [rdx]
00B78D43  48 85 C0                        test rax, rax
00B78D46  74 5E                           je 0x140b78da6
00B78D48  48 8B D0                        mov rdx, rax
00B78D4B  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00B78D4F  48 85 C0                        test rax, rax
00B78D52  75 F4                           jne 0x140b78d48
00B78D54  48 8B 0D DD 36 41 00            mov rcx, qword ptr [rip + 0x4136dd]
00B78D5B  48 3B D1                        cmp rdx, rcx
00B78D5E  74 4C                           je 0x140b78dac
00B78D60  F6 82 D8 00 00 00 02            test byte ptr [rdx + 0xd8], 2
00B78D67  74 D7                           je 0x140b78d40
00B78D69  48 8B 4A 08                     mov rcx, qword ptr [rdx + 8]
00B78D6D  48 8B C2                        mov rax, rdx
00B78D70  EB 07                           jmp 0x140b78d79
00B78D72  48 8B C1                        mov rax, rcx
00B78D75  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
00B78D79  48 85 C9                        test rcx, rcx
00B78D7C  75 F4                           jne 0x140b78d72
00B78D7E  EB 0C                           jmp 0x140b78d8c
00B78D80  48 8B C1                        mov rax, rcx
00B78D83  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
00B78D87  48 85 C9                        test rcx, rcx
00B78D8A  75 F4                           jne 0x140b78d80
00B78D8C  48 3B C2                        cmp rax, rdx
00B78D8F  74 AF                           je 0x140b78d40
00B78D91  80 88 D8 00 00 00 02            or byte ptr [rax + 0xd8], 2
00B78D98  48 8B 08                        mov rcx, qword ptr [rax]
00B78D9B  48 85 C9                        test rcx, rcx
00B78D9E  75 E0                           jne 0x140b78d80
00B78DA0  48 8B 40 10                     mov rax, qword ptr [rax + 0x10]
00B78DA4  EB E6                           jmp 0x140b78d8c
00B78DA6  48 8B 52 10                     mov rdx, qword ptr [rdx + 0x10]
00B78DAA  EB A8                           jmp 0x140b78d54
00B78DAC  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
00B78DB0  EB 07                           jmp 0x140b78db9
00B78DB2  48 8B C8                        mov rcx, rax
00B78DB5  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00B78DB9  48 85 C0                        test rax, rax
00B78DBC  75 F4                           jne 0x140b78db2
00B78DBE  48 8B 3D 73 36 41 00            mov rdi, qword ptr [rip + 0x413673]
00B78DC5  48 3B CF                        cmp rcx, rdi
00B78DC8  74 32                           je 0x140b78dfc
00B78DCA  F6 81 D8 00 00 00 02            test byte ptr [rcx + 0xd8], 2
00B78DD1  75 2F                           jne 0x140b78e02
00B78DD3  48 8B 01                        mov rax, qword ptr [rcx]
00B78DD6  48 85 C0                        test rax, rax
00B78DD9  74 4C                           je 0x140b78e27
00B78DDB  48 8B C8                        mov rcx, rax
00B78DDE  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00B78DE2  48 85 C0                        test rax, rax
00B78DE5  75 F4                           jne 0x140b78ddb
00B78DE7  48 8B 3D 4A 36 41 00            mov rdi, qword ptr [rip + 0x41364a]
00B78DEE  48 3B CF                        cmp rcx, rdi
00B78DF1  75 D7                           jne 0x140b78dca
00B78DF3  45 84 D2                        test r10b, r10b
00B78DF6  0F 85 26 FF FF FF               jne 0x140b78d22
00B78DFC  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
00B78E00  EB 32                           jmp 0x140b78e34
00B78E02  4C 8D 81 B0 00 00 00            lea r8, [rcx + 0xb0]
00B78E09  49 8B 00                        mov rax, qword ptr [r8]
00B78E0C  49 3B C0                        cmp rax, r8
00B78E0F  74 C2                           je 0x140b78dd3
00B78E11  4C 8B 48 F8                     mov r9, qword ptr [rax - 8]
00B78E15  41 8A 51 38                     mov dl, byte ptr [r9 + 0x38]
00B78E19  F6 C2 02                        test dl, 2
00B78E1C  0F 84 D5 02 00 00               je 0x140b790f7
00B78E22  48 8B 00                        mov rax, qword ptr [rax]
00B78E25  EB E5                           jmp 0x140b78e0c
00B78E27  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
00B78E2B  EB BA                           jmp 0x140b78de7
00B78E2D  48 8B F8                        mov rdi, rax
00B78E30  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00B78E34  48 85 C0                        test rax, rax
00B78E37  75 F4                           jne 0x140b78e2d
00B78E39  4C 8B 0D F8 35 41 00            mov r9, qword ptr [rip + 0x4135f8]
00B78E40  49 3B F9                        cmp rdi, r9
00B78E43  74 73                           je 0x140b78eb8
00B78E45  4C 8D B7 A0 00 00 00            lea r14, [rdi + 0xa0]
00B78E4C  41 8A 46 38                     mov al, byte ptr [r14 + 0x38]
00B78E50  A8 02                           test al, 2
00B78E52  74 48                           je 0x140b78e9c
00B78E54  49 8B 76 30                     mov rsi, qword ptr [r14 + 0x30]
00B78E58  FE C0                           inc al
00B78E5A  48 8B CE                        mov rcx, rsi
00B78E5D  41 88 46 38                     mov byte ptr [r14 + 0x38], al
00B78E61  BA 50 6F 50 70                  mov edx, 0x70506f50
00B78E66  E8 A5 78 69 FF                  call 0x140210710
00B78E6B  48 85 F6                        test rsi, rsi
00B78E6E  74 2C                           je 0x140b78e9c
00B78E70  83 7E 48 07                     cmp dword ptr [rsi + 0x48], 7
00B78E74  BA 50 6F 50 70                  mov edx, 0x70506f50
00B78E79  48 8B CE                        mov rcx, rsi
00B78E7C  0F 84 84 02 00 00               je 0x140b79106
00B78E82  E8 D9 97 6F FF                  call 0x140272660
00B78E87  BA 50 6F 50 70                  mov edx, 0x70506f50
00B78E8C  48 8B CE                        mov rcx, rsi
00B78E8F  48 8B D8                        mov rbx, rax
00B78E92  E8 49 EA 77 FF                  call 0x1402f78e0
00B78E97  48 8B F3                        mov rsi, rbx
00B78E9A  EB CF                           jmp 0x140b78e6b
00B78E9C  48 8B 07                        mov rax, qword ptr [rdi]
00B78E9F  48 85 C0                        test rax, rax
00B78EA2  74 0E                           je 0x140b78eb2
00B78EA4  48 8B F8                        mov rdi, rax
00B78EA7  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00B78EAB  48 85 C0                        test rax, rax
00B78EAE  75 F4                           jne 0x140b78ea4
00B78EB0  EB 87                           jmp 0x140b78e39
00B78EB2  48 8B 7F 10                     mov rdi, qword ptr [rdi + 0x10]
00B78EB6  EB 81                           jmp 0x140b78e39
00B78EB8  49 8B 41 08                     mov rax, qword ptr [r9 + 8]
00B78EBC  45 32 D2                        xor r10b, r10b
00B78EBF  EB 07                           jmp 0x140b78ec8
00B78EC1  4C 8B C8                        mov r9, rax
00B78EC4  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00B78EC8  48 85 C0                        test rax, rax
00B78ECB  75 F4                           jne 0x140b78ec1
00B78ECD  EB 0C                           jmp 0x140b78edb
00B78ECF  4C 8B C8                        mov r9, rax
00B78ED2  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00B78ED6  48 85 C0                        test rax, rax
00B78ED9  75 F4                           jne 0x140b78ecf
00B78EDB  48 8B 05 56 35 41 00            mov rax, qword ptr [rip + 0x413556]
00B78EE2  4C 3B C8                        cmp r9, rax
00B78EE5  74 32                           je 0x140b78f19
00B78EE7  49 8B 49 10                     mov rcx, qword ptr [r9 + 0x10]
00B78EEB  48 3B C8                        cmp rcx, rax
00B78EEE  74 16                           je 0x140b78f06
00B78EF0  41 8A 91 D8 00 00 00            mov dl, byte ptr [r9 + 0xd8]
00B78EF7  48 8D 81 D8 00 00 00            lea rax, [rcx + 0xd8]
00B78EFE  38 10                           cmp byte ptr [rax], dl
00B78F00  0F 87 24 02 00 00               ja 0x140b7912a
00B78F06  4D 8B 09                        mov r9, qword ptr [r9]
00B78F09  4D 85 C9                        test r9, r9
00B78F0C  74 06                           je 0x140b78f14
00B78F0E  49 8B 41 08                     mov rax, qword ptr [r9 + 8]
00B78F12  EB C2                           jmp 0x140b78ed6
00B78F14  4C 8B C9                        mov r9, rcx
00B78F17  EB C2                           jmp 0x140b78edb
00B78F19  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00B78F1D  EB 07                           jmp 0x140b78f26
00B78F1F  48 8B C1                        mov rax, rcx
00B78F22  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
00B78F26  48 85 C9                        test rcx, rcx
00B78F29  75 F4                           jne 0x140b78f1f
00B78F2B  4C 8B 0D 06 35 41 00            mov r9, qword ptr [rip + 0x413506]
00B78F32  49 3B C1                        cmp rax, r9
00B78F35  74 38                           je 0x140b78f6f
00B78F37  48 8D 90 C0 00 00 00            lea rdx, [rax + 0xc0]
00B78F3E  48 8B 0A                        mov rcx, qword ptr [rdx]
00B78F41  48 3B CA                        cmp rcx, rdx
00B78F44  75 35                           jne 0x140b78f7b
00B78F46  48 8B 08                        mov rcx, qword ptr [rax]
00B78F49  48 85 C9                        test rcx, rcx
00B78F4C  74 27                           je 0x140b78f75
00B78F4E  48 8B C1                        mov rax, rcx
00B78F51  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
00B78F55  48 85 C9                        test rcx, rcx
00B78F58  75 F4                           jne 0x140b78f4e
00B78F5A  4C 8B 0D D7 34 41 00            mov r9, qword ptr [rip + 0x4134d7]
00B78F61  49 3B C1                        cmp rax, r9
00B78F64  75 D1                           jne 0x140b78f37
00B78F66  45 84 D2                        test r10b, r10b
00B78F69  0F 85 49 FF FF FF               jne 0x140b78eb8
00B78F6F  49 8B 41 08                     mov rax, qword ptr [r9 + 8]
00B78F73  EB 27                           jmp 0x140b78f9c
00B78F75  48 8B 40 10                     mov rax, qword ptr [rax + 0x10]
00B78F79  EB DF                           jmp 0x140b78f5a
00B78F7B  4C 8B 41 28                     mov r8, qword ptr [rcx + 0x28]
00B78F7F  44 8A 88 D8 00 00 00            mov r9b, byte ptr [rax + 0xd8]
00B78F86  45 38 48 38                     cmp byte ptr [r8 + 0x38], r9b
00B78F8A  0F 87 A5 01 00 00               ja 0x140b79135
00B78F90  48 8B 09                        mov rcx, qword ptr [rcx]
00B78F93  EB AC                           jmp 0x140b78f41
00B78F95  4C 8B C8                        mov r9, rax
00B78F98  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00B78F9C  48 85 C0                        test rax, rax
00B78F9F  75 F4                           jne 0x140b78f95
00B78FA1  EB 0C                           jmp 0x140b78faf
00B78FA3  4C 8B C8                        mov r9, rax
00B78FA6  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00B78FAA  48 85 C0                        test rax, rax
00B78FAD  75 F4                           jne 0x140b78fa3
00B78FAF  4C 3B 0D 82 34 41 00            cmp r9, qword ptr [rip + 0x413482]
00B78FB6  0F 84 D9 00 00 00               je 0x140b79095
00B78FBC  41 8B 8F 78 01 00 00            mov ecx, dword ptr [r15 + 0x178]
00B78FC3  4D 8D 91 A0 00 00 00            lea r10, [r9 + 0xa0]
00B78FCA  49 8B D2                        mov rdx, r10
00B78FCD  E8 FA 02 00 00                  call 0x140b792cc
00B78FD2  84 C0                           test al, al
00B78FD4  0F 84 67 01 00 00               je 0x140b79141
00B78FDA  41 0F B6 42 38                  movzx eax, byte ptr [r10 + 0x38]
00B78FDF  49 8D 79 10                     lea rdi, [r9 + 0x10]
00B78FE3  48 8D 0C C0                     lea rcx, [rax + rax*8]
00B78FE7  41 FF 44 CF 10                  inc dword ptr [r15 + rcx*8 + 0x10]
00B78FEC  48 8B 17                        mov rdx, qword ptr [rdi]
00B78FEF  48 3B 15 42 34 41 00            cmp rdx, qword ptr [rip + 0x413442]
00B78FF6  74 24                           je 0x140b7901c
00B78FF8  41 8B 8F 78 01 00 00            mov ecx, dword ptr [r15 + 0x178]
00B78FFF  48 81 C2 A0 00 00 00            add rdx, 0xa0
00B79006  E8 C1 02 00 00                  call 0x140b792cc
00B7900B  84 C0                           test al, al
00B7900D  74 0D                           je 0x140b7901c
00B7900F  41 FF 42 60                     inc dword ptr [r10 + 0x60]
00B79013  48 8B 07                        mov rax, qword ptr [rdi]
00B79016  FF 80 F8 00 00 00               inc dword ptr [rax + 0xf8]
00B7901C  49 8D 5A 20                     lea rbx, [r10 + 0x20]
00B79020  4C 8B 1B                        mov r11, qword ptr [rbx]
00B79023  4C 3B DB                        cmp r11, rbx
00B79026  0F 85 41 01 00 00               jne 0x140b7916d
00B7902C  49 8D 5A 10                     lea rbx, [r10 + 0x10]
00B79030  4C 8B 1B                        mov r11, qword ptr [rbx]
00B79033  4C 3B DB                        cmp r11, rbx
00B79036  75 40                           jne 0x140b79078
00B79038  41 0F B6 42 38                  movzx eax, byte ptr [r10 + 0x38]
00B7903D  48 8D 0C C5 03 00 00 00         lea rcx, [rax*8 + 3]
00B79045  48 03 C8                        add rcx, rax
00B79048  49 8D 04 CF                     lea rax, [r15 + rcx*8]
00B7904C  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00B79050  48 39 01                        cmp qword ptr [rcx], rax
00B79053  0F 85 32 FC FF FF               jne 0x140b78c8b
00B79059  49 89 02                        mov qword ptr [r10], rax
00B7905C  49 89 4A 08                     mov qword ptr [r10 + 8], rcx
00B79060  4C 89 11                        mov qword ptr [rcx], r10
00B79063  4C 89 50 08                     mov qword ptr [rax + 8], r10
00B79067  4D 8B 09                        mov r9, qword ptr [r9]
00B7906A  4D 85 C9                        test r9, r9
00B7906D  74 58                           je 0x140b790c7
00B7906F  49 8B 41 08                     mov rax, qword ptr [r9 + 8]
00B79073  E9 32 FF FF FF                  jmp 0x140b78faa
00B79078  49 8B 53 F8                     mov rdx, qword ptr [r11 - 8]
00B7907C  41 8B 8F 78 01 00 00            mov ecx, dword ptr [r15 + 0x178]
00B79083  E8 44 02 00 00                  call 0x140b792cc
00B79088  84 C0                           test al, al
00B7908A  0F 85 FE 00 00 00               jne 0x140b7918e
00B79090  4D 8B 1B                        mov r11, qword ptr [r11]
00B79093  EB 9E                           jmp 0x140b79033
00B79095  48 8D 4D F0                     lea rcx, [rbp - 0x10]
00B79099  E8 62 02 00 00                  call 0x140b79300
00B7909E  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00B790A3  48 8D 05 6E 33 41 00            lea rax, [rip + 0x41336e]
00B790AA  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
00B790AF  48 8B 7C 24 70                  mov rdi, qword ptr [rsp + 0x70]
00B790B4  49 89 47 08                     mov qword ptr [r15 + 8], rax
00B790B8  41 C6 07 01                     mov byte ptr [r15], 1
00B790BC  48 83 C4 40                     add rsp, 0x40
00B790C0  41 5F                           pop r15
00B790C2  41 5E                           pop r14
00B790C4  5D                              pop rbp
00B790C5  C3                              ret
00B790C6  CC                              int3
00B790C7  4C 8B 0F                        mov r9, qword ptr [rdi]
00B790CA  E9 E0 FE FF FF                  jmp 0x140b78faf
00B790CF  40 F6 C7 04                     test dil, 4
00B790D3  0F 84 85 76 00 00               je 0x140b8075e
00B790D9  E8 EE CB F1 FF                  call 0x140a95ccc
00B790DE  8B D8                           mov ebx, eax
00B790E0  E8 A3 B2 92 FF                  call 0x1404a4388
00B790E5  85 DB                           test ebx, ebx
00B790E7  0F 88 68 FA FF FF               js 0x140b78b55
00B790ED  E8 F2 88 F5 FF                  call 0x140ad19e4
00B790F2  E9 5E FA FF FF                  jmp 0x140b78b55
00B790F7  80 CA 02                        or dl, 2
00B790FA  41 B2 01                        mov r10b, 1
00B790FD  41 88 51 38                     mov byte ptr [r9 + 0x38], dl
00B79101  E9 1C FD FF FF                  jmp 0x140b78e22
00B79106  E8 D5 E7 77 FF                  call 0x1402f78e0
00B7910B  BA 00 01 00 00                  mov edx, 0x100
00B79110  49 8B CE                        mov rcx, r14
00B79113  E8 38 01 00 00                  call 0x140b79250
00B79118  84 C0                           test al, al
00B7911A  0F 84 7C FD FF FF               je 0x140b78e9c
00B79120  41 C6 46 38 02                  mov byte ptr [r14 + 0x38], 2
00B79125  E9 72 FD FF FF                  jmp 0x140b78e9c
00B7912A  88 10                           mov byte ptr [rax], dl
00B7912C  49 8B 49 10                     mov rcx, qword ptr [r9 + 0x10]
00B79130  E9 D1 FD FF FF                  jmp 0x140b78f06
00B79135  41 B2 01                        mov r10b, 1
00B79138  45 88 48 38                     mov byte ptr [r8 + 0x38], r9b
00B7913C  E9 4F FE FF FF                  jmp 0x140b78f90
00B79141  48 8B 45 F8                     mov rax, qword ptr [rbp - 8]
00B79145  48 8D 4D F0                     lea rcx, [rbp - 0x10]
00B79149  48 39 08                        cmp qword ptr [rax], rcx
00B7914C  0F 85 39 FB FF FF               jne 0x140b78c8b
00B79152  49 89 42 08                     mov qword ptr [r10 + 8], rax
00B79156  48 8D 4D F0                     lea rcx, [rbp - 0x10]
00B7915A  49 89 0A                        mov qword ptr [r10], rcx
00B7915D  49 8D 79 10                     lea rdi, [r9 + 0x10]
00B79161  4C 89 10                        mov qword ptr [rax], r10
00B79164  4C 89 55 F8                     mov qword ptr [rbp - 8], r10
00B79168  E9 FA FE FF FF                  jmp 0x140b79067
00B7916D  49 8B 53 28                     mov rdx, qword ptr [r11 + 0x28]
00B79171  41 8B 8F 78 01 00 00            mov ecx, dword ptr [r15 + 0x178]
00B79178  E8 4F 01 00 00                  call 0x140b792cc
00B7917D  84 C0                           test al, al
00B7917F  0F 84 E4 75 00 00               je 0x140b80769
00B79185  41 FF 42 60                     inc dword ptr [r10 + 0x60]
00B79189  E9 DB 75 00 00                  jmp 0x140b80769
00B7918E  41 FF 42 58                     inc dword ptr [r10 + 0x58]
00B79192  E9 F9 FE FF FF                  jmp 0x140b79090
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IoBuildPoDeviceNotifyList(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_rsp;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_stack_p18 = v_rdi;
    v_rsp = (v_rsp) - (64);
    v_stack_m30 = v_stack_m38;
    v_stack_m38 = v_stack_m38;
    v_stack_m20 = v_stack_m28;
    v_stack_m28 = v_stack_m28;
    if ((((unsigned __int8)(a2)) & (1)) == 0) goto loc_00B790CF;
loc_00B78B55:
    a2 = 0;
    result = memset(a1, a2, 384, a4);
    *(unsigned int *)(a1 + 376) = (unsigned int)((unsigned int)(a2));
loc_00B78B75:
    *(unsigned __int64 *)(a1 + 48 - 16) = a1 + 48 - 24;
    *(unsigned __int64 *)(a1 + 48 - 24) = a1 + 48 - 24;
    *(unsigned __int64 *)(a1 + 48) = a1 + 48 - 8;
    *(unsigned __int64 *)(a1 + 48 - 8) = a1 + 48 - 8;
    *(unsigned __int64 *)(a1 + 48 + 16) = a1 + 48 + 8;
    *(unsigned __int64 *)(a1 + 48 + 8) = a1 + 48 + 8;
    *(unsigned __int64 *)(a1 + 48 + 32) = a1 + 48 + 24;
    *(unsigned __int64 *)(a1 + 48 + 24) = a1 + 48 + 24;
    a2 = (5) - (1);
    if (condition_is_not_equal) goto loc_00B78B75;
    goto loc_00B78BBE;
loc_00B78BB7:
loc_00B78BBE:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4274311) + 8) + 8) != 0) goto loc_00B78BB7;
    goto loc_00B78BD1;
loc_00B78BC5:
loc_00B78BCC:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4274311) + 8) + 8) + 8) != 0) goto loc_00B78BC5;
loc_00B78BD1:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4274311) + 8) + 8)) == (*(unsigned __int64 *)(v_rip + 4274272))) goto loc_00B78CAE;
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4274311) + 8) + 8) + 160 + 56) = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4274311) + 8) + 8) + 160 + 64) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4274311) + 8) + 8) + 32);
    result = IoGetAttachedDeviceReference(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4274311) + 8) + 8) + 32), a2, 384, a4);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4274311) + 8) + 8) + 160 + 48) = result;
    result = IopCaptureObjectName(*(unsigned __int64 *)(result + 8), a2, 384, a4);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4274311) + 8) + 8) + 160 + 80) = result;
    result = IopCaptureObjectName(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4274311) + 8) + 8) + 160 + 48), a2, 384, a4);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4274311) + 8) + 8) + 160 + 72) = result;
    result = ObfReferenceObject(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4274311) + 8) + 8) + 160 + 64), a2, 384, a4);
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4274311) + 8) + 8) + 160 + 56) = 0;
    result = IopCheckDeviceFlags(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4274311) + 8) + 8) + 160, (unsigned int)(0x2000ULL), 384, a4);
    if ((unsigned __int8)(result) != 0) {
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4274311) + 8) + 8) + 16)) == (*(unsigned __int64 *)(v_rip + 4274151))) goto loc_00B78C6B;
loc_00B78C5A:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4274311) + 8) + 8)) == 0) goto loc_00B78C92;
    goto loc_00B78BCC;
loc_00B78C6B:
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4274311) + 8) + 8)) + 448)) == 0) goto loc_00B78C5A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4274311) + 8) + 8)) + 396)))) & (4)) != 0) goto loc_00B78C5A;
    if ((*(unsigned __int64 *)(v_stack_m30)) == v_stack_m38) goto loc_00B78C9A;
loc_00B78C8B:
loc_00B78C92:
    goto loc_00B78BD1;
loc_00B78C9A:
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4274311) + 8) + 8) + 160 + 8) = v_stack_m30;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4274311) + 8) + 8) + 160) = v_stack_m38;
    *(unsigned __int64 *)(v_stack_m30) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4274311) + 8) + 8) + 160;
    v_stack_m30 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4274311) + 8) + 8) + 160;
    goto loc_00B78C5A;
loc_00B78CAE:
    if (v_stack_m38 == v_stack_m38) goto loc_00B78D22;
    if ((*(unsigned __int64 *)(v_stack_m38 + 8)) != v_stack_m38) goto loc_00B78C8B;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m38) + 8)) != v_stack_m38) goto loc_00B78C8B;
    v_stack_m38 = *(unsigned __int64 *)(v_stack_m38);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m38) + 8) = v_stack_m38;
    goto loc_00B78CF5;
loc_00B78CEE:
loc_00B78CF5:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m38 - 160 + 8) + 8) != 0) goto loc_00B78CEE;
    goto loc_00B78D08;
loc_00B78CFC:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m38 - 160 + 8) + 8) + 8) != 0) goto loc_00B78CFC;
loc_00B78D08:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m38 - 160 + 8) + 8)) == (v_stack_m38 - 160)) goto loc_00B78CAE;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m38 - 160 + 8) + 8)) != 0) goto loc_00B78CFC;
    goto loc_00B78D08;
loc_00B78D22:
    v_r10 = 0;
    goto loc_00B78D39;
loc_00B78D32:
loc_00B78D39:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273935) + 8) + 8) != 0) goto loc_00B78D32;
    goto loc_00B78D54;
loc_00B78D40:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273935) + 8)) == 0) goto loc_00B78DA6;
loc_00B78D48:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273935) + 8)) + 8) != 0) goto loc_00B78D48;
loc_00B78D54:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273935) + 8))) == (*(unsigned __int64 *)(v_rip + 4273885))) goto loc_00B78DAC;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273935) + 8)) + 216)) & (2)) == 0) goto loc_00B78D40;
    goto loc_00B78D79;
loc_00B78D72:
loc_00B78D79:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273935) + 8)) + 8) + 8) != 0) goto loc_00B78D72;
    goto loc_00B78D8C;
loc_00B78D80:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273935) + 8)) + 8) + 8) + 8) != 0) goto loc_00B78D80;
loc_00B78D8C:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273935) + 8)) + 8) + 8)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273935) + 8)))) goto loc_00B78D40;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273935) + 8)) + 8) + 8)) != 0) goto loc_00B78D80;
    goto loc_00B78D8C;
loc_00B78DA6:
    goto loc_00B78D54;
loc_00B78DAC:
    goto loc_00B78DB9;
loc_00B78DB2:
loc_00B78DB9:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273935) + 8)) + 8) + 8)) + 8) + 8) != 0) goto loc_00B78DB2;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273935) + 8)) + 8) + 8)) + 8)) == (*(unsigned __int64 *)(v_rip + 4273779))) goto loc_00B78DFC;
loc_00B78DCA:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273935) + 8)) + 8) + 8)) + 8) + 216)) & (2)) != 0) goto loc_00B78E02;
loc_00B78DD3:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273935) + 8)) + 8) + 8)) + 8)) == 0) goto loc_00B78E27;
loc_00B78DDB:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273935) + 8)) + 8) + 8)) + 8)) + 8) != 0) goto loc_00B78DDB;
loc_00B78DE7:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273935) + 8)) + 8) + 8)) + 8))) != (*(unsigned __int64 *)(v_rip + 4273738))) goto loc_00B78DCA;
    if (0 != 0) goto loc_00B78D22;
loc_00B78DFC:
    goto loc_00B78E34;
loc_00B78E02:
loc_00B78E0C:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273935) + 8)) + 8) + 8)) + 8)) + 176)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273935) + 8)) + 8) + 8)) + 8)) + 176)) goto loc_00B78DD3;
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273935) + 8)) + 8) + 8)) + 8)) + 176) - 8) + 56))) & (2)) == 0) goto loc_00B790F7;
loc_00B78E22:
    goto loc_00B78E0C;
loc_00B78E27:
    goto loc_00B78DE7;
loc_00B78E2D:
loc_00B78E34:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273935) + 8)) + 8) + 8)) + 8)) + 176)) + 8) != 0) goto loc_00B78E2D;
loc_00B78E39:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273935) + 8)) + 8) + 8)) + 8)) + 176))) == (*(unsigned __int64 *)(v_rip + 4273656))) goto loc_00B78EB8;
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273935) + 8)) + 8) + 8)) + 8)) + 176)) + 160 + 56))) & (2)) == 0) goto loc_00B78E9C;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273935) + 8)) + 8) + 8)) + 8)) + 176)) + 160 + 56)) + 1);
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273935) + 8)) + 8) + 8)) + 8)) + 176)) + 160 + 56) = (unsigned __int8)(result);
    result = ObfReferenceObjectWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273935) + 8)) + 8) + 8)) + 8)) + 176)) + 160 + 48), (unsigned int)(0x70506F50ULL), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273935) + 8)) + 8) + 8)) + 8)) + 176, *(unsigned __int64 *)(v_rip + 4273656));
loc_00B78E6B:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273935) + 8)) + 8) + 8)) + 8)) + 176)) + 160 + 48) == 0) goto loc_00B78E9C;
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273935) + 8)) + 8) + 8)) + 8)) + 176)) + 160 + 48) + 72)) == 7) goto loc_00B79106;
    result = IoGetLowerDeviceObjectWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273935) + 8)) + 8) + 8)) + 8)) + 176)) + 160 + 48), (unsigned int)(0x70506F50ULL), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273935) + 8)) + 8) + 8)) + 8)) + 176, *(unsigned __int64 *)(v_rip + 4273656));
    result = ObfDereferenceObjectWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273935) + 8)) + 8) + 8)) + 8)) + 176)) + 160 + 48), (unsigned int)(0x70506F50ULL), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273935) + 8)) + 8) + 8)) + 8)) + 176, *(unsigned __int64 *)(v_rip + 4273656));
    goto loc_00B78E6B;
loc_00B78E9C:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273935) + 8)) + 8) + 8)) + 8)) + 176))) == 0) goto loc_00B78EB2;
loc_00B78EA4:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273935) + 8)) + 8) + 8)) + 8)) + 176))) + 8) != 0) goto loc_00B78EA4;
    goto loc_00B78E39;
loc_00B78EB2:
    goto loc_00B78E39;
loc_00B78EB8:
    v_r10 = 0;
    goto loc_00B78EC8;
loc_00B78EC1:
loc_00B78EC8:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273656) + 8) + 8) != 0) goto loc_00B78EC1;
    goto loc_00B78EDB;
loc_00B78ECF:
loc_00B78ED6:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273656) + 8) + 8) + 8) != 0) goto loc_00B78ECF;
loc_00B78EDB:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273656) + 8) + 8)) == (*(unsigned __int64 *)(v_rip + 4273494))) goto loc_00B78F19;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273656) + 8) + 8) + 16)) == (*(unsigned __int64 *)(v_rip + 4273494))) goto loc_00B78F06;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273656) + 8) + 8) + 16) + 216)) > ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273656) + 8) + 8) + 216)))) goto loc_00B7912A;
loc_00B78F06:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273656) + 8) + 8)) == 0) goto loc_00B78F14;
    goto loc_00B78ED6;
loc_00B78F14:
    goto loc_00B78EDB;
loc_00B78F19:
    goto loc_00B78F26;
loc_00B78F1F:
loc_00B78F26:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273656) + 8) + 8)) + 8) + 8) + 8) != 0) goto loc_00B78F1F;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273656) + 8) + 8)) + 8) + 8)) == (*(unsigned __int64 *)(v_rip + 4273414))) goto loc_00B78F6F;
loc_00B78F37:
loc_00B78F41:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273656) + 8) + 8)) + 8) + 8) + 192)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273656) + 8) + 8)) + 8) + 8) + 192)) goto loc_00B78F7B;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273656) + 8) + 8)) + 8) + 8)) == 0) goto loc_00B78F75;
loc_00B78F4E:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273656) + 8) + 8)) + 8) + 8)) + 8) != 0) goto loc_00B78F4E;
loc_00B78F5A:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273656) + 8) + 8)) + 8) + 8))) != (*(unsigned __int64 *)(v_rip + 4273367))) goto loc_00B78F37;
    if (0 != 0) goto loc_00B78EB8;
loc_00B78F6F:
    goto loc_00B78F9C;
loc_00B78F75:
    goto loc_00B78F5A;
loc_00B78F7B:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273656) + 8) + 8)) + 8) + 8)) + 8) + 40) + 56)) > ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273367) + 8) + 16) + 216)))) goto loc_00B79135;
loc_00B78F90:
    goto loc_00B78F41;
loc_00B78F95:
loc_00B78F9C:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273367) + 8) + 16) + 8) != 0) goto loc_00B78F95;
    goto loc_00B78FAF;
loc_00B78FA3:
loc_00B78FAA:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273367) + 8) + 16) + 8) + 8) != 0) goto loc_00B78FA3;
loc_00B78FAF:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273367) + 8) + 16) + 8)) == (*(unsigned __int64 *)(v_rip + 4273282))) goto loc_00B79095;
    result = IopIsNotifyInBroadcast((unsigned int)(*(unsigned int *)(a1 + 376)), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273367) + 8) + 16) + 8) + 160, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273656) + 8) + 8)) + 8) + 8)) + 8) + 40), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273367) + 8) + 16) + 8));
    if ((unsigned __int8)(result) == 0) goto loc_00B79141;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273367) + 8) + 16) + 8) + 16)) == (*(unsigned __int64 *)(v_rip + 4273218))) goto loc_00B7901C;
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273367) + 8) + 16) + 8) + 16)) + (160);
    result = IopIsNotifyInBroadcast((unsigned int)(*(unsigned int *)(a1 + 376)), a2, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273656) + 8) + 8)) + 8) + 8)) + 8) + 40), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273367) + 8) + 16) + 8));
    if ((unsigned __int8)(result) != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273367) + 8) + 16) + 8) + 16);
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273367) + 8) + 16) + 8) + 160 + 32)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273367) + 8) + 16) + 8) + 160 + 32)) goto loc_00B7916D;
loc_00B79033:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273367) + 8) + 16) + 8) + 160 + 16)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273367) + 8) + 16) + 8) + 160 + 16)) goto loc_00B79078;
    a1 = (*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273367) + 8) + 16) + 8) + 160 + 56) * 8 + 3) + (*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273367) + 8) + 16) + 8) + 160 + 56));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + a1 * 8 + 8))) != (a1 + a1 * 8)) goto loc_00B78C8B;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273367) + 8) + 16) + 8) + 160) = a1 + a1 * 8;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273367) + 8) + 16) + 8) + 160 + 8) = *(unsigned __int64 *)(a1 + a1 * 8 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + a1 * 8 + 8)) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273367) + 8) + 16) + 8) + 160;
    *(unsigned __int64 *)(a1 + a1 * 8 + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273367) + 8) + 16) + 8) + 160;
loc_00B79067:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273367) + 8) + 16) + 8)) == 0) goto loc_00B790C7;
    goto loc_00B78FAA;
loc_00B79078:
    result = IopIsNotifyInBroadcast((unsigned int)(*(unsigned int *)(a1 + 376)), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273367) + 8) + 16) + 8) + 160 + 16) - 8), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273656) + 8) + 8)) + 8) + 8)) + 8) + 40), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273367) + 8) + 16) + 8)));
    if ((unsigned __int8)(result) != 0) goto loc_00B7918E;
loc_00B79090:
    goto loc_00B79033;
loc_00B79095:
    result = IopFreePoDeviceNotifyListHead(v_stack_m28, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273367) + 8) + 16) + 8) + 160 + 16) - 8), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273656) + 8) + 8)) + 8) + 8)) + 8) + 40), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273367) + 8) + 16) + 8)));
    *(unsigned __int64 *)(a1 + 8) = v_rip + 4273006;
    *(unsigned __int8 *)(a1) = 1;
    v_rsp = (v_rsp) + (64);
    return v_rip + 4273006;
loc_00B790C7:
    goto loc_00B78FAF;
loc_00B790CF:
    result = PnpPowerStateTransitionWatchdogPushRecord(v_stack_m28, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273367) + 8) + 16) + 8) + 160 + 16) - 8), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273656) + 8) + 8)) + 8) + 8)) + 8) + 40), *(unsigned __int64 *)(v_stack_p18));
    result = PnpLockDeviceActionQueue(v_stack_m28, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273367) + 8) + 16) + 8) + 160 + 16) - 8), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273656) + 8) + 8)) + 8) + 8)) + 8) + 40), *(unsigned __int64 *)(v_stack_p18));
    if (sign_flag) goto loc_00B78B55;
    result = PnpPowerStateTransitionWatchdogPopRecord(v_stack_m28, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273367) + 8) + 16) + 8) + 160 + 16) - 8), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273656) + 8) + 8)) + 8) + 8)) + 8) + 40), *(unsigned __int64 *)(v_stack_p18));
    goto loc_00B78B55;
loc_00B790F7:
    a2 = (unsigned __int8)((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273367) + 8) + 16) + 8) + 160 + 16) - 8)) | (2));
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p18) + 56) = (unsigned __int8)(a2);
    goto loc_00B78E22;
loc_00B79106:
    result = ObfDereferenceObjectWithTag(v_stack_m28, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273656) + 8) + 8)) + 8) + 8)) + 8) + 40), *(unsigned __int64 *)(v_stack_p18));
    result = IopCheckDeviceFlags(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273935) + 8)) + 8) + 8)) + 8)) + 176)) + 160, 256, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273656) + 8) + 8)) + 8) + 8)) + 8) + 40), *(unsigned __int64 *)(v_stack_p18));
    if ((unsigned __int8)(result) == 0) goto loc_00B78E9C;
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273935) + 8)) + 8) + 8)) + 8)) + 176)) + 160 + 56) = 2;
    goto loc_00B78E9C;
loc_00B7912A:
    *(unsigned __int8 *)(result) = 256;
    goto loc_00B78F06;
loc_00B79135:
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273656) + 8) + 8)) + 8) + 8)) + 8) + 40) + 56) = (unsigned __int8)(*(unsigned __int64 *)(v_stack_p18));
    goto loc_00B78F90;
loc_00B79141:
    if ((*(unsigned __int64 *)(v_stack_m20)) != v_stack_m28) goto loc_00B78C8B;
    *(unsigned __int64 *)(1 + 8) = v_stack_m20;
    *(unsigned __int64 *)(1) = v_stack_m28;
    *(unsigned __int64 *)(v_stack_m20) = 1;
    v_stack_m20 = 1;
    goto loc_00B79067;
loc_00B7916D:
    result = IopIsNotifyInBroadcast((unsigned int)(*(unsigned int *)(a1 + 376)), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273367) + 8) + 16) + 8) + 160 + 16)) + 40), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4273656) + 8) + 8)) + 8) + 8)) + 8) + 40), *(unsigned __int64 *)(v_stack_p18));
loc_00B7918E:
    goto loc_00B79090;
}
```

## 5. (Beta) C Style

```c
int64_t IoBuildPoDeviceNotifyList(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_rsp;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    v_stack_p18 = local_rdi;
    local_rsp = (local_rsp) - (64);
    v_stack_m30 = v_stack_m38;
    v_stack_m38 = v_stack_m38;
    v_stack_m20 = v_stack_m28;
    v_stack_m28 = v_stack_m28;
    if ((((uint8_t)(Arg2)) & (1)) == 0) goto loc_00B790CF;
loc_00B78B55:
    Arg2 = 0;
    result = memset(Arg1, Arg2, 384, a4);
    *(uint32_t *)(arg1 + 0x178) = (uint32_t)((uint32_t)(Arg2));
loc_00B78B75:
    *(void **)(arg1 + 0x30 - 0x10) = Arg1 + 48 - 24;
    *(void **)(arg1 + 0x30 - 0x18) = Arg1 + 48 - 24;
    *(void **)(arg1 + 0x30) = Arg1 + 48 - 8;
    *(void **)(arg1 + 0x30 - 0x8) = Arg1 + 48 - 8;
    *(void **)(arg1 + 0x30 + 0x10) = Arg1 + 48 + 8;
    *(void **)(arg1 + 0x30 + 0x8) = Arg1 + 48 + 8;
    *(void **)(arg1 + 0x30 + 0x20) = Arg1 + 48 + 24;
    *(void **)(arg1 + 0x30 + 0x18) = Arg1 + 48 + 24;
    Arg2 = (5) - (1);
    if (condition_is_not_equal) goto loc_00B78B75;
    goto loc_00B78BBE;
loc_00B78BB7:
loc_00B78BBE:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x413887) + 0x8) + 0x8) != 0) goto loc_00B78BB7;
    goto loc_00B78BD1;
loc_00B78BC5:
loc_00B78BCC:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x413887) + 0x8) + 0x8) + 0x8) != 0) goto loc_00B78BC5;
loc_00B78BD1:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x413887) + 0x8) + 0x8)) == (*(uint64_t *)(v_rip + 0x413860))) goto loc_00B78CAE;
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x413887) + 0x8) + 0x8) + 0xA0 + 0x38) = 0;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x413887) + 0x8) + 0x8) + 0xA0 + 0x40) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x413887) + 0x8) + 0x8) + 0x20);
    result = IoGetAttachedDeviceReference(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x413887) + 0x8) + 0x8) + 0x20), Arg2, 384, a4);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x413887) + 0x8) + 0x8) + 0xA0 + 0x30) = result;
    result = IopCaptureObjectName(*(uint64_t *)(result + 0x8), Arg2, 384, a4);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x413887) + 0x8) + 0x8) + 0xA0 + 0x50) = result;
    result = IopCaptureObjectName(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x413887) + 0x8) + 0x8) + 0xA0 + 0x30), Arg2, 384, a4);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x413887) + 0x8) + 0x8) + 0xA0 + 0x48) = result;
    result = ObfReferenceObject(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x413887) + 0x8) + 0x8) + 0xA0 + 0x40), Arg2, 384, a4);
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x413887) + 0x8) + 0x8) + 0xA0 + 0x38) = 0;
    result = IopCheckDeviceFlags(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x413887) + 0x8) + 0x8) + 160, (uint32_t)(0x2000ULL), 384, a4);
    if ((uint8_t)(result) != 0) {
    }
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x413887) + 0x8) + 0x8) + 0x10)) == (*(uint64_t *)(v_rip + 0x4137E7))) goto loc_00B78C6B;
loc_00B78C5A:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x413887) + 0x8) + 0x8)) == 0) goto loc_00B78C92;
    goto loc_00B78BCC;
loc_00B78C6B:
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x413887) + 0x8) + 0x8)) + 0x1C0)) == 0) goto loc_00B78C5A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x413887) + 0x8) + 0x8)) + 0x18C)))) & (4)) != 0) goto loc_00B78C5A;
    if ((*(uint64_t *)(v_stack_m30)) == v_stack_m38) goto loc_00B78C9A;
loc_00B78C8B:
loc_00B78C92:
    goto loc_00B78BD1;
loc_00B78C9A:
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x413887) + 0x8) + 0x8) + 0xA0 + 0x8) = v_stack_m30;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x413887) + 0x8) + 0x8) + 0xA0) = v_stack_m38;
    *(uint64_t *)(v_stack_m30) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x413887) + 0x8) + 0x8) + 160;
    v_stack_m30 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x413887) + 0x8) + 0x8) + 160;
    goto loc_00B78C5A;
loc_00B78CAE:
    if (v_stack_m38 == v_stack_m38) goto loc_00B78D22;
    if ((*(uint64_t *)(v_stack_m38 + 0x8)) != v_stack_m38) goto loc_00B78C8B;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m38) + 0x8)) != v_stack_m38) goto loc_00B78C8B;
    v_stack_m38 = *(uint64_t *)(v_stack_m38);
    *(uint64_t *)(*(uint64_t *)(v_stack_m38) + 0x8) = v_stack_m38;
    goto loc_00B78CF5;
loc_00B78CEE:
loc_00B78CF5:
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m38 - 0xA0 + 0x8) + 0x8) != 0) goto loc_00B78CEE;
    goto loc_00B78D08;
loc_00B78CFC:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m38 - 0xA0 + 0x8) + 0x8) + 0x8) != 0) goto loc_00B78CFC;
loc_00B78D08:
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m38 - 0xA0 + 0x8) + 0x8)) == (v_stack_m38 - 160)) goto loc_00B78CAE;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m38 - 0xA0 + 0x8) + 0x8)) != 0) goto loc_00B78CFC;
    goto loc_00B78D08;
loc_00B78D22:
    local_r10 = 0;
    goto loc_00B78D39;
loc_00B78D32:
loc_00B78D39:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x41370F) + 0x8) + 0x8) != 0) goto loc_00B78D32;
    goto loc_00B78D54;
loc_00B78D40:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x41370F) + 0x8)) == 0) goto loc_00B78DA6;
loc_00B78D48:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x41370F) + 0x8)) + 0x8) != 0) goto loc_00B78D48;
loc_00B78D54:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x41370F) + 0x8))) == (*(uint64_t *)(v_rip + 0x4136DD))) goto loc_00B78DAC;
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x41370F) + 0x8)) + 0xD8)) & (2)) == 0) goto loc_00B78D40;
    goto loc_00B78D79;
loc_00B78D72:
loc_00B78D79:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x41370F) + 0x8)) + 0x8) + 0x8) != 0) goto loc_00B78D72;
    goto loc_00B78D8C;
loc_00B78D80:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x41370F) + 0x8)) + 0x8) + 0x8) + 0x8) != 0) goto loc_00B78D80;
loc_00B78D8C:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x41370F) + 0x8)) + 0x8) + 0x8)) == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x41370F) + 0x8)))) goto loc_00B78D40;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x41370F) + 0x8)) + 0x8) + 0x8)) != 0) goto loc_00B78D80;
    goto loc_00B78D8C;
loc_00B78DA6:
    goto loc_00B78D54;
loc_00B78DAC:
    goto loc_00B78DB9;
loc_00B78DB2:
loc_00B78DB9:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x41370F) + 0x8)) + 0x8) + 0x8)) + 0x8) + 0x8) != 0) goto loc_00B78DB2;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x41370F) + 0x8)) + 0x8) + 0x8)) + 0x8)) == (*(uint64_t *)(v_rip + 0x413673))) goto loc_00B78DFC;
loc_00B78DCA:
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x41370F) + 0x8)) + 0x8) + 0x8)) + 0x8) + 0xD8)) & (2)) != 0) goto loc_00B78E02;
loc_00B78DD3:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x41370F) + 0x8)) + 0x8) + 0x8)) + 0x8)) == 0) goto loc_00B78E27;
loc_00B78DDB:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x41370F) + 0x8)) + 0x8) + 0x8)) + 0x8)) + 0x8) != 0) goto loc_00B78DDB;
loc_00B78DE7:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x41370F) + 0x8)) + 0x8) + 0x8)) + 0x8))) != (*(uint64_t *)(v_rip + 0x41364A))) goto loc_00B78DCA;
    if (0 != 0) goto loc_00B78D22;
loc_00B78DFC:
    goto loc_00B78E34;
loc_00B78E02:
loc_00B78E0C:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x41370F) + 0x8)) + 0x8) + 0x8)) + 0x8)) + 0xB0)) == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x41370F) + 0x8)) + 0x8) + 0x8)) + 0x8)) + 176)) goto loc_00B78DD3;
    if ((((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x41370F) + 0x8)) + 0x8) + 0x8)) + 0x8)) + 0xB0) - 0x8) + 0x38))) & (2)) == 0) goto loc_00B790F7;
loc_00B78E22:
    goto loc_00B78E0C;
loc_00B78E27:
    goto loc_00B78DE7;
loc_00B78E2D:
loc_00B78E34:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x41370F) + 0x8)) + 0x8) + 0x8)) + 0x8)) + 0xB0)) + 0x8) != 0) goto loc_00B78E2D;
loc_00B78E39:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x41370F) + 0x8)) + 0x8) + 0x8)) + 0x8)) + 0xB0))) == (*(uint64_t *)(v_rip + 0x4135F8))) goto loc_00B78EB8;
    if ((((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x41370F) + 0x8)) + 0x8) + 0x8)) + 0x8)) + 0xB0)) + 0xA0 + 0x38))) & (2)) == 0) goto loc_00B78E9C;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x41370F) + 0x8)) + 0x8) + 0x8)) + 0x8)) + 0xB0)) + 0xA0 + 0x38)) + 1);
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x41370F) + 0x8)) + 0x8) + 0x8)) + 0x8)) + 0xB0)) + 0xA0 + 0x38) = (uint8_t)(result);
    result = ObfReferenceObjectWithTag(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x41370F) + 0x8)) + 0x8) + 0x8)) + 0x8)) + 0xB0)) + 0xA0 + 0x30), (uint32_t)(0x70506F50ULL), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x41370F) + 0x8)) + 0x8) + 0x8)) + 0x8)) + 176, *(uint64_t *)(v_rip + 0x4135F8));
loc_00B78E6B:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x41370F) + 0x8)) + 0x8) + 0x8)) + 0x8)) + 0xB0)) + 0xA0 + 0x30) == 0) goto loc_00B78E9C;
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x41370F) + 0x8)) + 0x8) + 0x8)) + 0x8)) + 0xB0)) + 0xA0 + 0x30) + 0x48)) == 7) goto loc_00B79106;
    result = IoGetLowerDeviceObjectWithTag(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x41370F) + 0x8)) + 0x8) + 0x8)) + 0x8)) + 0xB0)) + 0xA0 + 0x30), (uint32_t)(0x70506F50ULL), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x41370F) + 0x8)) + 0x8) + 0x8)) + 0x8)) + 176, *(uint64_t *)(v_rip + 0x4135F8));
    result = ObfDereferenceObjectWithTag(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x41370F) + 0x8)) + 0x8) + 0x8)) + 0x8)) + 0xB0)) + 0xA0 + 0x30), (uint32_t)(0x70506F50ULL), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x41370F) + 0x8)) + 0x8) + 0x8)) + 0x8)) + 176, *(uint64_t *)(v_rip + 0x4135F8));
    goto loc_00B78E6B;
loc_00B78E9C:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x41370F) + 0x8)) + 0x8) + 0x8)) + 0x8)) + 0xB0))) == 0) goto loc_00B78EB2;
loc_00B78EA4:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x41370F) + 0x8)) + 0x8) + 0x8)) + 0x8)) + 0xB0))) + 0x8) != 0) goto loc_00B78EA4;
    goto loc_00B78E39;
loc_00B78EB2:
    goto loc_00B78E39;
loc_00B78EB8:
    local_r10 = 0;
    goto loc_00B78EC8;
loc_00B78EC1:
loc_00B78EC8:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4135F8) + 0x8) + 0x8) != 0) goto loc_00B78EC1;
    goto loc_00B78EDB;
loc_00B78ECF:
loc_00B78ED6:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4135F8) + 0x8) + 0x8) + 0x8) != 0) goto loc_00B78ECF;
loc_00B78EDB:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4135F8) + 0x8) + 0x8)) == (*(uint64_t *)(v_rip + 0x413556))) goto loc_00B78F19;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4135F8) + 0x8) + 0x8) + 0x10)) == (*(uint64_t *)(v_rip + 0x413556))) goto loc_00B78F06;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4135F8) + 0x8) + 0x8) + 0x10) + 0xD8)) > ((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4135F8) + 0x8) + 0x8) + 0xD8)))) goto loc_00B7912A;
loc_00B78F06:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4135F8) + 0x8) + 0x8)) == 0) goto loc_00B78F14;
    goto loc_00B78ED6;
loc_00B78F14:
    goto loc_00B78EDB;
loc_00B78F19:
    goto loc_00B78F26;
loc_00B78F1F:
loc_00B78F26:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4135F8) + 0x8) + 0x8)) + 0x8) + 0x8) + 0x8) != 0) goto loc_00B78F1F;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4135F8) + 0x8) + 0x8)) + 0x8) + 0x8)) == (*(uint64_t *)(v_rip + 0x413506))) goto loc_00B78F6F;
loc_00B78F37:
loc_00B78F41:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4135F8) + 0x8) + 0x8)) + 0x8) + 0x8) + 0xC0)) != (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4135F8) + 0x8) + 0x8)) + 0x8) + 0x8) + 192)) goto loc_00B78F7B;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4135F8) + 0x8) + 0x8)) + 0x8) + 0x8)) == 0) goto loc_00B78F75;
loc_00B78F4E:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4135F8) + 0x8) + 0x8)) + 0x8) + 0x8)) + 0x8) != 0) goto loc_00B78F4E;
loc_00B78F5A:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4135F8) + 0x8) + 0x8)) + 0x8) + 0x8))) != (*(uint64_t *)(v_rip + 0x4134D7))) goto loc_00B78F37;
    if (0 != 0) goto loc_00B78EB8;
loc_00B78F6F:
    goto loc_00B78F9C;
loc_00B78F75:
    goto loc_00B78F5A;
loc_00B78F7B:
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4135F8) + 0x8) + 0x8)) + 0x8) + 0x8)) + 0x8) + 0x28) + 0x38)) > ((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4134D7) + 0x8) + 0x10) + 0xD8)))) goto loc_00B79135;
loc_00B78F90:
    goto loc_00B78F41;
loc_00B78F95:
loc_00B78F9C:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4134D7) + 0x8) + 0x10) + 0x8) != 0) goto loc_00B78F95;
    goto loc_00B78FAF;
loc_00B78FA3:
loc_00B78FAA:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4134D7) + 0x8) + 0x10) + 0x8) + 0x8) != 0) goto loc_00B78FA3;
loc_00B78FAF:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4134D7) + 0x8) + 0x10) + 0x8)) == (*(uint64_t *)(v_rip + 0x413482))) goto loc_00B79095;
    result = IopIsNotifyInBroadcast((uint32_t)(*(uint32_t *)(arg1 + 0x178)), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4134D7) + 0x8) + 0x10) + 0x8) + 160, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4135F8) + 0x8) + 0x8)) + 0x8) + 0x8)) + 0x8) + 0x28), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4134D7) + 0x8) + 0x10) + 0x8));
    if ((uint8_t)(result) == 0) goto loc_00B79141;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4134D7) + 0x8) + 0x10) + 0x8) + 0x10)) == (*(uint64_t *)(v_rip + 0x413442))) goto loc_00B7901C;
    Arg2 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4134D7) + 0x8) + 0x10) + 0x8) + 0x10)) + (160);
    result = IopIsNotifyInBroadcast((uint32_t)(*(uint32_t *)(arg1 + 0x178)), Arg2, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4135F8) + 0x8) + 0x8)) + 0x8) + 0x8)) + 0x8) + 0x28), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4134D7) + 0x8) + 0x10) + 0x8));
    if ((uint8_t)(result) != 0) {
        result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4134D7) + 0x8) + 0x10) + 0x8) + 0x10);
    }
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4134D7) + 0x8) + 0x10) + 0x8) + 0xA0 + 0x20)) != (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4134D7) + 0x8) + 0x10) + 0x8) + 160 + 32)) goto loc_00B7916D;
loc_00B79033:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4134D7) + 0x8) + 0x10) + 0x8) + 0xA0 + 0x10)) != (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4134D7) + 0x8) + 0x10) + 0x8) + 160 + 16)) goto loc_00B79078;
    Arg1 = (*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4134D7) + 0x8) + 0x10) + 0x8) + 0xA0 + 0x38) * 8 + 3) + (*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4134D7) + 0x8) + 0x10) + 0x8) + 0xA0 + 0x38));
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + arg1 * 8 + 0x8))) != (Arg1 + Arg1 * 8)) goto loc_00B78C8B;
    *(void **)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4134D7) + 0x8) + 0x10) + 0x8) + 0xA0) = Arg1 + Arg1 * 8;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4134D7) + 0x8) + 0x10) + 0x8) + 0xA0 + 0x8) = *(uint64_t *)(arg1 + arg1 * 8 + 0x8);
    *(uint64_t *)(*(uint64_t *)(arg1 + arg1 * 8 + 0x8)) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4134D7) + 0x8) + 0x10) + 0x8) + 160;
    *(uint64_t *)(arg1 + arg1 * 8 + 0x8) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4134D7) + 0x8) + 0x10) + 0x8) + 160;
loc_00B79067:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4134D7) + 0x8) + 0x10) + 0x8)) == 0) goto loc_00B790C7;
    goto loc_00B78FAA;
loc_00B79078:
    result = IopIsNotifyInBroadcast((uint32_t)(*(uint32_t *)(arg1 + 0x178)), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4134D7) + 0x8) + 0x10) + 0x8) + 0xA0 + 0x10) - 0x8), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4135F8) + 0x8) + 0x8)) + 0x8) + 0x8)) + 0x8) + 0x28), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4134D7) + 0x8) + 0x10) + 0x8)));
    if ((uint8_t)(result) != 0) goto loc_00B7918E;
loc_00B79090:
    goto loc_00B79033;
loc_00B79095:
    result = IopFreePoDeviceNotifyListHead(v_stack_m28, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4134D7) + 0x8) + 0x10) + 0x8) + 0xA0 + 0x10) - 0x8), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4135F8) + 0x8) + 0x8)) + 0x8) + 0x8)) + 0x8) + 0x28), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4134D7) + 0x8) + 0x10) + 0x8)));
    *(uint64_t *)(arg1 + 0x8) = v_rip + 4273006;
    *(uint8_t *)(arg1) = 1;
    local_rsp = (local_rsp) + (64);
    return v_rip + 4273006;
loc_00B790C7:
    goto loc_00B78FAF;
loc_00B790CF:
    result = PnpPowerStateTransitionWatchdogPushRecord(v_stack_m28, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4134D7) + 0x8) + 0x10) + 0x8) + 0xA0 + 0x10) - 0x8), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4135F8) + 0x8) + 0x8)) + 0x8) + 0x8)) + 0x8) + 0x28), *(uint64_t *)(v_stack_p18));
    result = PnpLockDeviceActionQueue(v_stack_m28, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4134D7) + 0x8) + 0x10) + 0x8) + 0xA0 + 0x10) - 0x8), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4135F8) + 0x8) + 0x8)) + 0x8) + 0x8)) + 0x8) + 0x28), *(uint64_t *)(v_stack_p18));
    if (sign_flag) goto loc_00B78B55;
    result = PnpPowerStateTransitionWatchdogPopRecord(v_stack_m28, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4134D7) + 0x8) + 0x10) + 0x8) + 0xA0 + 0x10) - 0x8), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4135F8) + 0x8) + 0x8)) + 0x8) + 0x8)) + 0x8) + 0x28), *(uint64_t *)(v_stack_p18));
    goto loc_00B78B55;
loc_00B790F7:
    Arg2 = (uint8_t)((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4134D7) + 0x8) + 0x10) + 0x8) + 0xA0 + 0x10) - 0x8)) | (2));
    *(uint8_t *)(*(uint64_t *)(v_stack_p18) + 0x38) = (uint8_t)(Arg2);
    goto loc_00B78E22;
loc_00B79106:
    result = ObfDereferenceObjectWithTag(v_stack_m28, Arg2, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4135F8) + 0x8) + 0x8)) + 0x8) + 0x8)) + 0x8) + 0x28), *(uint64_t *)(v_stack_p18));
    result = IopCheckDeviceFlags(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x41370F) + 0x8)) + 0x8) + 0x8)) + 0x8)) + 0xB0)) + 160, 256, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4135F8) + 0x8) + 0x8)) + 0x8) + 0x8)) + 0x8) + 0x28), *(uint64_t *)(v_stack_p18));
    if ((uint8_t)(result) == 0) goto loc_00B78E9C;
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x41370F) + 0x8)) + 0x8) + 0x8)) + 0x8)) + 0xB0)) + 0xA0 + 0x38) = 2;
    goto loc_00B78E9C;
loc_00B7912A:
    *(uint8_t *)(result) = 256;
    goto loc_00B78F06;
loc_00B79135:
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4135F8) + 0x8) + 0x8)) + 0x8) + 0x8)) + 0x8) + 0x28) + 0x38) = (uint8_t)(*(uint64_t *)(v_stack_p18));
    goto loc_00B78F90;
loc_00B79141:
    if ((*(uint64_t *)(v_stack_m20)) != v_stack_m28) goto loc_00B78C8B;
    *(uint64_t *)(1 + 0x8) = v_stack_m20;
    *(uint64_t *)(1) = v_stack_m28;
    *(uint64_t *)(v_stack_m20) = 1;
    v_stack_m20 = 1;
    goto loc_00B79067;
loc_00B7916D:
    result = IopIsNotifyInBroadcast((uint32_t)(*(uint32_t *)(arg1 + 0x178)), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4134D7) + 0x8) + 0x10) + 0x8) + 0xA0 + 0x10)) + 0x28), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4135F8) + 0x8) + 0x8)) + 0x8) + 0x8)) + 0x8) + 0x28), *(uint64_t *)(v_stack_p18));
loc_00B7918E:
    goto loc_00B79090;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `- 0x18` | `64` | `R` |
| `Arg1` | `- 0x10` | `64` | `W` |
| `Arg1` | `- 0x8` | `64` | `R` |
| `Arg1` | `+ 0x0` | `8` | `W` |
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x0 + rcx*8` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x10` | `64` | `W` |
| `Arg1` | `+ 0x10 + rcx*8` | `32` | `R/W` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `W` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x48` | `64` | `R` |
| `Arg1` | `+ 0x178` | `32` | `R` |
| `Arg1` | `+ 0x178` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagelk&rva=0x00B78B0C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
