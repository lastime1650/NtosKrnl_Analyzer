# SepAdjustPrivileges

- RVA: `0x009C8DFC`–`0x009C9400` (길이 `1,540` bytes)
- VA: `0x00000001409C8DFC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A0984`
- 디코드: `372`개 명령, `1,540/1,540` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **17**; 고유 호출 대상: **8**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x009C8EAE` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009C8EC2` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009C8ED5` → [SepCopyTokenIntegrity](../../text/41/SepCopyTokenIntegrity_function_00419D10.md) (function, `0x00419D10`)
- `0x009C8EEB` → [RtlSidDominates](../../text/3F/RtlSidDominates_function_003FBD50.md) (function, `0x003FBD50`)
- `0x009C8F17` → [RtlSidDominates](../../text/3F/RtlSidDominates_function_003FBD50.md) (function, `0x003FBD50`)
- `0x009C8FA9` → [Feature_3055530299__private_IsEnabledDeviceUsageNoInline](../../text/60/Feature_3055530299__private_IsEnabledDeviceUsageNoInline_function_006065F8.md) (function, `0x006065F8`)
- `0x009C8FE1` → [SepTryAddUniqueAuditPrivilege](../../text/60/SepTryAddUniqueAuditPrivilege_function_0060664C.md) (function, `0x0060664C`)
- `0x009C9150` → [SepAdtTokenRightAdjusted](../90/SepAdtTokenRightAdjusted_function_0090445C.md) (function, `0x0090445C`)
- `0x009C91B4` → [Feature_3055530299__private_IsEnabledDeviceUsageNoInline](../../text/60/Feature_3055530299__private_IsEnabledDeviceUsageNoInline_function_006065F8.md) (function, `0x006065F8`)
- `0x009C9203` → [Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline](../../text/4E/Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline_function_004EF788.md) (function, `0x004EF788`)
- `0x009C9273` → [Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline](../../text/4E/Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline_function_004EF788.md) (function, `0x004EF788`)
- `0x009C929B` → [Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline](../../text/4E/Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline_function_004EF788.md) (function, `0x004EF788`)
- `0x009C9301` → [Feature_3055530299__private_IsEnabledDeviceUsageNoInline](../../text/60/Feature_3055530299__private_IsEnabledDeviceUsageNoInline_function_006065F8.md) (function, `0x006065F8`)
- `0x009C9326` → [SepTryAddUniqueAuditPrivilege](../../text/60/SepTryAddUniqueAuditPrivilege_function_0060664C.md) (function, `0x0060664C`)
- `0x009C936E` → [Feature_3055530299__private_IsEnabledDeviceUsageNoInline](../../text/60/Feature_3055530299__private_IsEnabledDeviceUsageNoInline_function_006065F8.md) (function, `0x006065F8`)
- `0x009C93A6` → [SepTryAddUniqueAuditPrivilege](../../text/60/SepTryAddUniqueAuditPrivilege_function_0060664C.md) (function, `0x0060664C`)
- `0x009C93D9` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [NtAdjustPrivilegesToken](NtAdjustPrivilegesToken_function_009C86C0.md) at `0x009C88AF`
- [NtAdjustPrivilegesToken](NtAdjustPrivilegesToken_function_009C86C0.md) at `0x009C88F5`

### Static image references
- `0x009C8E22` → RVA `0x00E0A740` (`.data`; read)
- `0x009C8EE4` → RVA `0x00F05838` (`.data`; read)
- `0x009C8F06` → RVA `0x00F05820` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **16**
  - `0x009C8EAE` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009C8EC2` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009C8ED5` → [SepCopyTokenIntegrity](../../text/41/SepCopyTokenIntegrity_function_00419D10.md) (`PAGE` → `.text`)
  - `0x009C8EEB` → [RtlSidDominates](../../text/3F/RtlSidDominates_function_003FBD50.md) (`PAGE` → `.text`)
  - `0x009C8F17` → [RtlSidDominates](../../text/3F/RtlSidDominates_function_003FBD50.md) (`PAGE` → `.text`)
  - `0x009C8FA9` → [Feature_3055530299__private_IsEnabledDeviceUsageNoInline](../../text/60/Feature_3055530299__private_IsEnabledDeviceUsageNoInline_function_006065F8.md) (`PAGE` → `.text`)
  - `0x009C8FE1` → [SepTryAddUniqueAuditPrivilege](../../text/60/SepTryAddUniqueAuditPrivilege_function_0060664C.md) (`PAGE` → `.text`)
  - `0x009C91B4` → [Feature_3055530299__private_IsEnabledDeviceUsageNoInline](../../text/60/Feature_3055530299__private_IsEnabledDeviceUsageNoInline_function_006065F8.md) (`PAGE` → `.text`)
  - `0x009C9203` → [Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline](../../text/4E/Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline_function_004EF788.md) (`PAGE` → `.text`)
  - `0x009C9273` → [Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline](../../text/4E/Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline_function_004EF788.md) (`PAGE` → `.text`)
  - `0x009C929B` → [Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline](../../text/4E/Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline_function_004EF788.md) (`PAGE` → `.text`)
  - `0x009C9301` → [Feature_3055530299__private_IsEnabledDeviceUsageNoInline](../../text/60/Feature_3055530299__private_IsEnabledDeviceUsageNoInline_function_006065F8.md) (`PAGE` → `.text`)
  - `0x009C9326` → [SepTryAddUniqueAuditPrivilege](../../text/60/SepTryAddUniqueAuditPrivilege_function_0060664C.md) (`PAGE` → `.text`)
  - `0x009C936E` → [Feature_3055530299__private_IsEnabledDeviceUsageNoInline](../../text/60/Feature_3055530299__private_IsEnabledDeviceUsageNoInline_function_006065F8.md) (`PAGE` → `.text`)
  - `0x009C93A6` → [SepTryAddUniqueAuditPrivilege](../../text/60/SepTryAddUniqueAuditPrivilege_function_0060664C.md) (`PAGE` → `.text`)
  - `0x009C93D9` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009C8DFC  48 8B C4                        mov rax, rsp
009C8DFF  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
009C8E03  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
009C8E07  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
009C8E0B  55                              push rbp
009C8E0C  41 54                           push r12
009C8E0E  41 55                           push r13
009C8E10  41 56                           push r14
009C8E12  41 57                           push r15
009C8E14  48 8D A8 C8 FC FF FF            lea rbp, [rax - 0x338]
009C8E1B  48 81 EC 10 04 00 00            sub rsp, 0x410
009C8E22  48 8B 05 17 19 44 00            mov rax, qword ptr [rip + 0x441917]
009C8E29  48 33 C4                        xor rax, rsp
009C8E2C  48 89 85 00 03 00 00            mov qword ptr [rbp + 0x300], rax
009C8E33  48 8B 85 70 03 00 00            mov rax, qword ptr [rbp + 0x370]
009C8E3A  48 8B D9                        mov rbx, rcx
009C8E3D  4C 8B AD 68 03 00 00            mov r13, qword ptr [rbp + 0x368]
009C8E44  33 C9                           xor ecx, ecx
009C8E46  4C 8B BD 80 03 00 00            mov r15, qword ptr [rbp + 0x380]
009C8E4D  8B F1                           mov esi, ecx
009C8E4F  4C 8B B5 78 03 00 00            mov r14, qword ptr [rbp + 0x378]
009C8E56  44 8B E1                        mov r12d, ecx
009C8E59  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
009C8E5D  41 8A F8                        mov dil, r8b
009C8E60  33 C0                           xor eax, eax
009C8E62  89 4C 24 50                     mov dword ptr [rsp + 0x50], ecx
009C8E66  88 4C 24 31                     mov byte ptr [rsp + 0x31], cl
009C8E6A  0F 57 C0                        xorps xmm0, xmm0
009C8E6D  88 4C 24 32                     mov byte ptr [rsp + 0x32], cl
009C8E71  41 B8 B0 01 00 00               mov r8d, 0x1b0
009C8E77  88 4C 24 4C                     mov byte ptr [rsp + 0x4c], cl
009C8E7B  48 89 4C 24 68                  mov qword ptr [rsp + 0x68], rcx
009C8E80  89 4C 24 34                     mov dword ptr [rsp + 0x34], ecx
009C8E84  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
009C8E88  48 8D 4D A0                     lea rcx, [rbp - 0x60]
009C8E8C  88 54 24 30                     mov byte ptr [rsp + 0x30], dl
009C8E90  33 D2                           xor edx, edx
009C8E92  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
009C8E97  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
009C8E9B  44 89 4C 24 60                  mov dword ptr [rsp + 0x60], r9d
009C8EA0  4C 89 6C 24 58                  mov qword ptr [rsp + 0x58], r13
009C8EA5  4C 89 7D 88                     mov qword ptr [rbp - 0x78], r15
009C8EA9  0F 11 44 24 78                  movups xmmword ptr [rsp + 0x78], xmm0
009C8EAE  E8 8D DD CF FF                  call 0x1406c6c40
009C8EB3  33 D2                           xor edx, edx
009C8EB5  48 8D 8D 50 01 00 00            lea rcx, [rbp + 0x150]
009C8EBC  41 B8 B0 01 00 00               mov r8d, 0x1b0
009C8EC2  E8 79 DD CF FF                  call 0x1406c6c40
009C8EC7  45 21 26                        and dword ptr [r14], r12d
009C8ECA  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
009C8ECF  48 8B CB                        mov rcx, rbx
009C8ED2  41 88 37                        mov byte ptr [r15], sil
009C8ED5  E8 36 0E A5 FF                  call 0x140419d10
009C8EDA  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
009C8EDF  4C 8D 44 24 31                  lea r8, [rsp + 0x31]
009C8EE4  48 8B 15 4D C9 53 00            mov rdx, qword ptr [rip + 0x53c94d]
009C8EEB  E8 60 2E A3 FF                  call 0x1403fbd50
009C8EF0  89 44 24 54                     mov dword ptr [rsp + 0x54], eax
009C8EF4  44 8B F8                        mov r15d, eax
009C8EF7  85 C0                           test eax, eax
009C8EF9  0F 88 D0 04 00 00               js 0x1409c93cf
009C8EFF  40 38 74 24 31                  cmp byte ptr [rsp + 0x31], sil
009C8F04  75 41                           jne 0x1409c8f47
009C8F06  48 8B 15 13 C9 53 00            mov rdx, qword ptr [rip + 0x53c913]
009C8F0D  4C 8D 44 24 32                  lea r8, [rsp + 0x32]
009C8F12  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
009C8F17  E8 34 2E A3 FF                  call 0x1403fbd50
009C8F1C  89 44 24 54                     mov dword ptr [rsp + 0x54], eax
009C8F20  44 8B F8                        mov r15d, eax
009C8F23  85 C0                           test eax, eax
009C8F25  0F 88 A4 04 00 00               js 0x1409c93cf
009C8F2B  8B 44 24 4C                     mov eax, dword ptr [rsp + 0x4c]
009C8F2F  41 B9 01 00 00 00               mov r9d, 1
009C8F35  40 38 74 24 32                  cmp byte ptr [rsp + 0x32], sil
009C8F3A  0F B6 C0                        movzx eax, al
009C8F3D  41 0F 44 C1                     cmove eax, r9d
009C8F41  89 44 24 4C                     mov dword ptr [rsp + 0x4c], eax
009C8F45  EB 06                           jmp 0x1409c8f4d
009C8F47  41 B9 01 00 00 00               mov r9d, 1
009C8F4D  40 84 FF                        test dil, dil
009C8F50  0F 84 DE 00 00 00               je 0x1409c9034
009C8F56  44 8A 7C 24 30                  mov r15b, byte ptr [rsp + 0x30]
009C8F5B  33 FF                           xor edi, edi
009C8F5D  8D 77 01                        lea esi, [rdi + 1]
009C8F60  8B CF                           mov ecx, edi
009C8F62  48 8B D6                        mov rdx, rsi
009C8F65  48 D3 E2                        shl rdx, cl
009C8F68  48 85 53 48                     test qword ptr [rbx + 0x48], rdx
009C8F6C  0F 84 AD 00 00 00               je 0x1409c901f
009C8F72  45 84 FF                        test r15b, r15b
009C8F75  0F 84 A1 00 00 00               je 0x1409c901c
009C8F7B  48 8B 43 50                     mov rax, qword ptr [rbx + 0x50]
009C8F7F  48 23 C2                        and rax, rdx
009C8F82  48 F7 D8                        neg rax
009C8F85  48 63 C7                        movsxd rax, edi
009C8F88  1B F6                           sbb esi, esi
009C8F8A  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
009C8F8E  F7 DE                           neg esi
009C8F90  83 C6 02                        add esi, 2
009C8F93  48 C1 E8 20                     shr rax, 0x20
009C8F97  89 44 24 5C                     mov dword ptr [rsp + 0x5c], eax
009C8F9B  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
009C8FA0  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
009C8FA5  89 74 24 40                     mov dword ptr [rsp + 0x40], esi
009C8FA9  E8 4A D6 C3 FF                  call 0x1406065f8
009C8FAE  85 C0                           test eax, eax
009C8FB0  75 21                           jne 0x1409c8fd3
009C8FB2  F2 0F 10 44 24 38               movsd xmm0, qword ptr [rsp + 0x38]
009C8FB8  41 8B C4                        mov eax, r12d
009C8FBB  41 FF C4                        inc r12d
009C8FBE  44 89 64 24 34                  mov dword ptr [rsp + 0x34], r12d
009C8FC3  48 8D 0C 40                     lea rcx, [rax + rax*2]
009C8FC7  F2 0F 11 44 8D A0               movsd qword ptr [rbp + rcx*4 - 0x60], xmm0
009C8FCD  89 74 8D A8                     mov dword ptr [rbp + rcx*4 - 0x58], esi
009C8FD1  EB 18                           jmp 0x1409c8feb
009C8FD3  4C 8D 44 24 38                  lea r8, [rsp + 0x38]
009C8FD8  48 8D 54 24 34                  lea rdx, [rsp + 0x34]
009C8FDD  48 8D 4D A0                     lea rcx, [rbp - 0x60]
009C8FE1  E8 66 D6 C3 FF                  call 0x14060664c
009C8FE6  44 8B 64 24 34                  mov r12d, dword ptr [rsp + 0x34]
009C8FEB  4D 85 ED                        test r13, r13
009C8FEE  74 19                           je 0x1409c9009
009C8FF0  41 8B 06                        mov eax, dword ptr [r14]
009C8FF3  F2 0F 10 44 24 38               movsd xmm0, qword ptr [rsp + 0x38]
009C8FF9  48 8D 0C 40                     lea rcx, [rax + rax*2]
009C8FFD  F2 41 0F 11 44 8D 04            movsd qword ptr [r13 + rcx*4 + 4], xmm0
009C9004  41 89 74 8D 0C                  mov dword ptr [r13 + rcx*4 + 0xc], esi
009C9009  48 8B 4B 48                     mov rcx, qword ptr [rbx + 0x48]
009C900D  BE 01 00 00 00                  mov esi, 1
009C9012  8B C7                           mov eax, edi
009C9014  48 0F B3 C1                     btr rcx, rax
009C9018  48 89 4B 48                     mov qword ptr [rbx + 0x48], rcx
009C901C  41 01 36                        add dword ptr [r14], esi
009C901F  03 FE                           add edi, esi
009C9021  83 FF 24                        cmp edi, 0x24
009C9024  0F 86 36 FF FF FF               jbe 0x1409c8f60
009C902A  44 8B 7C 24 54                  mov r15d, dword ptr [rsp + 0x54]
009C902F  E9 E2 00 00 00                  jmp 0x1409c9116
009C9034  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
009C9038  85 C0                           test eax, eax
009C903A  0F 84 D1 00 00 00               je 0x1409c9111
009C9040  4C 8B 95 60 03 00 00            mov r10, qword ptr [rbp + 0x360]
009C9047  4D 8B FD                        mov r15, r13
009C904A  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
009C904F  41 8B 0A                        mov ecx, dword ptr [r10]
009C9052  49 8B D1                        mov rdx, r9
009C9055  4C 8B 43 40                     mov r8, qword ptr [rbx + 0x40]
009C9059  48 D3 E2                        shl rdx, cl
009C905C  4C 85 C2                        test rdx, r8
009C905F  74 7A                           je 0x1409c90db
009C9061  44 01 4C 24 50                  add dword ptr [rsp + 0x50], r9d
009C9066  BF 00 00 00 00                  mov edi, 0
009C906B  49 8B 02                        mov rax, qword ptr [r10]
009C906E  41 BB 01 00 00 00               mov r11d, 1
009C9074  4C 8B 4B 48                     mov r9, qword ptr [rbx + 0x48]
009C9078  44 8B E8                        mov r13d, eax
009C907B  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
009C9080  41 8B CD                        mov ecx, r13d
009C9083  49 D3 E3                        shl r11, cl
009C9086  4C 85 5B 50                     test qword ptr [rbx + 0x50], r11
009C908A  49 8B C3                        mov rax, r11
009C908D  4C 89 5C 24 78                  mov qword ptr [rsp + 0x78], r11
009C9092  40 0F 95 C7                     setne dil
009C9096  49 23 C1                        and rax, r9
009C9099  48 F7 D8                        neg rax
009C909C  41 8B 42 08                     mov eax, dword ptr [r10 + 8]
009C90A0  1B C9                           sbb ecx, ecx
009C90A2  83 E1 02                        and ecx, 2
009C90A5  0B F9                           or edi, ecx
009C90A7  89 7C 24 40                     mov dword ptr [rsp + 0x40], edi
009C90AB  A8 04                           test al, 4
009C90AD  0F 84 C5 00 00 00               je 0x1409c9178
009C90B3  80 7C 24 30 00                  cmp byte ptr [rsp + 0x30], 0
009C90B8  74 1B                           je 0x1409c90d5
009C90BA  41 8B C5                        mov eax, r13d
009C90BD  49 0F B3 C1                     btr r9, rax
009C90C1  49 0F B3 C0                     btr r8, rax
009C90C5  4C 89 4B 48                     mov qword ptr [rbx + 0x48], r9
009C90C9  0F BA AB C8 00 00 00 0B         bts dword ptr [rbx + 0xc8], 0xb
009C90D1  4C 89 43 40                     mov qword ptr [rbx + 0x40], r8
009C90D5  41 B9 01 00 00 00               mov r9d, 1
009C90DB  49 83 C2 0C                     add r10, 0xc
009C90DF  4C 29 4C 24 70                  sub qword ptr [rsp + 0x70], r9
009C90E4  4C 89 95 60 03 00 00            mov qword ptr [rbp + 0x360], r10
009C90EB  0F 85 5E FF FF FF               jne 0x1409c904f
009C90F1  44 8B 4C 24 60                  mov r9d, dword ptr [rsp + 0x60]
009C90F6  44 8B 7C 24 54                  mov r15d, dword ptr [rsp + 0x54]
009C90FB  44 39 4C 24 50                  cmp dword ptr [rsp + 0x50], r9d
009C9100  72 04                           jb 0x1409c9106
009C9102  85 F6                           test esi, esi
009C9104  74 06                           je 0x1409c910c
009C9106  41 BF 06 01 00 00               mov r15d, 0x106
009C910C  4C 8B 6C 24 58                  mov r13, qword ptr [rsp + 0x58]
009C9111  BE 01 00 00 00                  mov esi, 1
009C9116  41 83 3E 00                     cmp dword ptr [r14], 0
009C911A  76 39                           jbe 0x1409c9155
009C911C  80 7C 24 30 00                  cmp byte ptr [rsp + 0x30], 0
009C9121  74 32                           je 0x1409c9155
009C9123  48 8B 45 88                     mov rax, qword ptr [rbp - 0x78]
009C9127  4C 8D 8D 50 01 00 00            lea r9, [rbp + 0x150]
009C912E  45 8B C4                        mov r8d, r12d
009C9131  48 8D 55 A0                     lea rdx, [rbp - 0x60]
009C9135  48 8B CB                        mov rcx, rbx
009C9138  40 88 30                        mov byte ptr [rax], sil
009C913B  41 8B C7                        mov eax, r15d
009C913E  C1 E8 1F                        shr eax, 0x1f
009C9141  40 32 C6                        xor al, sil
009C9144  88 44 24 28                     mov byte ptr [rsp + 0x28], al
009C9148  8B 44 24 48                     mov eax, dword ptr [rsp + 0x48]
009C914C  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
009C9150  E8 07 B3 F3 FF                  call 0x14090445c
009C9155  4D 85 ED                        test r13, r13
009C9158  0F 84 6E 02 00 00               je 0x1409c93cc
009C915E  41 8B 06                        mov eax, dword ptr [r14]
009C9161  3B C6                           cmp eax, esi
009C9163  0F 86 58 02 00 00               jbe 0x1409c93c1
009C9169  8D 04 40                        lea eax, [rax + rax*2]
009C916C  8D 04 85 04 00 00 00            lea eax, [rax*4 + 4]
009C9173  E9 4E 02 00 00                  jmp 0x1409c93c6
009C9178  49 23 D1                        and rdx, r9
009C917B  A8 02                           test al, 2
009C917D  0F 84 BD 01 00 00               je 0x1409c9340
009C9183  48 85 D2                        test rdx, rdx
009C9186  0F 85 49 FF FF FF               jne 0x1409c90d5
009C918C  38 54 24 30                     cmp byte ptr [rsp + 0x30], dl
009C9190  0F 84 9C 01 00 00               je 0x1409c9332
009C9196  4D 85 FF                        test r15, r15
009C9199  74 19                           je 0x1409c91b4
009C919B  41 8B 06                        mov eax, dword ptr [r14]
009C919E  F2 0F 10 44 24 38               movsd xmm0, qword ptr [rsp + 0x38]
009C91A4  48 8D 0C 40                     lea rcx, [rax + rax*2]
009C91A8  F2 41 0F 11 44 8F 04            movsd qword ptr [r15 + rcx*4 + 4], xmm0
009C91AF  41 89 7C 8F 0C                  mov dword ptr [r15 + rcx*4 + 0xc], edi
009C91B4  E8 3F D4 C3 FF                  call 0x1406065f8
009C91B9  45 33 C0                        xor r8d, r8d
009C91BC  45 8D 48 01                     lea r9d, [r8 + 1]
009C91C0  85 C0                           test eax, eax
009C91C2  75 25                           jne 0x1409c91e9
009C91C4  8B 54 24 48                     mov edx, dword ptr [rsp + 0x48]
009C91C8  F2 0F 10 44 24 38               movsd xmm0, qword ptr [rsp + 0x38]
009C91CE  48 8D 0C 52                     lea rcx, [rdx + rdx*2]
009C91D2  41 03 D1                        add edx, r9d
009C91D5  F2 0F 11 84 8D 50 01 00 00      movsd qword ptr [rbp + rcx*4 + 0x150], xmm0
009C91DE  89 BC 8D 58 01 00 00            mov dword ptr [rbp + rcx*4 + 0x158], edi
009C91E5  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
009C91E9  44 38 44 24 31                  cmp byte ptr [rsp + 0x31], r8b
009C91EE  74 52                           je 0x1409c9242
009C91F0  48 8B 4B 48                     mov rcx, qword ptr [rbx + 0x48]
009C91F4  4C 0F AB E9                     bts rcx, r13
009C91F8  48 89 4B 48                     mov qword ptr [rbx + 0x48], rcx
009C91FC  48 8B BD 60 03 00 00            mov rdi, qword ptr [rbp + 0x360]
009C9203  E8 80 65 B2 FF                  call 0x1404ef788
009C9208  85 C0                           test eax, eax
009C920A  0F 84 F1 00 00 00               je 0x1409c9301
009C9210  F7 83 C8 00 00 00 00 40 00 00   test dword ptr [rbx + 0xc8], 0x4000
009C921A  0F 84 E1 00 00 00               je 0x1409c9301
009C9220  8B 07                           mov eax, dword ptr [rdi]
009C9222  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
009C9227  48 0F A3 C1                     bt rcx, rax
009C922B  0F 83 CE 00 00 00               jae 0x1409c92ff
009C9231  48 8B 4B 48                     mov rcx, qword ptr [rbx + 0x48]
009C9235  4C 0F AB E9                     bts rcx, r13
009C9239  48 89 4B 48                     mov qword ptr [rbx + 0x48], rcx
009C923D  E9 BF 00 00 00                  jmp 0x1409c9301
009C9242  44 38 44 24 32                  cmp byte ptr [rsp + 0x32], r8b
009C9247  74 47                           je 0x1409c9290
009C9249  48 8B BD 60 03 00 00            mov rdi, qword ptr [rbp + 0x360]
009C9250  48 B9 84 06 16 20 11 00 00 00   movabs rcx, 0x1120160684
009C925A  8B 07                           mov eax, dword ptr [rdi]
009C925C  48 0F A3 C1                     bt rcx, rax
009C9260  72 0E                           jb 0x1409c9270
009C9262  48 8B 4B 48                     mov rcx, qword ptr [rbx + 0x48]
009C9266  4C 0F AB E9                     bts rcx, r13
009C926A  48 89 4B 48                     mov qword ptr [rbx + 0x48], rcx
009C926E  EB 03                           jmp 0x1409c9273
009C9270  41 03 F1                        add esi, r9d
009C9273  E8 10 65 B2 FF                  call 0x1404ef788
009C9278  85 C0                           test eax, eax
009C927A  74 87                           je 0x1409c9203
009C927C  48 B8 00 00 80 00 02 00 00 00   movabs rax, 0x200800000
009C9286  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
009C928B  E9 73 FF FF FF                  jmp 0x1409c9203
009C9290  44 38 44 24 4C                  cmp byte ptr [rsp + 0x4c], r8b
009C9295  0F 84 61 FF FF FF               je 0x1409c91fc
009C929B  E8 E8 64 B2 FF                  call 0x1404ef788
009C92A0  48 8B BD 60 03 00 00            mov rdi, qword ptr [rbp + 0x360]
009C92A7  85 C0                           test eax, eax
009C92A9  75 D1                           jne 0x1409c927c
009C92AB  8B 0F                           mov ecx, dword ptr [rdi]
009C92AD  44 8D 40 01                     lea r8d, [rax + 1]
009C92B1  41 8B D0                        mov edx, r8d
009C92B4  49 B9 00 00 80 00 02 00 00 00   movabs r9, 0x200800000
009C92BE  48 D3 E2                        shl rdx, cl
009C92C1  F7 83 C8 00 00 00 00 40 00 00   test dword ptr [rbx + 0xc8], 0x4000
009C92CB  4C 89 4C 24 68                  mov qword ptr [rsp + 0x68], r9
009C92D0  74 0D                           je 0x1409c92df
009C92D2  49 85 D1                        test r9, rdx
009C92D5  75 17                           jne 0x1409c92ee
009C92D7  41 03 F0                        add esi, r8d
009C92DA  E9 24 FF FF FF                  jmp 0x1409c9203
009C92DF  48 B8 00 00 80 02 02 00 00 00   movabs rax, 0x202800000
009C92E9  48 85 D0                        test rax, rdx
009C92EC  74 E9                           je 0x1409c92d7
009C92EE  48 8B 4B 48                     mov rcx, qword ptr [rbx + 0x48]
009C92F2  4C 0F AB E9                     bts rcx, r13
009C92F6  48 89 4B 48                     mov qword ptr [rbx + 0x48], rcx
009C92FA  E9 04 FF FF FF                  jmp 0x1409c9203
009C92FF  FF C6                           inc esi
009C9301  E8 F2 D2 C3 FF                  call 0x1406065f8
009C9306  85 C0                           test eax, eax
009C9308  74 21                           je 0x1409c932b
009C930A  48 8B 43 48                     mov rax, qword ptr [rbx + 0x48]
009C930E  48 85 44 24 78                  test qword ptr [rsp + 0x78], rax
009C9313  74 16                           je 0x1409c932b
009C9315  4C 8D 44 24 38                  lea r8, [rsp + 0x38]
009C931A  48 8D 54 24 48                  lea rdx, [rsp + 0x48]
009C931F  48 8D 8D 50 01 00 00            lea rcx, [rbp + 0x150]
009C9326  E8 21 D3 C3 FF                  call 0x14060664c
009C932B  4C 8B 95 60 03 00 00            mov r10, qword ptr [rbp + 0x360]
009C9332  41 B9 01 00 00 00               mov r9d, 1
009C9338  45 01 0E                        add dword ptr [r14], r9d
009C933B  E9 9B FD FF FF                  jmp 0x1409c90db
009C9340  48 85 D2                        test rdx, rdx
009C9343  0F 84 8C FD FF FF               je 0x1409c90d5
009C9349  80 7C 24 30 00                  cmp byte ptr [rsp + 0x30], 0
009C934E  74 E2                           je 0x1409c9332
009C9350  4D 85 FF                        test r15, r15
009C9353  74 19                           je 0x1409c936e
009C9355  41 8B 06                        mov eax, dword ptr [r14]
009C9358  F2 0F 10 44 24 38               movsd xmm0, qword ptr [rsp + 0x38]
009C935E  48 8D 0C 40                     lea rcx, [rax + rax*2]
009C9362  F2 41 0F 11 44 8F 04            movsd qword ptr [r15 + rcx*4 + 4], xmm0
009C9369  41 89 7C 8F 0C                  mov dword ptr [r15 + rcx*4 + 0xc], edi
009C936E  E8 85 D2 C3 FF                  call 0x1406065f8
009C9373  85 C0                           test eax, eax
009C9375  75 21                           jne 0x1409c9398
009C9377  F2 0F 10 44 24 38               movsd xmm0, qword ptr [rsp + 0x38]
009C937D  41 8B C4                        mov eax, r12d
009C9380  41 FF C4                        inc r12d
009C9383  44 89 64 24 34                  mov dword ptr [rsp + 0x34], r12d
009C9388  48 8D 0C 40                     lea rcx, [rax + rax*2]
009C938C  F2 0F 11 44 8D A0               movsd qword ptr [rbp + rcx*4 - 0x60], xmm0
009C9392  89 7C 8D A8                     mov dword ptr [rbp + rcx*4 - 0x58], edi
009C9396  EB 18                           jmp 0x1409c93b0
009C9398  4C 8D 44 24 38                  lea r8, [rsp + 0x38]
009C939D  48 8D 54 24 34                  lea rdx, [rsp + 0x34]
009C93A2  48 8D 4D A0                     lea rcx, [rbp - 0x60]
009C93A6  E8 A1 D2 C3 FF                  call 0x14060664c
009C93AB  44 8B 64 24 34                  mov r12d, dword ptr [rsp + 0x34]
009C93B0  48 8B 4B 48                     mov rcx, qword ptr [rbx + 0x48]
009C93B4  4C 0F B3 E9                     btr rcx, r13
009C93B8  48 89 4B 48                     mov qword ptr [rbx + 0x48], rcx
009C93BC  E9 6A FF FF FF                  jmp 0x1409c932b
009C93C1  B8 10 00 00 00                  mov eax, 0x10
009C93C6  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
009C93CA  89 01                           mov dword ptr [rcx], eax
009C93CC  41 8B C7                        mov eax, r15d
009C93CF  48 8B 8D 00 03 00 00            mov rcx, qword ptr [rbp + 0x300]
009C93D6  48 33 CC                        xor rcx, rsp
009C93D9  E8 62 32 CE FF                  call 0x1406ac640
009C93DE  4C 8D 9C 24 10 04 00 00         lea r11, [rsp + 0x410]
009C93E6  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
009C93EA  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
009C93EE  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
009C93F2  49 8B E3                        mov rsp, r11
009C93F5  41 5F                           pop r15
009C93F7  41 5E                           pop r14
009C93F9  41 5D                           pop r13
009C93FB  41 5C                           pop r12
009C93FD  5D                              pop rbp
009C93FE  C3                              ret
009C93FF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SepAdjustPrivileges(__int64 a1, int a2, unsigned __int8 a3, int a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m3C0;
    unsigned __int64 v_stack_m3C8;
    unsigned __int64 v_stack_m3D0;
    unsigned int v_stack_m3D8;
    unsigned int v_stack_m3DC;
    unsigned __int64 v_stack_m3E0;
    unsigned int v_stack_m3E4;
    unsigned int v_stack_m3E8;
    unsigned __int8 v_stack_m3EC;
    unsigned int v_stack_m3F0;
    unsigned int v_stack_m3F8;
    unsigned __int64 v_stack_m400;
    unsigned int v_stack_m404;
    unsigned __int8 v_stack_m406;
    unsigned __int8 v_stack_m407;
    unsigned __int8 v_stack_m408;
    unsigned __int8 v_stack_m410;
    unsigned int v_stack_m418;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (0x410ULL);
    result = (*(unsigned __int64 *)(v_rip + 4462871)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 824 + 768) = result;
    a1 = 0;
    *(unsigned __int64 *)(v_rsp - 824 - 112) = *(unsigned __int64 *)(v_rsp - 824 + 880);
    result = 0;
    v_stack_m3E8 = 0;
    v_stack_m407 = 0;
    v_stack_m406 = 0;
    v_stack_m3EC = 0;
    v_stack_m3D0 = 0;
    v_stack_m404 = 0;
    v_stack_m3F0 = 0;
    v_stack_m408 = (unsigned __int8)(a2);
    a2 = 0;
    v_stack_m400 = 0;
    v_stack_m3F8 = 0;
    v_stack_m3D8 = a4;
    v_stack_m3E0 = *(unsigned __int64 *)(v_rsp - 824 + 872);
    *(unsigned __int64 *)(v_rsp - 824 - 120) = *(unsigned __int64 *)(v_rsp - 824 + 896);
    v_stack_m3C0 = v_xmm0;
    result = memset(v_rsp - 824 - 96, a2, 432, a4);
    a2 = 0;
    result = memset(v_rsp - 824 + 336, a2, 432, a4);
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rsp - 824 + 896)) = 0;
    result = SepCopyTokenIntegrity(0, v_stack_m3C0, 432, a4);
    result = RtlSidDominates(v_stack_m3C0, *(unsigned __int64 *)(v_rip + 5491021), v_stack_m407, a4);
    v_stack_m3E4 = (unsigned int)(result);
    if (sign_flag) goto loc_009C93CF;
    if (v_stack_m407 != 0) goto loc_009C8F47;
    result = RtlSidDominates(v_stack_m3C0, *(unsigned __int64 *)(v_rip + 5490963), v_stack_m406, a4);
    v_stack_m3E4 = (unsigned int)(result);
    if (sign_flag) goto loc_009C93CF;
    result = (unsigned __int8)((unsigned int)(v_stack_m3EC));
    if (v_stack_m406 == 0) { result = 1; }
    v_stack_m3EC = (unsigned int)(result);
    goto loc_009C8F4D;
loc_009C8F47:
loc_009C8F4D:
    if (a3 == 0) goto loc_009C9034;
    v_rdi = 0;
loc_009C8F60:
    a2 = (v_rdi + 1) << (0);
    if (((*(unsigned __int64 *)(a1 + 72)) & (a2)) == 0) goto loc_009C901F;
    if ((unsigned __int8)(v_stack_m408) == 0) goto loc_009C901C;
    result = (*(unsigned __int64 *)(a1 + 80)) & (a2);
    result = -(result);
    v_stack_m3E0 = (unsigned int)((int)(0));
    v_rsi = (unsigned int)(-(v_rdi + 1));
    v_rsi = (unsigned int)((v_rsi) + (2));
    result = ((int)(0)) >> (32);
    v_stack_m3DC = (unsigned int)(result);
    v_stack_m400 = v_stack_m3E0;
    v_stack_m3F8 = (unsigned int)(v_rsi);
    result = Feature_3055530299__private_IsEnabledDeviceUsageNoInline(0, a2, v_stack_m406, 1);
    if ((unsigned int)(result) != 0) goto loc_009C8FD3;
    v_r12 = (unsigned int)((0) + 1);
    v_stack_m404 = (unsigned int)(v_r12);
    *(unsigned __int64 *)(v_rsp - 824 + 0 + 0 * 2 * 4 - 96) = v_xmm0;
    *(unsigned int *)(v_rsp - 824 + 0 + 0 * 2 * 4 - 88) = (unsigned int)(v_rsi);
    goto loc_009C8FEB;
loc_009C8FD3:
    result = SepTryAddUniqueAuditPrivilege(v_rsp - 824 - 96, v_stack_m404, v_stack_m400, 1);
loc_009C8FEB:
    if (*(unsigned __int64 *)(v_rsp - 824 + 872) != 0) {
        result = *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 824 + 888));
        a1 = result + result * 2;
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 824 + 872) + a1 * 4 + 4) = v_xmm0;
        *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 824 + 872) + a1 * 4 + 12) = (unsigned int)(v_rsi);
    }
    *(unsigned __int64 *)(a1 + 72) = *(unsigned __int64 *)(a1 + 72);
loc_009C901C:
loc_009C901F:
    v_rdi = (unsigned int)((v_rdi) + (1));
    if (((unsigned int)(v_rdi)) <= 36) goto loc_009C8F60;
    goto loc_009C9116;
loc_009C9034:
    if ((unsigned int)((unsigned int)(v_stack_m3D8)) == 0) goto loc_009C9111;
    v_stack_m3C8 = (unsigned int)(v_stack_m3D8);
loc_009C904F:
    a2 = (1) << ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 824 + 864)))));
    if (((a2) & (*(unsigned __int64 *)(a1 + 64))) == 0) goto loc_009C90DB;
    v_stack_m400 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 824 + 864));
    v_r11 = (1) << ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 824 + 864))))))));
    v_stack_m3C0 = v_r11;
    v_rdi = (((*(unsigned __int64 *)(a1 + 80)) & (v_r11)) != 0) ? 1 : 0;
    result = (v_r11) & (*(unsigned __int64 *)(a1 + 72));
    result = -(result);
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 824 + 864))))))) & (2));
    v_rdi = (unsigned int)((v_rdi) | ((unsigned int)(a1)));
    v_stack_m3F8 = (unsigned int)(v_rdi);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 824 + 864) + 8)))) & (4)) == 0) goto loc_009C9178;
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 824 + 864) + 8));
    if (v_stack_m408 != 0) {
        result = (unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 824 + 864)))));
        *(unsigned __int64 *)(a1 + 72) = *(unsigned __int64 *)(a1 + 72);
        *(unsigned __int64 *)(a1 + 64) = *(unsigned __int64 *)(a1 + 64);
    }
loc_009C90DB:
    v_r10 = (*(unsigned __int64 *)(v_rsp - 824 + 864)) + (12);
    *(unsigned __int64 *)(v_rsp - 824 + 864) = v_r10;
    if (condition_is_not_equal) goto loc_009C904F;
    if (v_stack_m3E8 < ((unsigned int)((unsigned int)(v_stack_m3D8)))) goto loc_009C9106;
    v_r15 = (unsigned int)(v_stack_m3E4);
    if (1 != 0) {
        v_r15 = 262;
    }
loc_009C9111:
loc_009C9116:
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 824 + 888))) <= 0) goto loc_009C9155;
    if (v_stack_m408 != 0) {
        result = *(unsigned __int64 *)(v_rsp - 824 - 120);
        a4 = v_rsp - 824 + 336;
        a3 = (unsigned int)((unsigned int)(v_stack_m404));
        a2 = v_rsp - 824 - 96;
        a1 = a1;
        *(unsigned __int8 *)(result) = 1;
        result = (unsigned int)(v_r15);
        result = (unsigned int)((result) >> (31));
        result = (unsigned __int8)((result) ^ (1));
        v_stack_m410 = (unsigned __int8)(result);
        result = v_stack_m3F0;
        v_stack_m418 = (unsigned int)(result);
        result = SepAdtTokenRightAdjusted(a1, a2, a3, a4);
    }
    if (v_stack_m3E0 == 0) goto loc_009C93CC;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 824 + 888))))) <= 1) goto loc_009C93C1;
    goto loc_009C93C6;
loc_009C9178:
    a2 = (a2) & (a4);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 824 + 888))) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 824 + 888))) * 2 * 4 + 4)) & (2)) == 0) goto loc_009C9340;
    if (a2 != 0) goto loc_009C90D5;
    if (v_stack_m408 == ((unsigned __int8)(a2))) goto loc_009C9332;
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 824 + 888))) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 824 + 888))) * 2 * 4 + 4;
    if (v_r15 != 0) {
        result = *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 824 + 888));
        a1 = result + result * 2;
        *(unsigned __int64 *)(v_r15 + a1 * 4 + 4) = v_xmm0;
        *(unsigned int *)(v_r15 + a1 * 4 + 12) = (unsigned int)(v_rdi);
    }
    result = Feature_3055530299__private_IsEnabledDeviceUsageNoInline(a1, a2, a3, a4);
    a3 = 0;
    if ((unsigned int)(result) == 0) {
        a2 = v_stack_m3F0;
        a1 = a2 + a2 * 2;
        a2 = (unsigned int)((a2) + ((unsigned int)(a3 + 1)));
        *(unsigned __int64 *)(v_rsp - 824 + a1 * 4 + 336) = v_xmm0;
        *(unsigned int *)(v_rsp - 824 + a1 * 4 + 344) = (unsigned int)(v_rdi);
        v_stack_m3F0 = a2;
    }
    if (v_stack_m407 == 0) goto loc_009C9242;
    *(unsigned __int64 *)(a1 + 72) = *(unsigned __int64 *)(a1 + 72);
loc_009C91FC:
loc_009C9203:
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline(*(unsigned __int64 *)(a1 + 72), a2, a3, a3 + 1);
    if ((unsigned int)(result) == 0) goto loc_009C9301;
    if (((*(unsigned int *)(a1 + 200)) & (0x4000ULL)) == 0) goto loc_009C9301;
    if (condition_is_above_or_equal) goto loc_009C92FF;
    *(unsigned __int64 *)(a1 + 72) = *(unsigned __int64 *)(a1 + 72);
    goto loc_009C9301;
loc_009C9242:
    if (v_stack_m406 == 0) goto loc_009C9290;
    if (v_stack_m406 < 0) goto loc_009C9270;
    *(unsigned __int64 *)(a1 + 72) = *(unsigned __int64 *)(a1 + 72);
    goto loc_009C9273;
loc_009C9270:
    v_rsi = (unsigned int)((1) + ((unsigned int)(a3 + 1)));
loc_009C9273:
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline(*(unsigned __int64 *)(a1 + 72), a2, a3, a3 + 1);
    if ((unsigned int)(result) == 0) goto loc_009C9203;
loc_009C927C:
    v_stack_m3D0 = result;
    goto loc_009C9203;
loc_009C9290:
    if (v_stack_m3EC == 0) goto loc_009C91FC;
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline(*(unsigned __int64 *)(a1 + 72), a2, a3, a3 + 1);
    if ((unsigned int)(result) != 0) goto loc_009C927C;
    a2 = ((unsigned int)((unsigned int)(result + 1))) << ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 824 + 864)))));
    v_stack_m3D0 = a3 + 1;
    if (((*(unsigned int *)(a1 + 200)) & (0x4000ULL)) == 0) goto loc_009C92DF;
    if (((a3 + 1) & (a2)) != 0) goto loc_009C92EE;
loc_009C92D7:
    v_rsi = (unsigned int)((v_rsi) + ((unsigned int)(result + 1)));
    goto loc_009C9203;
loc_009C92DF:
    if (((result) & (a2)) == 0) goto loc_009C92D7;
loc_009C92EE:
    *(unsigned __int64 *)(a1 + 72) = *(unsigned __int64 *)(a1 + 72);
    goto loc_009C9203;
loc_009C92FF:
    v_rsi = (unsigned int)((v_rsi) + 1);
loc_009C9301:
    result = Feature_3055530299__private_IsEnabledDeviceUsageNoInline(*(unsigned __int64 *)(a1 + 72), a2, result + 1, a3 + 1);
    if ((unsigned int)(result) == 0) goto loc_009C932B;
    result = *(unsigned __int64 *)(a1 + 72);
    if (((v_stack_m3C0) & (*(unsigned __int64 *)(a1 + 72))) != 0) {
        a3 = v_stack_m400;
        a2 = v_stack_m3F0;
        a1 = v_rsp - 824 + 336;
        result = SepTryAddUniqueAuditPrivilege(a1, a2, a3, a3 + 1);
    }
loc_009C9332:
    goto loc_009C90DB;
loc_009C9340:
    if (a2 == 0) goto loc_009C90D5;
    if (v_stack_m408 == 0) goto loc_009C9332;
    if (v_r15 != 0) {
        result = *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 824 + 888));
        a1 = result + result * 2;
        *(unsigned __int64 *)(v_r15 + a1 * 4 + 4) = v_xmm0;
        *(unsigned int *)(v_r15 + a1 * 4 + 12) = (unsigned int)(*(unsigned __int64 *)(v_rsp - 824 + 864));
    }
    result = Feature_3055530299__private_IsEnabledDeviceUsageNoInline(a1, a2, a3, 1);
    if ((unsigned int)(result) != 0) goto loc_009C9398;
    v_r12 = (unsigned int)(((unsigned int)(v_stack_m404)) + 1);
    v_stack_m404 = (unsigned int)(v_r12);
    *(unsigned __int64 *)(v_rsp - 824 + (unsigned int)((unsigned int)((unsigned int)(v_stack_m404))) + (unsigned int)((unsigned int)((unsigned int)(v_stack_m404))) * 2 * 4 - 96) = v_xmm0;
    *(unsigned int *)(v_rsp - 824 + (unsigned int)((unsigned int)((unsigned int)(v_stack_m404))) + (unsigned int)((unsigned int)((unsigned int)(v_stack_m404))) * 2 * 4 - 88) = (unsigned int)(*(unsigned __int64 *)(v_rsp - 824 + 864));
    goto loc_009C93B0;
loc_009C9398:
    result = SepTryAddUniqueAuditPrivilege(v_rsp - 824 - 96, v_stack_m404, v_stack_m400, 1);
loc_009C93B0:
    *(unsigned __int64 *)(a1 + 72) = *(unsigned __int64 *)(a1 + 72);
    goto loc_009C932B;
loc_009C93C1:
loc_009C93C6:
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 824 - 112)) = 16;
loc_009C93CC:
loc_009C93CF:
    a1 = (*(unsigned __int64 *)(v_rsp - 824 + 768)) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m404, v_stack_m400, 1);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SepAdjustPrivileges(void *Arg1, int32_t Arg2, uint8_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m3C0;
    uint64_t v_stack_m3C8;
    uint64_t v_stack_m3D0;
    uint32_t v_stack_m3D8;
    uint32_t v_stack_m3DC;
    uint64_t v_stack_m3E0;
    uint32_t v_stack_m3E4;
    uint32_t v_stack_m3E8;
    uint8_t v_stack_m3EC;
    uint32_t v_stack_m3F0;
    uint32_t v_stack_m3F8;
    uint64_t v_stack_m400;
    uint32_t v_stack_m404;
    uint8_t v_stack_m406;
    uint8_t v_stack_m407;
    uint8_t v_stack_m408;
    uint8_t v_stack_m410;
    uint32_t v_stack_m418;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (0x410ULL);
    result = (*(uint64_t *)(v_rip + 0x441917)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x338 + 0x300) = result;
    Arg1 = 0;
    *(uint64_t *)(local_rsp - 0x338 - 0x70) = *(uint64_t *)(local_rsp - 0x338 + 0x370);
    result = 0;
    v_stack_m3E8 = 0;
    v_stack_m407 = 0;
    v_stack_m406 = 0;
    v_stack_m3EC = 0;
    v_stack_m3D0 = 0;
    v_stack_m404 = 0;
    v_stack_m3F0 = 0;
    v_stack_m408 = (uint8_t)(Arg2);
    Arg2 = 0;
    v_stack_m400 = 0;
    v_stack_m3F8 = 0;
    v_stack_m3D8 = Arg4;
    v_stack_m3E0 = *(uint64_t *)(local_rsp - 0x338 + 0x368);
    *(uint64_t *)(local_rsp - 0x338 - 0x78) = *(uint64_t *)(local_rsp - 0x338 + 0x380);
    v_stack_m3C0 = v_xmm0;
    result = memset(local_rsp - 824 - 96, Arg2, 432, Arg4);
    Arg2 = 0;
    result = memset(local_rsp - 824 + 336, Arg2, 432, Arg4);
    *(uint8_t *)(*(uint64_t *)(local_rsp - 0x338 + 0x380)) = 0;
    result = SepCopyTokenIntegrity(0, v_stack_m3C0, 432, Arg4);
    result = RtlSidDominates(v_stack_m3C0, *(uint64_t *)(v_rip + 0x53C94D), v_stack_m407, Arg4);
    v_stack_m3E4 = (uint32_t)(result);
    if (sign_flag) goto loc_009C93CF;
    if (v_stack_m407 != 0) goto loc_009C8F47;
    result = RtlSidDominates(v_stack_m3C0, *(uint64_t *)(v_rip + 0x53C913), v_stack_m406, Arg4);
    v_stack_m3E4 = (uint32_t)(result);
    if (sign_flag) goto loc_009C93CF;
    result = (uint8_t)((uint32_t)(v_stack_m3EC));
    if (v_stack_m406 == 0) { result = 1; }
    v_stack_m3EC = (uint32_t)(result);
    goto loc_009C8F4D;
loc_009C8F47:
loc_009C8F4D:
    if (Arg3 == 0) goto loc_009C9034;
    local_rdi = 0;
loc_009C8F60:
    Arg2 = (local_rdi + 1) << (0);
    if (((*(uint64_t *)(arg1 + 0x48)) & (Arg2)) == 0) goto loc_009C901F;
    if ((uint8_t)(v_stack_m408) == 0) goto loc_009C901C;
    result = (*(uint64_t *)(arg1 + 0x50)) & (Arg2);
    result = -(result);
    v_stack_m3E0 = (uint32_t)((int32_t)(0));
    local_rsi = (uint32_t)(-(local_rdi + 1));
    local_rsi = (uint32_t)((local_rsi) + (2));
    result = ((int32_t)(0)) >> (32);
    v_stack_m3DC = (uint32_t)(result);
    v_stack_m400 = v_stack_m3E0;
    v_stack_m3F8 = (uint32_t)(local_rsi);
    result = Feature_3055530299__private_IsEnabledDeviceUsageNoInline(0, Arg2, v_stack_m406, 1);
    if ((uint32_t)(result) != 0) goto loc_009C8FD3;
    local_r12 = (uint32_t)((0) + 1);
    v_stack_m404 = (uint32_t)(local_r12);
    *(uint64_t *)(local_rsp - 0x338 + 0x0 + 0x0 * 2 * 4 - 0x60) = v_xmm0;
    *(uint32_t *)(local_rsp - 0x338 + 0x0 + 0x0 * 2 * 4 - 0x58) = (uint32_t)(local_rsi);
    goto loc_009C8FEB;
loc_009C8FD3:
    result = SepTryAddUniqueAuditPrivilege(local_rsp - 824 - 96, v_stack_m404, v_stack_m400, 1);
loc_009C8FEB:
    if (*(uint64_t *)(local_rsp - 0x338 + 0x368) != 0) {
        result = *(uint32_t *)(*(uint64_t *)(local_rsp - 0x338 + 0x378));
        Arg1 = result + result * 2;
        *(uint64_t *)(*(uint64_t *)(local_rsp - 0x338 + 0x368) + arg1 * 4 + 0x4) = v_xmm0;
        *(uint32_t *)(*(uint64_t *)(local_rsp - 0x338 + 0x368) + arg1 * 4 + 0xC) = (uint32_t)(local_rsi);
    }
    *(uint64_t *)(arg1 + 0x48) = *(uint64_t *)(arg1 + 0x48);
loc_009C901C:
loc_009C901F:
    local_rdi = (uint32_t)((local_rdi) + (1));
    if (((uint32_t)(local_rdi)) <= 36) goto loc_009C8F60;
    goto loc_009C9116;
loc_009C9034:
    if ((uint32_t)((uint32_t)(v_stack_m3D8)) == 0) goto loc_009C9111;
    v_stack_m3C8 = (uint32_t)(v_stack_m3D8);
loc_009C904F:
    Arg2 = (1) << ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x338 + 0x360)))));
    if (((Arg2) & (*(uint64_t *)(arg1 + 0x40))) == 0) goto loc_009C90DB;
    v_stack_m400 = *(uint64_t *)(*(uint64_t *)(local_rsp - 0x338 + 0x360));
    local_r11 = (1) << ((uint8_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x338 + 0x360))))))));
    v_stack_m3C0 = local_r11;
    local_rdi = (((*(uint64_t *)(arg1 + 0x50)) & (local_r11)) != 0) ? 1 : 0;
    result = (local_r11) & (*(uint64_t *)(arg1 + 0x48));
    result = -(result);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x338 + 0x360))))))) & (2));
    local_rdi = (uint32_t)((local_rdi) | ((uint32_t)(Arg1)));
    v_stack_m3F8 = (uint32_t)(local_rdi);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x338 + 0x360) + 0x8)))) & (4)) == 0) goto loc_009C9178;
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x338 + 0x360) + 0x8));
    if (v_stack_m408 != 0) {
        result = (uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x338 + 0x360)))));
        *(uint64_t *)(arg1 + 0x48) = *(uint64_t *)(arg1 + 0x48);
        *(uint64_t *)(arg1 + 0x40) = *(uint64_t *)(arg1 + 0x40);
    }
loc_009C90DB:
    local_r10 = (*(uint64_t *)(local_rsp - 0x338 + 0x360)) + (12);
    *(uint64_t *)(local_rsp - 0x338 + 0x360) = local_r10;
    if (condition_is_not_equal) goto loc_009C904F;
    if (v_stack_m3E8 < ((uint32_t)((uint32_t)(v_stack_m3D8)))) goto loc_009C9106;
    local_r15 = (uint32_t)(v_stack_m3E4);
    if (1 != 0) {
        local_r15 = 262;
    }
loc_009C9111:
loc_009C9116:
    if ((*(uint32_t *)(*(uint64_t *)(local_rsp - 0x338 + 0x378))) <= 0) goto loc_009C9155;
    if (v_stack_m408 != 0) {
        result = *(uint64_t *)(local_rsp - 0x338 - 0x78);
        Arg4 = local_rsp - 824 + 336;
        Arg3 = (uint32_t)((uint32_t)(v_stack_m404));
        Arg2 = local_rsp - 824 - 96;
        Arg1 = Arg1;
        *(uint8_t *)(result) = 1;
        result = (uint32_t)(local_r15);
        result = (uint32_t)((result) >> (31));
        result = (uint8_t)((result) ^ (1));
        v_stack_m410 = (uint8_t)(result);
        result = v_stack_m3F0;
        v_stack_m418 = (uint32_t)(result);
        result = SepAdtTokenRightAdjusted(Arg1, Arg2, Arg3, Arg4);
    }
    if (v_stack_m3E0 == 0) goto loc_009C93CC;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x338 + 0x378))))) <= 1) goto loc_009C93C1;
    goto loc_009C93C6;
loc_009C9178:
    Arg2 = (Arg2) & (Arg4);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x338 + 0x378))) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x338 + 0x378))) * 2 * 4 + 4)) & (2)) == 0) goto loc_009C9340;
    if (Arg2 != 0) goto loc_009C90D5;
    if (v_stack_m408 == ((uint8_t)(Arg2))) goto loc_009C9332;
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x338 + 0x378))) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x338 + 0x378))) * 2 * 4 + 4;
    if (local_r15 != 0) {
        result = *(uint32_t *)(*(uint64_t *)(local_rsp - 0x338 + 0x378));
        Arg1 = result + result * 2;
        *(uint64_t *)(local_r15 + arg1 * 4 + 0x4) = v_xmm0;
        *(uint32_t *)(local_r15 + arg1 * 4 + 0xC) = (uint32_t)(local_rdi);
    }
    result = Feature_3055530299__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, Arg3, Arg4);
    Arg3 = 0;
    if ((uint32_t)(result) == 0) {
        Arg2 = v_stack_m3F0;
        Arg1 = Arg2 + Arg2 * 2;
        Arg2 = (uint32_t)((Arg2) + ((uint32_t)(Arg3 + 1)));
        *(uint64_t *)(local_rsp - 0x338 + arg1 * 4 + 0x150) = v_xmm0;
        *(uint32_t *)(local_rsp - 0x338 + arg1 * 4 + 0x158) = (uint32_t)(local_rdi);
        v_stack_m3F0 = Arg2;
    }
    if (v_stack_m407 == 0) goto loc_009C9242;
    *(uint64_t *)(arg1 + 0x48) = *(uint64_t *)(arg1 + 0x48);
loc_009C91FC:
loc_009C9203:
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline(*(uint64_t *)(arg1 + 0x48), Arg2, Arg3, Arg3 + 1);
    if ((uint32_t)(result) == 0) goto loc_009C9301;
    if (((*(uint32_t *)(arg1 + 0xC8)) & (0x4000ULL)) == 0) goto loc_009C9301;
    if (condition_is_above_or_equal) goto loc_009C92FF;
    *(uint64_t *)(arg1 + 0x48) = *(uint64_t *)(arg1 + 0x48);
    goto loc_009C9301;
loc_009C9242:
    if (v_stack_m406 == 0) goto loc_009C9290;
    if (v_stack_m406 < 0) goto loc_009C9270;
    *(uint64_t *)(arg1 + 0x48) = *(uint64_t *)(arg1 + 0x48);
    goto loc_009C9273;
loc_009C9270:
    local_rsi = (uint32_t)((1) + ((uint32_t)(Arg3 + 1)));
loc_009C9273:
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline(*(uint64_t *)(arg1 + 0x48), Arg2, Arg3, Arg3 + 1);
    if ((uint32_t)(result) == 0) goto loc_009C9203;
loc_009C927C:
    v_stack_m3D0 = result;
    goto loc_009C9203;
loc_009C9290:
    if (v_stack_m3EC == 0) goto loc_009C91FC;
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline(*(uint64_t *)(arg1 + 0x48), Arg2, Arg3, Arg3 + 1);
    if ((uint32_t)(result) != 0) goto loc_009C927C;
    Arg2 = ((uint32_t)((uint32_t)(result + 1))) << ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x338 + 0x360)))));
    v_stack_m3D0 = Arg3 + 1;
    if (((*(uint32_t *)(arg1 + 0xC8)) & (0x4000ULL)) == 0) goto loc_009C92DF;
    if (((Arg3 + 1) & (Arg2)) != 0) goto loc_009C92EE;
loc_009C92D7:
    local_rsi = (uint32_t)((local_rsi) + ((uint32_t)(result + 1)));
    goto loc_009C9203;
loc_009C92DF:
    if (((result) & (Arg2)) == 0) goto loc_009C92D7;
loc_009C92EE:
    *(uint64_t *)(arg1 + 0x48) = *(uint64_t *)(arg1 + 0x48);
    goto loc_009C9203;
loc_009C92FF:
    local_rsi = (uint32_t)((local_rsi) + 1);
loc_009C9301:
    result = Feature_3055530299__private_IsEnabledDeviceUsageNoInline(*(uint64_t *)(arg1 + 0x48), Arg2, result + 1, Arg3 + 1);
    if ((uint32_t)(result) == 0) goto loc_009C932B;
    result = *(uint64_t *)(arg1 + 0x48);
    if (((v_stack_m3C0) & (*(uint64_t *)(arg1 + 0x48))) != 0) {
        Arg3 = v_stack_m400;
        Arg2 = v_stack_m3F0;
        Arg1 = local_rsp - 824 + 336;
        result = SepTryAddUniqueAuditPrivilege(Arg1, Arg2, Arg3, Arg3 + 1);
    }
loc_009C9332:
    goto loc_009C90DB;
loc_009C9340:
    if (Arg2 == 0) goto loc_009C90D5;
    if (v_stack_m408 == 0) goto loc_009C9332;
    if (local_r15 != 0) {
        result = *(uint32_t *)(*(uint64_t *)(local_rsp - 0x338 + 0x378));
        Arg1 = result + result * 2;
        *(uint64_t *)(local_r15 + arg1 * 4 + 0x4) = v_xmm0;
        *(uint32_t *)(local_r15 + arg1 * 4 + 0xC) = (uint32_t)(*(uint64_t *)(local_rsp - 0x338 + 0x360));
    }
    result = Feature_3055530299__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, Arg3, 1);
    if ((uint32_t)(result) != 0) goto loc_009C9398;
    local_r12 = (uint32_t)(((uint32_t)(v_stack_m404)) + 1);
    v_stack_m404 = (uint32_t)(local_r12);
    *(uint64_t *)(local_rsp - 0x338 + (uint32_t)((uint32_t)((uint32_t)(v_stack_m404))) + (uint32_t)((uint32_t)((uint32_t)(v_stack_m404))) * 2 * 4 - 0x60) = v_xmm0;
    *(uint32_t *)(local_rsp - 0x338 + (uint32_t)((uint32_t)((uint32_t)(v_stack_m404))) + (uint32_t)((uint32_t)((uint32_t)(v_stack_m404))) * 2 * 4 - 0x58) = (uint32_t)(*(uint64_t *)(local_rsp - 0x338 + 0x360));
    goto loc_009C93B0;
loc_009C9398:
    result = SepTryAddUniqueAuditPrivilege(local_rsp - 824 - 96, v_stack_m404, v_stack_m400, 1);
loc_009C93B0:
    *(uint64_t *)(arg1 + 0x48) = *(uint64_t *)(arg1 + 0x48);
    goto loc_009C932B;
loc_009C93C1:
loc_009C93C6:
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x338 - 0x70)) = 16;
loc_009C93CC:
loc_009C93CF:
    Arg1 = (*(uint64_t *)(local_rsp - 0x338 + 0x300)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m404, v_stack_m400, 1);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg1` | `+ 0x40` | `64` | `W` |
| `Arg1` | `+ 0x48` | `64` | `R` |
| `Arg1` | `+ 0x48` | `64` | `W` |
| `Arg1` | `+ 0x50` | `64` | `R` |
| `Arg1` | `+ 0xC8` | `32` | `R` |
| `Arg1` | `+ 0xC8` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009C8DFC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
