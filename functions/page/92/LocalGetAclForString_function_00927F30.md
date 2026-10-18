# LocalGetAclForString

- RVA: `0x00927F30`–`0x00928F9C` (길이 `4,204` bytes)
- VA: `0x0000000140927F30`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0008D770`
- 디코드: `1,058`개 명령, `4,204/4,204` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **46**; 고유 호출 대상: **28**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x00927FD0` → [wcsnicmp](../../text/50/wcsnicmp_function_005001C0.md) (function, `0x005001C0`)
- `0x00927FF5` → [FContainCallBackAce](FContainCallBackAce_function_00928FB0.md) (function, `0x00928FB0`)
- `0x0092800D` → [wcschr](../../text/50/wcschr_function_00501A60.md) (function, `0x00501A60`)
- `0x0092806D` → [LocalGetAceCount](LocalGetAceCount_function_00929140.md) (function, `0x00929140`)
- `0x0092808F` → [SddlpAlloc](SddlpAlloc_function_00925F88.md) (function, `0x00925F88`)
- `0x009280AA` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x009280F9` → [RtlNtStatusToDosError](RtlNtStatusToDosError_function_00926C40.md) (function, `0x00926C40`)
- `0x00928143` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0092821B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0092823C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0092829A` → [wcsnicmp](../../text/50/wcsnicmp_function_005001C0.md) (function, `0x005001C0`)
- `0x009282B8` → [wcstoul](../../text/50/wcstoul_function_005024A0.md) (function, `0x005024A0`)
- `0x009283AC` → [LookupSidInTable](LookupSidInTable_function_009293C0.md) (function, `0x009293C0`)
- `0x00928433` → [RtlLengthSid](../../text/45/RtlLengthSid_function_0045D270.md) (function, `0x0045D270`)
- `0x00928488` → [RtlValidSid](RtlValidSid_function_00929710.md) (function, `0x00929710`)
- `0x009284B8` → [RtlValidAcl](RtlValidAcl_function_0092A7A0.md) (function, `0x0092A7A0`)
- `0x0092853D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0092855C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009285A8` → [SddlpAlloc](SddlpAlloc_function_00925F88.md) (function, `0x00925F88`)
- `0x00928666` → [wcsnicmp](../../text/50/wcsnicmp_function_005001C0.md) (function, `0x005001C0`)
- `0x0092874B` → [wcsnicmp](../../text/50/wcsnicmp_function_005001C0.md) (function, `0x005001C0`)
- `0x009287CE` → [SddlAddMandatoryAce](../9A/SddlAddMandatoryAce_function_009A98AC.md) (function, `0x009A98AC`)
- `0x00928857` → [RtlCopySid](../9A/RtlCopySid_function_009A9A50.md) (function, `0x009A9A50`)
- `0x009288DF` → [LocalpConvertStringSidToSid](../A1/LocalpConvertStringSidToSid_function_00A17490.md) (function, `0x00A17490`)
- `0x00928995` → [SddlpAlloc](SddlpAlloc_function_00925F88.md) (function, `0x00925F88`)
- `0x009289CC` → [RtlLengthSid](../../text/45/RtlLengthSid_function_0045D270.md) (function, `0x0045D270`)
- `0x009289DA` → [RtlCopySid](../9A/RtlCopySid_function_009A9A50.md) (function, `0x009A9A50`)
- `0x009289EC` → [RtlLengthSid](../../text/45/RtlLengthSid_function_0045D270.md) (function, `0x0045D270`)
- `0x00928A01` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00928A21` → [RtlAddAce](RtlAddAce_function_00929D70.md) (function, `0x00929D70`)
- `0x00928A2D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00928ACC` → [LocalGetConditionForString](../A0/LocalGetConditionForString_function_00A01C20.md) (function, `0x00A01C20`)
- `0x00928B16` → [LocalGetRelativeAttributeForString](../AC/LocalGetRelativeAttributeForString_function_00AC74E4.md) (function, `0x00AC74E4`)
- `0x00928B6C` → [RtlNtStatusToDosError](RtlNtStatusToDosError_function_00926C40.md) (function, `0x00926C40`)
- `0x00928C31` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00928C43` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00928D3F` → [RtlAddAuditAccessAceEx](../78/RtlAddAuditAccessAceEx_function_0078D450.md) (function, `0x0078D450`)
- `0x00928D73` → [RtlpAddKnownAce](RtlpAddKnownAce_function_00929A20.md) (function, `0x00929A20`)
- `0x00928E10` → [RtlAddAuditAccessObjectAce](../78/RtlAddAuditAccessObjectAce_function_0078D4A0.md) (function, `0x0078D4A0`)
- `0x00928E51` → [RtlAddAccessAllowedObjectAce](../78/RtlAddAccessAllowedObjectAce_function_0078D120.md) (function, `0x0078D120`)
- `0x00928E7C` → [SddlAddProcessTrustLabelAce](../7A/SddlAddProcessTrustLabelAce_function_007A4F94.md) (function, `0x007A4F94`)
- `0x00928EC3` → [SddlAddAccessFilterAce](../7A/SddlAddAccessFilterAce_function_007A4D58.md) (function, `0x007A4D58`)
- `0x00928EED` → [SddlAddScopedPolicyIDAce](../7A/SddlAddScopedPolicyIDAce_function_007A50F4.md) (function, `0x007A50F4`)
- `0x00928F2E` → [RtlAddAccessDeniedObjectAce](../78/RtlAddAccessDeniedObjectAce_function_0078D1B0.md) (function, `0x0078D1B0`)
- `0x00928F3C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00928F88` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [LocalConvertStringSDToSD_Rev1](LocalConvertStringSDToSD_Rev1_function_0092656C.md) at `0x0092678D`
- [LocalConvertStringSDToSD_Rev1](LocalConvertStringSDToSD_Rev1_function_0092656C.md) at `0x009267D2`

### Static image references
- `0x00927F4C` → RVA `0x00E0A740` (`.data`; read)
- `0x00927FC9` → RVA `0x00011C88` (`.rdata`; read)
- `0x00928271` → RVA `0x00E08C58` (`.data`; read)
- `0x009282E8` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x009285F0` → RVA `0x00E08AB8` (`.data`; read)
- `0x00928722` → RVA `0x00E089A4` (`.data`; read)
- `0x00928763` → RVA `0x00E08990` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **21**
  - `0x00927FD0` → [wcsnicmp](../../text/50/wcsnicmp_function_005001C0.md) (`PAGE` → `.text`)
  - `0x0092800D` → [wcschr](../../text/50/wcschr_function_00501A60.md) (`PAGE` → `.text`)
  - `0x009280AA` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00928143` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0092821B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0092823C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0092829A` → [wcsnicmp](../../text/50/wcsnicmp_function_005001C0.md) (`PAGE` → `.text`)
  - `0x009282B8` → [wcstoul](../../text/50/wcstoul_function_005024A0.md) (`PAGE` → `.text`)
  - `0x00928433` → [RtlLengthSid](../../text/45/RtlLengthSid_function_0045D270.md) (`PAGE` → `.text`)
  - `0x0092853D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0092855C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00928666` → [wcsnicmp](../../text/50/wcsnicmp_function_005001C0.md) (`PAGE` → `.text`)
  - `0x0092874B` → [wcsnicmp](../../text/50/wcsnicmp_function_005001C0.md) (`PAGE` → `.text`)
  - `0x009289CC` → [RtlLengthSid](../../text/45/RtlLengthSid_function_0045D270.md) (`PAGE` → `.text`)
  - `0x009289EC` → [RtlLengthSid](../../text/45/RtlLengthSid_function_0045D270.md) (`PAGE` → `.text`)
  - `0x00928A01` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00928A2D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00928C31` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00928C43` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00928F3C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00928F88` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **5**
  - `0x0092887C` → [sub_00B22C34](../B2/Unknown_function_00B22C34.md) (`tail-transfer`)
  - `0x0092888C` → [sub_00B22C34](../B2/Unknown_function_00B22C34.md) (`tail-transfer`)
  - `0x009288BA` → [sub_00B22C34 + 0x78](../B2/Unknown_function_00B22C34.md) (`tail-transfer`)
  - `0x00928DB0` → [sub_00B22C34 + 0xDB](../B2/Unknown_function_00B22C34.md) (`tail-transfer`)
  - `0x00928DC1` → [sub_00B22C34 + 0xDB](../B2/Unknown_function_00B22C34.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00927F30  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00927F35  55                              push rbp
00927F36  56                              push rsi
00927F37  57                              push rdi
00927F38  41 54                           push r12
00927F3A  41 55                           push r13
00927F3C  41 56                           push r14
00927F3E  41 57                           push r15
00927F40  48 8D 6C 24 A0                  lea rbp, [rsp - 0x60]
00927F45  48 81 EC 60 01 00 00            sub rsp, 0x160
00927F4C  48 8B 05 ED 27 4E 00            mov rax, qword ptr [rip + 0x4e27ed]
00927F53  48 33 C4                        xor rax, rsp
00927F56  48 89 45 50                     mov qword ptr [rbp + 0x50], rax
00927F5A  33 FF                           xor edi, edi
00927F5C  4C 89 44 24 60                  mov qword ptr [rsp + 0x60], r8
00927F61  32 C0                           xor al, al
00927F63  89 7D 88                        mov dword ptr [rbp - 0x78], edi
00927F66  88 44 24 50                     mov byte ptr [rsp + 0x50], al
00927F6A  8B C7                           mov eax, edi
00927F6C  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00927F71  4D 8B E1                        mov r12, r9
00927F74  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00927F78  4D 8B E8                        mov r13, r8
00927F7B  89 45 D8                        mov dword ptr [rbp - 0x28], eax
00927F7E  0F B6 DA                        movzx ebx, dl
00927F81  48 89 7D C8                     mov qword ptr [rbp - 0x38], rdi
00927F85  48 8B F1                        mov rsi, rcx
00927F88  48 89 7D 80                     mov qword ptr [rbp - 0x80], rdi
00927F8C  44 8B F7                        mov r14d, edi
00927F8F  89 7C 24 6C                     mov dword ptr [rsp + 0x6c], edi
00927F93  48 89 7D B0                     mov qword ptr [rbp - 0x50], rdi
00927F97  89 7C 24 70                     mov dword ptr [rsp + 0x70], edi
00927F9B  48 89 7D D0                     mov qword ptr [rbp - 0x30], rdi
00927F9F  48 89 7C 24 78                  mov qword ptr [rsp + 0x78], rdi
00927FA4  66 C7 45 DC 00 01               mov word ptr [rbp - 0x24], 0x100
00927FAA  48 85 C9                        test rcx, rcx
00927FAD  0F 84 DF 0F 00 00               je 0x140928f92
00927FB3  4D 85 C0                        test r8, r8
00927FB6  0F 84 D6 0F 00 00               je 0x140928f92
00927FBC  4D 85 C9                        test r9, r9
00927FBF  0F 84 CD 0F 00 00               je 0x140928f92
00927FC5  44 8D 47 11                     lea r8d, [rdi + 0x11]
00927FC9  48 8D 15 B8 9C 6E FF            lea rdx, [rip - 0x916348]
00927FD0  E8 EB 81 BD FF                  call 0x1405001c0
00927FD5  85 C0                           test eax, eax
00927FD7  0F 84 FC 01 00 00               je 0x1409281d9
00927FDD  F6 DB                           neg bl
00927FDF  49 89 3C 24                     mov qword ptr [r12], rdi
00927FE3  48 8B CE                        mov rcx, rsi
00927FE6  48 8B DE                        mov rbx, rsi
00927FE9  1B C0                           sbb eax, eax
00927FEB  44 8B FF                        mov r15d, edi
00927FEE  83 C0 02                        add eax, 2
00927FF1  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
00927FF5  E8 B6 0F 00 00                  call 0x140928fb0
00927FFA  BA FF FF FF FF                  mov edx, 0xffffffff
00927FFF  85 C0                           test eax, eax
00928001  0F 85 52 01 00 00               jne 0x140928159
00928007  8D 57 3A                        lea edx, [rdi + 0x3a]
0092800A  48 8B CE                        mov rcx, rsi
0092800D  E8 4E 9A BD FF                  call 0x140501a60
00928012  49 89 04 24                     mov qword ptr [r12], rax
00928016  EB 1A                           jmp 0x140928032
00928018  45 85 FF                        test r15d, r15d
0092801B  0F 85 69 0B 00 00               jne 0x140928b8a
00928021  45 85 F6                        test r14d, r14d
00928024  0F 85 60 0B 00 00               jne 0x140928b8a
0092802A  85 FF                           test edi, edi
0092802C  0F 85 5D 0B 00 00               jne 0x140928b8f
00928032  49 8B 04 24                     mov rax, qword ptr [r12]
00928036  48 3B C6                        cmp rax, rsi
00928039  0F 84 53 0F 00 00               je 0x140928f92
0092803F  48 85 C0                        test rax, rax
00928042  0F 85 08 01 00 00               jne 0x140928150
00928048  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
0092804F  90                              nop
00928050  66 83 7C 46 02 00               cmp word ptr [rsi + rax*2 + 2], 0
00928056  48 8D 40 01                     lea rax, [rax + 1]
0092805A  75 F4                           jne 0x140928050
0092805C  48 8D 14 46                     lea rdx, [rsi + rax*2]
00928060  49 8B C4                        mov rax, r12
00928063  4C 8D 45 88                     lea r8, [rbp - 0x78]
00928067  48 8B CE                        mov rcx, rsi
0092806A  48 89 10                        mov qword ptr [rax], rdx
0092806D  E8 CE 10 00 00                  call 0x140929140
00928072  44 8B F0                        mov r14d, eax
00928075  85 C0                           test eax, eax
00928077  0F 85 AA 00 00 00               jne 0x140928127
0092807D  8B 5D 88                        mov ebx, dword ptr [rbp - 0x78]
00928080  85 DB                           test ebx, ebx
00928082  0F 85 0B 05 00 00               jne 0x140928593
00928088  BB 08 00 00 00                  mov ebx, 8
0092808D  8B CB                           mov ecx, ebx
0092808F  E8 F4 DE FF FF                  call 0x140925f88
00928094  49 89 45 00                     mov qword ptr [r13], rax
00928098  48 85 C0                        test rax, rax
0092809B  75 2E                           jne 0x1409280cb
0092809D  44 8B F3                        mov r14d, ebx
009280A0  41 8B C6                        mov eax, r14d
009280A3  48 8B 4D 50                     mov rcx, qword ptr [rbp + 0x50]
009280A7  48 33 CC                        xor rcx, rsp
009280AA  E8 91 45 D8 FF                  call 0x1406ac640
009280AF  48 8B 9C 24 A8 01 00 00         mov rbx, qword ptr [rsp + 0x1a8]
009280B7  48 81 C4 60 01 00 00            add rsp, 0x160
009280BE  41 5F                           pop r15
009280C0  41 5E                           pop r14
009280C2  41 5D                           pop r13
009280C4  41 5C                           pop r12
009280C6  5F                              pop rdi
009280C7  5E                              pop rsi
009280C8  5D                              pop rbp
009280C9  C3                              ret
009280CA  CC                              int3
009280CB  C6 00 02                        mov byte ptr [rax], 2
009280CE  33 C9                           xor ecx, ecx
009280D0  49 8B 45 00                     mov rax, qword ptr [r13]
009280D4  C6 40 01 00                     mov byte ptr [rax + 1], 0
009280D8  49 8B 45 00                     mov rax, qword ptr [r13]
009280DC  66 89 58 02                     mov word ptr [rax + 2], bx
009280E0  49 8B 45 00                     mov rax, qword ptr [r13]
009280E4  66 89 48 04                     mov word ptr [rax + 4], cx
009280E8  49 8B 45 00                     mov rax, qword ptr [r13]
009280EC  66 89 48 06                     mov word ptr [rax + 6], cx
009280F0  EB AE                           jmp 0x1409280a0
009280F2  BB 77 00 00 C0                  mov ebx, 0xc0000077
009280F7  8B CB                           mov ecx, ebx
009280F9  E8 42 EB FF FF                  call 0x140926c40
009280FE  4C 8B 6C 24 60                  mov r13, qword ptr [rsp + 0x60]
00928103  44 8B F0                        mov r14d, eax
00928106  49 8B 45 00                     mov rax, qword ptr [r13]
0092810A  45 85 F6                        test r14d, r14d
0092810D  0F 85 F7 00 00 00               jne 0x14092820a
00928113  8B 4D 98                        mov ecx, dword ptr [rbp - 0x68]
00928116  0F B6 5C 24 50                  movzx ebx, byte ptr [rsp + 0x50]
0092811B  66 89 48 02                     mov word ptr [rax + 2], cx
0092811F  84 DB                           test bl, bl
00928121  0F 85 02 01 00 00               jne 0x140928229
00928127  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
0092812B  48 85 C9                        test rcx, rcx
0092812E  0F 85 52 0E 00 00               jne 0x140928f86
00928134  48 8B 4D B0                     mov rcx, qword ptr [rbp - 0x50]
00928138  48 85 C9                        test rcx, rcx
0092813B  0F 84 5F FF FF FF               je 0x1409280a0
00928141  33 D2                           xor edx, edx
00928143  E8 28 A7 25 00                  call 0x140b82870
00928148  41 8B C6                        mov eax, r14d
0092814B  E9 53 FF FF FF                  jmp 0x1409280a3
00928150  48 8D 50 FE                     lea rdx, [rax - 2]
00928154  E9 07 FF FF FF                  jmp 0x140928060
00928159  66 39 3E                        cmp word ptr [rsi], di
0092815C  0F 84 D0 FE FF FF               je 0x140928032
00928162  49 83 3C 24 00                  cmp qword ptr [r12], 0
00928167  0F 85 AB FE FF FF               jne 0x140928018
0092816D  85 FF                           test edi, edi
0092816F  0F 85 A3 FE FF FF               jne 0x140928018
00928175  0F B7 0B                        movzx ecx, word ptr [rbx]
00928178  83 E9 22                        sub ecx, 0x22
0092817B  74 37                           je 0x1409281b4
0092817D  83 E9 06                        sub ecx, 6
00928180  74 19                           je 0x14092819b
00928182  83 E9 01                        sub ecx, 1
00928185  74 1E                           je 0x1409281a5
00928187  83 F9 11                        cmp ecx, 0x11
0092818A  74 3B                           je 0x1409281c7
0092818C  48 83 C3 02                     add rbx, 2
00928190  66 83 3B 00                     cmp word ptr [rbx], 0
00928194  75 CC                           jne 0x140928162
00928196  E9 7D FE FF FF                  jmp 0x140928018
0092819B  45 85 FF                        test r15d, r15d
0092819E  75 EC                           jne 0x14092818c
009281A0  41 FF C6                        inc r14d
009281A3  EB E7                           jmp 0x14092818c
009281A5  45 85 FF                        test r15d, r15d
009281A8  75 E2                           jne 0x14092818c
009281AA  45 85 F6                        test r14d, r14d
009281AD  74 23                           je 0x1409281d2
009281AF  44 03 F2                        add r14d, edx
009281B2  EB D8                           jmp 0x14092818c
009281B4  41 83 FE 01                     cmp r14d, 1
009281B8  76 18                           jbe 0x1409281d2
009281BA  33 C0                           xor eax, eax
009281BC  45 85 FF                        test r15d, r15d
009281BF  0F 94 C0                        sete al
009281C2  44 8B F8                        mov r15d, eax
009281C5  EB C5                           jmp 0x14092818c
009281C7  45 85 F6                        test r14d, r14d
009281CA  75 C0                           jne 0x14092818c
009281CC  49 89 1C 24                     mov qword ptr [r12], rbx
009281D0  EB BA                           jmp 0x14092818c
009281D2  BF 38 05 00 00                  mov edi, 0x538
009281D7  EB B3                           jmp 0x14092818c
009281D9  48 8D 46 22                     lea rax, [rsi + 0x22]
009281DD  49 89 7D 00                     mov qword ptr [r13], rdi
009281E1  49 89 04 24                     mov qword ptr [r12], rax
009281E5  E9 3D FF FF FF                  jmp 0x140928127
009281EA  8B 54 24 68                     mov edx, dword ptr [rsp + 0x68]
009281EE  45 33 C0                        xor r8d, r8d
009281F1  FF C7                           inc edi
009281F3  48 83 C3 20                     add rbx, 0x20
009281F7  83 FF 09                        cmp edi, 9
009281FA  0F 82 29 05 00 00               jb 0x140928729
00928200  49 8B 45 00                     mov rax, qword ptr [r13]
00928204  41 BE EC 03 00 00               mov r14d, 0x3ec
0092820A  33 F6                           xor esi, esi
0092820C  0F B6 5C 24 50                  movzx ebx, byte ptr [rsp + 0x50]
00928211  48 85 C0                        test rax, rax
00928214  74 0A                           je 0x140928220
00928216  33 D2                           xor edx, edx
00928218  48 8B C8                        mov rcx, rax
0092821B  E8 50 A6 25 00                  call 0x140b82870
00928220  49 89 75 00                     mov qword ptr [r13], rsi
00928224  E9 F6 FE FF FF                  jmp 0x14092811f
00928229  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
0092822E  48 85 C0                        test rax, rax
00928231  0F 84 F0 FE FF FF               je 0x140928127
00928237  33 D2                           xor edx, edx
00928239  48 8B C8                        mov rcx, rax
0092823C  E8 2F A6 25 00                  call 0x140b82870
00928241  E9 E1 FE FF FF                  jmp 0x140928127
00928246  49 83 C7 02                     add r15, 2
0092824A  66 41 83 3F 20                  cmp word ptr [r15], 0x20
0092824F  0F 84 7F 09 00 00               je 0x140928bd4
00928255  41 0F B7 07                     movzx eax, word ptr [r15]
00928259  66 83 F8 3B                     cmp ax, 0x3b
0092825D  0F 84 BD 00 00 00               je 0x140928320
00928263  66 83 F8 20                     cmp ax, 0x20
00928267  0F 84 77 09 00 00               je 0x140928be4
0092826D  41 80 FE 11                     cmp r14b, 0x11
00928271  48 8D 1D E0 09 4E 00            lea rbx, [rip + 0x4e09e0]
00928278  8B F2                           mov esi, edx
0092827A  41 BA 04 00 00 00               mov r10d, 4
00928280  41 0F 44 F2                     cmove esi, r10d
00928284  41 8B F8                        mov edi, r8d
00928287  8B 43 08                        mov eax, dword ptr [rbx + 8]
0092828A  23 C6                           and eax, esi
0092828C  3B C6                           cmp eax, esi
0092828E  75 13                           jne 0x1409282a3
00928290  44 8B 03                        mov r8d, dword ptr [rbx]
00928293  49 8B CF                        mov rcx, r15
00928296  48 8B 53 F8                     mov rdx, qword ptr [rbx - 8]
0092829A  E8 21 7F BD FF                  call 0x1405001c0
0092829F  85 C0                           test eax, eax
009282A1  74 3A                           je 0x1409282dd
009282A3  FF C7                           inc edi
009282A5  48 83 C3 18                     add rbx, 0x18
009282A9  83 FF 1C                        cmp edi, 0x1c
009282AC  72 D9                           jb 0x140928287
009282AE  45 33 C0                        xor r8d, r8d
009282B1  48 8D 55 C8                     lea rdx, [rbp - 0x38]
009282B5  49 8B CF                        mov rcx, r15
009282B8  E8 E3 A1 BD FF                  call 0x1405024a0
009282BD  09 44 24 54                     or dword ptr [rsp + 0x54], eax
009282C1  48 8B 45 C8                     mov rax, qword ptr [rbp - 0x38]
009282C5  49 3B C7                        cmp rax, r15
009282C8  0F 85 C3 05 00 00               jne 0x140928891
009282CE  49 8B 45 00                     mov rax, qword ptr [r13]
009282D2  41 BE 38 05 00 00               mov r14d, 0x538
009282D8  E9 2D FF FF FF                  jmp 0x14092820a
009282DD  83 FF 1C                        cmp edi, 0x1c
009282E0  73 CC                           jae 0x1409282ae
009282E2  8B C7                           mov eax, edi
009282E4  48 8D 0C 40                     lea rcx, [rax + rax*2]
009282E8  48 8D 05 11 7D 6D FF            lea rax, [rip - 0x9282ef]
009282EF  48 8D 04 C8                     lea rax, [rax + rcx*8]
009282F3  48 8D 80 50 8C E0 00            lea rax, [rax + 0xe08c50]
009282FA  48 85 C0                        test rax, rax
009282FD  74 AF                           je 0x1409282ae
009282FF  44 8B 44 24 54                  mov r8d, dword ptr [rsp + 0x54]
00928304  44 0B 40 0C                     or r8d, dword ptr [rax + 0xc]
00928308  8B 40 08                        mov eax, dword ptr [rax + 8]
0092830B  8B 54 24 68                     mov edx, dword ptr [rsp + 0x68]
0092830F  44 89 44 24 54                  mov dword ptr [rsp + 0x54], r8d
00928314  45 33 C0                        xor r8d, r8d
00928317  4D 8D 3C 47                     lea r15, [r15 + rax*2]
0092831B  E9 35 FF FF FF                  jmp 0x140928255
00928320  49 83 C7 02                     add r15, 2
00928324  41 8B D8                        mov ebx, r8d
00928327  49 8B FE                        mov rdi, r14
0092832A  83 FB 02                        cmp ebx, 2
0092832D  73 20                           jae 0x14092834f
0092832F  41 0F B7 07                     movzx eax, word ptr [r15]
00928333  66 83 F8 20                     cmp ax, 0x20
00928337  0F 84 B7 08 00 00               je 0x140928bf4
0092833D  66 83 F8 3B                     cmp ax, 0x3b
00928341  0F 85 2F 05 00 00               jne 0x140928876
00928347  49 83 C7 02                     add r15, 2
0092834B  FF C3                           inc ebx
0092834D  EB DB                           jmp 0x14092832a
0092834F  8B 55 B8                        mov edx, dword ptr [rbp - 0x48]
00928352  44 8B F2                        mov r14d, edx
00928355  85 D2                           test edx, edx
00928357  0F 85 A9 FD FF FF               jne 0x140928106
0092835D  41 0F B7 07                     movzx eax, word ptr [r15]
00928361  66 83 F8 20                     cmp ax, 0x20
00928365  0F 84 9D 08 00 00               je 0x140928c08
0092836B  33 F6                           xor esi, esi
0092836D  32 DB                           xor bl, bl
0092836F  48 89 75 B8                     mov qword ptr [rbp - 0x48], rsi
00928373  44 8B F6                        mov r14d, esi
00928376  88 5C 24 50                     mov byte ptr [rsp + 0x50], bl
0092837A  66 85 C0                        test ax, ax
0092837D  0F 84 AC 07 00 00               je 0x140928b2f
00928383  66 41 39 77 02                  cmp word ptr [r15 + 2], si
00928388  0F 84 A1 07 00 00               je 0x140928b2f
0092838E  49 8D 47 04                     lea rax, [r15 + 4]
00928392  45 33 C0                        xor r8d, r8d
00928395  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
0092839A  33 D2                           xor edx, edx
0092839C  48 8D 45 B8                     lea rax, [rbp - 0x48]
009283A0  49 8B CF                        mov rcx, r15
009283A3  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009283A8  88 5C 24 28                     mov byte ptr [rsp + 0x28], bl
009283AC  E8 0F 10 00 00                  call 0x1409293c0
009283B1  48 85 C0                        test rax, rax
009283B4  0F 84 05 05 00 00               je 0x1409288bf
009283BA  4C 8B 40 10                     mov r8, qword ptr [rax + 0x10]
009283BE  4C 89 44 24 58                  mov qword ptr [rsp + 0x58], r8
009283C3  48 8B 74 24 78                  mov rsi, qword ptr [rsp + 0x78]
009283C8  48 85 F6                        test rsi, rsi
009283CB  0F 84 A4 0B 00 00               je 0x140928f75
009283D1  4D 85 C0                        test r8, r8
009283D4  0F 84 9B 0B 00 00               je 0x140928f75
009283DA  66 83 3E 20                     cmp word ptr [rsi], 0x20
009283DE  48 8B DE                        mov rbx, rsi
009283E1  0F 84 69 07 00 00               je 0x140928b50
009283E7  40 80 FF 15                     cmp dil, 0x15
009283EB  77 0E                           ja 0x1409283fb
009283ED  B9 00 2E 24 00                  mov ecx, 0x242e00
009283F2  0F A3 F9                        bt ecx, edi
009283F5  0F 82 34 05 00 00               jb 0x14092892f
009283FB  44 8B 7C 24 6C                  mov r15d, dword ptr [rsp + 0x6c]
00928400  8B 54 24 70                     mov edx, dword ptr [rsp + 0x70]
00928404  0F B7 06                        movzx eax, word ptr [rsi]
00928407  66 83 F8 20                     cmp ax, 0x20
0092840B  0F 84 4F 08 00 00               je 0x140928c60
00928411  66 83 F8 29                     cmp ax, 0x29
00928415  0F 85 B3 FE FF FF               jne 0x1409282ce
0092841B  48 83 C6 02                     add rsi, 2
0092841F  4C 8B EF                        mov r13, rdi
00928422  83 FF 03                        cmp edi, 3
00928425  0F 85 AF 03 00 00               jne 0x1409287da
0092842B  BB 0C 00 00 00                  mov ebx, 0xc
00928430  49 8B C8                        mov rcx, r8
00928433  E8 38 4E B3 FF                  call 0x14045d270
00928438  8D 7B FC                        lea edi, [rbx - 4]
0092843B  03 F8                           add edi, eax
0092843D  3B FB                           cmp edi, ebx
0092843F  73 14                           jae 0x140928455
00928441  4C 8B 6C 24 60                  mov r13, qword ptr [rsp + 0x60]
00928446  41 BE 16 02 00 00               mov r14d, 0x216
0092844C  49 8B 45 00                     mov rax, qword ptr [r13]
00928450  E9 B5 FD FF FF                  jmp 0x14092820a
00928455  8B 45 98                        mov eax, dword ptr [rbp - 0x68]
00928458  03 C7                           add eax, edi
0092845A  89 45 98                        mov dword ptr [rbp - 0x68], eax
0092845D  3B C7                           cmp eax, edi
0092845F  72 E0                           jb 0x140928441
00928461  8B 55 90                        mov edx, dword ptr [rbp - 0x70]
00928464  3B C2                           cmp eax, edx
00928466  0F 87 34 04 00 00               ja 0x1409288a0
0092846C  45 85 ED                        test r13d, r13d
0092846F  0F 85 30 03 00 00               jne 0x1409287a5
00928475  4C 8B 6C 24 60                  mov r13, qword ptr [rsp + 0x60]
0092847A  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0092847F  0F B6 7C 24 51                  movzx edi, byte ptr [rsp + 0x51]
00928484  49 8B 5D 00                     mov rbx, qword ptr [r13]
00928488  E8 83 12 00 00                  call 0x140929710
0092848D  84 C0                           test al, al
0092848F  0F 84 83 00 00 00               je 0x140928518
00928495  44 0F B6 3B                     movzx r15d, byte ptr [rbx]
00928499  41 80 FF 04                     cmp r15b, 4
0092849D  0F 87 C9 03 00 00               ja 0x14092886c
009284A3  41 80 FF 02                     cmp r15b, 2
009284A7  77 03                           ja 0x1409284ac
009284A9  41 B7 02                        mov r15b, 2
009284AC  83 E7 E0                        and edi, 0xffffffe0
009284AF  0F 85 2E 06 00 00               jne 0x140928ae3
009284B5  48 8B CB                        mov rcx, rbx
009284B8  E8 E3 22 00 00                  call 0x14092a7a0
009284BD  84 C0                           test al, al
009284BF  0F 84 9B 06 00 00               je 0x140928b60
009284C5  44 0F B7 43 04                  movzx r8d, word ptr [rbx + 4]
009284CA  48 8D 53 08                     lea rdx, [rbx + 8]
009284CE  45 33 C9                        xor r9d, r9d
009284D1  41 8B C9                        mov ecx, r9d
009284D4  41 3B C8                        cmp ecx, r8d
009284D7  0F 82 34 03 00 00               jb 0x140928811
009284DD  44 0F B7 43 02                  movzx r8d, word ptr [rbx + 2]
009284E2  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
009284E7  4C 03 C3                        add r8, rbx
009284EA  49 3B D0                        cmp rdx, r8
009284ED  49 0F 47 D1                     cmova rdx, r9
009284F1  0F B6 4F 01                     movzx ecx, byte ptr [rdi + 1]
009284F5  66 83 C1 04                     add cx, 4
009284F9  66 C1 E1 02                     shl cx, 2
009284FD  48 85 D2                        test rdx, rdx
00928500  74 0F                           je 0x140928511
00928502  0F B7 C1                        movzx eax, cx
00928505  48 03 C2                        add rax, rdx
00928508  49 3B C0                        cmp rax, r8
0092850B  0F 86 1E 03 00 00               jbe 0x14092882f
00928511  BB 99 00 00 C0                  mov ebx, 0xc0000099
00928516  EB 0A                           jmp 0x140928522
00928518  BB 78 00 00 C0                  mov ebx, 0xc0000078
0092851D  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
00928522  0F B6 44 24 50                  movzx eax, byte ptr [rsp + 0x50]
00928527  85 DB                           test ebx, ebx
00928529  0F 88 C8 FB FF FF               js 0x1409280f7
0092852F  3C 01                           cmp al, 1
00928531  75 0F                           jne 0x140928542
00928533  48 85 FF                        test rdi, rdi
00928536  74 0A                           je 0x140928542
00928538  33 D2                           xor edx, edx
0092853A  48 8B CF                        mov rcx, rdi
0092853D  E8 2E A3 25 00                  call 0x140b82870
00928542  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
00928546  45 33 C0                        xor r8d, r8d
00928549  41 8B C0                        mov eax, r8d
0092854C  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00928551  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00928555  48 85 C9                        test rcx, rcx
00928558  74 0E                           je 0x140928568
0092855A  33 D2                           xor edx, edx
0092855C  E8 0F A3 25 00                  call 0x140b82870
00928561  45 33 C0                        xor r8d, r8d
00928564  4C 89 45 80                     mov qword ptr [rbp - 0x80], r8
00928568  48 8B 4D B0                     mov rcx, qword ptr [rbp - 0x50]
0092856C  44 89 44 24 6C                  mov dword ptr [rsp + 0x6c], r8d
00928571  48 85 C9                        test rcx, rcx
00928574  0F 85 C0 09 00 00               jne 0x140928f3a
0092857A  44 89 44 24 70                  mov dword ptr [rsp + 0x70], r8d
0092857F  66 83 3E 28                     cmp word ptr [rsi], 0x28
00928583  75 04                           jne 0x140928589
00928585  48 83 C6 02                     add rsi, 2
00928589  8B 45 94                        mov eax, dword ptr [rbp - 0x6c]
0092858C  8B 5D 88                        mov ebx, dword ptr [rbp - 0x78]
0092858F  FF C0                           inc eax
00928591  EB 5A                           jmp 0x1409285ed
00928593  B8 FF FF 00 00                  mov eax, 0xffff
00928598  6B FB 54                        imul edi, ebx, 0x54
0092859B  83 C7 08                        add edi, 8
0092859E  3B F8                           cmp edi, eax
009285A0  0F 47 F8                        cmova edi, eax
009285A3  8B CF                           mov ecx, edi
009285A5  89 7D 90                        mov dword ptr [rbp - 0x70], edi
009285A8  E8 DB D9 FF FF                  call 0x140925f88
009285AD  49 89 45 00                     mov qword ptr [r13], rax
009285B1  48 85 C0                        test rax, rax
009285B4  0F 84 97 04 00 00               je 0x140928a51
009285BA  C6 00 02                        mov byte ptr [rax], 2
009285BD  45 33 C0                        xor r8d, r8d
009285C0  49 8B 45 00                     mov rax, qword ptr [r13]
009285C4  B9 08 00 00 00                  mov ecx, 8
009285C9  89 4D 98                        mov dword ptr [rbp - 0x68], ecx
009285CC  C6 40 01 00                     mov byte ptr [rax + 1], 0
009285D0  49 8B 45 00                     mov rax, qword ptr [r13]
009285D4  66 89 78 02                     mov word ptr [rax + 2], di
009285D8  49 8B 45 00                     mov rax, qword ptr [r13]
009285DC  66 44 89 40 04                  mov word ptr [rax + 4], r8w
009285E1  49 8B 45 00                     mov rax, qword ptr [r13]
009285E5  66 44 89 40 06                  mov word ptr [rax + 6], r8w
009285EA  41 8B C0                        mov eax, r8d
009285ED  89 45 94                        mov dword ptr [rbp - 0x6c], eax
009285F0  48 8D 15 C1 04 4E 00            lea rdx, [rip + 0x4e04c1]
009285F7  44 89 75 B8                     mov dword ptr [rbp - 0x48], r14d
009285FB  3B C3                           cmp eax, ebx
009285FD  0F 83 03 FB FF FF               jae 0x140928106
00928603  0F 57 C0                        xorps xmm0, xmm0
00928606  C6 44 24 51 00                  mov byte ptr [rsp + 0x51], 0
0092860B  0F 57 C9                        xorps xmm1, xmm1
0092860E  44 89 44 24 54                  mov dword ptr [rsp + 0x54], r8d
00928613  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00928617  4C 89 45 A8                     mov qword ptr [rbp - 0x58], r8
0092861B  0F 11 4D F0                     movups xmmword ptr [rbp - 0x10], xmm1
0092861F  0F B7 06                        movzx eax, word ptr [rsi]
00928622  4C 89 45 A0                     mov qword ptr [rbp - 0x60], r8
00928626  66 83 F8 20                     cmp ax, 0x20
0092862A  0F 84 66 05 00 00               je 0x140928b96
00928630  66 83 F8 28                     cmp ax, 0x28
00928634  75 0E                           jne 0x140928644
00928636  48 83 C6 02                     add rsi, 2
0092863A  66 83 3E 20                     cmp word ptr [rsi], 0x20
0092863E  0F 84 65 05 00 00               je 0x140928ba9
00928644  48 8B DA                        mov rbx, rdx
00928647  41 8B F8                        mov edi, r8d
0092864A  8B 54 24 68                     mov edx, dword ptr [rsp + 0x68]
0092864E  8B 43 08                        mov eax, dword ptr [rbx + 8]
00928651  23 C2                           and eax, edx
00928653  3B C2                           cmp eax, edx
00928655  75 1C                           jne 0x140928673
00928657  48 85 F6                        test rsi, rsi
0092865A  74 31                           je 0x14092868d
0092865C  44 8B 03                        mov r8d, dword ptr [rbx]
0092865F  48 8B CE                        mov rcx, rsi
00928662  48 8B 53 F8                     mov rdx, qword ptr [rbx - 8]
00928666  E8 55 7B BD FF                  call 0x1405001c0
0092866B  8B 54 24 68                     mov edx, dword ptr [rsp + 0x68]
0092866F  85 C0                           test eax, eax
00928671  74 20                           je 0x140928693
00928673  FF C7                           inc edi
00928675  48 83 C3 18                     add rbx, 0x18
00928679  83 FF 11                        cmp edi, 0x11
0092867C  72 D0                           jb 0x14092864e
0092867E  49 8B 45 00                     mov rax, qword ptr [r13]
00928682  41 BE 0C 07 00 00               mov r14d, 0x70c
00928688  E9 7D FB FF FF                  jmp 0x14092820a
0092868D  83 7B 04 00                     cmp dword ptr [rbx + 4], 0
00928691  75 E0                           jne 0x140928673
00928693  83 FF 11                        cmp edi, 0x11
00928696  73 E6                           jae 0x14092867e
00928698  8B C7                           mov eax, edi
0092869A  4C 8D 0D 5F 79 6D FF            lea r9, [rip - 0x9286a1]
009286A1  48 8D 0C 40                     lea rcx, [rax + rax*2]
009286A5  49 8D 81 B0 8A E0 00            lea rax, [r9 + 0xe08ab0]
009286AC  48 8D 04 C8                     lea rax, [rax + rcx*8]
009286B0  48 85 C0                        test rax, rax
009286B3  74 C9                           je 0x14092867e
009286B5  0F B6 78 0C                     movzx edi, byte ptr [rax + 0xc]
009286B9  8B 40 08                        mov eax, dword ptr [rax + 8]
009286BC  40 88 7C 24 52                  mov byte ptr [rsp + 0x52], dil
009286C1  4C 8D 3C 46                     lea r15, [rsi + rax*2]
009286C5  0F B7 04 46                     movzx eax, word ptr [rsi + rax*2]
009286C9  66 83 F8 3B                     cmp ax, 0x3b
009286CD  0F 85 C3 00 00 00               jne 0x140928796
009286D3  49 83 C7 02                     add r15, 2
009286D7  8D 47 FB                        lea eax, [rdi - 5]
009286DA  3C 03                           cmp al, 3
009286DC  0F 86 D6 04 00 00               jbe 0x140928bb8
009286E2  40 80 FF 0B                     cmp dil, 0xb
009286E6  0F 84 CC 04 00 00               je 0x140928bb8
009286EC  66 41 83 3F 20                  cmp word ptr [r15], 0x20
009286F1  0F 84 CD 04 00 00               je 0x140928bc4
009286F7  4C 8B F7                        mov r14, rdi
009286FA  45 33 C0                        xor r8d, r8d
009286FD  4D 3B 3C 24                     cmp r15, qword ptr [r12]
00928701  0F 84 43 FB FF FF               je 0x14092824a
00928707  41 0F B7 07                     movzx eax, word ptr [r15]
0092870B  66 83 F8 3B                     cmp ax, 0x3b
0092870F  0F 84 31 FB FF FF               je 0x140928246
00928715  66 83 F8 20                     cmp ax, 0x20
00928719  0F 84 21 03 00 00               je 0x140928a40
0092871F  41 8B F8                        mov edi, r8d
00928722  48 8D 1D 7B 02 4E 00            lea rbx, [rip + 0x4e027b]
00928729  8B 43 FC                        mov eax, dword ptr [rbx - 4]
0092872C  23 C2                           and eax, edx
0092872E  3B C2                           cmp eax, edx
00928730  0F 85 BB FA FF FF               jne 0x1409281f1
00928736  8B 13                           mov edx, dword ptr [rbx]
00928738  85 D2                           test edx, edx
0092873A  0F 85 D0 01 00 00               jne 0x140928910
00928740  44 8B 43 F4                     mov r8d, dword ptr [rbx - 0xc]
00928744  49 8B CF                        mov rcx, r15
00928747  48 8B 53 EC                     mov rdx, qword ptr [rbx - 0x14]
0092874B  E8 70 7A BD FF                  call 0x1405001c0
00928750  85 C0                           test eax, eax
00928752  0F 85 92 FA FF FF               jne 0x1409281ea
00928758  83 FF 09                        cmp edi, 9
0092875B  0F 83 9F FA FF FF               jae 0x140928200
00928761  8B C7                           mov eax, edi
00928763  48 8D 0D 26 02 4E 00            lea rcx, [rip + 0x4e0226]
0092876A  48 C1 E0 05                     shl rax, 5
0092876E  48 03 C1                        add rax, rcx
00928771  0F 84 89 FA FF FF               je 0x140928200
00928777  44 0F B6 44 24 51               movzx r8d, byte ptr [rsp + 0x51]
0092877D  44 0A 40 0C                     or r8b, byte ptr [rax + 0xc]
00928781  8B 40 08                        mov eax, dword ptr [rax + 8]
00928784  8B 54 24 68                     mov edx, dword ptr [rsp + 0x68]
00928788  44 88 44 24 51                  mov byte ptr [rsp + 0x51], r8b
0092878D  4D 8D 3C 47                     lea r15, [r15 + rax*2]
00928791  E9 64 FF FF FF                  jmp 0x1409286fa
00928796  66 83 F8 20                     cmp ax, 0x20
0092879A  0F 84 33 FF FF FF               je 0x1409286d3
009287A0  E9 29 FB FF FF                  jmp 0x1409282ce
009287A5  41 83 FD 11                     cmp r13d, 0x11
009287A9  0F 85 B2 01 00 00               jne 0x140928961
009287AF  8B 44 24 54                     mov eax, dword ptr [rsp + 0x54]
009287B3  4C 8B 6C 24 60                  mov r13, qword ptr [rsp + 0x60]
009287B8  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
009287BD  44 0F B6 44 24 51               movzx r8d, byte ptr [rsp + 0x51]
009287C3  4C 8B CF                        mov r9, rdi
009287C6  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
009287CA  49 8B 4D 00                     mov rcx, qword ptr [r13]
009287CE  E8 D9 10 08 00                  call 0x1409a98ac
009287D3  8B D8                           mov ebx, eax
009287D5  E9 48 FD FF FF                  jmp 0x140928522
009287DA  41 83 FD 15                     cmp r13d, 0x15
009287DE  0F 87 69 07 00 00               ja 0x140928f4d
009287E4  4C 8D 0D 15 78 6D FF            lea r9, [rip - 0x9287eb]
009287EB  41 8B 8C B9 6C 33 04 00         mov ecx, dword ptr [r9 + rdi*4 + 0x4336c]
009287F3  49 03 C9                        add rcx, r9
009287F6  FF E1                           jmp rcx
009287F8  CC                              int3
009287F9  CC                              int3
009287FA  CC                              int3
009287FB  CC                              int3
009287FC  41 83 FF FC                     cmp r15d, -4
00928800  0F 86 71 04 00 00               jbe 0x140928c77
00928806  41 BE 16 02 00 00               mov r14d, 0x216
0092880C  E9 16 F9 FF FF                  jmp 0x140928127
00928811  0F B7 43 02                     movzx eax, word ptr [rbx + 2]
00928815  48 03 C3                        add rax, rbx
00928818  48 3B D0                        cmp rdx, rax
0092881B  0F 83 3F 03 00 00               jae 0x140928b60
00928821  0F B7 42 02                     movzx eax, word ptr [rdx + 2]
00928825  FF C1                           inc ecx
00928827  48 03 D0                        add rdx, rax
0092882A  E9 A5 FC FF FF                  jmp 0x1409284d4
0092882F  0F B6 44 24 51                  movzx eax, byte ptr [rsp + 0x51]
00928834  4C 8B C7                        mov r8, rdi
00928837  88 42 01                        mov byte ptr [rdx + 1], al
0092883A  8B 44 24 54                     mov eax, dword ptr [rsp + 0x54]
0092883E  66 89 4A 02                     mov word ptr [rdx + 2], cx
00928842  89 42 04                        mov dword ptr [rdx + 4], eax
00928845  44 88 0A                        mov byte ptr [rdx], r9b
00928848  48 83 C2 08                     add rdx, 8
0092884C  0F B6 4F 01                     movzx ecx, byte ptr [rdi + 1]
00928850  8D 0C 8D 08 00 00 00            lea ecx, [rcx*4 + 8]
00928857  E8 F4 11 08 00                  call 0x1409a9a50
0092885C  66 FF 43 04                     inc word ptr [rbx + 4]
00928860  33 C0                           xor eax, eax
00928862  44 88 3B                        mov byte ptr [rbx], r15b
00928865  8B D8                           mov ebx, eax
00928867  E9 B6 FC FF FF                  jmp 0x140928522
0092886C  BB 59 00 00 C0                  mov ebx, 0xc0000059
00928871  E9 A7 FC FF FF                  jmp 0x14092851d
00928876  41 8D 46 FB                     lea eax, [r14 - 5]
0092887A  3C 03                           cmp al, 3
0092887C  0F 86 B2 A3 1F 00               jbe 0x140b22c34
00928882  40 80 FF 0B                     cmp dil, 0xb
00928886  0F 85 42 FA FF FF               jne 0x1409282ce
0092888C  E9 A3 A3 1F 00                  jmp 0x140b22c34
00928891  8B 54 24 68                     mov edx, dword ptr [rsp + 0x68]
00928895  4C 8B F8                        mov r15, rax
00928898  45 33 C0                        xor r8d, r8d
0092889B  E9 B5 F9 FF FF                  jmp 0x140928255
009288A0  8B 4D 88                        mov ecx, dword ptr [rbp - 0x78]
009288A3  2B 4D 94                        sub ecx, dword ptr [rbp - 0x6c]
009288A6  8B C7                           mov eax, edi
009288A8  48 0F AF C8                     imul rcx, rax
009288AC  B8 FF FF FF FF                  mov eax, 0xffffffff
009288B1  48 3B C8                        cmp rcx, rax
009288B4  0F 87 87 FB FF FF               ja 0x140928441
009288BA  E9 ED A3 1F 00                  jmp 0x140b22cac
009288BF  4C 8B 45 B8                     mov r8, qword ptr [rbp - 0x48]
009288C3  4C 89 44 24 58                  mov qword ptr [rsp + 0x58], r8
009288C8  4D 85 C0                        test r8, r8
009288CB  75 2D                           jne 0x1409288fa
009288CD  48 83 6C 24 78 04               sub qword ptr [rsp + 0x78], 4
009288D3  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
009288D8  48 8D 55 C0                     lea rdx, [rbp - 0x40]
009288DC  49 8B CF                        mov rcx, r15
009288DF  E8 AC EB 0E 00                  call 0x140a17490
009288E4  85 C0                           test eax, eax
009288E6  0F 88 7E 02 00 00               js 0x140928b6a
009288EC  4C 8B 45 C0                     mov r8, qword ptr [rbp - 0x40]
009288F0  4C 89 44 24 58                  mov qword ptr [rsp + 0x58], r8
009288F5  4D 85 C0                        test r8, r8
009288F8  74 02                           je 0x1409288fc
009288FA  B3 01                           mov bl, 1
009288FC  88 5C 24 50                     mov byte ptr [rsp + 0x50], bl
00928900  45 85 F6                        test r14d, r14d
00928903  0F 84 BA FA FF FF               je 0x1409283c3
00928909  E9 F8 F7 FF FF                  jmp 0x140928106
0092890E  66 90                           nop
00928910  44 3B C2                        cmp r8d, edx
00928913  0F 83 D1 F8 FF FF               jae 0x1409281ea
00928919  48 8B 43 04                     mov rax, qword ptr [rbx + 4]
0092891D  41 8B C8                        mov ecx, r8d
00928920  44 38 34 01                     cmp byte ptr [rcx + rax], r14b
00928924  0F 84 16 FE FF FF               je 0x140928740
0092892A  41 FF C0                        inc r8d
0092892D  EB E1                           jmp 0x140928910
0092892F  66 83 3B 3B                     cmp word ptr [rbx], 0x3b
00928933  0F 84 23 01 00 00               je 0x140928a5c
00928939  44 8B 7C 24 6C                  mov r15d, dword ptr [rsp + 0x6c]
0092893E  8B 54 24 70                     mov edx, dword ptr [rsp + 0x70]
00928942  45 85 FF                        test r15d, r15d
00928945  75 08                           jne 0x14092894f
00928947  85 D2                           test edx, edx
00928949  0F 84 7F F9 FF FF               je 0x1409282ce
0092894F  45 85 F6                        test r14d, r14d
00928952  0F 84 AC FA FF FF               je 0x140928404
00928958  49 8B 45 00                     mov rax, qword ptr [r13]
0092895C  E9 A9 F8 FF FF                  jmp 0x14092820a
00928961  41 8D 45 FF                     lea eax, [r13 - 1]
00928965  83 F8 14                        cmp eax, 0x14
00928968  0F 87 FD 05 00 00               ja 0x140928f6b
0092896E  48 8D 15 8B 76 6D FF            lea rdx, [rip - 0x928975]
00928975  48 98                           cdqe
00928977  8B 8C 82 C4 33 04 00            mov ecx, dword ptr [rdx + rax*4 + 0x433c4]
0092897E  48 03 CA                        add rcx, rdx
00928981  FF E1                           jmp rcx
00928983  CC                              int3
00928984  CC                              int3
00928985  CC                              int3
00928986  CC                              int3
00928987  81 FF FF FF 00 00               cmp edi, 0xffff
0092898D  0F 83 5F F7 FF FF               jae 0x1409280f2
00928993  8B CF                           mov ecx, edi
00928995  E8 EE D5 FF FF                  call 0x140925f88
0092899A  4C 8B F8                        mov r15, rax
0092899D  48 85 C0                        test rax, rax
009289A0  0F 84 BB 05 00 00               je 0x140928f61
009289A6  0F B6 44 24 52                  movzx eax, byte ptr [rsp + 0x52]
009289AB  4C 8B 6C 24 58                  mov r13, qword ptr [rsp + 0x58]
009289B0  41 88 07                        mov byte ptr [r15], al
009289B3  49 8B CD                        mov rcx, r13
009289B6  0F B6 44 24 51                  movzx eax, byte ptr [rsp + 0x51]
009289BB  41 88 47 01                     mov byte ptr [r15 + 1], al
009289BF  8B 44 24 54                     mov eax, dword ptr [rsp + 0x54]
009289C3  41 89 47 04                     mov dword ptr [r15 + 4], eax
009289C7  66 41 89 7F 02                  mov word ptr [r15 + 2], di
009289CC  E8 9F 48 B3 FF                  call 0x14045d270
009289D1  8B C8                           mov ecx, eax
009289D3  49 8D 57 08                     lea rdx, [r15 + 8]
009289D7  4D 8B C5                        mov r8, r13
009289DA  E8 71 10 08 00                  call 0x1409a9a50
009289DF  8B 44 24 6C                     mov eax, dword ptr [rsp + 0x6c]
009289E3  85 C0                           test eax, eax
009289E5  74 1F                           je 0x140928a06
009289E7  49 8B CD                        mov rcx, r13
009289EA  8B D8                           mov ebx, eax
009289EC  E8 7F 48 B3 FF                  call 0x14045d270
009289F1  48 8B 55 80                     mov rdx, qword ptr [rbp - 0x80]
009289F5  44 8B C3                        mov r8d, ebx
009289F8  8B C8                           mov ecx, eax
009289FA  48 83 C1 08                     add rcx, 8
009289FE  49 03 CF                        add rcx, r15
00928A01  E8 3A DE D9 FF                  call 0x1406c6840
00928A06  4C 8B 6C 24 60                  mov r13, qword ptr [rsp + 0x60]
00928A0B  4D 8B CF                        mov r9, r15
00928A0E  BA 02 00 00 00                  mov edx, 2
00928A13  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
00928A17  41 B8 FF FF FF FF               mov r8d, 0xffffffff
00928A1D  49 8B 4D 00                     mov rcx, qword ptr [r13]
00928A21  E8 4A 13 00 00                  call 0x140929d70
00928A26  33 D2                           xor edx, edx
00928A28  49 8B CF                        mov rcx, r15
00928A2B  8B D8                           mov ebx, eax
00928A2D  E8 3E 9E 25 00                  call 0x140b82870
00928A32  E9 E6 FA FF FF                  jmp 0x14092851d
00928A37  66 0F 1F 84 00 00 00 00 00      nop word ptr [rax + rax]
00928A40  49 83 C7 02                     add r15, 2
00928A44  66 41 83 3F 20                  cmp word ptr [r15], 0x20
00928A49  0F 85 D0 FC FF FF               jne 0x14092871f
00928A4F  EB EF                           jmp 0x140928a40
00928A51  41 BE 08 00 00 00               mov r14d, 8
00928A57  E9 CB F6 FF FF                  jmp 0x140928127
00928A5C  0F B7 43 02                     movzx eax, word ptr [rbx + 2]
00928A60  48 83 C3 02                     add rbx, 2
00928A64  66 83 F8 20                     cmp ax, 0x20
00928A68  0F 84 AE 01 00 00               je 0x140928c1c
00928A6E  66 83 F8 28                     cmp ax, 0x28
00928A72  0F 85 C6 00 00 00               jne 0x140928b3e
00928A78  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
00928A7C  48 85 C9                        test rcx, rcx
00928A7F  0F 85 AA 01 00 00               jne 0x140928c2f
00928A85  33 F6                           xor esi, esi
00928A87  48 8B 4D B0                     mov rcx, qword ptr [rbp - 0x50]
00928A8B  89 74 24 6C                     mov dword ptr [rsp + 0x6c], esi
00928A8F  48 85 C9                        test rcx, rcx
00928A92  0F 85 A9 01 00 00               jne 0x140928c41
00928A98  89 74 24 70                     mov dword ptr [rsp + 0x70], esi
00928A9C  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
00928AA1  48 8B CB                        mov rcx, rbx
00928AA4  40 80 FF 12                     cmp dil, 0x12
00928AA8  74 4F                           je 0x140928af9
00928AAA  C6 44 24 40 00                  mov byte ptr [rsp + 0x40], 0
00928AAF  4C 8D 4C 24 6C                  lea r9, [rsp + 0x6c]
00928AB4  C6 44 24 38 00                  mov byte ptr [rsp + 0x38], 0
00928AB9  4C 8D 45 80                     lea r8, [rbp - 0x80]
00928ABD  48 89 74 24 30                  mov qword ptr [rsp + 0x30], rsi
00928AC2  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
00928AC7  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00928ACC  E8 4F 91 0D 00                  call 0x140a01c20
00928AD1  4C 8B 44 24 58                  mov r8, qword ptr [rsp + 0x58]
00928AD6  44 8B F0                        mov r14d, eax
00928AD9  48 8B 74 24 78                  mov rsi, qword ptr [rsp + 0x78]
00928ADE  E9 56 FE FF FF                  jmp 0x140928939
00928AE3  F7 C7 DF FF FF FF               test edi, 0xffffffdf
00928AE9  0F 84 C6 F9 FF FF               je 0x1409284b5
00928AEF  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00928AF4  E9 24 FA FF FF                  jmp 0x14092851d
00928AF9  C6 44 24 38 00                  mov byte ptr [rsp + 0x38], 0
00928AFE  4C 8D 4C 24 70                  lea r9, [rsp + 0x70]
00928B03  48 89 74 24 30                  mov qword ptr [rsp + 0x30], rsi
00928B08  4C 8D 45 B0                     lea r8, [rbp - 0x50]
00928B0C  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
00928B11  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00928B16  E8 C9 E9 19 00                  call 0x140ac74e4
00928B1B  44 8B F0                        mov r14d, eax
00928B1E  85 C0                           test eax, eax
00928B20  0F 84 2B 01 00 00               je 0x140928c51
00928B26  49 8B 45 00                     mov rax, qword ptr [r13]
00928B2A  E9 DD F6 FF FF                  jmp 0x14092820c
00928B2F  49 8B 45 00                     mov rax, qword ptr [r13]
00928B33  41 BE 34 05 00 00               mov r14d, 0x534
00928B39  E9 D3 F6 FF FF                  jmp 0x140928211
00928B3E  48 8B F3                        mov rsi, rbx
00928B41  48 89 5C 24 78                  mov qword ptr [rsp + 0x78], rbx
00928B46  E9 EE FD FF FF                  jmp 0x140928939
00928B4B  0F 1F 44 00 00                  nop dword ptr [rax + rax]
00928B50  48 83 C3 02                     add rbx, 2
00928B54  66 83 3B 20                     cmp word ptr [rbx], 0x20
00928B58  0F 85 89 F8 FF FF               jne 0x1409283e7
00928B5E  EB F0                           jmp 0x140928b50
00928B60  BB 77 00 00 C0                  mov ebx, 0xc0000077
00928B65  E9 B3 F9 FF FF                  jmp 0x14092851d
00928B6A  8B C8                           mov ecx, eax
00928B6C  E8 CF E0 FF FF                  call 0x140926c40
00928B71  44 8B F0                        mov r14d, eax
00928B74  85 C0                           test eax, eax
00928B76  0F 84 70 FD FF FF               je 0x1409288ec
00928B7C  4C 8B 45 C0                     mov r8, qword ptr [rbp - 0x40]
00928B80  4C 89 44 24 58                  mov qword ptr [rsp + 0x58], r8
00928B85  E9 72 FD FF FF                  jmp 0x1409288fc
00928B8A  BF 38 05 00 00                  mov edi, 0x538
00928B8F  8B C7                           mov eax, edi
00928B91  E9 0D F5 FF FF                  jmp 0x1409280a3
00928B96  0F B7 46 02                     movzx eax, word ptr [rsi + 2]
00928B9A  48 83 C6 02                     add rsi, 2
00928B9E  66 83 F8 20                     cmp ax, 0x20
00928BA2  74 F2                           je 0x140928b96
00928BA4  E9 87 FA FF FF                  jmp 0x140928630
00928BA9  48 83 C6 02                     add rsi, 2
00928BAD  66 83 3E 20                     cmp word ptr [rsi], 0x20
00928BB1  74 F6                           je 0x140928ba9
00928BB3  E9 8C FA FF FF                  jmp 0x140928644
00928BB8  49 8B 45 00                     mov rax, qword ptr [r13]
00928BBC  C6 00 04                        mov byte ptr [rax], 4
00928BBF  E9 28 FB FF FF                  jmp 0x1409286ec
00928BC4  49 83 C7 02                     add r15, 2
00928BC8  66 41 83 3F 20                  cmp word ptr [r15], 0x20
00928BCD  74 F5                           je 0x140928bc4
00928BCF  E9 23 FB FF FF                  jmp 0x1409286f7
00928BD4  49 83 C7 02                     add r15, 2
00928BD8  66 41 83 3F 20                  cmp word ptr [r15], 0x20
00928BDD  74 F5                           je 0x140928bd4
00928BDF  E9 71 F6 FF FF                  jmp 0x140928255
00928BE4  49 83 C7 02                     add r15, 2
00928BE8  66 41 83 3F 20                  cmp word ptr [r15], 0x20
00928BED  74 F5                           je 0x140928be4
00928BEF  E9 79 F6 FF FF                  jmp 0x14092826d
00928BF4  41 0F B7 47 02                  movzx eax, word ptr [r15 + 2]
00928BF9  49 83 C7 02                     add r15, 2
00928BFD  66 83 F8 20                     cmp ax, 0x20
00928C01  74 F1                           je 0x140928bf4
00928C03  E9 35 F7 FF FF                  jmp 0x14092833d
00928C08  41 0F B7 47 02                  movzx eax, word ptr [r15 + 2]
00928C0D  49 83 C7 02                     add r15, 2
00928C11  66 83 F8 20                     cmp ax, 0x20
00928C15  74 F1                           je 0x140928c08
00928C17  E9 4F F7 FF FF                  jmp 0x14092836b
00928C1C  0F B7 43 02                     movzx eax, word ptr [rbx + 2]
00928C20  48 83 C3 02                     add rbx, 2
00928C24  66 83 F8 20                     cmp ax, 0x20
00928C28  74 F2                           je 0x140928c1c
00928C2A  E9 3F FE FF FF                  jmp 0x140928a6e
00928C2F  33 D2                           xor edx, edx
00928C31  E8 3A 9C 25 00                  call 0x140b82870
00928C36  33 F6                           xor esi, esi
00928C38  48 89 75 80                     mov qword ptr [rbp - 0x80], rsi
00928C3C  E9 46 FE FF FF                  jmp 0x140928a87
00928C41  33 D2                           xor edx, edx
00928C43  E8 28 9C 25 00                  call 0x140b82870
00928C48  48 89 75 B0                     mov qword ptr [rbp - 0x50], rsi
00928C4C  E9 47 FE FF FF                  jmp 0x140928a98
00928C51  48 8B 74 24 78                  mov rsi, qword ptr [rsp + 0x78]
00928C56  4C 8B 44 24 58                  mov r8, qword ptr [rsp + 0x58]
00928C5B  E9 D9 FC FF FF                  jmp 0x140928939
00928C60  48 83 C6 02                     add rsi, 2
00928C64  48 89 74 24 78                  mov qword ptr [rsp + 0x78], rsi
00928C69  0F B7 06                        movzx eax, word ptr [rsi]
00928C6C  66 83 F8 20                     cmp ax, 0x20
00928C70  74 EE                           je 0x140928c60
00928C72  E9 9A F7 FF FF                  jmp 0x140928411
00928C77  41 8D 47 03                     lea eax, [r15 + 3]
00928C7B  83 E0 FC                        and eax, 0xfffffffc
00928C7E  8D 58 0C                        lea ebx, [rax + 0xc]
00928C81  3B D8                           cmp ebx, eax
00928C83  0F 82 B8 F7 FF FF               jb 0x140928441
00928C89  E9 A2 F7 FF FF                  jmp 0x140928430
00928C8E  8D 5A 0C                        lea ebx, [rdx + 0xc]
00928C91  3B DA                           cmp ebx, edx
00928C93  0F 82 A8 F7 FF FF               jb 0x140928441
00928C99  E9 92 F7 FF FF                  jmp 0x140928430
00928C9E  48 83 7D A8 00                  cmp qword ptr [rbp - 0x58], 0
00928CA3  BB 20 00 00 00                  mov ebx, 0x20
00928CA8  B8 10 00 00 00                  mov eax, 0x10
00928CAD  0F 44 D8                        cmove ebx, eax
00928CB0  48 83 7D A0 00                  cmp qword ptr [rbp - 0x60], 0
00928CB5  0F 84 75 F7 FF FF               je 0x140928430
00928CBB  03 D8                           add ebx, eax
00928CBD  E9 6E F7 FF FF                  jmp 0x140928430
00928CC2  48 83 7D A8 00                  cmp qword ptr [rbp - 0x58], 0
00928CC7  B9 10 00 00 00                  mov ecx, 0x10
00928CCC  B8 20 00 00 00                  mov eax, 0x20
00928CD1  0F 44 C1                        cmove eax, ecx
00928CD4  48 83 7D A0 00                  cmp qword ptr [rbp - 0x60], 0
00928CD9  8D 48 10                        lea ecx, [rax + 0x10]
00928CDC  0F 44 C8                        cmove ecx, eax
00928CDF  41 83 FF FC                     cmp r15d, -4
00928CE3  0F 87 1D FB FF FF               ja 0x140928806
00928CE9  41 8D 47 03                     lea eax, [r15 + 3]
00928CED  83 E0 FC                        and eax, 0xfffffffc
00928CF0  8D 1C 01                        lea ebx, [rcx + rax]
00928CF3  3B D8                           cmp ebx, eax
00928CF5  0F 82 46 F7 FF FF               jb 0x140928441
00928CFB  E9 30 F7 FF FF                  jmp 0x140928430
00928D00  0F B6 54 24 51                  movzx edx, byte ptr [rsp + 0x51]
00928D05  4C 8B 6C 24 60                  mov r13, qword ptr [rsp + 0x60]
00928D0A  0F B6 CA                        movzx ecx, dl
00928D0D  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
00928D12  0F B6 C2                        movzx eax, dl
00928D15  44 8B 4C 24 54                  mov r9d, dword ptr [rsp + 0x54]
00928D1A  80 E1 80                        and cl, 0x80
00928D1D  88 4C 24 30                     mov byte ptr [rsp + 0x30], cl
00928D21  44 8B C2                        mov r8d, edx
00928D24  49 8B 4D 00                     mov rcx, qword ptr [r13]
00928D28  24 40                           and al, 0x40
00928D2A  88 44 24 28                     mov byte ptr [rsp + 0x28], al
00928D2E  41 81 E0 3F FF FF FF            and r8d, 0xffffff3f
00928D35  BA 02 00 00 00                  mov edx, 2
00928D3A  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00928D3F  E8 0C 47 E6 FF                  call 0x14078d450
00928D44  8B D8                           mov ebx, eax
00928D46  E9 D7 F7 FF FF                  jmp 0x140928522
00928D4B  4C 8B 6C 24 60                  mov r13, qword ptr [rsp + 0x60]
00928D50  BA 02 00 00 00                  mov edx, 2
00928D55  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
00928D5A  44 0F B6 44 24 51               movzx r8d, byte ptr [rsp + 0x51]
00928D60  44 8B 4C 24 54                  mov r9d, dword ptr [rsp + 0x54]
00928D65  49 8B 4D 00                     mov rcx, qword ptr [r13]
00928D69  C6 44 24 28 01                  mov byte ptr [rsp + 0x28], 1
00928D6E  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00928D73  E8 A8 0C 00 00                  call 0x140929a20
00928D78  8B D8                           mov ebx, eax
00928D7A  E9 A3 F7 FF FF                  jmp 0x140928522
00928D7F  81 FF FF FF 00 00               cmp edi, 0xffff
00928D85  0F 83 67 F3 FF FF               jae 0x1409280f2
00928D8B  0F B6 5C 24 51                  movzx ebx, byte ptr [rsp + 0x51]
00928D90  F6 C3 E0                        test bl, 0xe0
00928D93  0F 85 59 F3 FF FF               jne 0x1409280f2
00928D99  83 7C 24 54 00                  cmp dword ptr [rsp + 0x54], 0
00928D9E  0F 85 4E F3 FF FF               jne 0x1409280f2
00928DA4  4C 8B 6C 24 58                  mov r13, qword ptr [rsp + 0x58]
00928DA9  41 8B 4D 02                     mov ecx, dword ptr [r13 + 2]
00928DAD  2B 4D D8                        sub ecx, dword ptr [rbp - 0x28]
00928DB0  0F 85 59 9F 1F 00               jne 0x140b22d0f
00928DB6  41 0F B7 4D 06                  movzx ecx, word ptr [r13 + 6]
00928DBB  0F B7 45 DC                     movzx eax, word ptr [rbp - 0x24]
00928DBF  2B C8                           sub ecx, eax
00928DC1  E9 49 9F 1F 00                  jmp 0x140b22d0f
00928DC6  0F B6 54 24 51                  movzx edx, byte ptr [rsp + 0x51]
00928DCB  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
00928DD0  0F B6 CA                        movzx ecx, dl
00928DD3  4C 8B 6C 24 60                  mov r13, qword ptr [rsp + 0x60]
00928DD8  0F B6 C2                        movzx eax, dl
00928DDB  44 8B 4C 24 54                  mov r9d, dword ptr [rsp + 0x54]
00928DE0  24 40                           and al, 0x40
00928DE2  80 E1 80                        and cl, 0x80
00928DE5  44 8B C2                        mov r8d, edx
00928DE8  88 4C 24 40                     mov byte ptr [rsp + 0x40], cl
00928DEC  BA 04 00 00 00                  mov edx, 4
00928DF1  49 8B 4D 00                     mov rcx, qword ptr [r13]
00928DF5  88 44 24 38                     mov byte ptr [rsp + 0x38], al
00928DF9  48 8B 45 A0                     mov rax, qword ptr [rbp - 0x60]
00928DFD  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00928E02  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00928E07  48 8B 45 A8                     mov rax, qword ptr [rbp - 0x58]
00928E0B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00928E10  E8 8B 46 E6 FF                  call 0x14078d4a0
00928E15  8B D8                           mov ebx, eax
00928E17  E9 06 F7 FF FF                  jmp 0x140928522
00928E1C  48 8B 45 A0                     mov rax, qword ptr [rbp - 0x60]
00928E20  BA 04 00 00 00                  mov edx, 4
00928E25  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
00928E2A  4C 8B 6C 24 60                  mov r13, qword ptr [rsp + 0x60]
00928E2F  44 0F B6 44 24 51               movzx r8d, byte ptr [rsp + 0x51]
00928E35  44 8B 4C 24 54                  mov r9d, dword ptr [rsp + 0x54]
00928E3A  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00928E3F  49 8B 4D 00                     mov rcx, qword ptr [r13]
00928E43  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00928E48  48 8B 45 A8                     mov rax, qword ptr [rbp - 0x58]
00928E4C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00928E51  E8 CA 42 E6 FF                  call 0x14078d120
00928E56  8B D8                           mov ebx, eax
00928E58  E9 C5 F6 FF FF                  jmp 0x140928522
00928E5D  8B 44 24 54                     mov eax, dword ptr [rsp + 0x54]
00928E61  4C 8B 6C 24 60                  mov r13, qword ptr [rsp + 0x60]
00928E66  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
00928E6B  44 0F B6 44 24 51               movzx r8d, byte ptr [rsp + 0x51]
00928E71  4C 8B CF                        mov r9, rdi
00928E74  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00928E78  49 8B 4D 00                     mov rcx, qword ptr [r13]
00928E7C  E8 13 C1 E7 FF                  call 0x1407a4f94
00928E81  8B D8                           mov ebx, eax
00928E83  E9 9A F6 FF FF                  jmp 0x140928522
00928E88  41 81 FF FF FF 00 00            cmp r15d, 0xffff
00928E8F  0F 83 5D F2 FF FF               jae 0x1409280f2
00928E95  48 8B 45 80                     mov rax, qword ptr [rbp - 0x80]
00928E99  4C 8B 6C 24 60                  mov r13, qword ptr [rsp + 0x60]
00928E9E  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
00928EA3  44 0F B6 44 24 51               movzx r8d, byte ptr [rsp + 0x51]
00928EA9  4C 8B CF                        mov r9, rdi
00928EAC  66 44 89 7C 24 38               mov word ptr [rsp + 0x38], r15w
00928EB2  49 8B 4D 00                     mov rcx, qword ptr [r13]
00928EB6  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00928EBB  8B 44 24 54                     mov eax, dword ptr [rsp + 0x54]
00928EBF  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00928EC3  E8 90 BE E7 FF                  call 0x1407a4d58
00928EC8  8B D8                           mov ebx, eax
00928ECA  E9 53 F6 FF FF                  jmp 0x140928522
00928ECF  4C 8B 6C 24 60                  mov r13, qword ptr [rsp + 0x60]
00928ED4  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
00928ED9  44 0F B6 44 24 51               movzx r8d, byte ptr [rsp + 0x51]
00928EDF  44 8B 4C 24 54                  mov r9d, dword ptr [rsp + 0x54]
00928EE4  49 8B 4D 00                     mov rcx, qword ptr [r13]
00928EE8  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00928EED  E8 02 C2 E7 FF                  call 0x1407a50f4
00928EF2  8B D8                           mov ebx, eax
00928EF4  E9 29 F6 FF FF                  jmp 0x140928522
00928EF9  48 8B 45 A0                     mov rax, qword ptr [rbp - 0x60]
00928EFD  BA 04 00 00 00                  mov edx, 4
00928F02  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
00928F07  4C 8B 6C 24 60                  mov r13, qword ptr [rsp + 0x60]
00928F0C  44 0F B6 44 24 51               movzx r8d, byte ptr [rsp + 0x51]
00928F12  44 8B 4C 24 54                  mov r9d, dword ptr [rsp + 0x54]
00928F17  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00928F1C  49 8B 4D 00                     mov rcx, qword ptr [r13]
00928F20  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00928F25  48 8B 45 A8                     mov rax, qword ptr [rbp - 0x58]
00928F29  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00928F2E  E8 7D 42 E6 FF                  call 0x14078d1b0
00928F33  8B D8                           mov ebx, eax
00928F35  E9 E8 F5 FF FF                  jmp 0x140928522
00928F3A  33 D2                           xor edx, edx
00928F3C  E8 2F 99 25 00                  call 0x140b82870
00928F41  45 33 C0                        xor r8d, r8d
00928F44  4C 89 45 B0                     mov qword ptr [rbp - 0x50], r8
00928F48  E9 2D F6 FF FF                  jmp 0x14092857a
00928F4D  4C 8B 6C 24 60                  mov r13, qword ptr [rsp + 0x60]
00928F52  41 BE 38 05 00 00               mov r14d, 0x538
00928F58  49 8B 45 00                     mov rax, qword ptr [r13]
00928F5C  E9 A9 F2 FF FF                  jmp 0x14092820a
00928F61  BB 17 00 00 C0                  mov ebx, 0xc0000017
00928F66  E9 8C F1 FF FF                  jmp 0x1409280f7
00928F6B  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00928F70  E9 82 F1 FF FF                  jmp 0x1409280f7
00928F75  49 8B 45 00                     mov rax, qword ptr [r13]
00928F79  41 BE 38 05 00 00               mov r14d, 0x538
00928F7F  33 F6                           xor esi, esi
00928F81  E9 8B F2 FF FF                  jmp 0x140928211
00928F86  33 D2                           xor edx, edx
00928F88  E8 E3 98 25 00                  call 0x140b82870
00928F8D  E9 A2 F1 FF FF                  jmp 0x140928134
00928F92  B8 57 00 00 00                  mov eax, 0x57
00928F97  E9 07 F1 FF FF                  jmp 0x1409280a3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall LocalGetAclForString(__int64 a1, unsigned __int8 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m100;
    unsigned int v_stack_m104;
    unsigned int v_stack_m108;
    unsigned int v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned int v_stack_m128;
    unsigned int v_stack_m12C;
    unsigned int v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int8 v_stack_m148;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB8;
    unsigned __int16 v_stack_mBC;
    unsigned int v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned int v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p20;
    unsigned __int8 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int8 v_stack_p38;
    unsigned __int8 v_stack_p40;
    unsigned __int8 v_stack_p50;
    unsigned __int8 v_stack_p51;
    unsigned __int8 v_stack_p52;
    unsigned int v_stack_p54;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned int v_stack_p68;
    unsigned int v_stack_p6C;
    unsigned int v_stack_p70;
    unsigned __int64 v_stack_p78;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (352);
    result = (*(unsigned __int64 *)(v_rip + 5122029)) ^ (v_rsp);
    v_stack_m48 = result;
    v_rdi = 0;
    v_stack_m138 = a3;
    result = 0;
    v_stack_m110 = 0;
    v_stack_m148 = 0;
    v_stack_m140 = 0;
    v_stack_mD8 = 0;
    v_stack_mC0 = 0;
    v_stack_mD0 = 0;
    v_stack_m118 = 0;
    v_stack_m12C = 0;
    v_stack_mE8 = 0;
    v_stack_m128 = 0;
    v_stack_mC8 = 0;
    v_stack_m120 = 0;
    v_stack_mBC = 256;
    if (a1 == 0) goto loc_00928F92;
    if (a3 == 0) goto loc_00928F92;
    if (a4 == 0) goto loc_00928F92;
    result = wcsnicmp(a1, v_rip - 9528136, v_rdi + 17, a4);
    if ((unsigned int)(result) == 0) goto loc_009281D9;
    v_rbx = (unsigned __int8)(-(a2));
    *(unsigned __int64 *)(a4) = 0;
    result = (unsigned int)((result) + (2));
    v_stack_m130 = (unsigned int)(result);
    result = FContainCallBackAce(a1, v_rip - 9528136, v_rdi + 17, a4);
    if ((unsigned int)(result) != 0) goto loc_00928159;
    result = wcschr(a1, v_rdi + 58, v_rdi + 17, a4);
    *(unsigned __int64 *)(a4) = result;
    goto loc_00928032;
loc_00928018:
    if (0 != 0) goto loc_00928B8A;
    if (0 != 0) goto loc_00928B8A;
    if (0 != 0) goto loc_00928B8F;
loc_00928032:
    if ((*(unsigned __int64 *)(a4)) == a1) goto loc_00928F92;
    if (*(unsigned __int64 *)(a4) != 0) goto loc_00928150;
loc_00928050:
    if ((*(unsigned __int16 *)(a1 + -1 * 2 + 2)) != 0) goto loc_00928050;
loc_00928060:
    *(unsigned __int64 *)(a4) = a1 + -1 + 1 * 2;
    result = LocalGetAceCount(a1, a1 + -1 + 1 * 2, v_stack_m110, a4);
    if ((unsigned int)(result) != 0) goto loc_00928127;
    if ((unsigned int)((unsigned int)(v_stack_m110)) != 0) goto loc_00928593;
    result = SddlpAlloc(8, a1 + -1 + 1 * 2, v_stack_m110, a4);
    *(unsigned __int64 *)(a3) = result;
    if (result != 0) goto loc_009280CB;
loc_009280A0:
loc_009280A3:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a1 + -1 + 1 * 2, v_stack_m110, a4);
    v_rsp = (v_rsp) + (352);
    return result;
loc_009280CB:
    *(unsigned __int8 *)(result) = 2;
    a1 = 0;
    *(unsigned __int8 *)(*(unsigned __int64 *)(a3) + 1) = 0;
    *(unsigned __int16 *)(*(unsigned __int64 *)(a3) + 2) = (unsigned __int16)(v_stack_p10);
    *(unsigned __int16 *)(*(unsigned __int64 *)(a3) + 4) = 0;
    *(unsigned __int16 *)(*(unsigned __int64 *)(a3) + 6) = 0;
    goto loc_009280A0;
loc_009280F7:
    result = RtlNtStatusToDosError((unsigned int)((unsigned int)(v_stack_p10)), a1 + -1 + 1 * 2, v_stack_m110, a4);
loc_00928106:
    if ((unsigned int)((unsigned int)((unsigned int)(result))) != 0) goto loc_0092820A;
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p60) + 2) = (unsigned __int16)((unsigned int)(v_stack_m100));
loc_0092811F:
    if ((unsigned __int8)(v_stack_p50) != 0) goto loc_00928229;
loc_00928127:
    if (v_stack_m118 != 0) goto loc_00928F86;
loc_00928134:
    if (v_stack_mE8 == 0) goto loc_009280A0;
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_mE8, a2, v_stack_m110, a4);
    goto loc_009280A3;
loc_00928150:
    goto loc_00928060;
loc_00928159:
    if ((*(unsigned __int16 *)(a1)) == 0) goto loc_00928032;
loc_00928162:
    if ((*(unsigned __int64 *)(a4)) != 0) goto loc_00928018;
    if (0 != 0) goto loc_00928018;
    a1 = (unsigned int)((*(unsigned __int16 *)(v_stack_p50)) - (34));
    if (condition_is_equal) goto loc_009281B4;
    a1 = (unsigned int)((a1) - (6));
    if (condition_is_equal) goto loc_0092819B;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_009281A5;
    if (((unsigned int)(a1)) == 17) goto loc_009281C7;
loc_0092818C:
    v_rbx = (v_stack_p50) + (2);
    if ((*(unsigned __int16 *)(v_rbx)) != 0) goto loc_00928162;
    goto loc_00928018;
loc_0092819B:
    if (0 != 0) goto loc_0092818C;
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)(result))) + 1);
    goto loc_0092818C;
loc_009281A5:
    if (0 != 0) goto loc_0092818C;
    if ((unsigned int)(v_r14) == 0) goto loc_009281D2;
    v_r14 = (unsigned int)((v_r14) + ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))) - 2)));
    goto loc_0092818C;
loc_009281B4:
    if (((unsigned int)(v_r14)) <= 1) goto loc_009281D2;
    result = 0;
    result = (0 == 0) ? 1 : 0;
    goto loc_0092818C;
loc_009281C7:
    if ((unsigned int)(v_r14) != 0) goto loc_0092818C;
    *(unsigned __int64 *)(a4) = v_rbx;
    goto loc_0092818C;
loc_009281D2:
    goto loc_0092818C;
loc_009281D9:
    *(unsigned __int64 *)(v_stack_p60) = (unsigned int)(0x538ULL);
    *(unsigned __int64 *)(a4) = a1 + 34;
    goto loc_00928127;
loc_009281EA:
    a3 = 0;
loc_009281F1:
    v_rdi = (unsigned int)(((unsigned int)(0x538ULL)) + 1);
    v_rbx = (v_rbx) + (32);
    if (((unsigned int)(v_rdi)) < 9) goto loc_00928729;
loc_00928200:
loc_0092820A:
    v_rsi = 0;
loc_0092820C:
loc_00928211:
    result = *(unsigned __int64 *)(v_stack_p60);
    if (*(unsigned __int64 *)(v_stack_p60) != 0) {
        a2 = 0;
        a1 = *(unsigned __int64 *)(v_stack_p60);
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    *(unsigned __int64 *)(v_stack_p60) = 0;
    goto loc_0092811F;
loc_00928229:
    if (v_stack_p58 == 0) goto loc_00928127;
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_p58, a2, a3, a4);
    goto loc_00928127;
loc_00928246:
    v_r15 = ((unsigned int)((unsigned int)(result))) + (2);
loc_0092824A:
    if ((*(unsigned __int16 *)(v_r15)) == 32) goto loc_00928BD4;
loc_00928255:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_r15))) == 59) goto loc_00928320;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_r15))) == 32) goto loc_00928BE4;
loc_0092826D:
    v_rsi = 0;
    if (((unsigned __int8)((unsigned int)(0x3ECULL))) == 17) { v_rsi = 4; }
loc_00928287:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 5114336 + 8))) & ((unsigned int)(v_rsi)));
    if (((unsigned int)(result)) != ((unsigned int)(v_rsi))) goto loc_009282A3;
    result = wcsnicmp(v_r15, *(unsigned __int64 *)(v_rip + 5114336 - 8), (unsigned int)(*(unsigned int *)(v_rip + 5114336)), a4);
    if ((unsigned int)(result) == 0) goto loc_009282DD;
loc_009282A3:
    v_rdi = (unsigned int)((0) + 1);
    v_rbx = (v_rip + 5114336) + (24);
    if (((unsigned int)(v_rdi)) < 28) goto loc_00928287;
loc_009282AE:
    a3 = 0;
    result = wcstoul(v_r15, v_stack_mD0, a3, a4);
    if (v_stack_mD0 != v_r15) goto loc_00928891;
loc_009282CE:
    goto loc_0092820A;
loc_009282DD:
    if (((unsigned int)(v_rdi)) >= 28) goto loc_009282AE;
    if (v_rip - 9601775 + (unsigned int)((unsigned int)(v_rdi)) + (unsigned int)((unsigned int)(v_rdi)) * 2 * 8 + 14715984 == 0) goto loc_009282AE;
    a3 = (unsigned int)(((unsigned int)(v_stack_p54)) | (*(unsigned int *)(v_rip - 9601775 + (unsigned int)((unsigned int)(v_rdi)) + (unsigned int)((unsigned int)(v_rdi)) * 2 * 8 + 14715984 + 12)));
    v_stack_p54 = (unsigned int)(a3);
    a3 = 0;
    goto loc_00928255;
loc_00928320:
    v_r15 = (v_r15 + (unsigned int)(*(unsigned int *)(v_rip - 9601775 + (unsigned int)((unsigned int)(v_rdi)) + (unsigned int)((unsigned int)(v_rdi)) * 2 * 8 + 14715984 + 8)) * 2) + (2);
loc_0092832A:
    if (0 >= 2) goto loc_0092834F;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_r15))) == 32) goto loc_00928BF4;
loc_0092833D:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_r15))) != 59) goto loc_00928876;
    v_r15 = (v_r15) + (2);
    v_rbx = (unsigned int)((0) + 1);
    goto loc_0092832A;
loc_0092834F:
    if ((unsigned int)((unsigned int)(v_stack_mE0)) != 0) goto loc_00928106;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_r15))) == 32) goto loc_00928C08;
loc_0092836B:
    v_rsi = 0;
    v_rbx = 0;
    v_stack_mE0 = 0;
    v_stack_p50 = 0;
    if ((unsigned __int16)(*(unsigned __int16 *)(v_r15)) == 0) goto loc_00928B2F;
    if ((*(unsigned __int16 *)(v_r15 + 2)) == 0) goto loc_00928B2F;
    a3 = 0;
    v_stack_p78 = v_r15 + 4;
    a2 = 0;
    v_stack_p30 = v_stack_mE0;
    v_stack_p28 = 0;
    result = LookupSidInTable(v_r15, a2, a3, a4);
    if (result == 0) goto loc_009288BF;
    v_stack_p58 = *(unsigned __int64 *)(result + 16);
loc_009283C3:
    if (v_stack_p78 == 0) goto loc_00928F75;
    if (*(unsigned __int64 *)(result + 16) == 0) goto loc_00928F75;
    if ((*(unsigned __int16 *)(v_stack_p78)) == 32) goto loc_00928B50;
loc_009283E7:
    if (((unsigned __int8)((unsigned int)(0x538ULL))) > 21) goto loc_009283FB;
    if (((unsigned __int8)((unsigned int)(0x538ULL))) < 21) goto loc_0092892F;
loc_009283FB:
loc_00928404:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_p78))) == 32) goto loc_00928C60;
loc_00928411:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_p78))) != 41) goto loc_009282CE;
    v_rsi = (v_stack_p78) + (2);
    if (((unsigned int)((unsigned int)(0x538ULL))) != 3) goto loc_009287DA;
loc_00928430:
    result = RtlLengthSid(*(unsigned __int64 *)(result + 16), (unsigned int)(v_stack_p70), *(unsigned __int64 *)(result + 16), a4);
    v_rdi = (unsigned int)((12 - 4) + ((unsigned int)(result)));
    if (((unsigned int)(v_rdi)) >= 12) goto loc_00928455;
loc_00928441:
    goto loc_0092820A;
loc_00928455:
    result = (unsigned int)(((unsigned int)(v_stack_m100)) + ((unsigned int)(v_rdi)));
    v_stack_m100 = (unsigned int)(result);
    if (((unsigned int)(result)) < ((unsigned int)(v_rdi))) goto loc_00928441;
    if (((unsigned int)(result)) > ((unsigned int)((unsigned int)(v_stack_m108)))) goto loc_009288A0;
    if ((unsigned int)(v_stack_p60) != 0) goto loc_009287A5;
    result = RtlValidSid(v_stack_p58, (unsigned int)(v_stack_m108), *(unsigned __int64 *)(result + 16), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00928518;
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p60)))) > 4) goto loc_0092886C;
    v_r15 = *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p60));
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p60)))) <= 2) {
        v_r15 = 2;
    }
    v_rdi = (unsigned int)((v_stack_p51) & (0xFFFFFFE0ULL));
    if (condition_is_not_equal) goto loc_00928AE3;
loc_009284B5:
    result = RtlValidAcl(*(unsigned __int64 *)(v_stack_p60), (unsigned int)(v_stack_m108), *(unsigned __int64 *)(result + 16), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00928B60;
    a4 = 0;
loc_009284D4:
    if (0 < ((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p60) + 4)))) goto loc_00928811;
    a3 = (*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p60) + 2)) + (*(unsigned __int64 *)(v_stack_p60));
    a2 = *(unsigned __int64 *)(v_stack_p60) + 8;
    if ((*(unsigned __int64 *)(v_stack_p60) + 8) > a3) { a2 = 0; }
    a1 = (unsigned __int16)((*(unsigned __int8 *)(v_stack_p58 + 1)) + (4));
    a1 = (unsigned __int16)((a1) << (2));
    if (a2 == 0) goto loc_00928511;
    result = ((unsigned __int16)(a1)) + (a2);
    if (result <= a3) goto loc_0092882F;
loc_00928511:
    goto loc_00928522;
loc_00928518:
loc_0092851D:
loc_00928522:
    if (sign_flag) goto loc_009280F7;
    if (((unsigned __int8)(v_stack_p50)) != 1) goto loc_00928542;
    result = v_stack_p50;
    if (v_stack_p58 != 0) {
        a2 = 0;
        a1 = v_stack_p58;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    a3 = 0;
    v_stack_p58 = 0;
    v_stack_mD8 = 0;
    result = 0;
    if (v_stack_m118 != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(v_stack_m118, a2, a3, a4);
        a3 = 0;
        v_stack_m118 = 0;
    }
    v_stack_p6C = 0;
    if (v_stack_mE8 != 0) goto loc_00928F3A;
loc_0092857A:
    v_stack_p70 = 0;
    if ((*(unsigned __int16 *)(v_rsi)) == 40) {
        v_rsi = (v_rsi) + (2);
    }
    result = (unsigned int)(((unsigned int)(v_stack_m104)) + 1);
    goto loc_009285ED;
loc_00928593:
    v_rdi = (unsigned int)((v_stack_p58) * ((unsigned int)((unsigned int)(v_stack_m110))));
    v_rdi = (unsigned int)((v_rdi) + (8));
    if (((unsigned int)(v_rdi)) > ((unsigned int)((unsigned int)(0xFFFFULL)))) { v_rdi = (unsigned int)((unsigned int)(0xFFFFULL)); }
    v_stack_m108 = (unsigned int)(v_rdi);
    result = SddlpAlloc((unsigned int)((unsigned int)(v_rdi)), a2, a3, a4);
    *(unsigned __int64 *)(v_stack_p60) = result;
    if (result == 0) goto loc_00928A51;
    *(unsigned __int8 *)(result) = 2;
    a3 = 0;
    v_stack_m100 = 8;
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p60) + 1) = 0;
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p60) + 2) = (unsigned __int16)(v_rdi);
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p60) + 4) = 0;
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p60) + 6) = 0;
loc_009285ED:
    v_stack_m104 = 0;
    v_stack_mE0 = 534;
    if (0 >= ((unsigned int)((unsigned int)(v_stack_m110)))) goto loc_00928106;
    v_stack_p51 = 0;
    v_stack_p54 = 0;
    v_stack_mB8 = v_xmm0;
    v_stack_mF0 = 0;
    v_stack_mA8 = v_xmm1;
    v_stack_mF8 = 0;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rsi))) == 32) goto loc_00928B96;
loc_00928630:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rsi))) != 40) goto loc_00928644;
    v_rsi = (v_rsi) + (2);
    if ((*(unsigned __int16 *)(v_rsi)) == 32) goto loc_00928BA9;
loc_00928644:
loc_0092864E:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 5113025 + 8))) & ((unsigned int)((unsigned int)(v_stack_p68))));
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(v_stack_p68)))) goto loc_00928673;
    if (v_rsi == 0) goto loc_0092868D;
    result = wcsnicmp(v_rsi, *(unsigned __int64 *)(v_rip + 5113025 - 8), (unsigned int)(*(unsigned int *)(v_rip + 5113025)), a4);
    if ((unsigned int)(result) == 0) goto loc_00928693;
loc_00928673:
    v_rdi = (unsigned int)((0) + 1);
    v_rbx = (v_rip + 5113025) + (24);
    if (((unsigned int)(v_rdi)) < 17) goto loc_0092864E;
loc_0092867E:
    goto loc_0092820A;
loc_0092868D:
    if ((*(unsigned int *)(v_rbx + 4)) != 0) goto loc_00928673;
loc_00928693:
    if (((unsigned int)(v_rdi)) >= 17) goto loc_0092867E;
    if (v_rip - 9602721 + 14715568 + (unsigned int)((unsigned int)(v_rdi)) + (unsigned int)((unsigned int)(v_rdi)) * 2 * 8 == 0) goto loc_0092867E;
    v_stack_p52 = (unsigned __int8)(*(unsigned __int8 *)(v_rip - 9602721 + 14715568 + (unsigned int)((unsigned int)(v_rdi)) + (unsigned int)((unsigned int)(v_rdi)) * 2 * 8 + 12));
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rsi + (unsigned int)(*(unsigned int *)(v_rip - 9602721 + 14715568 + (unsigned int)((unsigned int)(v_rdi)) + (unsigned int)((unsigned int)(v_rdi)) * 2 * 8 + 8)) * 2))) != 59) goto loc_00928796;
loc_009286D3:
    v_r15 = (v_rsi + (unsigned int)(*(unsigned int *)(v_rip - 9602721 + 14715568 + (unsigned int)((unsigned int)(v_rdi)) + (unsigned int)((unsigned int)(v_rdi)) * 2 * 8 + 8)) * 2) + (2);
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rip - 9602721 + 14715568 + (unsigned int)((unsigned int)(v_rdi)) + (unsigned int)((unsigned int)(v_rdi)) * 2 * 8 + 12) - 5)) <= 3) goto loc_00928BB8;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rip - 9602721 + 14715568 + (unsigned int)((unsigned int)(v_rdi)) + (unsigned int)((unsigned int)(v_rdi)) * 2 * 8 + 12))) == 11) goto loc_00928BB8;
loc_009286EC:
    if ((*(unsigned __int16 *)(v_r15)) == 32) goto loc_00928BC4;
loc_009286F7:
loc_009286FA:
    a3 = 0;
    if (v_r15 == (*(unsigned __int64 *)(a4))) goto loc_0092824A;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_r15))) == 59) goto loc_00928246;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_r15))) == 32) goto loc_00928A40;
loc_0092871F:
loc_00928729:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 5112443 - 4))) & ((unsigned int)((unsigned int)(v_stack_p68))));
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(v_stack_p68)))) goto loc_009281F1;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5112443))) != 0) goto loc_00928910;
loc_00928740:
    result = wcsnicmp(v_r15, *(unsigned __int64 *)(v_rip + 5112443 - 20), (unsigned int)(*(unsigned int *)(v_rip + 5112443 - 12)), v_rip - 9602721);
    if ((unsigned int)(result) != 0) goto loc_009281EA;
    if (0 >= 9) goto loc_00928200;
    result = (0) << (5);
    result = (result) + (v_rip + 5112358);
    if (condition_is_equal) goto loc_00928200;
    a3 = (unsigned __int8)((v_stack_p51) | (*(unsigned __int8 *)(result + 12)));
    v_stack_p51 = (unsigned __int8)(a3);
    goto loc_009286FA;
loc_00928796:
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(result + 8)))) == 32) goto loc_009286D3;
    goto loc_009282CE;
loc_009287A5:
    if (((unsigned int)(v_stack_p60)) != 17) goto loc_00928961;
    v_stack_p28 = (unsigned int)((unsigned int)(v_stack_p54));
    result = SddlAddMandatoryAce(*(unsigned __int64 *)(v_stack_p60), (unsigned int)(v_stack_p68), v_stack_p51, v_stack_p58);
    goto loc_00928522;
loc_009287DA:
    if (((unsigned int)(v_stack_p60)) > 21) goto loc_00928F4D;
    a1 = ((unsigned int)(*(unsigned int *)(v_rip - 9603051 + v_stack_p58 * 4 + 275308))) + (v_rip - 9603051);
loc_00928811:
    result = (*(unsigned __int16 *)((unsigned int)((unsigned int)(result)) + 2)) + ((unsigned int)((unsigned int)(result)));
    if (((unsigned int)(v_stack_p68)) >= result) goto loc_00928B60;
    a1 = (unsigned int)((a1) + 1);
    a2 = ((unsigned int)(v_stack_p68)) + (*(unsigned __int16 *)((unsigned int)(v_stack_p68) + 2));
    goto loc_009284D4;
loc_0092882F:
    *(unsigned __int8 *)(a2 + 1) = (unsigned __int8)(v_stack_p51);
    *(unsigned __int16 *)(a2 + 2) = (unsigned __int16)(a1);
    *(unsigned int *)(a2 + 4) = (unsigned int)((unsigned int)(v_stack_p54));
    *(unsigned __int8 *)(a2) = (unsigned __int8)(v_rip - 9603051);
    a2 = (a2) + (8);
    result = RtlCopySid(*(unsigned __int8 *)(v_stack_p58 + 1) * 4 + 8, a2, v_stack_p58, v_rip - 9603051);
    result = 0;
    *(unsigned __int8 *)((unsigned int)((unsigned int)(result))) = (unsigned __int8)(v_r15 + (unsigned int)(*(unsigned int *)(result + 8)) * 2);
    goto loc_00928522;
loc_0092886C:
    goto loc_0092851D;
loc_00928876:
    if (((unsigned __int8)(v_stack_p58)) != 11) goto loc_009282CE;
loc_00928891:
    a3 = 0;
    goto loc_00928255;
loc_009288A0:
    a1 = (unsigned int)(((unsigned int)(v_stack_m110)) - (v_stack_m104));
    a1 = (a1) * ((unsigned int)((unsigned int)(v_stack_p58)));
    if (a1 > ((unsigned int)(0xFFFFFFFFULL))) goto loc_00928441;
loc_009288BF:
    v_stack_p58 = v_stack_mE0;
    if (v_stack_mE0 != 0) goto loc_009288FA;
    result = LocalpConvertStringSidToSid(*(unsigned __int8 *)(v_rip - 9602721 + 14715568 + (unsigned int)((unsigned int)(v_rdi)) + (unsigned int)((unsigned int)(v_rdi)) * 2 * 8 + 12) - 5, v_stack_mD8, v_stack_p78, v_rip - 9603051);
    if (sign_flag) goto loc_00928B6A;
loc_009288EC:
    v_stack_p58 = v_stack_mD8;
    v_rbx = (unsigned int)(0xC0000059ULL);
    if (v_stack_mD8 != 0) {
        v_rbx = 1;
    }
    v_stack_p50 = (unsigned __int8)(v_rbx);
    if ((unsigned int)(*(unsigned __int8 *)(v_rip - 9602721 + 14715568 + (unsigned int)((unsigned int)(v_rdi)) + (unsigned int)((unsigned int)(v_rdi)) * 2 * 8 + 12)) == 0) goto loc_009283C3;
    goto loc_00928106;
loc_00928910:
    if (((unsigned int)(v_stack_mD8)) >= ((unsigned int)(v_stack_mD8))) goto loc_009281EA;
    if ((*(unsigned __int8 *)((unsigned int)((unsigned int)(v_stack_mD8)) + *(unsigned __int64 *)(v_rbx + 4) * 1)) == ((unsigned __int8)(*(unsigned __int8 *)(v_rip - 9602721 + 14715568 + (unsigned int)((unsigned int)(v_rdi)) + (unsigned int)((unsigned int)(v_rdi)) * 2 * 8 + 12)))) goto loc_00928740;
    a3 = (unsigned int)((v_stack_mD8) + 1);
    goto loc_00928910;
loc_0092892F:
    if ((*(unsigned __int16 *)(v_rbx)) == 59) goto loc_00928A5C;
loc_00928939:
    if ((unsigned int)((unsigned int)(v_stack_p6C)) != 0) goto loc_0092894F;
    if ((unsigned int)((unsigned int)(v_stack_p70)) == 0) goto loc_009282CE;
loc_0092894F:
    if ((unsigned int)(*(unsigned __int8 *)(v_rip - 9602721 + 14715568 + (unsigned int)((unsigned int)(v_rdi)) + (unsigned int)((unsigned int)(v_rdi)) * 2 * 8 + 12)) == 0) goto loc_00928404;
    goto loc_0092820A;
loc_00928961:
    if (((unsigned int)(v_stack_p60 - 1)) > 20) goto loc_00928F6B;
    a1 = ((unsigned int)(*(unsigned int *)(v_rip - 9603445 + v_stack_p60 - 1 * 4 + 275396))) + (v_rip - 9603445);
loc_00928A40:
    v_r15 = ((unsigned int)(v_stack_p6C)) + (2);
    if ((*(unsigned __int16 *)(v_r15)) != 32) goto loc_0092871F;
    goto loc_00928A40;
loc_00928A51:
    goto loc_00928127;
loc_00928A5C:
    v_rbx = (v_rbx) + (2);
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rbx + 2))) == 32) goto loc_00928C1C;
loc_00928A6E:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rbx + 2))) != 40) goto loc_00928B3E;
    if (v_stack_m118 != 0) goto loc_00928C2F;
    v_rsi = 0;
loc_00928A87:
    v_stack_p6C = 0;
    if (v_stack_mE8 != 0) goto loc_00928C41;
loc_00928A98:
    v_stack_p70 = 0;
    if (((unsigned __int8)(v_stack_p58)) == 18) goto loc_00928AF9;
    v_stack_p40 = 0;
    v_stack_p38 = 0;
    v_stack_p30 = 0;
    v_stack_p28 = 0;
    v_stack_p20 = 0;
    result = LocalGetConditionForString(v_rbx, v_stack_p78, v_stack_m118, v_stack_p6C);
    goto loc_00928939;
loc_00928AE3:
    if ((((unsigned int)(v_stack_p58)) & (0xFFFFFFDFULL)) == 0) goto loc_009284B5;
    goto loc_0092851D;
loc_00928AF9:
    v_stack_p38 = 0;
    v_stack_p30 = v_stack_p78;
    v_stack_p28 = v_stack_p78;
    v_stack_p20 = v_stack_p78;
    result = LocalGetRelativeAttributeForString(v_rbx, v_stack_p78, v_stack_mE8, v_stack_p70);
    if ((unsigned int)(result) == 0) goto loc_00928C51;
    goto loc_0092820C;
loc_00928B2F:
    goto loc_00928211;
loc_00928B3E:
    v_stack_p78 = (unsigned int)(0xC000000DULL);
    goto loc_00928939;
loc_00928B50:
    v_rbx = ((unsigned int)(0xC000000DULL)) + (2);
    if ((*(unsigned __int16 *)(v_rbx)) != 32) goto loc_009283E7;
    goto loc_00928B50;
loc_00928B60:
    goto loc_0092851D;
loc_00928B6A:
    result = RtlNtStatusToDosError((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_p60))), v_stack_p78, v_stack_mE8, v_stack_p70);
    if ((unsigned int)(result) == 0) goto loc_009288EC;
    v_stack_p58 = v_stack_mD8;
    goto loc_009288FC;
loc_00928B8A:
loc_00928B8F:
    goto loc_009280A3;
loc_00928B96:
    v_rsi = ((unsigned int)(0xC000000DULL)) + (2);
    if (((unsigned __int16)(*(unsigned __int16 *)((unsigned int)(0xC000000DULL) + 2))) == 32) goto loc_00928B96;
    goto loc_00928630;
loc_00928BA9:
    v_rsi = (v_rsi) + (2);
    if ((*(unsigned __int16 *)(v_rsi)) == 32) goto loc_00928BA9;
    goto loc_00928644;
loc_00928BB8:
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p60)) = 4;
    goto loc_009286EC;
loc_00928BC4:
    v_r15 = (v_r15) + (2);
    if ((*(unsigned __int16 *)(v_r15)) == 32) goto loc_00928BC4;
    goto loc_009286F7;
loc_00928BD4:
    v_r15 = (v_r15) + (2);
    if ((*(unsigned __int16 *)(v_r15)) == 32) goto loc_00928BD4;
    goto loc_00928255;
loc_00928BE4:
    v_r15 = (v_r15) + (2);
    if ((*(unsigned __int16 *)(v_r15)) == 32) goto loc_00928BE4;
    goto loc_0092826D;
loc_00928BF4:
    v_r15 = (v_r15) + (2);
    if (((unsigned __int16)(*(unsigned __int16 *)(v_r15 + 2))) == 32) goto loc_00928BF4;
    goto loc_0092833D;
loc_00928C08:
    v_r15 = (v_r15) + (2);
    if (((unsigned __int16)(*(unsigned __int16 *)(v_r15 + 2))) == 32) goto loc_00928C08;
    goto loc_0092836B;
loc_00928C1C:
    v_rbx = ((unsigned int)(0xC0000077ULL)) + (2);
    if (((unsigned __int16)(*(unsigned __int16 *)((unsigned int)(0xC0000077ULL) + 2))) == 32) goto loc_00928C1C;
    goto loc_00928A6E;
loc_00928C2F:
    a2 = 0;
    result = ExFreePoolWithTag((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_p60))), a2, v_stack_mD8, v_stack_p70);
    v_rsi = 0;
    v_stack_m118 = 0;
    goto loc_00928A87;
loc_00928C41:
    a2 = 0;
    result = ExFreePoolWithTag((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_p60))), a2, v_stack_mD8, v_stack_p70);
    v_stack_mE8 = 0;
    goto loc_00928A98;
loc_00928C51:
    goto loc_00928939;
loc_00928C60:
    v_rsi = (v_stack_p78) + (2);
    v_stack_p78 = v_rsi;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rsi))) == 32) goto loc_00928C60;
    goto loc_00928411;
loc_00928F3A:
    a2 = 0;
    result = ExFreePoolWithTag((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_p60))), a2, v_stack_p58, v_stack_p70);
    a3 = 0;
    v_stack_mE8 = 0;
    goto loc_0092857A;
loc_00928F4D:
    goto loc_0092820A;
loc_00928F6B:
    goto loc_009280F7;
loc_00928F75:
    v_rsi = 0;
    goto loc_00928211;
loc_00928F86:
    a2 = 0;
    result = ExFreePoolWithTag((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_p60))), a2, a3, v_stack_p70);
    goto loc_00928134;
loc_00928F92:
    goto loc_009280A3;
}
```

