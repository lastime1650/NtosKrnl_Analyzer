# EtwpApplyPayloadFilterInternal

- RVA: `0x003F43D0`–`0x003F4C9C` (길이 `2,252` bytes)
- VA: `0x00000001403F43D0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00097200`
- 디코드: `597`개 명령, `2,252/2,252` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **11**; 고유 호출 대상: **8**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x003F44F9` → [RtlpGetStackLimits](../2F/RtlpGetStackLimits_function_002F5F50.md) (function, `0x002F5F50`)
- `0x003F4542` → [_chkstk](../6B/_chkstk_function_006BA960.md) (function, `0x006BA960`)
- `0x003F4571` → [_chkstk](../6B/_chkstk_function_006BA960.md) (function, `0x006BA960`)
- `0x003F45B7` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x003F4616` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x003F4865` → [EtwpApplyPredicate](EtwpApplyPredicate_function_003F4CB0.md) (function, `0x003F4CB0`)
- `0x003F48DA` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x003F4AFA` → [EtwpGetFieldValue](EtwpGetFieldValue_function_003F4D70.md) (function, `0x003F4D70`)
- `0x003F4BB9` → [EtwpGetFieldValue](EtwpGetFieldValue_function_003F4D70.md) (function, `0x003F4D70`)
- `0x003F4C06` → [EtwpGetFieldValue](EtwpGetFieldValue_function_003F4D70.md) (function, `0x003F4D70`)
- `0x003F4C12` → [RtlLengthRequiredSid](../../page/9C/RtlLengthRequiredSid_function_009CA4D0.md) (function, `0x009CA4D0`)

### Direct callers
- [sub_003F434B](Unknown_function_003F434B.md) at `0x003F4384`