## 5. (Beta) C Style

```c
int64_t LocalGetAclForString(void *Arg1, uint8_t Arg2, void *Arg3, void *Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m100;
    uint32_t v_stack_m104;
    uint32_t v_stack_m108;
    uint32_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint32_t v_stack_m128;
    uint32_t v_stack_m12C;
    uint32_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint8_t v_stack_m148;
    uint64_t v_stack_m48;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB8;
    uint16_t v_stack_mBC;
    uint32_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint32_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p10;
    uint32_t v_stack_p20;
    uint8_t v_stack_p28;
    uint64_t v_stack_p30;
    uint8_t v_stack_p38;
    uint8_t v_stack_p40;
    uint8_t v_stack_p50;
    uint8_t v_stack_p51;
    uint8_t v_stack_p52;
    uint32_t v_stack_p54;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint32_t v_stack_p68;
    uint32_t v_stack_p6C;
    uint32_t v_stack_p70;
    uint64_t v_stack_p78;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (352);
    result = (*(uint64_t *)(v_rip + 0x4E27ED)) ^ (local_rsp);
    v_stack_m48 = result;
    local_rdi = 0;
    v_stack_m138 = Arg3;
    result = 0;
    v_stack_m110 = 0;
    v_stack_m148 = 0;
    v_stack_m140 = 0;
    v_stack_mD8 = 0;
    v_stack_mC0 = 0;
    v_stack_mD0 = 0;
    v_stack_m118 = 0;
    v_stack_m12C = 0;
    v_stack_mE8 = 0;
    v_stack_m128 = 0;
    v_stack_mC8 = 0;
    v_stack_m120 = 0;
    v_stack_mBC = 256;
    if (Arg1 == NULL) goto loc_00928F92;
    if (Arg3 == NULL) goto loc_00928F92;
    if (Arg4 == NULL) goto loc_00928F92;
    result = wcsnicmp(Arg1, v_rip - 9528136, local_rdi + 17, Arg4);
    if ((uint32_t)(result) == 0) goto loc_009281D9;
    local_rbx = (uint8_t)(-(Arg2));
    *(uint64_t *)(arg4) = 0;
    result = (uint32_t)((result) + (2));
    v_stack_m130 = (uint32_t)(result);
    result = FContainCallBackAce(Arg1, v_rip - 9528136, local_rdi + 17, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00928159;
    result = wcschr(Arg1, local_rdi + 58, local_rdi + 17, Arg4);
    *(uint64_t *)(arg4) = result;
    goto loc_00928032;
loc_00928018:
    if (0 != 0) goto loc_00928B8A;
    if (0 != 0) goto loc_00928B8A;
    if (0 != 0) goto loc_00928B8F;
loc_00928032:
    if ((*(uint64_t *)(arg4)) == Arg1) goto loc_00928F92;
    if (*(uint64_t *)(arg4) != 0) goto loc_00928150;
loc_00928050:
    if ((*(uint16_t *)(arg1 + - 0x1 * 2 + 0x2)) != 0) goto loc_00928050;
loc_00928060:
    *(void **)(arg4) = Arg1 + -1 + 1 * 2;
    result = LocalGetAceCount(Arg1, Arg1 + -1 + 1 * 2, v_stack_m110, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00928127;
    if ((uint32_t)((uint32_t)(v_stack_m110)) != 0) goto loc_00928593;
    result = SddlpAlloc(8, Arg1 + -1 + 1 * 2, v_stack_m110, Arg4);
    *(uint64_t *)(arg3) = result;
    if (result != 0) goto loc_009280CB;
loc_009280A0:
loc_009280A3:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg1 + -1 + 1 * 2, v_stack_m110, Arg4);
    local_rsp = (local_rsp) + (352);
    return result;
loc_009280CB:
    *(uint8_t *)(result) = 2;
    Arg1 = 0;
    *(uint8_t *)(*(uint64_t *)(arg3) + 0x1) = 0;
    *(uint16_t *)(*(uint64_t *)(arg3) + 0x2) = (uint16_t)(v_stack_p10);
    *(uint16_t *)(*(uint64_t *)(arg3) + 0x4) = 0;
    *(uint16_t *)(*(uint64_t *)(arg3) + 0x6) = 0;
    goto loc_009280A0;
loc_009280F7:
    result = RtlNtStatusToDosError((uint32_t)((uint32_t)(v_stack_p10)), Arg1 + -1 + 1 * 2, v_stack_m110, Arg4);
loc_00928106:
    if ((uint32_t)((uint32_t)((uint32_t)(result))) != 0) goto loc_0092820A;
    *(uint16_t *)(*(uint64_t *)(v_stack_p60) + 0x2) = (uint16_t)((uint32_t)(v_stack_m100));
loc_0092811F:
    if ((uint8_t)(v_stack_p50) != 0) goto loc_00928229;
loc_00928127:
    if (v_stack_m118 != 0) goto loc_00928F86;
loc_00928134:
    if (v_stack_mE8 == 0) goto loc_009280A0;
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_mE8, Arg2, v_stack_m110, Arg4);
    goto loc_009280A3;
loc_00928150:
    goto loc_00928060;
loc_00928159:
    if ((*(uint16_t *)(arg1)) == 0) goto loc_00928032;
loc_00928162:
    if ((*(uint64_t *)(arg4)) != 0) goto loc_00928018;
    if (0 != 0) goto loc_00928018;
    Arg1 = (uint32_t)((*(uint16_t *)(v_stack_p50)) - (34));
    if (condition_is_equal) goto loc_009281B4;
    Arg1 = (uint32_t)((Arg1) - (6));
    if (condition_is_equal) goto loc_0092819B;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_009281A5;
    if (((uint32_t)(Arg1)) == 17) goto loc_009281C7;
loc_0092818C:
    local_rbx = (v_stack_p50) + (2);
    if ((*(uint16_t *)(local_rbx)) != 0) goto loc_00928162;
    goto loc_00928018;
loc_0092819B:
    if (0 != 0) goto loc_0092818C;
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)(result))) + 1);
    goto loc_0092818C;
loc_009281A5:
    if (0 != 0) goto loc_0092818C;
    if ((uint32_t)(local_r14) == 0) goto loc_009281D2;
    local_r14 = (uint32_t)((local_r14) + ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))) - 2)));
    goto loc_0092818C;
loc_009281B4:
    if (((uint32_t)(local_r14)) <= 1) goto loc_009281D2;
    result = 0;
    result = (0 == 0) ? 1 : 0;
    goto loc_0092818C;
loc_009281C7:
    if ((uint32_t)(local_r14) != 0) goto loc_0092818C;
    *(uint64_t *)(arg4) = local_rbx;
    goto loc_0092818C;
loc_009281D2:
    goto loc_0092818C;
loc_009281D9:
    *(uint64_t *)(v_stack_p60) = (uint32_t)(0x538ULL);
    *(void **)(arg4) = Arg1 + 34;
    goto loc_00928127;
loc_009281EA:
    Arg3 = 0;
loc_009281F1:
    local_rdi = (uint32_t)(((uint32_t)(0x538ULL)) + 1);
    local_rbx = (local_rbx) + (32);
    if (((uint32_t)(local_rdi)) < 9) goto loc_00928729;
loc_00928200:
loc_0092820A:
    local_rsi = 0;
loc_0092820C:
loc_00928211:
    result = *(uint64_t *)(v_stack_p60);
    if (*(uint64_t *)(v_stack_p60) != 0) {
        Arg2 = 0;
        Arg1 = *(uint64_t *)(v_stack_p60);
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, Arg4);
    }
    *(uint64_t *)(v_stack_p60) = 0;
    goto loc_0092811F;
loc_00928229:
    if (v_stack_p58 == 0) goto loc_00928127;
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_p58, Arg2, Arg3, Arg4);
    goto loc_00928127;
loc_00928246:
    local_r15 = ((uint32_t)((uint32_t)(result))) + (2);
loc_0092824A:
    if ((*(uint16_t *)(local_r15)) == 32) goto loc_00928BD4;
loc_00928255:
    if (((uint16_t)(*(uint16_t *)(local_r15))) == 59) goto loc_00928320;
    if (((uint16_t)(*(uint16_t *)(local_r15))) == 32) goto loc_00928BE4;
loc_0092826D:
    local_rsi = 0;
    if (((uint8_t)((uint32_t)(0x3ECULL))) == 17) { local_rsi = 4; }
loc_00928287:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x4E09E0 + 0x8))) & ((uint32_t)(local_rsi)));
    if (((uint32_t)(result)) != ((uint32_t)(local_rsi))) goto loc_009282A3;
    result = wcsnicmp(local_r15, *(uint64_t *)(v_rip + 0x4E09E0 - 0x8), (uint32_t)(*(uint32_t *)(v_rip + 0x4E09E0)), Arg4);
    if ((uint32_t)(result) == 0) goto loc_009282DD;
loc_009282A3:
    local_rdi = (uint32_t)((0) + 1);
    local_rbx = (v_rip + 5114336) + (24);
    if (((uint32_t)(local_rdi)) < 28) goto loc_00928287;
loc_009282AE:
    Arg3 = 0;
    result = wcstoul(local_r15, v_stack_mD0, Arg3, Arg4);
    if (v_stack_mD0 != local_r15) goto loc_00928891;
loc_009282CE:
    goto loc_0092820A;
loc_009282DD:
    if (((uint32_t)(local_rdi)) >= 28) goto loc_009282AE;
    if (v_rip - 9601775 + (uint32_t)((uint32_t)(local_rdi)) + (uint32_t)((uint32_t)(local_rdi)) * 2 * 8 + 14715984 == 0) goto loc_009282AE;
    Arg3 = (uint32_t)(((uint32_t)(v_stack_p54)) | (*(uint32_t *)(v_rip - 0x9282EF + (uint32_t)((uint32_t)(local_rdi)) + (uint32_t)((uint32_t)(local_rdi)) * 2 * 8 + 0xE08C50 + 0xC)));
    v_stack_p54 = (uint32_t)(Arg3);
    Arg3 = 0;
    goto loc_00928255;
loc_00928320:
    local_r15 = (local_r15 + (uint32_t)(*(uint32_t *)(v_rip - 0x9282EF + (uint32_t)((uint32_t)(local_rdi)) + (uint32_t)((uint32_t)(local_rdi)) * 2 * 8 + 0xE08C50 + 0x8)) * 2) + (2);
loc_0092832A:
    if (0 >= 2) goto loc_0092834F;
    if (((uint16_t)(*(uint16_t *)(local_r15))) == 32) goto loc_00928BF4;
loc_0092833D:
    if (((uint16_t)(*(uint16_t *)(local_r15))) != 59) goto loc_00928876;
    local_r15 = (local_r15) + (2);
    local_rbx = (uint32_t)((0) + 1);
    goto loc_0092832A;
loc_0092834F:
    if ((uint32_t)((uint32_t)(v_stack_mE0)) != 0) goto loc_00928106;
    if (((uint16_t)(*(uint16_t *)(local_r15))) == 32) goto loc_00928C08;
loc_0092836B:
    local_rsi = 0;
    local_rbx = 0;
    v_stack_mE0 = 0;
    v_stack_p50 = 0;
    if ((uint16_t)(*(uint16_t *)(local_r15)) == 0) goto loc_00928B2F;
    if ((*(uint16_t *)(local_r15 + 0x2)) == 0) goto loc_00928B2F;
    Arg3 = 0;
    v_stack_p78 = local_r15 + 4;
    Arg2 = 0;
    v_stack_p30 = v_stack_mE0;
    v_stack_p28 = 0;
    result = LookupSidInTable(local_r15, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_009288BF;
    v_stack_p58 = *(uint64_t *)(result + 0x10);
loc_009283C3:
    if (v_stack_p78 == 0) goto loc_00928F75;
    if (*(uint64_t *)(result + 0x10) == 0) goto loc_00928F75;
    if ((*(uint16_t *)(v_stack_p78)) == 32) goto loc_00928B50;
loc_009283E7:
    if (((uint8_t)((uint32_t)(0x538ULL))) > 21) goto loc_009283FB;
    if (((uint8_t)((uint32_t)(0x538ULL))) < 21) goto loc_0092892F;
loc_009283FB:
loc_00928404:
    if (((uint16_t)(*(uint16_t *)(v_stack_p78))) == 32) goto loc_00928C60;
loc_00928411:
    if (((uint16_t)(*(uint16_t *)(v_stack_p78))) != 41) goto loc_009282CE;
    local_rsi = (v_stack_p78) + (2);
    if (((uint32_t)((uint32_t)(0x538ULL))) != 3) goto loc_009287DA;
loc_00928430:
    result = RtlLengthSid(*(uint64_t *)(result + 0x10), (uint32_t)(v_stack_p70), *(uint64_t *)(result + 0x10), Arg4);
    local_rdi = (uint32_t)((12 - 4) + ((uint32_t)(result)));
    if (((uint32_t)(local_rdi)) >= 12) goto loc_00928455;
loc_00928441:
    goto loc_0092820A;
loc_00928455:
    result = (uint32_t)(((uint32_t)(v_stack_m100)) + ((uint32_t)(local_rdi)));
    v_stack_m100 = (uint32_t)(result);
    if (((uint32_t)(result)) < ((uint32_t)(local_rdi))) goto loc_00928441;
    if (((uint32_t)(result)) > ((uint32_t)((uint32_t)(v_stack_m108)))) goto loc_009288A0;
    if ((uint32_t)(v_stack_p60) != 0) goto loc_009287A5;
    result = RtlValidSid(v_stack_p58, (uint32_t)(v_stack_m108), *(uint64_t *)(result + 0x10), Arg4);
    if ((uint8_t)(result) == 0) goto loc_00928518;
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_stack_p60)))) > 4) goto loc_0092886C;
    local_r15 = *(uint8_t *)(*(uint64_t *)(v_stack_p60));
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_stack_p60)))) <= 2) {
        local_r15 = 2;
    }
    local_rdi = (uint32_t)((v_stack_p51) & (0xFFFFFFE0ULL));
    if (condition_is_not_equal) goto loc_00928AE3;
loc_009284B5:
    result = RtlValidAcl(*(uint64_t *)(v_stack_p60), (uint32_t)(v_stack_m108), *(uint64_t *)(result + 0x10), Arg4);
    if ((uint8_t)(result) == 0) goto loc_00928B60;
    Arg4 = 0;
loc_009284D4:
    if (0 < ((uint32_t)(*(uint16_t *)(*(uint64_t *)(v_stack_p60) + 0x4)))) goto loc_00928811;
    Arg3 = (*(uint16_t *)(*(uint64_t *)(v_stack_p60) + 0x2)) + (*(uint64_t *)(v_stack_p60));
    Arg2 = *(uint64_t *)(v_stack_p60) + 8;
    if ((*(uint64_t *)(v_stack_p60) + 8) > Arg3) { Arg2 = 0; }
    Arg1 = (uint16_t)((*(uint8_t *)(v_stack_p58 + 0x1)) + (4));
    Arg1 = (uint16_t)((Arg1) << (2));
    if (Arg2 == 0) goto loc_00928511;
    result = ((uint16_t)(Arg1)) + (Arg2);
    if (result <= Arg3) goto loc_0092882F;
loc_00928511:
    goto loc_00928522;
loc_00928518:
loc_0092851D:
loc_00928522:
    if (sign_flag) goto loc_009280F7;
    if (((uint8_t)(v_stack_p50)) != 1) goto loc_00928542;
    result = v_stack_p50;
    if (v_stack_p58 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_p58;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, Arg4);
    }
    Arg3 = 0;
    v_stack_p58 = 0;
    v_stack_mD8 = 0;
    result = 0;
    if (v_stack_m118 != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(v_stack_m118, Arg2, Arg3, Arg4);
        Arg3 = 0;
        v_stack_m118 = 0;
    }
    v_stack_p6C = 0;
    if (v_stack_mE8 != 0) goto loc_00928F3A;
loc_0092857A:
    v_stack_p70 = 0;
    if ((*(uint16_t *)(local_rsi)) == 40) {
        local_rsi = (local_rsi) + (2);
    }
    result = (uint32_t)(((uint32_t)(v_stack_m104)) + 1);
    goto loc_009285ED;
loc_00928593:
    local_rdi = (uint32_t)((v_stack_p58) * ((uint32_t)((uint32_t)(v_stack_m110))));
    local_rdi = (uint32_t)((local_rdi) + (8));
    if (((uint32_t)(local_rdi)) > ((uint32_t)((uint32_t)(0xFFFFULL)))) { local_rdi = (uint32_t)((uint32_t)(0xFFFFULL)); }
    v_stack_m108 = (uint32_t)(local_rdi);
    result = SddlpAlloc((uint32_t)((uint32_t)(local_rdi)), Arg2, Arg3, Arg4);
    *(uint64_t *)(v_stack_p60) = result;
    if (result == 0) goto loc_00928A51;
    *(uint8_t *)(result) = 2;
    Arg3 = 0;
    v_stack_m100 = 8;
    *(uint8_t *)(*(uint64_t *)(v_stack_p60) + 0x1) = 0;
    *(uint16_t *)(*(uint64_t *)(v_stack_p60) + 0x2) = (uint16_t)(local_rdi);
    *(uint16_t *)(*(uint64_t *)(v_stack_p60) + 0x4) = 0;
    *(uint16_t *)(*(uint64_t *)(v_stack_p60) + 0x6) = 0;
loc_009285ED:
    v_stack_m104 = 0;
    v_stack_mE0 = 534;
    if (0 >= ((uint32_t)((uint32_t)(v_stack_m110)))) goto loc_00928106;
    v_stack_p51 = 0;
    v_stack_p54 = 0;
    v_stack_mB8 = v_xmm0;
    v_stack_mF0 = 0;
    v_stack_mA8 = v_xmm1;
    v_stack_mF8 = 0;
    if (((uint16_t)(*(uint16_t *)(local_rsi))) == 32) goto loc_00928B96;
loc_00928630:
    if (((uint16_t)(*(uint16_t *)(local_rsi))) != 40) goto loc_00928644;
    local_rsi = (local_rsi) + (2);
    if ((*(uint16_t *)(local_rsi)) == 32) goto loc_00928BA9;
loc_00928644:
loc_0092864E:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x4E04C1 + 0x8))) & ((uint32_t)((uint32_t)(v_stack_p68))));
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(v_stack_p68)))) goto loc_00928673;
    if (local_rsi == 0) goto loc_0092868D;
    result = wcsnicmp(local_rsi, *(uint64_t *)(v_rip + 0x4E04C1 - 0x8), (uint32_t)(*(uint32_t *)(v_rip + 0x4E04C1)), Arg4);
    if ((uint32_t)(result) == 0) goto loc_00928693;
loc_00928673:
    local_rdi = (uint32_t)((0) + 1);
    local_rbx = (v_rip + 5113025) + (24);
    if (((uint32_t)(local_rdi)) < 17) goto loc_0092864E;
loc_0092867E:
    goto loc_0092820A;
loc_0092868D:
    if ((*(uint32_t *)(local_rbx + 0x4)) != 0) goto loc_00928673;
loc_00928693:
    if (((uint32_t)(local_rdi)) >= 17) goto loc_0092867E;
    if (v_rip - 9602721 + 14715568 + (uint32_t)((uint32_t)(local_rdi)) + (uint32_t)((uint32_t)(local_rdi)) * 2 * 8 == 0) goto loc_0092867E;
    v_stack_p52 = (uint8_t)(*(uint8_t *)(v_rip - 0x9286A1 + 0xE08AB0 + (uint32_t)((uint32_t)(local_rdi)) + (uint32_t)((uint32_t)(local_rdi)) * 2 * 8 + 0xC));
    if (((uint16_t)(*(uint16_t *)(local_rsi + (uint32_t)(*(uint32_t *)(v_rip - 0x9286A1 + 0xE08AB0 + (uint32_t)((uint32_t)(local_rdi)) + (uint32_t)((uint32_t)(local_rdi)) * 2 * 8 + 0x8)) * 2))) != 59) goto loc_00928796;
loc_009286D3:
    local_r15 = (local_rsi + (uint32_t)(*(uint32_t *)(v_rip - 0x9286A1 + 0xE08AB0 + (uint32_t)((uint32_t)(local_rdi)) + (uint32_t)((uint32_t)(local_rdi)) * 2 * 8 + 0x8)) * 2) + (2);
    if (((uint8_t)(*(uint8_t *)(v_rip - 0x9286A1 + 0xE08AB0 + (uint32_t)((uint32_t)(local_rdi)) + (uint32_t)((uint32_t)(local_rdi)) * 2 * 8 + 0xC) - 5)) <= 3) goto loc_00928BB8;
    if (((uint8_t)(*(uint8_t *)(v_rip - 0x9286A1 + 0xE08AB0 + (uint32_t)((uint32_t)(local_rdi)) + (uint32_t)((uint32_t)(local_rdi)) * 2 * 8 + 0xC))) == 11) goto loc_00928BB8;
loc_009286EC:
    if ((*(uint16_t *)(local_r15)) == 32) goto loc_00928BC4;
loc_009286F7:
loc_009286FA:
    Arg3 = 0;
    if (local_r15 == (*(uint64_t *)(arg4))) goto loc_0092824A;
    if (((uint16_t)(*(uint16_t *)(local_r15))) == 59) goto loc_00928246;
    if (((uint16_t)(*(uint16_t *)(local_r15))) == 32) goto loc_00928A40;
loc_0092871F:
loc_00928729:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x4E027B - 0x4))) & ((uint32_t)((uint32_t)(v_stack_p68))));
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(v_stack_p68)))) goto loc_009281F1;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4E027B))) != 0) goto loc_00928910;
loc_00928740:
    result = wcsnicmp(local_r15, *(uint64_t *)(v_rip + 0x4E027B - 0x14), (uint32_t)(*(uint32_t *)(v_rip + 0x4E027B - 0xC)), v_rip - 9602721);
    if ((uint32_t)(result) != 0) goto loc_009281EA;
    if (0 >= 9) goto loc_00928200;
    result = (0) << (5);
    result = (result) + (v_rip + 5112358);
    if (condition_is_equal) goto loc_00928200;
    Arg3 = (uint8_t)((v_stack_p51) | (*(uint8_t *)(result + 0xC)));
    v_stack_p51 = (uint8_t)(Arg3);
    goto loc_009286FA;
loc_00928796:
    if (((uint16_t)((uint32_t)(*(uint32_t *)(result + 0x8)))) == 32) goto loc_009286D3;
    goto loc_009282CE;
loc_009287A5:
    if (((uint32_t)(v_stack_p60)) != 17) goto loc_00928961;
    v_stack_p28 = (uint32_t)((uint32_t)(v_stack_p54));
    result = SddlAddMandatoryAce(*(uint64_t *)(v_stack_p60), (uint32_t)(v_stack_p68), v_stack_p51, v_stack_p58);
    goto loc_00928522;
loc_009287DA:
    if (((uint32_t)(v_stack_p60)) > 21) goto loc_00928F4D;
    Arg1 = ((uint32_t)(*(uint32_t *)(v_rip - 0x9287EB + v_stack_p58 * 4 + 0x4336C))) + (v_rip - 9603051);
loc_00928811:
    result = (*(uint16_t *)((uint32_t)((uint32_t)(result)) + 0x2)) + ((uint32_t)((uint32_t)(result)));
    if (((uint32_t)(v_stack_p68)) >= result) goto loc_00928B60;
    Arg1 = (uint32_t)((Arg1) + 1);
    Arg2 = ((uint32_t)(v_stack_p68)) + (*(uint16_t *)((uint32_t)(v_stack_p68) + 0x2));
    goto loc_009284D4;
loc_0092882F:
    *(uint8_t *)(Arg2 + 0x1) = (uint8_t)(v_stack_p51);
    *(uint16_t *)(Arg2 + 0x2) = (uint16_t)(Arg1);
    *(uint32_t *)(Arg2 + 0x4) = (uint32_t)((uint32_t)(v_stack_p54));
    *(uint8_t *)(Arg2) = (uint8_t)(v_rip - 9603051);
    Arg2 = (Arg2) + (8);
    result = RtlCopySid(*(uint8_t *)(v_stack_p58 + 0x1) * 4 + 8, Arg2, v_stack_p58, v_rip - 9603051);
    result = 0;
    *(uint8_t *)((uint32_t)((uint32_t)(result))) = (uint8_t)(local_r15 + (uint32_t)(*(uint32_t *)(result + 0x8)) * 2);
    goto loc_00928522;
loc_0092886C:
    goto loc_0092851D;
loc_00928876:
    if (((uint8_t)(v_stack_p58)) != 11) goto loc_009282CE;
loc_00928891:
    Arg3 = 0;
    goto loc_00928255;
loc_009288A0:
    Arg1 = (uint32_t)(((uint32_t)(v_stack_m110)) - (v_stack_m104));
    Arg1 = (Arg1) * ((uint32_t)((uint32_t)(v_stack_p58)));
    if (Arg1 > ((uint32_t)(0xFFFFFFFFULL))) goto loc_00928441;
loc_009288BF:
    v_stack_p58 = v_stack_mE0;
    if (v_stack_mE0 != 0) goto loc_009288FA;
    result = LocalpConvertStringSidToSid(*(uint8_t *)(v_rip - 0x9286A1 + 0xE08AB0 + (uint32_t)((uint32_t)(local_rdi)) + (uint32_t)((uint32_t)(local_rdi)) * 2 * 8 + 0xC) - 5, v_stack_mD8, v_stack_p78, v_rip - 9603051);
    if (sign_flag) goto loc_00928B6A;
loc_009288EC:
    v_stack_p58 = v_stack_mD8;
    local_rbx = (uint32_t)(0xC0000059ULL);
    if (v_stack_mD8 != 0) {
        local_rbx = 1;
    }
    v_stack_p50 = (uint8_t)(local_rbx);
    if ((uint32_t)(*(uint8_t *)(v_rip - 0x9286A1 + 0xE08AB0 + (uint32_t)((uint32_t)(local_rdi)) + (uint32_t)((uint32_t)(local_rdi)) * 2 * 8 + 0xC)) == 0) goto loc_009283C3;
    goto loc_00928106;
loc_00928910:
    if (((uint32_t)(v_stack_mD8)) >= ((uint32_t)(v_stack_mD8))) goto loc_009281EA;
    if ((*(uint8_t *)((uint32_t)((uint32_t)(v_stack_mD8)) + *(uint64_t *)(local_rbx + 0x4) * 1)) == ((uint8_t)(*(uint8_t *)(v_rip - 0x9286A1 + 0xE08AB0 + (uint32_t)((uint32_t)(local_rdi)) + (uint32_t)((uint32_t)(local_rdi)) * 2 * 8 + 0xC)))) goto loc_00928740;
    Arg3 = (uint32_t)((v_stack_mD8) + 1);
    goto loc_00928910;
loc_0092892F:
    if ((*(uint16_t *)(local_rbx)) == 59) goto loc_00928A5C;
loc_00928939:
    if ((uint32_t)((uint32_t)(v_stack_p6C)) != 0) goto loc_0092894F;
    if ((uint32_t)((uint32_t)(v_stack_p70)) == 0) goto loc_009282CE;
loc_0092894F:
    if ((uint32_t)(*(uint8_t *)(v_rip - 0x9286A1 + 0xE08AB0 + (uint32_t)((uint32_t)(local_rdi)) + (uint32_t)((uint32_t)(local_rdi)) * 2 * 8 + 0xC)) == 0) goto loc_00928404;
    goto loc_0092820A;
loc_00928961:
    if (((uint32_t)(v_stack_p60 - 1)) > 20) goto loc_00928F6B;
    Arg1 = ((uint32_t)(*(uint32_t *)(v_rip - 0x928975 + v_stack_p60 - 0x1 * 4 + 0x433C4))) + (v_rip - 9603445);
loc_00928A40:
    local_r15 = ((uint32_t)(v_stack_p6C)) + (2);
    if ((*(uint16_t *)(local_r15)) != 32) goto loc_0092871F;
    goto loc_00928A40;
loc_00928A51:
    goto loc_00928127;
loc_00928A5C:
    local_rbx = (local_rbx) + (2);
    if (((uint16_t)(*(uint16_t *)(local_rbx + 0x2))) == 32) goto loc_00928C1C;
loc_00928A6E:
    if (((uint16_t)(*(uint16_t *)(local_rbx + 0x2))) != 40) goto loc_00928B3E;
    if (v_stack_m118 != 0) goto loc_00928C2F;
    local_rsi = 0;
loc_00928A87:
    v_stack_p6C = 0;
    if (v_stack_mE8 != 0) goto loc_00928C41;
loc_00928A98:
    v_stack_p70 = 0;
    if (((uint8_t)(v_stack_p58)) == 18) goto loc_00928AF9;
    v_stack_p40 = 0;
    v_stack_p38 = 0;
    v_stack_p30 = 0;
    v_stack_p28 = 0;
    v_stack_p20 = 0;
    result = LocalGetConditionForString(local_rbx, v_stack_p78, v_stack_m118, v_stack_p6C);
    goto loc_00928939;
loc_00928AE3:
    if ((((uint32_t)(v_stack_p58)) & (0xFFFFFFDFULL)) == 0) goto loc_009284B5;
    goto loc_0092851D;
loc_00928AF9:
    v_stack_p38 = 0;
    v_stack_p30 = v_stack_p78;
    v_stack_p28 = v_stack_p78;
    v_stack_p20 = v_stack_p78;
    result = LocalGetRelativeAttributeForString(local_rbx, v_stack_p78, v_stack_mE8, v_stack_p70);
    if ((uint32_t)(result) == 0) goto loc_00928C51;
    goto loc_0092820C;
loc_00928B2F:
    goto loc_00928211;
loc_00928B3E:
    v_stack_p78 = (uint32_t)(0xC000000DULL);
    goto loc_00928939;
loc_00928B50:
    local_rbx = ((uint32_t)(0xC000000DULL)) + (2);
    if ((*(uint16_t *)(local_rbx)) != 32) goto loc_009283E7;
    goto loc_00928B50;
loc_00928B60:
    goto loc_0092851D;
loc_00928B6A:
    result = RtlNtStatusToDosError((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_p60))), v_stack_p78, v_stack_mE8, v_stack_p70);
    if ((uint32_t)(result) == 0) goto loc_009288EC;
    v_stack_p58 = v_stack_mD8;
    goto loc_009288FC;
loc_00928B8A:
loc_00928B8F:
    goto loc_009280A3;
loc_00928B96:
    local_rsi = ((uint32_t)(0xC000000DULL)) + (2);
    if (((uint16_t)(*(uint16_t *)((uint32_t)(0xC000000DULL) + 0x2))) == 32) goto loc_00928B96;
    goto loc_00928630;
loc_00928BA9:
    local_rsi = (local_rsi) + (2);
    if ((*(uint16_t *)(local_rsi)) == 32) goto loc_00928BA9;
    goto loc_00928644;
loc_00928BB8:
    *(uint8_t *)(*(uint64_t *)(v_stack_p60)) = 4;
    goto loc_009286EC;
loc_00928BC4:
    local_r15 = (local_r15) + (2);
    if ((*(uint16_t *)(local_r15)) == 32) goto loc_00928BC4;
    goto loc_009286F7;
loc_00928BD4:
    local_r15 = (local_r15) + (2);
    if ((*(uint16_t *)(local_r15)) == 32) goto loc_00928BD4;
    goto loc_00928255;
loc_00928BE4:
    local_r15 = (local_r15) + (2);
    if ((*(uint16_t *)(local_r15)) == 32) goto loc_00928BE4;
    goto loc_0092826D;
loc_00928BF4:
    local_r15 = (local_r15) + (2);
    if (((uint16_t)(*(uint16_t *)(local_r15 + 0x2))) == 32) goto loc_00928BF4;
    goto loc_0092833D;
loc_00928C08:
    local_r15 = (local_r15) + (2);
    if (((uint16_t)(*(uint16_t *)(local_r15 + 0x2))) == 32) goto loc_00928C08;
    goto loc_0092836B;
loc_00928C1C:
    local_rbx = ((uint32_t)(0xC0000077ULL)) + (2);
    if (((uint16_t)(*(uint16_t *)((uint32_t)(0xC0000077ULL) + 0x2))) == 32) goto loc_00928C1C;
    goto loc_00928A6E;
loc_00928C2F:
    Arg2 = 0;
    result = ExFreePoolWithTag((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_p60))), Arg2, v_stack_mD8, v_stack_p70);
    local_rsi = 0;
    v_stack_m118 = 0;
    goto loc_00928A87;
loc_00928C41:
    Arg2 = 0;
    result = ExFreePoolWithTag((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_p60))), Arg2, v_stack_mD8, v_stack_p70);
    v_stack_mE8 = 0;
    goto loc_00928A98;
loc_00928C51:
    goto loc_00928939;
loc_00928C60:
    local_rsi = (v_stack_p78) + (2);
    v_stack_p78 = local_rsi;
    if (((uint16_t)(*(uint16_t *)(local_rsi))) == 32) goto loc_00928C60;
    goto loc_00928411;
loc_00928F3A:
    Arg2 = 0;
    result = ExFreePoolWithTag((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_p60))), Arg2, v_stack_p58, v_stack_p70);
    Arg3 = 0;
    v_stack_mE8 = 0;
    goto loc_0092857A;
loc_00928F4D:
    goto loc_0092820A;
loc_00928F6B:
    goto loc_009280F7;
loc_00928F75:
    local_rsi = 0;
    goto loc_00928211;
loc_00928F86:
    Arg2 = 0;
    result = ExFreePoolWithTag((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_p60))), Arg2, Arg3, v_stack_p70);
    goto loc_00928134;
loc_00928F92:
    goto loc_009280A3;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `16` | `R` |
| `Arg1` | `+ 0x0 + rax*2` | `64` | `R` |
| `Arg1` | `+ 0x2 + rax*2` | `16` | `R` |
| `Arg1` | `+ 0x22` | `64` | `R` |
| `Arg3` | `+ 0x0` | `64` | `R` |
| `Arg3` | `+ 0x0` | `64` | `W` |
| `Arg4` | `+ 0x0` | `64` | `R` |
| `Arg4` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00927F30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