### Static image references
- `0x003F43FB` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x003F4616` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (`.text` → `PAGE`)
  - `0x003F4C12` → [RtlLengthRequiredSid](../../page/9C/RtlLengthRequiredSid_function_009CA4D0.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003F43D0  40 55                           push rbp
003F43D2  41 54                           push r12
003F43D4  41 55                           push r13
003F43D6  41 56                           push r14
003F43D8  41 57                           push r15
003F43DA  48 81 EC B0 00 00 00            sub rsp, 0xb0
003F43E1  48 8D 6C 24 30                  lea rbp, [rsp + 0x30]
003F43E6  48 89 9D B0 00 00 00            mov qword ptr [rbp + 0xb0], rbx
003F43ED  48 89 B5 B8 00 00 00            mov qword ptr [rbp + 0xb8], rsi
003F43F4  48 89 BD C0 00 00 00            mov qword ptr [rbp + 0xc0], rdi
003F43FB  48 8B 05 3E 63 A1 00            mov rax, qword ptr [rip + 0xa1633e]
003F4402  48 33 C5                        xor rax, rbp
003F4405  48 89 45 78                     mov qword ptr [rbp + 0x78], rax
003F4409  45 0F B6 F1                     movzx r14d, r9b
003F440D  4D 8B F8                        mov r15, r8
003F4410  8B DA                           mov ebx, edx
003F4412  33 FF                           xor edi, edi
003F4414  48 89 7D 28                     mov qword ptr [rbp + 0x28], rdi
003F4418  40 88 7D 02                     mov byte ptr [rbp + 2], dil
003F441C  C7 45 04 0D 00 00 C0            mov dword ptr [rbp + 4], 0xc000000d
003F4423  81 FA 80 00 00 00               cmp edx, 0x80
003F4429  0F 87 26 08 00 00               ja 0x1403f4c55
003F442F  44 0F B7 09                     movzx r9d, word ptr [rcx]
003F4433  66 44 89 4D 50                  mov word ptr [rbp + 0x50], r9w
003F4438  44 0F B6 51 02                  movzx r10d, byte ptr [rcx + 2]
003F443D  44 88 55 20                     mov byte ptr [rbp + 0x20], r10b
003F4441  EB 0A                           jmp 0x1403f444d
003F4443  B8 0D 00 00 C0                  mov eax, 0xc000000d
003F4448  E9 86 04 00 00                  jmp 0x1403f48d3
003F444D  41 8B C9                        mov ecx, r9d
003F4450  B8 05 41 10 04                  mov eax, 0x4104105
003F4455  41 F7 E1                        mul r9d
003F4458  41 8B C1                        mov eax, r9d
003F445B  2B C2                           sub eax, edx
003F445D  D1 E8                           shr eax, 1
003F445F  03 C2                           add eax, edx
003F4461  C1 E8 05                        shr eax, 5
003F4464  6B C0 3F                        imul eax, eax, 0x3f
003F4467  2B C8                           sub ecx, eax
003F4469  0F B6 C9                        movzx ecx, cl
003F446C  4C 8B A5 D8 00 00 00            mov r12, qword ptr [rbp + 0xd8]
003F4473  49 8B 44 24 08                  mov rax, qword ptr [r12 + 8]
003F4478  48 0F A3 C8                     bt rax, rcx
003F447C  0F 83 9A 04 00 00               jae 0x1403f491c
003F4482  89 7D 08                        mov dword ptr [rbp + 8], edi
003F4485  45 0F B7 5C 24 20               movzx r11d, word ptr [r12 + 0x20]
003F448B  4D 03 DC                        add r11, r12
003F448E  44 8B C7                        mov r8d, edi
003F4491  41 0F B7 4C 24 22               movzx ecx, word ptr [r12 + 0x22]
003F4497  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
003F44A1  48 F7 E1                        mul rcx
003F44A4  48 C1 EA 03                     shr rdx, 3
003F44A8  4C 89 5D 48                     mov qword ptr [rbp + 0x48], r11
003F44AC  44 3B C2                        cmp r8d, edx
003F44AF  73 17                           jae 0x1403f44c8
003F44B1  66 45 39 0B                     cmp word ptr [r11], r9w
003F44B5  0F 85 77 04 00 00               jne 0x1403f4932
003F44BB  45 38 53 02                     cmp byte ptr [r11 + 2], r10b
003F44BF  0F 85 6D 04 00 00               jne 0x1403f4932
003F44C5  44 3B C2                        cmp r8d, edx
003F44C8  0F 84 4E 04 00 00               je 0x1403f491c
003F44CE  4C 8B EF                        mov r13, rdi
003F44D1  8B FB                           mov edi, ebx
003F44D3  C1 E7 04                        shl edi, 4
003F44D6  41 0F B6 43 03                  movzx eax, byte ptr [r11 + 3]
003F44DB  FF C0                           inc eax
003F44DD  89 45 54                        mov dword ptr [rbp + 0x54], eax
003F44E0  8D 34 85 00 00 00 00            lea esi, [rax*4]
003F44E7  33 C0                           xor eax, eax
003F44E9  48 89 45 60                     mov qword ptr [rbp + 0x60], rax
003F44ED  48 89 45 18                     mov qword ptr [rbp + 0x18], rax
003F44F1  48 8D 55 60                     lea rdx, [rbp + 0x60]
003F44F5  48 8D 4D 18                     lea rcx, [rbp + 0x18]
003F44F9  E8 52 1A F0 FF                  call 0x1402f5f50
003F44FE  48 8B 55 18                     mov rdx, qword ptr [rbp + 0x18]
003F4502  84 C0                           test al, al
003F4504  4D 8B CD                        mov r9, r13
003F4507  49 0F 44 D5                     cmove rdx, r13
003F450B  8D 8F 00 10 00 00               lea ecx, [rdi + 0x1000]
003F4511  03 CE                           add ecx, esi
003F4513  48 8D 45 60                     lea rax, [rbp + 0x60]
003F4517  48 2B C2                        sub rax, rdx
003F451A  48 3B C1                        cmp rax, rcx
003F451D  0F 82 5B 04 00 00               jb 0x1403f497e
003F4523  8B C6                           mov eax, esi
003F4525  48 8D 4E 0F                     lea rcx, [rsi + 0xf]
003F4529  48 BA F0 FF FF FF FF FF FF 0F   movabs rdx, 0xffffffffffffff0
003F4533  48 3B C8                        cmp rcx, rax
003F4536  77 03                           ja 0x1403f453b
003F4538  48 8B CA                        mov rcx, rdx
003F453B  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
003F453F  48 8B C1                        mov rax, rcx
003F4542  E8 19 64 2C 00                  call 0x1406ba960
003F4547  48 2B E1                        sub rsp, rcx
003F454A  4C 8D 4C 24 30                  lea r9, [rsp + 0x30]
003F454F  4C 89 4D 10                     mov qword ptr [rbp + 0x10], r9
003F4553  45 84 F6                        test r14b, r14b
003F4556  0F 84 CE 03 00 00               je 0x1403f492a
003F455C  8B C7                           mov eax, edi
003F455E  48 8D 4F 0F                     lea rcx, [rdi + 0xf]
003F4562  48 3B C8                        cmp rcx, rax
003F4565  77 03                           ja 0x1403f456a
003F4567  48 8B CA                        mov rcx, rdx
003F456A  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
003F456E  48 8B C1                        mov rax, rcx
003F4571  E8 EA 63 2C 00                  call 0x1406ba960
003F4576  48 2B E1                        sub rsp, rcx
003F4579  4C 8D 6C 24 30                  lea r13, [rsp + 0x30]
003F457E  45 84 F6                        test r14b, r14b
003F4581  0F 84 A3 03 00 00               je 0x1403f492a
003F4587  85 FF                           test edi, edi
003F4589  74 7F                           je 0x1403f460a
003F458B  41 F6 C7 03                     test r15b, 3
003F458F  0F 85 81 00 00 00               jne 0x1403f4616
003F4595  8B CF                           mov ecx, edi
003F4597  49 03 CF                        add rcx, r15
003F459A  48 BE 00 00 FF FF FF 7F 00 00   movabs rsi, 0x7fffffff0000
003F45A4  48 3B CE                        cmp rcx, rsi
003F45A7  77 72                           ja 0x1403f461b
003F45A9  49 3B CF                        cmp rcx, r15
003F45AC  72 6D                           jb 0x1403f461b
003F45AE  44 8B C7                        mov r8d, edi
003F45B1  49 8B D7                        mov rdx, r15
003F45B4  49 8B CD                        mov rcx, r13
003F45B7  E8 84 22 2D 00                  call 0x1406c6840
003F45BC  33 D2                           xor edx, edx
003F45BE  8B CA                           mov ecx, edx
003F45C0  89 55 38                        mov dword ptr [rbp + 0x38], edx
003F45C3  8B C2                           mov eax, edx
003F45C5  44 8B C2                        mov r8d, edx
003F45C8  3B C3                           cmp eax, ebx
003F45CA  73 54                           jae 0x1403f4620
003F45CC  8B D2                           mov edx, edx
003F45CE  41 8B C0                        mov eax, r8d
003F45D1  48 03 C0                        add rax, rax
003F45D4  45 8B 4C C5 08                  mov r9d, dword ptr [r13 + rax*8 + 8]
003F45D9  45 85 C9                        test r9d, r9d
003F45DC  74 16                           je 0x1403f45f4
003F45DE  48 03 D2                        add rdx, rdx
003F45E1  4D 8B 44 D5 00                  mov r8, qword ptr [r13 + rdx*8]
003F45E6  4B 8D 14 08                     lea rdx, [r8 + r9]
003F45EA  49 3B D0                        cmp rdx, r8
003F45ED  72 13                           jb 0x1403f4602
003F45EF  48 3B D6                        cmp rdx, rsi
003F45F2  77 0E                           ja 0x1403f4602
003F45F4  FF C1                           inc ecx
003F45F6  8B D1                           mov edx, ecx
003F45F8  8B C1                           mov eax, ecx
003F45FA  89 4D 38                        mov dword ptr [rbp + 0x38], ecx
003F45FD  44 8B C1                        mov r8d, ecx
003F4600  EB C6                           jmp 0x1403f45c8
003F4602  0F B6 06                        movzx eax, byte ptr [rsi]
003F4605  8B 4D 38                        mov ecx, dword ptr [rbp + 0x38]
003F4608  EB EA                           jmp 0x1403f45f4
003F460A  48 BE 00 00 FF FF FF 7F 00 00   movabs rsi, 0x7fffffff0000
003F4614  EB 98                           jmp 0x1403f45ae
003F4616  E8 B5 59 4A 00                  call 0x140899fd0
003F461B  0F B6 06                        movzx eax, byte ptr [rsi]
003F461E  EB 8E                           jmp 0x1403f45ae
003F4620  4C 8B 4D 10                     mov r9, qword ptr [rbp + 0x10]
003F4624  EB 08                           jmp 0x1403f462e
003F4626  8B 45 04                        mov eax, dword ptr [rbp + 4]
003F4629  E9 A5 02 00 00                  jmp 0x1403f48d3
003F462E  45 0F B7 5C 24 24               movzx r11d, word ptr [r12 + 0x24]
003F4634  4D 03 DC                        add r11, r12
003F4637  4C 89 5D 30                     mov qword ptr [rbp + 0x30], r11
003F463B  33 F6                           xor esi, esi
003F463D  44 8B C6                        mov r8d, esi
003F4640  89 75 04                        mov dword ptr [rbp + 4], esi
003F4643  8B FE                           mov edi, esi
003F4645  4D 8B FD                        mov r15, r13
003F4648  48 8B 45 48                     mov rax, qword ptr [rbp + 0x48]
003F464C  0F B7 40 04                     movzx eax, word ptr [rax + 4]
003F4650  4D 8D 34 83                     lea r14, [r11 + rax*4]
003F4654  4D 8B D1                        mov r10, r9
003F4657  4C 89 4D 40                     mov qword ptr [rbp + 0x40], r9
003F465B  8B C6                           mov eax, esi
003F465D  89 45 0C                        mov dword ptr [rbp + 0xc], eax
003F4660  3B 45 54                        cmp eax, dword ptr [rbp + 0x54]
003F4663  0F 83 37 01 00 00               jae 0x1403f47a0
003F4669  44 3B C3                        cmp r8d, ebx
003F466C  0F 84 94 02 00 00               je 0x1403f4906
003F4672  41 0F B6 0E                     movzx ecx, byte ptr [r14]
003F4676  0F B6 C1                        movzx eax, cl
003F4679  24 0F                           and al, 0xf
003F467B  41 0F B7 56 02                  movzx edx, word ptr [r14 + 2]
003F4680  3C 07                           cmp al, 7
003F4682  0F 84 C6 02 00 00               je 0x1403f494e
003F4688  8B F2                           mov esi, edx
003F468A  3C 08                           cmp al, 8
003F468C  0F 84 9E 04 00 00               je 0x1403f4b30
003F4692  F6 C1 10                        test cl, 0x10
003F4695  0F 85 AE 04 00 00               jne 0x1403f4b49
003F469B  41 0F B6 4E 01                  movzx ecx, byte ptr [r14 + 1]
003F46A0  48 89 4D 18                     mov qword ptr [rbp + 0x18], rcx
003F46A4  41 F6 06 20                     test byte ptr [r14], 0x20
003F46A8  0F 85 DC 03 00 00               jne 0x1403f4a8a
003F46AE  45 33 D2                        xor r10d, r10d
003F46B1  45 8B CA                        mov r9d, r10d
003F46B4  85 F6                           test esi, esi
003F46B6  0F 84 51 02 00 00               je 0x1403f490d
003F46BC  0F AF F1                        imul esi, ecx
003F46BF  41 8B 47 08                     mov eax, dword ptr [r15 + 8]
003F46C3  2B C7                           sub eax, edi
003F46C5  3B C6                           cmp eax, esi
003F46C7  0F 82 39 02 00 00               jb 0x1403f4906
003F46CD  44 8B 45 04                     mov r8d, dword ptr [rbp + 4]
003F46D1  48 8B 45 40                     mov rax, qword ptr [rbp + 0x40]
003F46D5  44 88 40 03                     mov byte ptr [rax + 3], r8b
003F46D9  8B 00                           mov eax, dword ptr [rax]
003F46DB  8B CF                           mov ecx, edi
003F46DD  C1 E1 0C                        shl ecx, 0xc
003F46E0  33 C8                           xor ecx, eax
003F46E2  81 E1 00 F0 FF 00               and ecx, 0xfff000
003F46E8  33 C8                           xor ecx, eax
003F46EA  8B D1                           mov edx, ecx
003F46EC  33 D6                           xor edx, esi
003F46EE  81 E2 FF 0F 00 00               and edx, 0xfff
003F46F4  33 D1                           xor edx, ecx
003F46F6  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
003F46FA  89 11                           mov dword ptr [rcx], edx
003F46FC  8B C2                           mov eax, edx
003F46FE  C1 E8 18                        shr eax, 0x18
003F4701  41 3B C0                        cmp eax, r8d
003F4704  0F 85 FC 01 00 00               jne 0x1403f4906
003F470A  8B C2                           mov eax, edx
003F470C  C1 E8 0C                        shr eax, 0xc
003F470F  25 FF 0F 00 00                  and eax, 0xfff
003F4714  3B C7                           cmp eax, edi
003F4716  0F 85 EA 01 00 00               jne 0x1403f4906
003F471C  81 E2 FF 0F 00 00               and edx, 0xfff
003F4722  3B D6                           cmp edx, esi
003F4724  0F 85 DC 01 00 00               jne 0x1403f4906
003F472A  41 8D 04 31                     lea eax, [r9 + rsi]
003F472E  03 F8                           add edi, eax
003F4730  41 3B 7F 08                     cmp edi, dword ptr [r15 + 8]
003F4734  0F 87 58 05 00 00               ja 0x1403f4c92
003F473A  0F 85 4B 05 00 00               jne 0x1403f4c8b
003F4740  41 FF C0                        inc r8d
003F4743  44 89 45 04                     mov dword ptr [rbp + 4], r8d
003F4747  33 F6                           xor esi, esi
003F4749  44 3B C3                        cmp r8d, ebx
003F474C  73 31                           jae 0x1403f477f
003F474E  8B FE                           mov edi, esi
003F4750  49 83 C7 10                     add r15, 0x10
003F4754  48 8B C3                        mov rax, rbx
003F4757  48 C1 E0 04                     shl rax, 4
003F475B  49 03 C5                        add rax, r13
003F475E  4C 3B F8                        cmp r15, rax
003F4761  0F 83 2B 05 00 00               jae 0x1403f4c92
003F4767  8B 55 08                        mov edx, dword ptr [rbp + 8]
003F476A  85 D2                           test edx, edx
003F476C  0F 85 AD 03 00 00               jne 0x1403f4b1f
003F4772  89 75 08                        mov dword ptr [rbp + 8], esi
003F4775  41 3B 7F 08                     cmp edi, dword ptr [r15 + 8]
003F4779  0F 84 E0 04 00 00               je 0x1403f4c5f
003F477F  4C 8B 4D 10                     mov r9, qword ptr [rbp + 0x10]
003F4783  4C 8B 5D 30                     mov r11, qword ptr [rbp + 0x30]
003F4787  8B 45 0C                        mov eax, dword ptr [rbp + 0xc]
003F478A  FF C0                           inc eax
003F478C  49 83 C6 04                     add r14, 4
003F4790  48 83 C1 04                     add rcx, 4
003F4794  48 89 4D 40                     mov qword ptr [rbp + 0x40], rcx
003F4798  4C 8B D1                        mov r10, rcx
003F479B  E9 BD FE FF FF                  jmp 0x1403f465d
003F47A0  83 7D 08 00                     cmp dword ptr [rbp + 8], 0
003F47A4  0F 85 5C 01 00 00               jne 0x1403f4906
003F47AA  48 8B 5D 48                     mov rbx, qword ptr [rbp + 0x48]
003F47AE  0F B7 43 04                     movzx eax, word ptr [rbx + 4]
003F47B2  4D 8D 04 83                     lea r8, [r11 + rax*4]
003F47B6  4C 89 45 18                     mov qword ptr [rbp + 0x18], r8
003F47BA  0F B7 53 08                     movzx edx, word ptr [rbx + 8]
003F47BE  41 0F B7 4C 24 28               movzx ecx, word ptr [r12 + 0x28]
003F47C4  49 03 CC                        add rcx, r12
003F47C7  4C 8D 3C 91                     lea r15, [rcx + rdx*4]
003F47CB  C6 45 01 00                     mov byte ptr [rbp + 1], 0
003F47CF  45 32 DB                        xor r11b, r11b
003F47D2  44 88 5D 00                     mov byte ptr [rbp], r11b
003F47D6  C6 45 03 01                     mov byte ptr [rbp + 3], 1
003F47DA  44 8B D6                        mov r10d, esi
003F47DD  44 89 55 04                     mov dword ptr [rbp + 4], r10d
003F47E1  0F B7 43 0A                     movzx eax, word ptr [rbx + 0xa]
003F47E5  44 3B D0                        cmp r10d, eax
003F47E8  0F 83 D5 00 00 00               jae 0x1403f48c3
003F47EE  41 0F B7 47 02                  movzx eax, word ptr [r15 + 2]
003F47F3  48 8D 0C 40                     lea rcx, [rax + rax*2]
003F47F7  49 8D 7C 24 38                  lea rdi, [r12 + 0x38]
003F47FC  48 8D 3C CF                     lea rdi, [rdi + rcx*8]
003F4800  40 B6 01                        mov sil, 1
003F4803  45 32 F6                        xor r14b, r14b
003F4806  33 C0                           xor eax, eax
003F4808  8B D8                           mov ebx, eax
003F480A  66 0F 1F 44 00 00               nop word ptr [rax + rax]
003F4810  41 0F B7 0F                     movzx ecx, word ptr [r15]
003F4814  8B C1                           mov eax, ecx
003F4816  C1 E8 02                        shr eax, 2
003F4819  83 E0 3F                        and eax, 0x3f
003F481C  3B D8                           cmp ebx, eax
003F481E  73 6A                           jae 0x1403f488a
003F4820  0F B7 07                        movzx eax, word ptr [rdi]
003F4823  41 0F B6 14 80                  movzx edx, byte ptr [r8 + rax*4]
003F4828  83 E2 0F                        and edx, 0xf
003F482B  45 8B 0C 81                     mov r9d, dword ptr [r9 + rax*4]
003F482F  41 8B C9                        mov ecx, r9d
003F4832  81 E1 FF 0F 00 00               and ecx, 0xfff
003F4838  41 8B C1                        mov eax, r9d
003F483B  48 C1 E8 18                     shr rax, 0x18
003F483F  48 03 C0                        add rax, rax
003F4842  49 C1 E9 0C                     shr r9, 0xc
003F4846  41 81 E1 FF 0F 00 00            and r9d, 0xfff
003F484D  4D 03 4C C5 00                  add r9, qword ptr [r13 + rax*8]
003F4852  48 8D 45 02                     lea rax, [rbp + 2]
003F4856  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
003F485B  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
003F485F  4C 8B C7                        mov r8, rdi
003F4862  49 8B CC                        mov rcx, r12
003F4865  E8 46 04 00 00                  call 0x1403f4cb0
003F486A  84 C0                           test al, al
003F486C  0F 84 A3 00 00 00               je 0x1403f4915
003F4872  40 22 75 02                     and sil, byte ptr [rbp + 2]
003F4876  44 0A 75 02                     or r14b, byte ptr [rbp + 2]
003F487A  FF C3                           inc ebx
003F487C  48 83 C7 18                     add rdi, 0x18
003F4880  4C 8B 45 18                     mov r8, qword ptr [rbp + 0x18]
003F4884  4C 8B 4D 10                     mov r9, qword ptr [rbp + 0x10]
003F4888  EB 86                           jmp 0x1403f4810
003F488A  F6 C1 02                        test cl, 2
003F488D  41 0F B6 D6                     movzx edx, r14b
003F4891  40 0F B6 C6                     movzx eax, sil
003F4895  0F 44 D0                        cmove edx, eax
003F4898  44 0F B6 5D 00                  movzx r11d, byte ptr [rbp]
003F489D  F6 C1 01                        test cl, 1
003F48A0  0F 85 48 01 00 00               jne 0x1403f49ee
003F48A6  44 0A DA                        or r11b, dl
003F48A9  44 88 5D 00                     mov byte ptr [rbp], r11b
003F48AD  75 14                           jne 0x1403f48c3
003F48AF  44 8B 55 04                     mov r10d, dword ptr [rbp + 4]
003F48B3  41 FF C2                        inc r10d
003F48B6  49 83 C7 04                     add r15, 4
003F48BA  48 8B 5D 48                     mov rbx, qword ptr [rbp + 0x48]
003F48BE  E9 1A FF FF FF                  jmp 0x1403f47dd
003F48C3  44 0A 5D 01                     or r11b, byte ptr [rbp + 1]
003F48C7  48 8B 85 E0 00 00 00            mov rax, qword ptr [rbp + 0xe0]
003F48CE  44 88 18                        mov byte ptr [rax], r11b
003F48D1  33 C0                           xor eax, eax
003F48D3  48 8B 4D 78                     mov rcx, qword ptr [rbp + 0x78]
003F48D7  48 33 CD                        xor rcx, rbp
003F48DA  E8 61 7D 2B 00                  call 0x1406ac640
003F48DF  48 8B 9D B0 00 00 00            mov rbx, qword ptr [rbp + 0xb0]
003F48E6  48 8B B5 B8 00 00 00            mov rsi, qword ptr [rbp + 0xb8]
003F48ED  48 8B BD C0 00 00 00            mov rdi, qword ptr [rbp + 0xc0]
003F48F4  48 8D A5 80 00 00 00            lea rsp, [rbp + 0x80]
003F48FB  41 5F                           pop r15
003F48FD  41 5E                           pop r14
003F48FF  41 5D                           pop r13
003F4901  41 5C                           pop r12
003F4903  5D                              pop rbp
003F4904  C3                              ret
003F4905  CC                              int3
003F4906  B8 06 02 00 C0                  mov eax, 0xc0000206
003F490B  EB C6                           jmp 0x1403f48d3
003F490D  41 0F B6 06                     movzx eax, byte ptr [r14]
003F4911  A8 10                           test al, 0x10
003F4913  74 73                           je 0x1403f4988
003F4915  B8 30 00 00 C0                  mov eax, 0xc0000030
003F491A  EB B7                           jmp 0x1403f48d3
003F491C  48 8B 85 E0 00 00 00            mov rax, qword ptr [rbp + 0xe0]
003F4923  C6 00 01                        mov byte ptr [rax], 1
003F4926  33 C0                           xor eax, eax
003F4928  EB A9                           jmp 0x1403f48d3
003F492A  4D 8B EF                        mov r13, r15
003F492D  E9 FC FC FF FF                  jmp 0x1403f462e
003F4932  41 0F B6 43 03                  movzx eax, byte ptr [r11 + 3]
003F4937  66 41 3B 43 06                  cmp ax, word ptr [r11 + 6]
003F493C  0F 83 13 03 00 00               jae 0x1403f4c55
003F4942  49 83 C3 0C                     add r11, 0xc
003F4946  41 FF C0                        inc r8d
003F4949  E9 5A FB FF FF                  jmp 0x1403f44a8
003F494E  66 85 D2                        test dx, dx
003F4951  75 C2                           jne 0x1403f4915
003F4953  45 88 42 03                     mov byte ptr [r10 + 3], r8b
003F4957  41 8B 02                        mov eax, dword ptr [r10]
003F495A  8B CF                           mov ecx, edi
003F495C  81 E1 FF 0F 00 00               and ecx, 0xfff
003F4962  C1 E1 0C                        shl ecx, 0xc
003F4965  25 FF 0F 00 FF                  and eax, 0xff000fff
003F496A  33 C8                           xor ecx, eax
003F496C  81 E1 00 F0 FF FF               and ecx, 0xfffff000
003F4972  41 89 0A                        mov dword ptr [r10], ecx
003F4975  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
003F4979  E9 09 FE FF FF                  jmp 0x1403f4787
003F497E  B8 9A 00 00 C0                  mov eax, 0xc000009a
003F4983  E9 4B FF FF FF                  jmp 0x1403f48d3
003F4988  83 F9 01                        cmp ecx, 1
003F498B  75 88                           jne 0x1403f4915
003F498D  24 0F                           and al, 0xf
003F498F  3C 04                           cmp al, 4
003F4991  74 7C                           je 0x1403f4a0f
003F4993  3C 03                           cmp al, 3
003F4995  0F 85 47 02 00 00               jne 0x1403f4be2
003F499B  41 8B 57 08                     mov edx, dword ptr [r15 + 8]
003F499F  3B FA                           cmp edi, edx
003F49A1  0F 83 AE 02 00 00               jae 0x1403f4c55
003F49A7  8B C7                           mov eax, edi
003F49A9  49 03 07                        add rax, qword ptr [r15]
003F49AC  2B D7                           sub edx, edi
003F49AE  41 8B F2                        mov esi, r10d
003F49B1  45 8B C2                        mov r8d, r10d
003F49B4  44 3B C2                        cmp r8d, edx
003F49B7  73 16                           jae 0x1403f49cf
003F49B9  80 38 00                        cmp byte ptr [rax], 0
003F49BC  74 11                           je 0x1403f49cf
003F49BE  FF C6                           inc esi
003F49C0  44 8B C6                        mov r8d, esi
003F49C3  89 75 58                        mov dword ptr [rbp + 0x58], esi
003F49C6  48 FF C0                        inc rax
003F49C9  48 89 45 68                     mov qword ptr [rbp + 0x68], rax
003F49CD  EB E5                           jmp 0x1403f49b4
003F49CF  EB 0A                           jmp 0x1403f49db
003F49D1  B8 0D 00 00 C0                  mov eax, 0xc000000d
003F49D6  E9 F8 FE FF FF                  jmp 0x1403f48d3
003F49DB  3B F2                           cmp esi, edx
003F49DD  0F 84 47 02 00 00               je 0x1403f4c2a
003F49E3  41 B9 01 00 00 00               mov r9d, 1
003F49E9  E9 CE FC FF FF                  jmp 0x1403f46bc
003F49EE  80 7D 03 00                     cmp byte ptr [rbp + 3], 0
003F49F2  74 7F                           je 0x1403f4a73
003F49F4  88 55 01                        mov byte ptr [rbp + 1], dl
003F49F7  C6 45 03 00                     mov byte ptr [rbp + 3], 0
003F49FB  44 8B 55 04                     mov r10d, dword ptr [rbp + 4]
003F49FF  41 FF C2                        inc r10d
003F4A02  49 83 C7 04                     add r15, 4
003F4A06  48 8B 5D 48                     mov rbx, qword ptr [rbp + 0x48]
003F4A0A  E9 CE FD FF FF                  jmp 0x1403f47dd
003F4A0F  41 8B 47 08                     mov eax, dword ptr [r15 + 8]
003F4A13  2B C7                           sub eax, edi
003F4A15  83 F8 02                        cmp eax, 2
003F4A18  0F 82 37 02 00 00               jb 0x1403f4c55
003F4A1E  8B D7                           mov edx, edi
003F4A20  49 03 17                        add rdx, qword ptr [r15]
003F4A23  D1 E8                           shr eax, 1
003F4A25  41 8B F2                        mov esi, r10d
003F4A28  45 8B C2                        mov r8d, r10d
003F4A2B  44 3B C0                        cmp r8d, eax
003F4A2E  73 18                           jae 0x1403f4a48
003F4A30  66 83 3A 00                     cmp word ptr [rdx], 0
003F4A34  74 12                           je 0x1403f4a48
003F4A36  FF C6                           inc esi
003F4A38  44 8B C6                        mov r8d, esi
003F4A3B  89 75 58                        mov dword ptr [rbp + 0x58], esi
003F4A3E  48 83 C2 02                     add rdx, 2
003F4A42  48 89 55 70                     mov qword ptr [rbp + 0x70], rdx
003F4A46  EB E3                           jmp 0x1403f4a2b
003F4A48  EB 0A                           jmp 0x1403f4a54
003F4A4A  B8 0D 00 00 C0                  mov eax, 0xc000000d
003F4A4F  E9 7F FE FF FF                  jmp 0x1403f48d3
003F4A54  3B F0                           cmp esi, eax
003F4A56  0F 85 DD 01 00 00               jne 0x1403f4c39
003F4A5C  C7 45 08 02 00 00 00            mov dword ptr [rbp + 8], 2
003F4A63  45 8B CA                        mov r9d, r10d
003F4A66  0F 84 D8 01 00 00               je 0x1403f4c44
003F4A6C  03 F6                           add esi, esi
003F4A6E  E9 49 FC FF FF                  jmp 0x1403f46bc
003F4A73  20 55 01                        and byte ptr [rbp + 1], dl
003F4A76  44 8B 55 04                     mov r10d, dword ptr [rbp + 4]
003F4A7A  41 FF C2                        inc r10d
003F4A7D  49 83 C7 04                     add r15, 4
003F4A81  48 8B 5D 48                     mov rbx, qword ptr [rbp + 0x48]
003F4A85  E9 53 FD FF FF                  jmp 0x1403f47dd
003F4A8A  3B 4D 0C                        cmp ecx, dword ptr [rbp + 0xc]
003F4A8D  0F 83 82 FE FF FF               jae 0x1403f4915
003F4A93  48 8D 14 8D 00 00 00 00         lea rdx, [rcx*4]
003F4A9B  42 0F B6 0C 1A                  movzx ecx, byte ptr [rdx + r11]
003F4AA0  0F B6 C1                        movzx eax, cl
003F4AA3  24 0F                           and al, 0xf
003F4AA5  FE C8                           dec al
003F4AA7  3C 01                           cmp al, 1
003F4AA9  0F 87 66 FE FF FF               ja 0x1403f4915
003F4AAF  F6 C1 30                        test cl, 0x30
003F4AB2  0F 85 5D FE FF FF               jne 0x1403f4915
003F4AB8  66 42 83 7C 1A 02 08            cmp word ptr [rdx + r11 + 2], 8
003F4ABF  0F 87 50 FE FF FF               ja 0x1403f4915
003F4AC5  42 80 7C 1A 01 01               cmp byte ptr [rdx + r11 + 1], 1
003F4ACB  0F 85 44 FE FF FF               jne 0x1403f4915
003F4AD1  0F AE E8                        lfence
003F4AD4  42 8B 0C 0A                     mov ecx, dword ptr [rdx + r9]
003F4AD8  42 0F B7 54 1A 02               movzx edx, word ptr [rdx + r11 + 2]
003F4ADE  8B C1                           mov eax, ecx
003F4AE0  48 C1 E8 18                     shr rax, 0x18
003F4AE4  48 03 C0                        add rax, rax
003F4AE7  48 C1 E9 0C                     shr rcx, 0xc
003F4AEB  81 E1 FF 0F 00 00               and ecx, 0xfff
003F4AF1  49 03 4C C5 00                  add rcx, qword ptr [r13 + rax*8]
003F4AF6  4C 8D 45 28                     lea r8, [rbp + 0x28]
003F4AFA  E8 71 02 00 00                  call 0x1403f4d70
003F4AFF  84 C0                           test al, al
003F4B01  0F 84 0E FE FF FF               je 0x1403f4915
003F4B07  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
003F4B0B  48 89 4D 18                     mov qword ptr [rbp + 0x18], rcx
003F4B0F  8B C1                           mov eax, ecx
003F4B11  48 3B C1                        cmp rax, rcx
003F4B14  0F 84 94 FB FF FF               je 0x1403f46ae
003F4B1A  E9 F6 FD FF FF                  jmp 0x1403f4915
003F4B1F  41 39 57 08                     cmp dword ptr [r15 + 8], edx
003F4B23  0F 82 DD FD FF FF               jb 0x1403f4906
003F4B29  8B FA                           mov edi, edx
003F4B2B  E9 42 FC FF FF                  jmp 0x1403f4772
003F4B30  BE 08 00 00 00                  mov esi, 8
003F4B35  80 BD D0 00 00 00 00            cmp byte ptr [rbp + 0xd0], 0
003F4B3C  B8 04 00 00 00                  mov eax, 4
003F4B41  0F 44 F0                        cmove esi, eax
003F4B44  E9 49 FB FF FF                  jmp 0x1403f4692
003F4B49  3B 75 0C                        cmp esi, dword ptr [rbp + 0xc]
003F4B4C  0F 83 C3 FD FF FF               jae 0x1403f4915
003F4B52  48 8D 14 B5 00 00 00 00         lea rdx, [rsi*4]
003F4B5A  42 0F B6 0C 1A                  movzx ecx, byte ptr [rdx + r11]
003F4B5F  0F B6 C1                        movzx eax, cl
003F4B62  24 0F                           and al, 0xf
003F4B64  FE C8                           dec al
003F4B66  3C 01                           cmp al, 1
003F4B68  0F 87 A7 FD FF FF               ja 0x1403f4915
003F4B6E  F6 C1 30                        test cl, 0x30
003F4B71  0F 85 9E FD FF FF               jne 0x1403f4915
003F4B77  66 42 83 7C 1A 02 08            cmp word ptr [rdx + r11 + 2], 8
003F4B7E  0F 87 91 FD FF FF               ja 0x1403f4915
003F4B84  42 80 7C 1A 01 01               cmp byte ptr [rdx + r11 + 1], 1
003F4B8A  0F 85 85 FD FF FF               jne 0x1403f4915
003F4B90  0F AE E8                        lfence
003F4B93  42 8B 0C 0A                     mov ecx, dword ptr [rdx + r9]
003F4B97  42 0F B7 54 1A 02               movzx edx, word ptr [rdx + r11 + 2]
003F4B9D  8B C1                           mov eax, ecx
003F4B9F  48 C1 E8 18                     shr rax, 0x18
003F4BA3  48 03 C0                        add rax, rax
003F4BA6  48 C1 E9 0C                     shr rcx, 0xc
003F4BAA  81 E1 FF 0F 00 00               and ecx, 0xfff
003F4BB0  49 03 4C C5 00                  add rcx, qword ptr [r13 + rax*8]
003F4BB5  4C 8D 45 28                     lea r8, [rbp + 0x28]
003F4BB9  E8 B2 01 00 00                  call 0x1403f4d70
003F4BBE  84 C0                           test al, al
003F4BC0  0F 84 4F FD FF FF               je 0x1403f4915
003F4BC6  48 8B 75 28                     mov rsi, qword ptr [rbp + 0x28]
003F4BCA  8B C6                           mov eax, esi
003F4BCC  48 3B C6                        cmp rax, rsi
003F4BCF  0F 85 40 FD FF FF               jne 0x1403f4915
003F4BD5  4C 8B 4D 10                     mov r9, qword ptr [rbp + 0x10]
003F4BD9  4C 8B 5D 30                     mov r11, qword ptr [rbp + 0x30]
003F4BDD  E9 B9 FA FF FF                  jmp 0x1403f469b
003F4BE2  3C 06                           cmp al, 6
003F4BE4  0F 85 2B FD FF FF               jne 0x1403f4915
003F4BEA  8B CF                           mov ecx, edi
003F4BEC  48 FF C1                        inc rcx
003F4BEF  41 8B 47 08                     mov eax, dword ptr [r15 + 8]
003F4BF3  2B C7                           sub eax, edi
003F4BF5  83 F8 02                        cmp eax, 2
003F4BF8  72 5B                           jb 0x1403f4c55
003F4BFA  49 03 0F                        add rcx, qword ptr [r15]
003F4BFD  4C 8D 45 28                     lea r8, [rbp + 0x28]
003F4C01  BA 01 00 00 00                  mov edx, 1
003F4C06  E8 65 01 00 00                  call 0x1403f4d70
003F4C0B  84 C0                           test al, al
003F4C0D  74 46                           je 0x1403f4c55
003F4C0F  8B 4D 28                        mov ecx, dword ptr [rbp + 0x28]
003F4C12  E8 B9 58 5D 00                  call 0x1409ca4d0
003F4C17  8B F0                           mov esi, eax
003F4C19  83 F8 FF                        cmp eax, -1
003F4C1C  74 37                           je 0x1403f4c55
003F4C1E  45 33 C9                        xor r9d, r9d
003F4C21  48 8B 4D 18                     mov rcx, qword ptr [rbp + 0x18]
003F4C25  E9 92 FA FF FF                  jmp 0x1403f46bc
003F4C2A  C7 45 08 01 00 00 00            mov dword ptr [rbp + 8], 1
003F4C31  45 8B CA                        mov r9d, r10d
003F4C34  E9 83 FA FF FF                  jmp 0x1403f46bc
003F4C39  41 B9 02 00 00 00               mov r9d, 2
003F4C3F  E9 22 FE FF FF                  jmp 0x1403f4a66
003F4C44  8B C8                           mov ecx, eax
003F4C46  8B C7                           mov eax, edi
003F4C48  48 8D 14 48                     lea rdx, [rax + rcx*2]
003F4C4C  41 8B 47 08                     mov eax, dword ptr [r15 + 8]
003F4C50  48 3B D0                        cmp rdx, rax
003F4C53  74 2D                           je 0x1403f4c82
003F4C55  B8 0D 00 00 C0                  mov eax, 0xc000000d
003F4C5A  E9 74 FC FF FF                  jmp 0x1403f48d3
003F4C5F  41 FF C0                        inc r8d
003F4C62  44 89 45 04                     mov dword ptr [rbp + 4], r8d
003F4C66  4C 8B 4D 10                     mov r9, qword ptr [rbp + 0x10]
003F4C6A  4C 8B 5D 30                     mov r11, qword ptr [rbp + 0x30]
003F4C6E  44 3B C3                        cmp r8d, ebx
003F4C71  0F 83 10 FB FF FF               jae 0x1403f4787
003F4C77  8B FE                           mov edi, esi
003F4C79  49 83 C7 10                     add r15, 0x10
003F4C7D  E9 05 FB FF FF                  jmp 0x1403f4787
003F4C82  48 8B 4D 18                     mov rcx, qword ptr [rbp + 0x18]
003F4C86  E9 E1 FD FF FF                  jmp 0x1403f4a6c
003F4C8B  33 F6                           xor esi, esi
003F4C8D  E9 ED FA FF FF                  jmp 0x1403f477f
003F4C92  B8 01 00 00 C0                  mov eax, 0xc0000001
003F4C97  E9 37 FC FF FF                  jmp 0x1403f48d3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpApplyPayloadFilterInternal(__int64 a1, __int64 a2, __int64 a3, unsigned __int8 a4, unsigned __int8 a5, __int64 a6, __int64 a7)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m50;
    unsigned int v_stack_m54;
    unsigned __int16 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int8 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned int v_stack_m9C;
    unsigned int v_stack_mA0;
    unsigned int v_stack_mA4;
    unsigned __int8 v_stack_mA5;
    unsigned __int8 v_stack_mA6;
    unsigned __int8 v_stack_mA7;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned int v_stack_mB8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (176);
    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_stack_p18 = v_rdi;
    result = (*(unsigned __int64 *)(v_rip + 10576702)) ^ (v_stack_mA8);
    v_stack_m30 = result;
    v_rdi = 0;
    v_stack_m80 = 0;
    v_stack_mA6 = 0;
    v_stack_mA4 = 0xC000000DULL;
    if (((unsigned int)(a2)) > 128) goto loc_003F4C55;
    v_stack_m58 = (unsigned __int16)(*(unsigned __int16 *)(a1));
    v_stack_m88 = (unsigned __int8)(*(unsigned __int8 *)(a1 + 2));
    goto loc_003F444D;
loc_003F444D:
    result = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(a1)))) - ((unsigned int)(a2)));
    result = (unsigned int)((result) >> (1));
    result = (unsigned int)((result) + ((unsigned int)(a2)));
    result = (unsigned int)((result) >> (5));
    result = (unsigned int)((result) * ((unsigned int)(result)));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(a1)))) - ((unsigned int)(result)));
    if (condition_is_above_or_equal) goto loc_003F491C;
    v_stack_mA0 = 0;
    v_r11 = (*(unsigned __int16 *)(a6 + 32)) + (a6);
    a2 = (a2) >> (3);
loc_003F44A8:
    v_stack_m60 = v_r11;
    if (0 >= ((unsigned int)(a2))) goto loc_003F44C8;
    if ((*(unsigned __int16 *)(v_r11)) != ((unsigned __int16)(*(unsigned __int16 *)(a1)))) goto loc_003F4932;
    if ((*(unsigned __int8 *)(v_r11 + 2)) != ((unsigned __int8)(*(unsigned __int8 *)(a1 + 2)))) goto loc_003F4932;
loc_003F44C8:
    if (0 == ((unsigned int)(a2))) goto loc_003F491C;
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a2))))) << (4));
    result = (unsigned int)((*(unsigned __int8 *)(v_r11 + 3)) + 1);
    v_stack_m54 = (unsigned int)(result);
    result = 0;
    v_stack_m48 = 0;
    v_stack_m90 = 0;
    result = RtlpGetStackLimits(v_stack_m90, v_stack_m48, 0, *(unsigned __int16 *)(a1));
    a2 = v_stack_m90;
    if ((unsigned __int8)(result) == 0) { a2 = 0; }
    a1 = (unsigned int)((v_rdi + 4096) + ((unsigned int)(result * 4)));
    result = (v_stack_m48) - (a2);
    if (result < a1) goto loc_003F497E;
    if ((result * 4 + 15) <= ((unsigned int)((unsigned int)(result * 4)))) {
        a1 = a2;
    }
    a1 = (a1) & (-16);
    result = _chkstk(a1, a2, 0, 0);
    v_rsp = (v_rsp) - (a1);
    v_stack_m98 = v_stack_mA8;
    if (a4 == 0) goto loc_003F492A;
    if ((v_rdi + 15) <= ((unsigned int)((unsigned int)(v_rdi)))) {
        a1 = a2;
    }
    a1 = (a1) & (-16);
    result = _chkstk(a1, a2, 0, v_stack_mA8);
    v_rsp = (v_rsp) - (a1);
    if (a4 == 0) goto loc_003F492A;
    if ((unsigned int)(v_rdi) == 0) goto loc_003F460A;
    if ((((unsigned __int8)(a3)) & (3)) != 0) goto loc_003F4616;
    a1 = ((unsigned int)((unsigned int)(v_rdi))) + (a3);
    if (a1 > (result * 4)) goto loc_003F461B;
    if (a1 < a3) goto loc_003F461B;
loc_003F45AE:
    result = memcpy(v_stack_mA8, a3, (unsigned int)((unsigned int)(v_rdi)), v_stack_mA8);
    a2 = 0;
    v_stack_m70 = 0;
loc_003F45C8:
    if (0 >= ((unsigned int)((unsigned int)((unsigned int)(a2))))) goto loc_003F4620;
    result = (0) + (0);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mA8 + result * 8 + 8))) == 0) goto loc_003F45F4;
    a2 = (0) + (0);
    if ((*(unsigned __int64 *)(v_stack_mA8 + a2 * 8) + (unsigned int)(*(unsigned int *)(v_stack_mA8 + result * 8 + 8)) * 1) < (*(unsigned __int64 *)(v_stack_mA8 + a2 * 8))) goto loc_003F4602;
    if ((*(unsigned __int64 *)(v_stack_mA8 + a2 * 8) + (unsigned int)(*(unsigned int *)(v_stack_mA8 + result * 8 + 8)) * 1) > (result * 4)) goto loc_003F4602;
loc_003F45F4:
    a1 = (unsigned int)((0) + 1);
    v_stack_m70 = (unsigned int)(a1);
    goto loc_003F45C8;
loc_003F4602:
    goto loc_003F45F4;
loc_003F460A:
    goto loc_003F45AE;
loc_003F4616:
    result = ExRaiseDatatypeMisalignment((unsigned int)(v_stack_m70), (unsigned int)((unsigned int)(a1)), (unsigned int)((unsigned int)(a1)), (unsigned int)(*(unsigned int *)(v_stack_mA8 + result * 8 + 8)));
loc_003F461B:
    goto loc_003F45AE;
loc_003F4620:
    goto loc_003F462E;
loc_003F462E:
    v_r11 = (*(unsigned __int16 *)(a6 + 36)) + (a6);
    v_stack_m78 = v_r11;
    v_rsi = 0;
    v_stack_mA4 = 0;
    v_stack_m68 = v_stack_m98;
loc_003F465D:
    v_stack_m9C = 0;
    if (0 >= v_stack_m54) goto loc_003F47A0;
    if (0 == ((unsigned int)((unsigned int)((unsigned int)(a2))))) goto loc_003F4906;
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(v_r11 + *(unsigned __int16 *)(v_stack_m60 + 4) * 4))) & (15));
    if (((unsigned __int8)(result)) == 7) goto loc_003F494E;
    if (((unsigned __int8)(result)) == 8) goto loc_003F4B30;
loc_003F4692:
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_r11 + *(unsigned __int16 *)(v_stack_m60 + 4) * 4))) & (16)) != 0) goto loc_003F4B49;
loc_003F469B:
    v_stack_m90 = *(unsigned __int8 *)(v_r11 + *(unsigned __int16 *)(v_stack_m60 + 4) * 4 + 1);
    if (((*(unsigned __int8 *)(v_r11 + *(unsigned __int16 *)(v_stack_m60 + 4) * 4)) & (32)) != 0) goto loc_003F4A8A;
loc_003F46AE:
    v_r10 = 0;
    if ((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_r11 + *(unsigned __int16 *)(v_stack_m60 + 4) * 4 + 2)))) == 0) goto loc_003F490D;
loc_003F46BC:
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_r11 + *(unsigned __int16 *)(v_stack_m60 + 4) * 4 + 2)))) * ((unsigned int)(*(unsigned __int8 *)(v_r11 + *(unsigned __int16 *)(v_stack_m60 + 4) * 4 + 1))));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_mA8 + 8))) - (0));
    if (((unsigned int)(result)) < ((unsigned int)(v_rsi))) goto loc_003F4906;
    *(unsigned __int8 *)(v_stack_m68 + 3) = (unsigned __int8)((unsigned int)(v_stack_mA4));
    a1 = (unsigned int)((0) << (12));
    a1 = (unsigned int)((a1) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m68)))));
    a1 = (unsigned int)((a1) & (0xFFF000ULL));
    a1 = (unsigned int)((a1) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m68)))));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(a1))) ^ ((unsigned int)(v_rsi)));
    a2 = (unsigned int)((a2) & (0xFFFULL));
    a2 = (unsigned int)((a2) ^ ((unsigned int)(a1)));
    *(unsigned int *)(v_stack_m68) = (unsigned int)(a2);
    result = (unsigned int)(((unsigned int)((unsigned int)(a2))) >> (24));
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(v_stack_mA4)))) goto loc_003F4906;
    result = (unsigned int)(((unsigned int)((unsigned int)(a2))) >> (12));
    result = (unsigned int)((result) & (0xFFFULL));
    if (((unsigned int)(result)) != 0) goto loc_003F4906;
    a2 = (unsigned int)((a2) & (0xFFFULL));
    if (((unsigned int)(a2)) != ((unsigned int)(v_rsi))) goto loc_003F4906;
    v_rdi = (unsigned int)((0) + ((unsigned int)(0 + v_rsi * 1)));
    if (((unsigned int)(v_rdi)) > (*(unsigned int *)(v_stack_mA8 + 8))) goto loc_003F4C92;
    if (((unsigned int)(v_rdi)) != (*(unsigned int *)(v_stack_mA8 + 8))) goto loc_003F4C8B;
    a3 = (unsigned int)(((unsigned int)(v_stack_mA4)) + 1);
    v_stack_mA4 = (unsigned int)(a3);
    v_rsi = 0;
    if (((unsigned int)(a3)) >= ((unsigned int)((unsigned int)((unsigned int)(a2))))) goto loc_003F477F;
    v_r15 = (v_stack_mA8) + (16);
    result = ((unsigned int)((unsigned int)(a2))) << (4);
    result = (result) + (v_stack_mA8);
    if (v_r15 >= result) goto loc_003F4C92;
    if ((unsigned int)((unsigned int)(v_stack_mA0)) != 0) goto loc_003F4B1F;
loc_003F4772:
    v_stack_mA0 = 0;
    if (0 == (*(unsigned int *)(v_r15 + 8))) goto loc_003F4C5F;
loc_003F477F:
loc_003F4787:
    result = (unsigned int)(((unsigned int)(v_stack_m9C)) + 1);
    v_r14 = (v_r11 + *(unsigned __int16 *)(v_stack_m60 + 4) * 4) + (4);
    a1 = (v_stack_m68) + (4);
    v_stack_m68 = a1;
    goto loc_003F465D;
loc_003F47A0:
    if (v_stack_mA0 != 0) goto loc_003F4906;
    v_stack_m90 = v_stack_m78 + *(unsigned __int16 *)(v_stack_m60 + 4) * 4;
    a1 = (*(unsigned __int16 *)(a6 + 40)) + (a6);
    v_stack_mA7 = 0;
    v_r11 = 0;
    v_stack_mA8 = 0;
    v_stack_mA5 = 1;
loc_003F47DD:
    v_stack_mA4 = 0;
    if (0 >= ((unsigned int)(*(unsigned __int16 *)(v_stack_m60 + 10)))) goto loc_003F48C3;
    v_r14 = 0;
    result = 0;
loc_003F4810:
    result = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(a1 + *(unsigned __int16 *)(v_stack_m60 + 8) * 4)))) >> (2));
    result = (unsigned int)((result) & (63));
    if (0 >= ((unsigned int)(result))) goto loc_003F488A;
    a2 = (unsigned int)((*(unsigned __int8 *)(v_stack_m78 + *(unsigned __int16 *)(v_stack_m60 + 4) * 4 + *(unsigned __int16 *)(a6 + 56 + *(unsigned __int16 *)(a1 + *(unsigned __int16 *)(v_stack_m60 + 8) * 4 + 2) + *(unsigned __int16 *)(a1 + *(unsigned __int16 *)(v_stack_m60 + 8) * 4 + 2) * 2 * 8) * 4)) & (15));
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m98 + *(unsigned __int16 *)(a6 + 56 + *(unsigned __int16 *)(a1 + *(unsigned __int16 *)(v_stack_m60 + 8) * 4 + 2) + *(unsigned __int16 *)(a1 + *(unsigned __int16 *)(v_stack_m60 + 8) * 4 + 2) * 2 * 8) * 4))))) & (0xFFFULL));
    result = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m98 + *(unsigned __int16 *)(a6 + 56 + *(unsigned __int16 *)(a1 + *(unsigned __int16 *)(v_stack_m60 + 8) * 4 + 2) + *(unsigned __int16 *)(a1 + *(unsigned __int16 *)(v_stack_m60 + 8) * 4 + 2) * 2 * 8) * 4))))) >> (24);
    result = (result) + (result);
    a4 = ((unsigned int)(*(unsigned int *)(v_stack_m98 + *(unsigned __int16 *)(a6 + 56 + *(unsigned __int16 *)(a1 + *(unsigned __int16 *)(v_stack_m60 + 8) * 4 + 2) + *(unsigned __int16 *)(a1 + *(unsigned __int16 *)(v_stack_m60 + 8) * 4 + 2) * 2 * 8) * 4))) >> (12);
    a4 = (unsigned int)((a4) & (0xFFFULL));
    a4 = (a4) + (*(unsigned __int64 *)(v_stack_mA8 + result * 8));
    v_stack_mB0 = v_stack_mA6;
    v_stack_mB8 = (unsigned int)(a1);
    result = EtwpApplyPredicate(a6, a2, a6 + 56 + *(unsigned __int16 *)(a1 + *(unsigned __int16 *)(v_stack_m60 + 8) * 4 + 2) + *(unsigned __int16 *)(a1 + *(unsigned __int16 *)(v_stack_m60 + 8) * 4 + 2) * 2 * 8, a4);
    if ((unsigned __int8)(result) == 0) goto loc_003F4915;
    v_rsi = (unsigned __int8)((1) & (v_stack_mA6));
    v_r14 = (unsigned __int8)((v_r14) | (v_stack_mA6));
    v_rbx = (unsigned int)((0) + 1);
    v_rdi = (a6 + 56 + *(unsigned __int16 *)(a1 + *(unsigned __int16 *)(v_stack_m60 + 8) * 4 + 2) + *(unsigned __int16 *)(a1 + *(unsigned __int16 *)(v_stack_m60 + 8) * 4 + 2) * 2 * 8) + (24);
    goto loc_003F4810;
loc_003F488A:
    a2 = (unsigned __int8)(v_r14);
    if ((((unsigned __int8)(a6)) & (2)) == 0) { a2 = (unsigned int)((unsigned __int8)(v_rsi)); }
    if ((((unsigned __int8)(a6)) & (1)) != 0) goto loc_003F49EE;
    v_r11 = (unsigned __int8)((v_stack_mA8) | ((unsigned __int8)(a2)));
    v_stack_mA8 = (unsigned __int8)(v_r11);
    if (condition_is_not_equal) goto loc_003F48C3;
    v_r10 = (unsigned int)(((unsigned int)(v_stack_mA4)) + 1);
    v_r15 = (a1 + *(unsigned __int16 *)(v_stack_m60 + 8) * 4) + (4);
    goto loc_003F47DD;
loc_003F48C3:
    v_r11 = (unsigned __int8)((v_r11) | (v_stack_mA7));
    *(unsigned __int8 *)(a7) = (unsigned __int8)(v_r11);
    result = 0;
loc_003F48D3:
    a1 = (v_stack_m30) ^ (v_stack_mA8);
    result = _security_check_cookie(a1, a2, v_stack_m90, v_stack_m98);
    return result;
loc_003F4906:
    goto loc_003F48D3;
loc_003F490D:
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_r14))) & (16)) == 0) goto loc_003F4988;
loc_003F4915:
    goto loc_003F48D3;
loc_003F491C:
    *(unsigned __int8 *)(a7) = 1;
    result = 0;
    goto loc_003F48D3;
loc_003F492A:
    goto loc_003F462E;
loc_003F4932:
    if (((unsigned __int16)(*(unsigned __int8 *)(v_r11 + 3))) >= (*(unsigned __int16 *)(v_r11 + 6))) goto loc_003F4C55;
    v_r11 = (v_r11) + (12);
    a3 = (unsigned int)((v_stack_m90) + 1);
    goto loc_003F44A8;
loc_003F494E:
    if ((unsigned __int16)(a2) != 0) goto loc_003F4915;
    *(unsigned __int8 *)(v_r10 + 3) = (unsigned __int8)(a3);
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_p18))) & (0xFFFULL));
    a1 = (unsigned int)((a1) << (12));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r10))) & (0xFF000FFFULL));
    a1 = (unsigned int)((a1) ^ ((unsigned int)(result)));
    a1 = (unsigned int)((a1) & (0xFFFFF000ULL));
    *(unsigned int *)(v_r10) = (unsigned int)(a1);
    goto loc_003F4787;
loc_003F497E:
    goto loc_003F48D3;
loc_003F4988:
    if (((unsigned int)(v_stack_m68)) != 1) goto loc_003F4915;
    result = (unsigned __int8)(((unsigned int)(0xC000009AULL)) & (15));
    if (((unsigned __int8)(result)) == 4) goto loc_003F4A0F;
    if (((unsigned __int8)(result)) != 3) goto loc_003F4BE2;
    if (((unsigned int)(v_stack_p18)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_r15 + 8))))) goto loc_003F4C55;
    result = ((unsigned int)((unsigned int)(v_stack_p18))) + (*(unsigned __int64 *)(v_r15));
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r15 + 8))) - ((unsigned int)(v_stack_p18)));
loc_003F49B4:
    if (((unsigned int)((unsigned int)((unsigned int)(v_r10)))) >= ((unsigned int)(a2))) goto loc_003F49CF;
    if ((*(unsigned __int8 *)(result)) == 0) goto loc_003F49CF;
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(v_r10))) + 1);
    v_stack_m50 = (unsigned int)(v_rsi);
    result = (result) + 1;
    v_stack_m40 = result;
    goto loc_003F49B4;
loc_003F49CF:
    goto loc_003F49DB;
loc_003F49DB:
    if (((unsigned int)(v_rsi)) == ((unsigned int)(a2))) goto loc_003F4C2A;
    goto loc_003F46BC;
loc_003F49EE:
    if (v_stack_mA5 == 0) goto loc_003F4A73;
    v_stack_mA7 = (unsigned __int8)(a2);
    v_stack_mA5 = 0;
    v_r10 = (unsigned int)(((unsigned int)(v_stack_mA4)) + 1);
    v_r15 = (v_r15) + (4);
    goto loc_003F47DD;
loc_003F4A0F:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r15 + 8))) - ((unsigned int)(v_stack_p18)));
    if (((unsigned int)(result)) < 2) goto loc_003F4C55;
    a2 = ((unsigned int)((unsigned int)(v_stack_p18))) + (*(unsigned __int64 *)(v_r15));
    result = (unsigned int)((result) >> (1));
loc_003F4A2B:
    if (((unsigned int)((unsigned int)((unsigned int)(v_r10)))) >= ((unsigned int)(result))) goto loc_003F4A48;
    if ((*(unsigned __int16 *)(a2)) == 0) goto loc_003F4A48;
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(v_r10))) + 1);
    v_stack_m50 = (unsigned int)(v_rsi);
    a2 = (a2) + (2);
    v_stack_m38 = a2;
    goto loc_003F4A2B;
loc_003F4A48:
    goto loc_003F4A54;
loc_003F4A54:
    if (((unsigned int)(v_rsi)) != ((unsigned int)(result))) goto loc_003F4C39;
    v_stack_mA0 = 2;
loc_003F4A66:
    if (((unsigned int)(v_rsi)) == ((unsigned int)(result))) goto loc_003F4C44;
loc_003F4A6C:
    v_rsi = (unsigned int)((v_rsi) + ((unsigned int)(v_rsi)));
    goto loc_003F46BC;
loc_003F4A73:
    v_r10 = (unsigned int)(((unsigned int)(v_stack_mA4)) + 1);
    v_r15 = (v_r15) + (4);
    goto loc_003F47DD;
loc_003F4A8A:
    if (((unsigned int)(v_stack_m68)) >= v_stack_m9C) goto loc_003F4915;
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(v_stack_m68 * 4 + v_r11 * 1))) & (15));
    result = (unsigned __int8)((result) - 1);
    if (((unsigned __int8)(result)) > 1) goto loc_003F4915;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_stack_m68 * 4 + v_r11 * 1))) & (48)) != 0) goto loc_003F4915;
    if ((*(unsigned __int16 *)(v_stack_m68 * 4 + v_r11 * 1 + 2)) > 8) goto loc_003F4915;
    if ((*(unsigned __int8 *)(v_stack_m68 * 4 + v_r11 * 1 + 1)) != 1) goto loc_003F4915;
    result = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m68 * 4 + (unsigned int)((unsigned int)(v_r10)) * 1))))) >> (24);
    result = (result) + (result);
    a1 = ((unsigned int)(*(unsigned int *)(v_stack_m68 * 4 + (unsigned int)((unsigned int)(v_r10)) * 1))) >> (12);
    a1 = (unsigned int)((a1) & (0xFFFULL));
    a1 = (a1) + (*(unsigned __int64 *)(v_r15 + result * 8));
    result = EtwpGetFieldValue(a1, *(unsigned __int16 *)(v_stack_m68 * 4 + v_r11 * 1 + 2), v_stack_m80, (unsigned int)((unsigned int)(v_r10)));
    if ((unsigned __int8)(result) == 0) goto loc_003F4915;
    v_stack_m90 = v_stack_m80;
    if (((unsigned int)((unsigned int)(v_stack_m80))) == v_stack_m80) goto loc_003F46AE;
    goto loc_003F4915;
loc_003F4B1F:
    if ((*(unsigned int *)(v_r15 + 8)) < ((unsigned int)(*(unsigned __int16 *)(v_stack_m68 * 4 + v_r11 * 1 + 2)))) goto loc_003F4906;
    goto loc_003F4772;
loc_003F4B30:
    v_rsi = 8;
    if (a5 == 0) { v_rsi = 4; }
    goto loc_003F4692;
loc_003F4B49:
    if (((unsigned int)(v_rsi)) >= v_stack_m9C) goto loc_003F4915;
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(v_rsi * 4 + v_r11 * 1))) & (15));
    result = (unsigned __int8)((result) - 1);
    if (((unsigned __int8)(result)) > 1) goto loc_003F4915;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_rsi * 4 + v_r11 * 1))) & (48)) != 0) goto loc_003F4915;
    if ((*(unsigned __int16 *)(v_rsi * 4 + v_r11 * 1 + 2)) > 8) goto loc_003F4915;
    if ((*(unsigned __int8 *)(v_rsi * 4 + v_r11 * 1 + 1)) != 1) goto loc_003F4915;
    result = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi * 4 + (unsigned int)((unsigned int)(v_r10)) * 1))))) >> (24);
    result = (result) + (result);
    a1 = ((unsigned int)(*(unsigned int *)(v_rsi * 4 + (unsigned int)((unsigned int)(v_r10)) * 1))) >> (12);
    a1 = (unsigned int)((a1) & (0xFFFULL));
    a1 = (a1) + (*(unsigned __int64 *)(v_r15 + result * 8));
    result = EtwpGetFieldValue(a1, *(unsigned __int16 *)(v_rsi * 4 + v_r11 * 1 + 2), v_stack_m80, (unsigned int)((unsigned int)(v_r10)));
    if ((unsigned __int8)(result) == 0) goto loc_003F4915;
    if (((unsigned int)((unsigned int)(v_stack_m80))) != v_stack_m80) goto loc_003F4915;
    goto loc_003F469B;
loc_003F4BE2:
    if (((unsigned __int8)((unsigned int)((unsigned int)(v_stack_m80)))) != 6) goto loc_003F4915;
    a1 = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_stack_m68 * 4 + v_r11 * 1 + 2)))))) + 1;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r15 + 8))) - ((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_stack_m68 * 4 + v_r11 * 1 + 2))))));
    if (((unsigned int)(result)) < 2) goto loc_003F4C55;
    a1 = (a1) + (*(unsigned __int64 *)(v_r15));
    result = EtwpGetFieldValue(a1, 1, v_stack_m80, v_stack_m98);
    if ((unsigned __int8)(result) == 0) goto loc_003F4C55;
    result = RtlLengthRequiredSid((unsigned int)(v_stack_m80), 1, v_stack_m80, v_stack_m98);
    if (((unsigned int)(result)) == -1) goto loc_003F4C55;
    a4 = 0;
    goto loc_003F46BC;
loc_003F4C2A:
    v_stack_mA0 = 1;
    goto loc_003F46BC;
loc_003F4C39:
    goto loc_003F4A66;
loc_003F4C44:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_stack_m68 * 4 + v_r11 * 1 + 2))))) + (unsigned int)((unsigned int)(result)) * 2) == ((unsigned int)(*(unsigned int *)(v_r15 + 8)))) goto loc_003F4C82;
loc_003F4C55:
    goto loc_003F48D3;
loc_003F4C5F:
    a3 = (unsigned int)((v_stack_m80) + 1);
    v_stack_mA4 = (unsigned int)(a3);
    if (((unsigned int)(a3)) >= ((unsigned int)(v_stack_m60))) goto loc_003F4787;
    v_r15 = (v_r15) + (16);
    goto loc_003F4787;
loc_003F4C82:
    goto loc_003F4A6C;
loc_003F4C8B:
    v_rsi = 0;
    goto loc_003F477F;
loc_003F4C92:
    goto loc_003F48D3;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpApplyPayloadFilterInternal(void *Arg1, int64_t Arg2, int64_t Arg3, uint8_t Arg4, uint8_t Arg5, void *Arg6, void *Arg7)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg6 = (uint8_t *)Arg6;
    uint8_t *arg7 = (uint8_t *)Arg7;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_m50;
    uint32_t v_stack_m54;
    uint16_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint8_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint32_t v_stack_m9C;
    uint32_t v_stack_mA0;
    uint32_t v_stack_mA4;
    uint8_t v_stack_mA5;
    uint8_t v_stack_mA6;
    uint8_t v_stack_mA7;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint32_t v_stack_mB8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (176);
    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    v_stack_p18 = local_rdi;
    result = (*(uint64_t *)(v_rip + 0xA1633E)) ^ (v_stack_mA8);
    v_stack_m30 = result;
    local_rdi = 0;
    v_stack_m80 = 0;
    v_stack_mA6 = 0;
    v_stack_mA4 = 0xC000000DULL;
    if (((uint32_t)(Arg2)) > 128) goto loc_003F4C55;
    v_stack_m58 = (uint16_t)(*(uint16_t *)(arg1));
    v_stack_m88 = (uint8_t)(*(uint8_t *)(arg1 + 0x2));
    goto loc_003F444D;
loc_003F444D:
    result = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(arg1)))) - ((uint32_t)(Arg2)));
    result = (uint32_t)((result) >> (1));
    result = (uint32_t)((result) + ((uint32_t)(Arg2)));
    result = (uint32_t)((result) >> (5));
    result = (uint32_t)((result) * ((uint32_t)(result)));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(arg1)))) - ((uint32_t)(result)));
    if (condition_is_above_or_equal) goto loc_003F491C;
    v_stack_mA0 = 0;
    local_r11 = (*(uint16_t *)(arg6 + 0x20)) + (Arg6);
    Arg2 = (Arg2) >> (3);
loc_003F44A8:
    v_stack_m60 = local_r11;
    if (0 >= ((uint32_t)(Arg2))) goto loc_003F44C8;
    if ((*(uint16_t *)(local_r11)) != ((uint16_t)(*(uint16_t *)(arg1)))) goto loc_003F4932;
    if ((*(uint8_t *)(local_r11 + 0x2)) != ((uint8_t)(*(uint8_t *)(arg1 + 0x2)))) goto loc_003F4932;
loc_003F44C8:
    if (0 == ((uint32_t)(Arg2))) goto loc_003F491C;
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg2))))) << (4));
    result = (uint32_t)((*(uint8_t *)(local_r11 + 0x3)) + 1);
    v_stack_m54 = (uint32_t)(result);
    result = 0;
    v_stack_m48 = 0;
    v_stack_m90 = 0;
    result = RtlpGetStackLimits(v_stack_m90, v_stack_m48, 0, *(uint16_t *)(arg1));
    Arg2 = v_stack_m90;
    if ((uint8_t)(result) == 0) { Arg2 = 0; }
    Arg1 = (uint32_t)((local_rdi + 4096) + ((uint32_t)(result * 4)));
    result = (v_stack_m48) - (Arg2);
    if (result < Arg1) goto loc_003F497E;
    if ((result * 4 + 15) <= ((uint32_t)((uint32_t)(result * 4)))) {
        Arg1 = Arg2;
    }
    Arg1 = (Arg1) & (-16);
    result = _chkstk(Arg1, Arg2, 0, 0);
    local_rsp = (local_rsp) - (Arg1);
    v_stack_m98 = v_stack_mA8;
    if (Arg4 == 0) goto loc_003F492A;
    if ((local_rdi + 15) <= ((uint32_t)((uint32_t)(local_rdi)))) {
        Arg1 = Arg2;
    }
    Arg1 = (Arg1) & (-16);
    result = _chkstk(Arg1, Arg2, 0, v_stack_mA8);
    local_rsp = (local_rsp) - (Arg1);
    if (Arg4 == 0) goto loc_003F492A;
    if ((uint32_t)(local_rdi) == 0) goto loc_003F460A;
    if ((((uint8_t)(Arg3)) & (3)) != 0) goto loc_003F4616;
    Arg1 = ((uint32_t)((uint32_t)(local_rdi))) + (Arg3);
    if (Arg1 > (result * 4)) goto loc_003F461B;
    if (Arg1 < Arg3) goto loc_003F461B;
loc_003F45AE:
    result = memcpy(v_stack_mA8, Arg3, (uint32_t)((uint32_t)(local_rdi)), v_stack_mA8);
    Arg2 = 0;
    v_stack_m70 = 0;
loc_003F45C8:
    if (0 >= ((uint32_t)((uint32_t)((uint32_t)(Arg2))))) goto loc_003F4620;
    result = (0) + (0);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mA8 + result * 8 + 0x8))) == 0) goto loc_003F45F4;
    Arg2 = (0) + (0);
    if ((*(uint64_t *)(v_stack_mA8 + Arg2 * 8) + (uint32_t)(*(uint32_t *)(v_stack_mA8 + result * 8 + 0x8)) * 1) < (*(uint64_t *)(v_stack_mA8 + Arg2 * 8))) goto loc_003F4602;
    if ((*(uint64_t *)(v_stack_mA8 + Arg2 * 8) + (uint32_t)(*(uint32_t *)(v_stack_mA8 + result * 8 + 0x8)) * 1) > (result * 4)) goto loc_003F4602;
loc_003F45F4:
    Arg1 = (uint32_t)((0) + 1);
    v_stack_m70 = (uint32_t)(Arg1);
    goto loc_003F45C8;
loc_003F4602:
    goto loc_003F45F4;
loc_003F460A:
    goto loc_003F45AE;
loc_003F4616:
    result = ExRaiseDatatypeMisalignment((uint32_t)(v_stack_m70), (uint32_t)((uint32_t)(Arg1)), (uint32_t)((uint32_t)(Arg1)), (uint32_t)(*(uint32_t *)(v_stack_mA8 + result * 8 + 0x8)));
loc_003F461B:
    goto loc_003F45AE;
loc_003F4620:
    goto loc_003F462E;
loc_003F462E:
    local_r11 = (*(uint16_t *)(arg6 + 0x24)) + (Arg6);
    v_stack_m78 = local_r11;
    local_rsi = 0;
    v_stack_mA4 = 0;
    v_stack_m68 = v_stack_m98;
loc_003F465D:
    v_stack_m9C = 0;
    if (0 >= v_stack_m54) goto loc_003F47A0;
    if (0 == ((uint32_t)((uint32_t)((uint32_t)(Arg2))))) goto loc_003F4906;
    result = (uint8_t)(((uint8_t)(*(uint8_t *)(local_r11 + *(uint16_t *)(v_stack_m60 + 0x4) * 4))) & (15));
    if (((uint8_t)(result)) == 7) goto loc_003F494E;
    if (((uint8_t)(result)) == 8) goto loc_003F4B30;
loc_003F4692:
    if ((((uint8_t)(*(uint8_t *)(local_r11 + *(uint16_t *)(v_stack_m60 + 0x4) * 4))) & (16)) != 0) goto loc_003F4B49;
loc_003F469B:
    v_stack_m90 = *(uint8_t *)(local_r11 + *(uint16_t *)(v_stack_m60 + 0x4) * 4 + 0x1);
    if (((*(uint8_t *)(local_r11 + *(uint16_t *)(v_stack_m60 + 0x4) * 4)) & (32)) != 0) goto loc_003F4A8A;
loc_003F46AE:
    local_r10 = 0;
    if ((uint32_t)((uint32_t)((uint32_t)(*(uint16_t *)(local_r11 + *(uint16_t *)(v_stack_m60 + 0x4) * 4 + 0x2)))) == 0) goto loc_003F490D;
loc_003F46BC:
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(local_r11 + *(uint16_t *)(v_stack_m60 + 0x4) * 4 + 0x2)))) * ((uint32_t)(*(uint8_t *)(local_r11 + *(uint16_t *)(v_stack_m60 + 0x4) * 4 + 0x1))));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_mA8 + 0x8))) - (0));
    if (((uint32_t)(result)) < ((uint32_t)(local_rsi))) goto loc_003F4906;
    *(uint8_t *)(v_stack_m68 + 0x3) = (uint8_t)((uint32_t)(v_stack_mA4));
    Arg1 = (uint32_t)((0) << (12));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m68)))));
    Arg1 = (uint32_t)((Arg1) & (0xFFF000ULL));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m68)))));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) ^ ((uint32_t)(local_rsi)));
    Arg2 = (uint32_t)((Arg2) & (0xFFFULL));
    Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)(Arg1)));
    *(uint32_t *)(v_stack_m68) = (uint32_t)(Arg2);
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg2))) >> (24));
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(v_stack_mA4)))) goto loc_003F4906;
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg2))) >> (12));
    result = (uint32_t)((result) & (0xFFFULL));
    if (((uint32_t)(result)) != 0) goto loc_003F4906;
    Arg2 = (uint32_t)((Arg2) & (0xFFFULL));
    if (((uint32_t)(Arg2)) != ((uint32_t)(local_rsi))) goto loc_003F4906;
    local_rdi = (uint32_t)((0) + ((uint32_t)(0 + local_rsi * 1)));
    if (((uint32_t)(local_rdi)) > (*(uint32_t *)(v_stack_mA8 + 0x8))) goto loc_003F4C92;
    if (((uint32_t)(local_rdi)) != (*(uint32_t *)(v_stack_mA8 + 0x8))) goto loc_003F4C8B;
    Arg3 = (uint32_t)(((uint32_t)(v_stack_mA4)) + 1);
    v_stack_mA4 = (uint32_t)(Arg3);
    local_rsi = 0;
    if (((uint32_t)(Arg3)) >= ((uint32_t)((uint32_t)((uint32_t)(Arg2))))) goto loc_003F477F;
    local_r15 = (v_stack_mA8) + (16);
    result = ((uint32_t)((uint32_t)(Arg2))) << (4);
    result = (result) + (v_stack_mA8);
    if (local_r15 >= result) goto loc_003F4C92;
    if ((uint32_t)((uint32_t)(v_stack_mA0)) != 0) goto loc_003F4B1F;
loc_003F4772:
    v_stack_mA0 = 0;
    if (0 == (*(uint32_t *)(local_r15 + 0x8))) goto loc_003F4C5F;
loc_003F477F:
loc_003F4787:
    result = (uint32_t)(((uint32_t)(v_stack_m9C)) + 1);
    local_r14 = (local_r11 + *(uint16_t *)(v_stack_m60 + 0x4) * 4) + (4);
    Arg1 = (v_stack_m68) + (4);
    v_stack_m68 = Arg1;
    goto loc_003F465D;
loc_003F47A0:
    if (v_stack_mA0 != 0) goto loc_003F4906;
    v_stack_m90 = v_stack_m78 + *(uint16_t *)(v_stack_m60 + 0x4) * 4;
    Arg1 = (*(uint16_t *)(arg6 + 0x28)) + (Arg6);
    v_stack_mA7 = 0;
    local_r11 = 0;
    v_stack_mA8 = 0;
    v_stack_mA5 = 1;
loc_003F47DD:
    v_stack_mA4 = 0;
    if (0 >= ((uint32_t)(*(uint16_t *)(v_stack_m60 + 0xA)))) goto loc_003F48C3;
    local_r14 = 0;
    result = 0;
loc_003F4810:
    result = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(arg1 + *(uint16_t *)(v_stack_m60 + 0x8) * 4)))) >> (2));
    result = (uint32_t)((result) & (63));
    if (0 >= ((uint32_t)(result))) goto loc_003F488A;
    Arg2 = (uint32_t)((*(uint8_t *)(v_stack_m78 + *(uint16_t *)(v_stack_m60 + 0x4) * 4 + *(uint16_t *)(arg6 + 0x38 + *(uint16_t *)(arg1 + *(uint16_t *)(v_stack_m60 + 0x8) * 4 + 0x2) + *(uint16_t *)(arg1 + *(uint16_t *)(v_stack_m60 + 0x8) * 4 + 0x2) * 2 * 8) * 4)) & (15));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m98 + *(uint16_t *)(arg6 + 0x38 + *(uint16_t *)(arg1 + *(uint16_t *)(v_stack_m60 + 0x8) * 4 + 0x2) + *(uint16_t *)(arg1 + *(uint16_t *)(v_stack_m60 + 0x8) * 4 + 0x2) * 2 * 8) * 4))))) & (0xFFFULL));
    result = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m98 + *(uint16_t *)(arg6 + 0x38 + *(uint16_t *)(arg1 + *(uint16_t *)(v_stack_m60 + 0x8) * 4 + 0x2) + *(uint16_t *)(arg1 + *(uint16_t *)(v_stack_m60 + 0x8) * 4 + 0x2) * 2 * 8) * 4))))) >> (24);
    result = (result) + (result);
    Arg4 = ((uint32_t)(*(uint32_t *)(v_stack_m98 + *(uint16_t *)(arg6 + 0x38 + *(uint16_t *)(arg1 + *(uint16_t *)(v_stack_m60 + 0x8) * 4 + 0x2) + *(uint16_t *)(arg1 + *(uint16_t *)(v_stack_m60 + 0x8) * 4 + 0x2) * 2 * 8) * 4))) >> (12);
    Arg4 = (uint32_t)((Arg4) & (0xFFFULL));
    Arg4 = (Arg4) + (*(uint64_t *)(v_stack_mA8 + result * 8));
    v_stack_mB0 = v_stack_mA6;
    v_stack_mB8 = (uint32_t)(Arg1);
    result = EtwpApplyPredicate(Arg6, Arg2, Arg6 + 56 + *(uint16_t *)(arg1 + *(uint16_t *)(v_stack_m60 + 0x8) * 4 + 0x2) + *(uint16_t *)(arg1 + *(uint16_t *)(v_stack_m60 + 0x8) * 4 + 0x2) * 2 * 8, Arg4);
    if ((uint8_t)(result) == 0) goto loc_003F4915;
    local_rsi = (uint8_t)((1) & (v_stack_mA6));
    local_r14 = (uint8_t)((local_r14) | (v_stack_mA6));
    local_rbx = (uint32_t)((0) + 1);
    local_rdi = (Arg6 + 56 + *(uint16_t *)(arg1 + *(uint16_t *)(v_stack_m60 + 0x8) * 4 + 0x2) + *(uint16_t *)(arg1 + *(uint16_t *)(v_stack_m60 + 0x8) * 4 + 0x2) * 2 * 8) + (24);
    goto loc_003F4810;
loc_003F488A:
    Arg2 = (uint8_t)(local_r14);
    if ((((uint8_t)(Arg6)) & (2)) == 0) { Arg2 = (uint32_t)((uint8_t)(local_rsi)); }
    if ((((uint8_t)(Arg6)) & (1)) != 0) goto loc_003F49EE;
    local_r11 = (uint8_t)((v_stack_mA8) | ((uint8_t)(Arg2)));
    v_stack_mA8 = (uint8_t)(local_r11);
    if (condition_is_not_equal) goto loc_003F48C3;
    local_r10 = (uint32_t)(((uint32_t)(v_stack_mA4)) + 1);
    local_r15 = (Arg1 + *(uint16_t *)(v_stack_m60 + 0x8) * 4) + (4);
    goto loc_003F47DD;
loc_003F48C3:
    local_r11 = (uint8_t)((local_r11) | (v_stack_mA7));
    *(uint8_t *)(arg7) = (uint8_t)(local_r11);
    result = 0;
loc_003F48D3:
    Arg1 = (v_stack_m30) ^ (v_stack_mA8);
    result = _security_check_cookie(Arg1, Arg2, v_stack_m90, v_stack_m98);
    return result;
loc_003F4906:
    goto loc_003F48D3;
loc_003F490D:
    if ((((uint8_t)(*(uint8_t *)(local_r14))) & (16)) == 0) goto loc_003F4988;
loc_003F4915:
    goto loc_003F48D3;
loc_003F491C:
    *(uint8_t *)(arg7) = 1;
    result = 0;
    goto loc_003F48D3;
loc_003F492A:
    goto loc_003F462E;
loc_003F4932:
    if (((uint16_t)(*(uint8_t *)(local_r11 + 0x3))) >= (*(uint16_t *)(local_r11 + 0x6))) goto loc_003F4C55;
    local_r11 = (local_r11) + (12);
    Arg3 = (uint32_t)((v_stack_m90) + 1);
    goto loc_003F44A8;
loc_003F494E:
    if ((uint16_t)(Arg2) != 0) goto loc_003F4915;
    *(uint8_t *)(local_r10 + 0x3) = (uint8_t)(Arg3);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_p18))) & (0xFFFULL));
    Arg1 = (uint32_t)((Arg1) << (12));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r10))) & (0xFF000FFFULL));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)(result)));
    Arg1 = (uint32_t)((Arg1) & (0xFFFFF000ULL));
    *(uint32_t *)(local_r10) = (uint32_t)(Arg1);
    goto loc_003F4787;
loc_003F497E:
    goto loc_003F48D3;
loc_003F4988:
    if (((uint32_t)(v_stack_m68)) != 1) goto loc_003F4915;
    result = (uint8_t)(((uint32_t)(0xC000009AULL)) & (15));
    if (((uint8_t)(result)) == 4) goto loc_003F4A0F;
    if (((uint8_t)(result)) != 3) goto loc_003F4BE2;
    if (((uint32_t)(v_stack_p18)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(local_r15 + 0x8))))) goto loc_003F4C55;
    result = ((uint32_t)((uint32_t)(v_stack_p18))) + (*(uint64_t *)(local_r15));
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r15 + 0x8))) - ((uint32_t)(v_stack_p18)));
loc_003F49B4:
    if (((uint32_t)((uint32_t)((uint32_t)(local_r10)))) >= ((uint32_t)(Arg2))) goto loc_003F49CF;
    if ((*(uint8_t *)(result)) == 0) goto loc_003F49CF;
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(local_r10))) + 1);
    v_stack_m50 = (uint32_t)(local_rsi);
    result = (result) + 1;
    v_stack_m40 = result;
    goto loc_003F49B4;
loc_003F49CF:
    goto loc_003F49DB;
loc_003F49DB:
    if (((uint32_t)(local_rsi)) == ((uint32_t)(Arg2))) goto loc_003F4C2A;
    goto loc_003F46BC;
loc_003F49EE:
    if (v_stack_mA5 == 0) goto loc_003F4A73;
    v_stack_mA7 = (uint8_t)(Arg2);
    v_stack_mA5 = 0;
    local_r10 = (uint32_t)(((uint32_t)(v_stack_mA4)) + 1);
    local_r15 = (local_r15) + (4);
    goto loc_003F47DD;
loc_003F4A0F:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r15 + 0x8))) - ((uint32_t)(v_stack_p18)));
    if (((uint32_t)(result)) < 2) goto loc_003F4C55;
    Arg2 = ((uint32_t)((uint32_t)(v_stack_p18))) + (*(uint64_t *)(local_r15));
    result = (uint32_t)((result) >> (1));
loc_003F4A2B:
    if (((uint32_t)((uint32_t)((uint32_t)(local_r10)))) >= ((uint32_t)(result))) goto loc_003F4A48;
    if ((*(uint16_t *)(Arg2)) == 0) goto loc_003F4A48;
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(local_r10))) + 1);
    v_stack_m50 = (uint32_t)(local_rsi);
    Arg2 = (Arg2) + (2);
    v_stack_m38 = Arg2;
    goto loc_003F4A2B;
loc_003F4A48:
    goto loc_003F4A54;
loc_003F4A54:
    if (((uint32_t)(local_rsi)) != ((uint32_t)(result))) goto loc_003F4C39;
    v_stack_mA0 = 2;
loc_003F4A66:
    if (((uint32_t)(local_rsi)) == ((uint32_t)(result))) goto loc_003F4C44;
loc_003F4A6C:
    local_rsi = (uint32_t)((local_rsi) + ((uint32_t)(local_rsi)));
    goto loc_003F46BC;
loc_003F4A73:
    local_r10 = (uint32_t)(((uint32_t)(v_stack_mA4)) + 1);
    local_r15 = (local_r15) + (4);
    goto loc_003F47DD;
loc_003F4A8A:
    if (((uint32_t)(v_stack_m68)) >= v_stack_m9C) goto loc_003F4915;
    result = (uint8_t)(((uint8_t)(*(uint8_t *)(v_stack_m68 * 4 + local_r11 * 1))) & (15));
    result = (uint8_t)((result) - 1);
    if (((uint8_t)(result)) > 1) goto loc_003F4915;
    if ((((uint8_t)(*(uint8_t *)(v_stack_m68 * 4 + local_r11 * 1))) & (48)) != 0) goto loc_003F4915;
    if ((*(uint16_t *)(v_stack_m68 * 4 + local_r11 * 1 + 0x2)) > 8) goto loc_003F4915;
    if ((*(uint8_t *)(v_stack_m68 * 4 + local_r11 * 1 + 0x1)) != 1) goto loc_003F4915;
    result = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m68 * 4 + (uint32_t)((uint32_t)(local_r10)) * 1))))) >> (24);
    result = (result) + (result);
    Arg1 = ((uint32_t)(*(uint32_t *)(v_stack_m68 * 4 + (uint32_t)((uint32_t)(local_r10)) * 1))) >> (12);
    Arg1 = (uint32_t)((Arg1) & (0xFFFULL));
    Arg1 = (Arg1) + (*(uint64_t *)(local_r15 + result * 8));
    result = EtwpGetFieldValue(Arg1, *(uint16_t *)(v_stack_m68 * 4 + local_r11 * 1 + 0x2), v_stack_m80, (uint32_t)((uint32_t)(local_r10)));
    if ((uint8_t)(result) == 0) goto loc_003F4915;
    v_stack_m90 = v_stack_m80;
    if (((uint32_t)((uint32_t)(v_stack_m80))) == v_stack_m80) goto loc_003F46AE;
    goto loc_003F4915;
loc_003F4B1F:
    if ((*(uint32_t *)(local_r15 + 0x8)) < ((uint32_t)(*(uint16_t *)(v_stack_m68 * 4 + local_r11 * 1 + 0x2)))) goto loc_003F4906;
    goto loc_003F4772;
loc_003F4B30:
    local_rsi = 8;
    if (Arg5 == 0) { local_rsi = 4; }
    goto loc_003F4692;
loc_003F4B49:
    if (((uint32_t)(local_rsi)) >= v_stack_m9C) goto loc_003F4915;
    result = (uint8_t)(((uint8_t)(*(uint8_t *)(local_rsi * 4 + local_r11 * 1))) & (15));
    result = (uint8_t)((result) - 1);
    if (((uint8_t)(result)) > 1) goto loc_003F4915;
    if ((((uint8_t)(*(uint8_t *)(local_rsi * 4 + local_r11 * 1))) & (48)) != 0) goto loc_003F4915;
    if ((*(uint16_t *)(local_rsi * 4 + local_r11 * 1 + 0x2)) > 8) goto loc_003F4915;
    if ((*(uint8_t *)(local_rsi * 4 + local_r11 * 1 + 0x1)) != 1) goto loc_003F4915;
    result = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi * 4 + (uint32_t)((uint32_t)(local_r10)) * 1))))) >> (24);
    result = (result) + (result);
    Arg1 = ((uint32_t)(*(uint32_t *)(local_rsi * 4 + (uint32_t)((uint32_t)(local_r10)) * 1))) >> (12);
    Arg1 = (uint32_t)((Arg1) & (0xFFFULL));
    Arg1 = (Arg1) + (*(uint64_t *)(local_r15 + result * 8));
    result = EtwpGetFieldValue(Arg1, *(uint16_t *)(local_rsi * 4 + local_r11 * 1 + 0x2), v_stack_m80, (uint32_t)((uint32_t)(local_r10)));
    if ((uint8_t)(result) == 0) goto loc_003F4915;
    if (((uint32_t)((uint32_t)(v_stack_m80))) != v_stack_m80) goto loc_003F4915;
    goto loc_003F469B;
loc_003F4BE2:
    if (((uint8_t)((uint32_t)((uint32_t)(v_stack_m80)))) != 6) goto loc_003F4915;
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint16_t *)(v_stack_m68 * 4 + local_r11 * 1 + 0x2)))))) + 1;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r15 + 0x8))) - ((uint32_t)((uint32_t)((uint32_t)(*(uint16_t *)(v_stack_m68 * 4 + local_r11 * 1 + 0x2))))));
    if (((uint32_t)(result)) < 2) goto loc_003F4C55;
    Arg1 = (Arg1) + (*(uint64_t *)(local_r15));
    result = EtwpGetFieldValue(Arg1, 1, v_stack_m80, v_stack_m98);
    if ((uint8_t)(result) == 0) goto loc_003F4C55;
    result = RtlLengthRequiredSid((uint32_t)(v_stack_m80), 1, v_stack_m80, v_stack_m98);
    if (((uint32_t)(result)) == -1) goto loc_003F4C55;
    Arg4 = 0;
    goto loc_003F46BC;
loc_003F4C2A:
    v_stack_mA0 = 1;
    goto loc_003F46BC;
loc_003F4C39:
    goto loc_003F4A66;
loc_003F4C44:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint16_t *)(v_stack_m68 * 4 + local_r11 * 1 + 0x2))))) + (uint32_t)((uint32_t)(result)) * 2) == ((uint32_t)(*(uint32_t *)(local_r15 + 0x8)))) goto loc_003F4C82;
loc_003F4C55:
    goto loc_003F48D3;
loc_003F4C5F:
    Arg3 = (uint32_t)((v_stack_m80) + 1);
    v_stack_mA4 = (uint32_t)(Arg3);
    if (((uint32_t)(Arg3)) >= ((uint32_t)(v_stack_m60))) goto loc_003F4787;
    local_r15 = (local_r15) + (16);
    goto loc_003F4787;
loc_003F4C82:
    goto loc_003F4A6C;
loc_003F4C8B:
    local_rsi = 0;
    goto loc_003F477F;
loc_003F4C92:
    goto loc_003F48D3;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `16` | `R` |
| `Arg1` | `+ 0x2` | `8` | `R` |
| `Arg6` | `+ 0x0` | `16` | `R` |
| `Arg6` | `+ 0x0 + rcx*8` | `64` | `R` |
| `Arg6` | `+ 0x8` | `64` | `R` |
| `Arg6` | `+ 0x20` | `16` | `R` |
| `Arg6` | `+ 0x22` | `16` | `R` |
| `Arg6` | `+ 0x24` | `16` | `R` |
| `Arg6` | `+ 0x28` | `16` | `R` |
| `Arg6` | `+ 0x38` | `64` | `R` |
| `Arg7` | `+ 0x0` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003F43D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
