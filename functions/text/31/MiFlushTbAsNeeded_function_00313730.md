# MiFlushTbAsNeeded

- RVA: `0x00313730`–`0x00313C69` (길이 `1,337` bytes)
- VA: `0x0000000140313730`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00074620`
- 디코드: `323`개 명령, `1,337/1,337` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **10**; 고유 호출 대상: **10**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00313777` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00313790` → [MiGetProcessorFlushList](../24/MiGetProcessorFlushList_function_00242C90.md) (function, `0x00242C90`)
- `0x003138A7` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00313971` → [MiFlushTbList](MiFlushTbList_function_00311FC0.md) (function, `0x00311FC0`)
- `0x00313980` → [MiReleaseProcessorFlushList](MiReleaseProcessorFlushList_function_00313C70.md) (function, `0x00313C70`)
- `0x00313990` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00313A48` → [MiCompareTbFlushTimeStamp](MiCompareTbFlushTimeStamp_function_0031ADE4.md) (function, `0x0031ADE4`)
- `0x00313A7E` → [MiInsertTbFlushEntry](../29/MiInsertTbFlushEntry_function_00293670.md) (function, `0x00293670`)
- `0x00313BC7` → [qsort](../50/qsort_function_005009F0.md) (function, `0x005009F0`)
- `0x00313BCF` → [MiCompressTbFlushList](../2A/MiCompressTbFlushList_function_002A93A8.md) (function, `0x002A93A8`)

### Direct callers
- [MiLinkPoolCommitChain](MiLinkPoolCommitChain_function_00313D20.md) at `0x00313D7E`

### Static image references
- `0x00313747` → RVA `0x00E0A740` (`.data`; read)
- `0x00313849` → RVA `0x00E2DC80` (`.data`; read)
- `0x00313860` → RVA `0x00010880` (`.rdata`; read)
- `0x00313BBA` → RVA `0x00695890` (`MiTbFlushSort`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00313730  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00313735  55                              push rbp
00313736  56                              push rsi
00313737  57                              push rdi
00313738  41 54                           push r12
0031373A  41 55                           push r13
0031373C  41 56                           push r14
0031373E  41 57                           push r15
00313740  48 81 EC 20 01 00 00            sub rsp, 0x120
00313747  48 8B 05 F2 6F AF 00            mov rax, qword ptr [rip + 0xaf6ff2]
0031374E  48 33 C4                        xor rax, rsp
00313751  48 89 84 24 10 01 00 00         mov qword ptr [rsp + 0x110], rax
00313759  49 8B E8                        mov rbp, r8
0031375C  44 89 4C 24 34                  mov dword ptr [rsp + 0x34], r9d
00313761  48 8B FA                        mov rdi, rdx
00313764  48 8B D9                        mov rbx, rcx
00313767  33 D2                           xor edx, edx
00313769  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
0031376E  41 B8 C8 00 00 00               mov r8d, 0xc8
00313774  45 8B F9                        mov r15d, r9d
00313777  E8 C4 34 3B 00                  call 0x1406c6c40
0031377C  45 33 F6                        xor r14d, r14d
0031377F  45 33 ED                        xor r13d, r13d
00313782  44 89 74 24 30                  mov dword ptr [rsp + 0x30], r14d
00313787  45 85 FF                        test r15d, r15d
0031378A  0F 84 21 02 00 00               je 0x1403139b1
00313790  E8 FB F4 F2 FF                  call 0x140242c90
00313795  BA 01 00 00 00                  mov edx, 1
0031379A  4C 8B E0                        mov r12, rax
0031379D  44 89 68 10                     mov dword ptr [rax + 0x10], r13d
003137A1  89 50 14                        mov dword ptr [rax + 0x14], edx
003137A4  48 89 18                        mov qword ptr [rax], rbx
003137A7  8B 8B B8 00 00 00               mov ecx, dword ptr [rbx + 0xb8]
003137AD  C1 E9 08                        shr ecx, 8
003137B0  C0 E9 03                        shr cl, 3
003137B3  22 CA                           and cl, dl
003137B5  88 48 18                        mov byte ptr [rax + 0x18], cl
003137B8  8B 83 B8 00 00 00               mov eax, dword ptr [rbx + 0xb8]
003137BE  A8 0F                           test al, 0xf
003137C0  75 20                           jne 0x1403137e2
003137C2  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
003137CB  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
003137D2  48 81 C1 00 04 00 00            add rcx, 0x400
003137D9  48 3B D9                        cmp rbx, rcx
003137DC  0F 85 47 04 00 00               jne 0x140313c29
003137E2  8B 83 B8 00 00 00               mov eax, dword ptr [rbx + 0xb8]
003137E8  33 C9                           xor ecx, ecx
003137EA  A8 0F                           test al, 0xf
003137EC  0F 44 CA                        cmove ecx, edx
003137EF  41 83 64 24 10 DB               and dword ptr [r12 + 0x10], 0xffffffdb
003137F5  41 89 4C 24 08                  mov dword ptr [r12 + 8], ecx
003137FA  66 45 89 6C 24 19               mov word ptr [r12 + 0x19], r13w
00313800  45 89 6C 24 1C                  mov dword ptr [r12 + 0x1c], r13d
00313805  4D 89 6C 24 20                  mov qword ptr [r12 + 0x20], r13
0031380A  4D 89 6C 24 28                  mov qword ptr [r12 + 0x28], r13
0031380F  33 F6                           xor esi, esi
00313811  49 B9 FF FF FF FF FF F6 FF FF   movabs r9, 0xfffff6ffffffffff
0031381B  49 B8 00 00 00 00 80 F6 FF FF   movabs r8, 0xfffff68000000000
00313825  48 3B F5                        cmp rsi, rbp
00313828  0F 83 40 01 00 00               jae 0x14031396e
0031382E  48 8B 1F                        mov rbx, qword ptr [rdi]
00313831  48 F7 C3 01 0C 00 00            test rbx, 0xc01
00313838  0F 94 C1                        sete cl
0031383B  48 F7 C3 E0 03 00 00            test rbx, 0x3e0
00313842  0F 94 C0                        sete al
00313845  84 C8                           test al, cl
00313847  74 42                           je 0x14031388b
00313849  48 8B 05 30 A4 B1 00            mov rax, qword ptr [rip + 0xb1a430]
00313850  48 85 C0                        test rax, rax
00313853  74 0B                           je 0x140313860
00313855  F6 C3 10                        test bl, 0x10
00313858  75 53                           jne 0x1403138ad
0031385A  48 F7 D0                        not rax
0031385D  48 23 D8                        and rbx, rax
00313860  48 8B 05 19 D0 CF FF            mov rax, qword ptr [rip - 0x302fe7]
00313867  48 C1 EB 20                     shr rbx, 0x20
0031386B  48 89 07                        mov qword ptr [rdi], rax
0031386E  85 DB                           test ebx, ebx
00313870  75 41                           jne 0x1403138b3
00313872  45 33 F6                        xor r14d, r14d
00313875  44 89 74 24 30                  mov dword ptr [rsp + 0x30], r14d
0031387A  45 33 ED                        xor r13d, r13d
0031387D  48 FF C6                        inc rsi
00313880  BA 01 00 00 00                  mov edx, 1
00313885  48 83 C7 08                     add rdi, 8
00313889  EB 90                           jmp 0x14031381b
0031388B  45 85 FF                        test r15d, r15d
0031388E  75 ED                           jne 0x14031387d
00313890  48 2B EE                        sub rbp, rsi
00313893  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00313898  4C 8B CD                        mov r9, rbp
0031389B  41 8D 4F 1A                     lea ecx, [r15 + 0x1a]
0031389F  4C 8B C7                        mov r8, rdi
003138A2  BA 00 51 00 00                  mov edx, 0x5100
003138A7  E8 B4 9D 1E 00                  call 0x1404fd660
003138AC  CC                              int3
003138AD  48 83 E3 EF                     and rbx, 0xffffffffffffffef
003138B1  EB AD                           jmp 0x140313860
003138B3  41 3B DD                        cmp ebx, r13d
003138B6  0F 85 8A 01 00 00               jne 0x140313a46
003138BC  45 85 F6                        test r14d, r14d
003138BF  74 BC                           je 0x14031387d
003138C1  48 8B DF                        mov rbx, rdi
003138C4  4C 8B F2                        mov r14, rdx
003138C7  48 C1 E3 19                     shl rbx, 0x19
003138CB  49 8B C0                        mov rax, r8
003138CE  48 C1 E0 19                     shl rax, 0x19
003138D2  48 2B D8                        sub rbx, rax
003138D5  48 C1 FB 10                     sar rbx, 0x10
003138D9  41 83 7C 24 08 01               cmp dword ptr [r12 + 8], 1
003138DF  0F 85 92 02 00 00               jne 0x140313b77
003138E5  45 33 FF                        xor r15d, r15d
003138E8  45 8B 4C 24 1C                  mov r9d, dword ptr [r12 + 0x1c]
003138ED  45 85 C9                        test r9d, r9d
003138F0  0F 84 F1 01 00 00               je 0x140313ae7
003138F6  41 8B 44 24 10                  mov eax, dword ptr [r12 + 0x10]
003138FB  A8 02                           test al, 2
003138FD  0F 85 9D 01 00 00               jne 0x140313aa0
00313903  41 8D 41 FF                     lea eax, [r9 - 1]
00313907  4D 8D 14 C4                     lea r10, [r12 + rax*8]
0031390B  49 8B 44 C4 28                  mov rax, qword ptr [r12 + rax*8 + 0x28]
00313910  48 A9 00 0C 00 00               test rax, 0xc00
00313916  0F 85 CB 01 00 00               jne 0x140313ae7
0031391C  4C 8B C0                        mov r8, rax
0031391F  48 8B C8                        mov rcx, rax
00313922  41 81 E0 FF 03 00 00            and r8d, 0x3ff
00313929  48 81 E1 00 F0 FF FF            and rcx, 0xfffffffffffff000
00313930  49 8D 50 01                     lea rdx, [r8 + 1]
00313934  48 C1 E2 0C                     shl rdx, 0xc
00313938  48 03 D1                        add rdx, rcx
0031393B  48 3B D3                        cmp rdx, rbx
0031393E  75 16                           jne 0x140313956
00313940  4B 8D 0C 30                     lea rcx, [r8 + r14]
00313944  49 3B C8                        cmp rcx, r8
00313947  76 0D                           jbe 0x140313956
00313949  48 81 F9 FF 03 00 00            cmp rcx, 0x3ff
00313950  0F 86 EA 02 00 00               jbe 0x140313c40
00313956  41 8D 49 FF                     lea ecx, [r9 - 1]
0031395A  48 8D 49 05                     lea rcx, [rcx + 5]
0031395E  49 8B 04 CC                     mov rax, qword ptr [r12 + rcx*8]
00313962  4D 8D 14 CC                     lea r10, [r12 + rcx*8]
00313966  48 8B C8                        mov rcx, rax
00313969  E9 5B 01 00 00                  jmp 0x140313ac9
0031396E  49 8B CC                        mov rcx, r12
00313971  E8 4A E6 FF FF                  call 0x140311fc0
00313976  48 8D 44 24 40                  lea rax, [rsp + 0x40]
0031397B  4C 3B E0                        cmp r12, rax
0031397E  74 05                           je 0x140313985
00313980  E8 EB 02 00 00                  call 0x140313c70
00313985  48 8B 8C 24 10 01 00 00         mov rcx, qword ptr [rsp + 0x110]
0031398D  48 33 CC                        xor rcx, rsp
00313990  E8 AB 8C 39 00                  call 0x1406ac640
00313995  48 8B 9C 24 60 01 00 00         mov rbx, qword ptr [rsp + 0x160]
0031399D  48 81 C4 20 01 00 00            add rsp, 0x120
003139A4  41 5F                           pop r15
003139A6  41 5E                           pop r14
003139A8  41 5D                           pop r13
003139AA  41 5C                           pop r12
003139AC  5F                              pop rdi
003139AD  5E                              pop rsi
003139AE  5D                              pop rbp
003139AF  C3                              ret
003139B0  CC                              int3
003139B1  8B 83 B8 00 00 00               mov eax, dword ptr [rbx + 0xb8]
003139B7  4C 8D 64 24 40                  lea r12, [rsp + 0x40]
003139BC  C1 E8 08                        shr eax, 8
003139BF  BA 01 00 00 00                  mov edx, 1
003139C4  C0 E8 03                        shr al, 3
003139C7  22 C2                           and al, dl
003139C9  C7 44 24 4C 14 00 00 00         mov dword ptr [rsp + 0x4c], 0x14
003139D1  88 44 24 58                     mov byte ptr [rsp + 0x58], al
003139D5  8B 83 B8 00 00 00               mov eax, dword ptr [rbx + 0xb8]
003139DB  C7 44 24 50 08 00 00 00         mov dword ptr [rsp + 0x50], 8
003139E3  89 54 24 54                     mov dword ptr [rsp + 0x54], edx
003139E7  48 89 5C 24 40                  mov qword ptr [rsp + 0x40], rbx
003139EC  A8 0F                           test al, 0xf
003139EE  75 20                           jne 0x140313a10
003139F0  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
003139F9  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00313A00  48 81 C1 00 04 00 00            add rcx, 0x400
00313A07  48 3B D9                        cmp rbx, rcx
00313A0A  0F 85 26 02 00 00               jne 0x140313c36
00313A10  8B 83 B8 00 00 00               mov eax, dword ptr [rbx + 0xb8]
00313A16  33 C9                           xor ecx, ecx
00313A18  A8 0F                           test al, 0xf
00313A1A  8B 44 24 50                     mov eax, dword ptr [rsp + 0x50]
00313A1E  0F 44 CA                        cmove ecx, edx
00313A21  83 E0 DB                        and eax, 0xffffffdb
00313A24  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
00313A28  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00313A2C  66 44 89 6C 24 59               mov word ptr [rsp + 0x59], r13w
00313A32  44 89 6C 24 5C                  mov dword ptr [rsp + 0x5c], r13d
00313A37  4C 89 6C 24 60                  mov qword ptr [rsp + 0x60], r13
00313A3C  4C 89 6C 24 68                  mov qword ptr [rsp + 0x68], r13
00313A41  E9 C9 FD FF FF                  jmp 0x14031380f
00313A46  8B CB                           mov ecx, ebx
00313A48  E8 97 73 00 00                  call 0x14031ade4
00313A4D  84 C0                           test al, al
00313A4F  0F 84 FA 00 00 00               je 0x140313b4f
00313A55  48 8B D7                        mov rdx, rdi
00313A58  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00313A62  48 C1 E2 19                     shl rdx, 0x19
00313A66  48 8B C0                        mov rax, rax
00313A69  45 33 C9                        xor r9d, r9d
00313A6C  48 C1 E0 19                     shl rax, 0x19
00313A70  48 2B D0                        sub rdx, rax
00313A73  49 8B CC                        mov rcx, r12
00313A76  48 C1 FA 10                     sar rdx, 0x10
00313A7A  45 8D 41 01                     lea r8d, [r9 + 1]
00313A7E  E8 ED FB F7 FF                  call 0x140293670
00313A83  41 BE 01 00 00 00               mov r14d, 1
00313A89  44 89 74 24 30                  mov dword ptr [rsp + 0x30], r14d
00313A8E  44 8B EB                        mov r13d, ebx
00313A91  49 B9 FF FF FF FF FF F6 FF FF   movabs r9, 0xfffff6ffffffffff
00313A9B  E9 DD FD FF FF                  jmp 0x14031387d
00313AA0  45 85 C9                        test r9d, r9d
00313AA3  74 42                           je 0x140313ae7
00313AA5  41 8B 44 24 10                  mov eax, dword ptr [r12 + 0x10]
00313AAA  A8 02                           test al, 2
00313AAC  75 39                           jne 0x140313ae7
00313AAE  41 8D 49 FF                     lea ecx, [r9 - 1]
00313AB2  48 8D 49 05                     lea rcx, [rcx + 5]
00313AB6  49 8B 04 CC                     mov rax, qword ptr [r12 + rcx*8]
00313ABA  4D 8D 14 CC                     lea r10, [r12 + rcx*8]
00313ABE  48 8B C8                        mov rcx, rax
00313AC1  48 A9 00 0C 00 00               test rax, 0xc00
00313AC7  75 1E                           jne 0x140313ae7
00313AC9  4D 8B DE                        mov r11, r14
00313ACC  48 8B D1                        mov rdx, rcx
00313ACF  49 C1 E3 0C                     shl r11, 0xc
00313AD3  48 81 E2 00 F0 FF FF            and rdx, 0xfffffffffffff000
00313ADA  4E 8D 04 1B                     lea r8, [rbx + r11]
00313ADE  49 3B D0                        cmp rdx, r8
00313AE1  0F 84 F8 00 00 00               je 0x140313bdf
00313AE7  45 3B 4C 24 0C                  cmp r9d, dword ptr [r12 + 0xc]
00313AEC  74 69                           je 0x140313b57
00313AEE  4D 85 F6                        test r14, r14
00313AF1  74 75                           je 0x140313b68
00313AF3  49 8D 46 FF                     lea rax, [r14 - 1]
00313AF7  48 8B CB                        mov rcx, rbx
00313AFA  48 3D FF 03 00 00               cmp rax, 0x3ff
00313B00  BA 00 04 00 00                  mov edx, 0x400
00313B05  49 0F 46 D6                     cmovbe rdx, r14
00313B09  48 81 E1 00 F0 FF FF            and rcx, 0xfffffffffffff000
00313B10  48 8D 42 FF                     lea rax, [rdx - 1]
00313B14  25 FF 03 00 00                  and eax, 0x3ff
00313B19  48 0B C1                        or rax, rcx
00313B1C  48 8B CA                        mov rcx, rdx
00313B1F  4B 89 44 CC 28                  mov qword ptr [r12 + r9*8 + 0x28], rax
00313B24  45 8B 4C 24 1C                  mov r9d, dword ptr [r12 + 0x1c]
00313B29  49 01 54 24 20                  add qword ptr [r12 + 0x20], rdx
00313B2E  41 FF C1                        inc r9d
00313B31  48 C1 E1 0C                     shl rcx, 0xc
00313B35  48 03 D9                        add rbx, rcx
00313B38  45 89 4C 24 1C                  mov dword ptr [r12 + 0x1c], r9d
00313B3D  4C 2B F2                        sub r14, rdx
00313B40  74 AC                           je 0x140313aee
00313B42  45 3B 4C 24 0C                  cmp r9d, dword ptr [r12 + 0xc]
00313B47  0F 84 98 FD FF FF               je 0x1403138e5
00313B4D  EB 9F                           jmp 0x140313aee
00313B4F  45 33 F6                        xor r14d, r14d
00313B52  E9 32 FF FF FF                  jmp 0x140313a89
00313B57  45 85 FF                        test r15d, r15d
00313B5A  74 4E                           je 0x140313baa
00313B5C  41 80 7C 24 19 00               cmp byte ptr [r12 + 0x19], 0
00313B62  0F 84 F6 00 00 00               je 0x140313c5e
00313B68  44 8B 74 24 30                  mov r14d, dword ptr [rsp + 0x30]
00313B6D  44 8B 7C 24 34                  mov r15d, dword ptr [rsp + 0x34]
00313B72  E9 1A FF FF FF                  jmp 0x140313a91
00313B77  41 8B 4C 24 10                  mov ecx, dword ptr [r12 + 0x10]
00313B7C  F6 C1 04                        test cl, 4
00313B7F  0F 85 60 FD FF FF               jne 0x1403138e5
00313B85  49 8B C0                        mov rax, r8
00313B88  48 3B D8                        cmp rbx, rax
00313B8B  0F 82 54 FD FF FF               jb 0x1403138e5
00313B91  49 8B C1                        mov rax, r9
00313B94  48 3B D8                        cmp rbx, rax
00313B97  0F 87 48 FD FF FF               ja 0x1403138e5
00313B9D  83 C9 04                        or ecx, 4
00313BA0  41 89 4C 24 10                  mov dword ptr [r12 + 0x10], ecx
00313BA5  E9 3B FD FF FF                  jmp 0x1403138e5
00313BAA  41 80 7C 24 19 00               cmp byte ptr [r12 + 0x19], 0
00313BB0  75 B6                           jne 0x140313b68
00313BB2  49 8B D1                        mov rdx, r9
00313BB5  49 8D 4C 24 28                  lea rcx, [r12 + 0x28]
00313BBA  4C 8D 0D CF 1C 38 00            lea r9, [rip + 0x381ccf]
00313BC1  41 B8 08 00 00 00               mov r8d, 8
00313BC7  E8 24 CE 1E 00                  call 0x1405009f0
00313BCC  49 8B CC                        mov rcx, r12
00313BCF  E8 D4 57 F9 FF                  call 0x1402a93a8
00313BD4  41 BF 01 00 00 00               mov r15d, 1
00313BDA  E9 09 FD FF FF                  jmp 0x1403138e8
00313BDF  81 E1 FF 03 00 00               and ecx, 0x3ff
00313BE5  49 8D 14 0E                     lea rdx, [r14 + rcx]
00313BE9  48 81 FA FF 03 00 00            cmp rdx, 0x3ff
00313BF0  0F 87 F1 FE FF FF               ja 0x140313ae7
00313BF6  48 3B D1                        cmp rdx, rcx
00313BF9  0F 86 E8 FE FF FF               jbe 0x140313ae7
00313BFF  4D 01 74 24 20                  add qword ptr [r12 + 0x20], r14
00313C04  49 2B C3                        sub rax, r11
00313C07  44 8B 7C 24 34                  mov r15d, dword ptr [rsp + 0x34]
00313C0C  4A 8D 0C 30                     lea rcx, [rax + r14]
00313C10  44 8B 74 24 30                  mov r14d, dword ptr [rsp + 0x30]
00313C15  48 33 C1                        xor rax, rcx
00313C18  48 25 00 FC FF FF               and rax, 0xfffffffffffffc00
00313C1E  48 33 C1                        xor rax, rcx
00313C21  49 89 02                        mov qword ptr [r10], rax
00313C24  E9 68 FE FF FF                  jmp 0x140313a91
00313C29  33 C9                           xor ecx, ecx
00313C2B  41 83 4C 24 10 09               or dword ptr [r12 + 0x10], 9
00313C31  E9 B9 FB FF FF                  jmp 0x1403137ef
00313C36  33 C9                           xor ecx, ecx
00313C38  8D 41 09                        lea eax, [rcx + 9]
00313C3B  E9 E1 FD FF FF                  jmp 0x140313a21
00313C40  4D 01 74 24 20                  add qword ptr [r12 + 0x20], r14
00313C45  4A 8D 0C 30                     lea rcx, [rax + r14]
00313C49  48 33 C1                        xor rax, rcx
00313C4C  48 25 00 FC FF FF               and rax, 0xfffffffffffffc00
00313C52  48 33 C1                        xor rax, rcx
00313C55  49 89 42 28                     mov qword ptr [r10 + 0x28], rax
00313C59  E9 0A FF FF FF                  jmp 0x140313b68
00313C5E  41 C6 44 24 19 01               mov byte ptr [r12 + 0x19], 1
00313C64  E9 FF FE FF FF                  jmp 0x140313b68
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiFlushTbAsNeeded(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m118;
    unsigned int v_stack_m124;
    unsigned int v_stack_m128;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_p30;
    unsigned int v_stack_p34;
    unsigned __int64 v_stack_p40;
    unsigned int v_stack_p48;
    unsigned int v_stack_p4C;
    unsigned int v_stack_p50;
    unsigned int v_stack_p54;
    unsigned __int8 v_stack_p58;
    unsigned __int16 v_stack_p59;
    unsigned int v_stack_p5C;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (288);
    result = (*(unsigned __int64 *)(v_rip + 11497458)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m124 = a4;
    a2 = 0;
    result = memset(v_stack_m118, a2, 200, a4);
    v_r14 = 0;
    v_r13 = 0;
    v_stack_m128 = 0;
    if ((unsigned int)((unsigned int)(a4)) == 0) goto loc_003139B1;
    result = MiGetProcessorFlushList(v_stack_m118, a2, 200, a4);
    *(unsigned int *)(result + 16) = 0;
    *(unsigned int *)(result + 20) = 1;
    *(unsigned __int64 *)(result) = a1;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 184))) >> (8));
    a1 = (unsigned __int8)((a1) >> (3));
    a1 = (unsigned __int8)((a1) & (1));
    *(unsigned __int8 *)(result + 24) = (unsigned __int8)(a1);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 184)))) & (15)) != 0) goto loc_003137E2;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) + (0x400ULL);
    if (a1 != a1) goto loc_00313C29;
loc_003137E2:
    a1 = 0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 184)))) & (15)) == 0) { a1 = 1; }
loc_003137EF:
    *(unsigned int *)(result + 8) = (unsigned int)(a1);
    *(unsigned __int16 *)(result + 25) = 0;
    *(unsigned int *)(result + 28) = 0;
    *(unsigned __int64 *)(result + 32) = 0;
    *(unsigned __int64 *)(result + 40) = 0;
loc_0031380F:
    v_rsi = 0;
loc_0031381B:
    if (0 >= a3) goto loc_0031396E;
    a1 = (((*(unsigned __int64 *)(a2)) & (0xC01ULL)) == 0) ? 1 : 0;
    result = (((*(unsigned __int64 *)(a2)) & (992)) == 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_0031388B;
    if (*(unsigned __int64 *)(v_rip + 11641904) == 0) goto loc_00313860;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a2))) & (16)) != 0) goto loc_003138AD;
    result = ~(*(unsigned __int64 *)(v_rip + 11641904));
    v_rbx = (*(unsigned __int64 *)(a2)) & (result);
loc_00313860:
    v_rbx = (v_rbx) >> (32);
    *(unsigned __int64 *)(a2) = *(unsigned __int64 *)(v_rip - 3157991);
    if ((unsigned int)(v_rbx) != 0) goto loc_003138B3;
    v_r14 = 0;
    v_stack_m128 = 0;
    v_r13 = 0;
loc_0031387D:
    v_rsi = (v_rsi) + 1;
    v_rdi = (a2) + (8);
    goto loc_0031381B;
loc_0031388B:
    if ((unsigned int)((unsigned int)(a4)) != 0) goto loc_0031387D;
    v_rbp = (a3) - (v_rsi);
    v_stack_m138 = v_rbx;
    result = KeBugCheckEx((unsigned int)(a4) + 26, (unsigned int)(0x5100ULL), v_rdi, v_rbp);
loc_003138AD:
    v_rbx = (v_rbx) & (-17);
    goto loc_00313860;
loc_003138B3:
    if (((unsigned int)(v_rbx)) != 0) goto loc_00313A46;
    if (0 == 0) goto loc_0031387D;
    v_rbx = (v_rdi) << (25);
    result = (v_rdi) << (25);
    v_rbx = (v_rbx) - (result);
    v_rbx = (v_rbx) >> (16);
    if ((*(unsigned int *)(result + 8)) != 1) goto loc_00313B77;
loc_003138E5:
    v_r15 = 0;
loc_003138E8:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(result + 28))) == 0) goto loc_00313AE7;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 16)))) & (2)) != 0) goto loc_00313AA0;
    if (((*(unsigned __int64 *)(result + (unsigned int)(*(unsigned int *)(result + 28)) - 1 * 8 + 40)) & (0xC00ULL)) != 0) goto loc_00313AE7;
    a3 = (unsigned int)((*(unsigned __int64 *)(result + (unsigned int)(*(unsigned int *)(result + 28)) - 1 * 8 + 40)) & (0x3FFULL));
    a1 = (*(unsigned __int64 *)(result + (unsigned int)(*(unsigned int *)(result + 28)) - 1 * 8 + 40)) & (0xFFFFFFFFFFFFF000ULL);
    a2 = (a3 + 1) << (12);
    a2 = (a2) + (a1);
    if (a2 != v_rbx) goto loc_00313956;
    if ((a3 + (unsigned int)(0x5100ULL) * 1) <= a3) goto loc_00313956;
    if ((a3 + (unsigned int)(0x5100ULL) * 1) <= 0x3FFULL) goto loc_00313C40;
loc_00313956:
    goto loc_00313AC9;
loc_0031396E:
    result = MiFlushTbList(result, a2, a3, (unsigned int)(*(unsigned int *)(result + 28)));
    result = v_stack_m118;
    if (result != v_stack_m118) {
        result = MiReleaseProcessorFlushList(result, a2, a3, (unsigned int)(*(unsigned int *)(result + 28)));
    }
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, (unsigned int)(*(unsigned int *)(result + 28)));
    v_rsp = (v_rsp) + (288);
    return result;
loc_003139B1:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p8 + 184))) >> (8));
    result = (unsigned __int8)((result) >> (3));
    result = (unsigned __int8)((result) & (1));
    v_stack_p4C = 20;
    v_stack_p58 = (unsigned __int8)(result);
    v_stack_p50 = 8;
    v_stack_p54 = 1;
    v_stack_p40 = v_stack_p8;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p8 + 184)))) & (15)) != 0) goto loc_00313A10;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) + (0x400ULL);
    if (v_stack_p8 != a1) goto loc_00313C36;
loc_00313A10:
    a1 = 0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p8 + 184)))) & (15)) == 0) { a1 = 1; }
loc_00313A21:
    result = (unsigned int)(((unsigned int)(v_stack_p50)) & (0xFFFFFFDBULL));
    v_stack_p48 = (unsigned int)(a1);
    v_stack_p50 = (unsigned int)(result);
    v_stack_p59 = 0;
    v_stack_p5C = 0;
    v_stack_p60 = 0;
    v_stack_p68 = 0;
    goto loc_0031380F;
loc_00313A46:
    result = MiCompareTbFlushTimeStamp((unsigned int)((unsigned int)(v_stack_p8)), 1, a3, (unsigned int)(*(unsigned int *)(result + 28)));
    if ((unsigned __int8)(result) == 0) goto loc_00313B4F;
    a2 = (v_rdi) << (25);
    a4 = 0;
    result = (result) << (25);
    a2 = (a2) - (result);
    a2 = (a2) >> (16);
    result = MiInsertTbFlushEntry(v_stack_p40, a2, a4 + 1, a4);
loc_00313A89:
    v_stack_p30 = 1;
loc_00313A91:
    goto loc_0031387D;
loc_00313AA0:
    if (0 == 0) goto loc_00313AE7;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p40 + 16)))) & (2)) != 0) goto loc_00313AE7;
    if (((*(unsigned __int64 *)(v_stack_p40 + a4 - 1 + 5 * 8)) & (0xC00ULL)) != 0) goto loc_00313AE7;
loc_00313AC9:
    v_r11 = (1) << (12);
    a2 = (*(unsigned __int64 *)(v_stack_p40 + a4 - 1 + 5 * 8)) & (0xFFFFFFFFFFFFF000ULL);
    if (a2 == (v_stack_p8 + v_r11 * 1)) goto loc_00313BDF;
loc_00313AE7:
    if (0 == (*(unsigned int *)(v_stack_p40 + 12))) goto loc_00313B57;
loc_00313AEE:
    if (1 == 0) goto loc_00313B68;
    a2 = (unsigned int)(0x400ULL);
    if ((1 - 1) <= 0x3FFULL) { a2 = 1; }
    a1 = (v_stack_p8) & (0xFFFFFFFFFFFFF000ULL);
    result = (unsigned int)((a2 - 1) & (0x3FFULL));
    result = (result) | (a1);
    *(unsigned __int64 *)(v_stack_p40 + a4 * 8 + 40) = result;
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p40 + 28))) + 1);
    a1 = (a2) << (12);
    v_rbx = (v_stack_p8) + (a1);
    *(unsigned int *)(v_stack_p40 + 28) = a4;
    v_r14 = (1) - (a2);
    if (condition_is_equal) goto loc_00313AEE;
    if (a4 == (*(unsigned int *)(v_stack_p40 + 12))) goto loc_003138E5;
    goto loc_00313AEE;
loc_00313B4F:
    v_r14 = 0;
    goto loc_00313A89;
loc_00313B57:
    if (0 == 0) goto loc_00313BAA;
    if ((*(unsigned __int8 *)(v_stack_p40 + 25)) == 0) goto loc_00313C5E;
loc_00313B68:
    goto loc_00313A91;
loc_00313B77:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p40 + 16)))) & (4)) != 0) goto loc_003138E5;
    if (v_rbx < (v_stack_p8 + v_r11 * 1)) goto loc_003138E5;
    if (v_rbx > a4) goto loc_003138E5;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p40 + 16))) | (4));
    *(unsigned int *)(v_stack_p40 + 16) = (unsigned int)(a1);
    goto loc_003138E5;
loc_00313BAA:
    if ((*(unsigned __int8 *)(v_stack_p40 + 25)) != 0) goto loc_00313B68;
    result = qsort(v_stack_p40 + 40, a4, 8, v_rip + 3677391);
    result = MiCompressTbFlushList(v_stack_p40, a4, 8, v_rip + 3677391);
    goto loc_003138E8;
loc_00313BDF:
    a1 = (unsigned int)((v_stack_p40) & (0x3FFULL));
    if (((unsigned int)(v_stack_p30) + a1 * 1) > 0x3FFULL) goto loc_00313AE7;
    if (((unsigned int)(v_stack_p30) + a1 * 1) <= a1) goto loc_00313AE7;
    result = (result) - (v_r11);
    result = (result) ^ (result + (unsigned int)(v_stack_p30) * 1);
    result = (result) & (0xFFFFFFFFFFFFFC00ULL);
    result = (result) ^ (result + (unsigned int)(v_stack_p30) * 1);
    *(unsigned __int64 *)(v_stack_p40 + a4 - 1 + 5 * 8) = result;
    goto loc_00313A91;
loc_00313C29:
    a1 = 0;
    goto loc_003137EF;
loc_00313C36:
    a1 = 0;
    goto loc_00313A21;
loc_00313C40:
    result = (a1 + 9) ^ (a1 + 9 + (unsigned int)(v_stack_p30) * 1);
    result = (result) & (0xFFFFFFFFFFFFFC00ULL);
    result = (result) ^ (a1 + 9 + (unsigned int)(v_stack_p30) * 1);
    *(unsigned __int64 *)(v_stack_p40 + a4 - 1 + 5 * 8 + 40) = result;
    goto loc_00313B68;
loc_00313C5E:
    *(unsigned __int8 *)(v_stack_p40 + 25) = 1;
    goto loc_00313B68;
}
```

## 5. (Beta) C Style

```c
int64_t MiFlushTbAsNeeded(void *Arg1, void *Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r11;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m118;
    uint32_t v_stack_m124;
    uint32_t v_stack_m128;
    uint64_t v_stack_m138;
    uint64_t v_stack_m48;
    uint32_t v_stack_p30;
    uint32_t v_stack_p34;
    uint64_t v_stack_p40;
    uint32_t v_stack_p48;
    uint32_t v_stack_p4C;
    uint32_t v_stack_p50;
    uint32_t v_stack_p54;
    uint8_t v_stack_p58;
    uint16_t v_stack_p59;
    uint32_t v_stack_p5C;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (288);
    result = (*(uint64_t *)(v_rip + 0xAF6FF2)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m124 = Arg4;
    Arg2 = 0;
    result = memset(v_stack_m118, Arg2, 200, Arg4);
    local_r14 = 0;
    local_r13 = 0;
    v_stack_m128 = 0;
    if ((uint32_t)((uint32_t)(Arg4)) == 0) goto loc_003139B1;
    result = MiGetProcessorFlushList(v_stack_m118, Arg2, 200, Arg4);
    *(uint32_t *)(result + 0x10) = 0;
    *(uint32_t *)(result + 0x14) = 1;
    *(void **)(result) = Arg1;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xB8))) >> (8));
    Arg1 = (uint8_t)((Arg1) >> (3));
    Arg1 = (uint8_t)((Arg1) & (1));
    *(uint8_t *)(result + 0x18) = (uint8_t)(Arg1);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0xB8)))) & (15)) != 0) goto loc_003137E2;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) + (0x400ULL);
    if (Arg1 != Arg1) goto loc_00313C29;
loc_003137E2:
    Arg1 = 0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0xB8)))) & (15)) == 0) { Arg1 = 1; }
loc_003137EF:
    *(uint32_t *)(result + 0x8) = (uint32_t)(Arg1);
    *(uint16_t *)(result + 0x19) = 0;
    *(uint32_t *)(result + 0x1C) = 0;
    *(uint64_t *)(result + 0x20) = 0;
    *(uint64_t *)(result + 0x28) = 0;
loc_0031380F:
    local_rsi = 0;
loc_0031381B:
    if (0 >= Arg3) goto loc_0031396E;
    Arg1 = (((*(uint64_t *)(arg2)) & (0xC01ULL)) == 0) ? 1 : 0;
    result = (((*(uint64_t *)(arg2)) & (992)) == 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_0031388B;
    if (*(uint64_t *)(v_rip + 0xB1A430) == 0) goto loc_00313860;
    if ((((uint8_t)(*(uint64_t *)(arg2))) & (16)) != 0) goto loc_003138AD;
    result = ~(*(uint64_t *)(v_rip + 0xB1A430));
    local_rbx = (*(uint64_t *)(arg2)) & (result);
loc_00313860:
    local_rbx = (local_rbx) >> (32);
    *(uint64_t *)(arg2) = *(uint64_t *)(v_rip - 0x302FE7);
    if ((uint32_t)(local_rbx) != 0) goto loc_003138B3;
    local_r14 = 0;
    v_stack_m128 = 0;
    local_r13 = 0;
loc_0031387D:
    local_rsi = (local_rsi) + 1;
    local_rdi = (Arg2) + (8);
    goto loc_0031381B;
loc_0031388B:
    if ((uint32_t)((uint32_t)(Arg4)) != 0) goto loc_0031387D;
    local_rbp = (Arg3) - (local_rsi);
    v_stack_m138 = local_rbx;
    result = KeBugCheckEx((uint32_t)(Arg4) + 26, (uint32_t)(0x5100ULL), local_rdi, local_rbp);
loc_003138AD:
    local_rbx = (local_rbx) & (-17);
    goto loc_00313860;
loc_003138B3:
    if (((uint32_t)(local_rbx)) != 0) goto loc_00313A46;
    if (0 == 0) goto loc_0031387D;
    local_rbx = (local_rdi) << (25);
    result = (local_rdi) << (25);
    local_rbx = (local_rbx) - (result);
    local_rbx = (local_rbx) >> (16);
    if ((*(uint32_t *)(result + 0x8)) != 1) goto loc_00313B77;
loc_003138E5:
    local_r15 = 0;
loc_003138E8:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x1C))) == 0) goto loc_00313AE7;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x10)))) & (2)) != 0) goto loc_00313AA0;
    if (((*(uint64_t *)(result + (uint32_t)(*(uint32_t *)(result + 0x1C)) - 0x1 * 8 + 0x28)) & (0xC00ULL)) != 0) goto loc_00313AE7;
    Arg3 = (uint32_t)((*(uint64_t *)(result + (uint32_t)(*(uint32_t *)(result + 0x1C)) - 0x1 * 8 + 0x28)) & (0x3FFULL));
    Arg1 = (*(uint64_t *)(result + (uint32_t)(*(uint32_t *)(result + 0x1C)) - 0x1 * 8 + 0x28)) & (0xFFFFFFFFFFFFF000ULL);
    Arg2 = (Arg3 + 1) << (12);
    Arg2 = (Arg2) + (Arg1);
    if (Arg2 != local_rbx) goto loc_00313956;
    if ((Arg3 + (uint32_t)(0x5100ULL) * 1) <= Arg3) goto loc_00313956;
    if ((Arg3 + (uint32_t)(0x5100ULL) * 1) <= 0x3FFULL) goto loc_00313C40;
loc_00313956:
    goto loc_00313AC9;
loc_0031396E:
    result = MiFlushTbList(result, Arg2, Arg3, (uint32_t)(*(uint32_t *)(result + 0x1C)));
    result = v_stack_m118;
    if (result != v_stack_m118) {
        result = MiReleaseProcessorFlushList(result, Arg2, Arg3, (uint32_t)(*(uint32_t *)(result + 0x1C)));
    }
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, (uint32_t)(*(uint32_t *)(result + 0x1C)));
    local_rsp = (local_rsp) + (288);
    return result;
loc_003139B1:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p8 + 0xB8))) >> (8));
    result = (uint8_t)((result) >> (3));
    result = (uint8_t)((result) & (1));
    v_stack_p4C = 20;
    v_stack_p58 = (uint8_t)(result);
    v_stack_p50 = 8;
    v_stack_p54 = 1;
    v_stack_p40 = v_stack_p8;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0xB8)))) & (15)) != 0) goto loc_00313A10;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) + (0x400ULL);
    if (v_stack_p8 != Arg1) goto loc_00313C36;
loc_00313A10:
    Arg1 = 0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0xB8)))) & (15)) == 0) { Arg1 = 1; }
loc_00313A21:
    result = (uint32_t)(((uint32_t)(v_stack_p50)) & (0xFFFFFFDBULL));
    v_stack_p48 = (uint32_t)(Arg1);
    v_stack_p50 = (uint32_t)(result);
    v_stack_p59 = 0;
    v_stack_p5C = 0;
    v_stack_p60 = 0;
    v_stack_p68 = 0;
    goto loc_0031380F;
loc_00313A46:
    result = MiCompareTbFlushTimeStamp((uint32_t)((uint32_t)(v_stack_p8)), 1, Arg3, (uint32_t)(*(uint32_t *)(result + 0x1C)));
    if ((uint8_t)(result) == 0) goto loc_00313B4F;
    Arg2 = (local_rdi) << (25);
    Arg4 = 0;
    result = (result) << (25);
    Arg2 = (Arg2) - (result);
    Arg2 = (Arg2) >> (16);
    result = MiInsertTbFlushEntry(v_stack_p40, Arg2, Arg4 + 1, Arg4);
loc_00313A89:
    v_stack_p30 = 1;
loc_00313A91:
    goto loc_0031387D;
loc_00313AA0:
    if (0 == 0) goto loc_00313AE7;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p40 + 0x10)))) & (2)) != 0) goto loc_00313AE7;
    if (((*(uint64_t *)(v_stack_p40 + Arg4 - 0x1 + 0x5 * 8)) & (0xC00ULL)) != 0) goto loc_00313AE7;
loc_00313AC9:
    local_r11 = (1) << (12);
    Arg2 = (*(uint64_t *)(v_stack_p40 + Arg4 - 0x1 + 0x5 * 8)) & (0xFFFFFFFFFFFFF000ULL);
    if (Arg2 == (v_stack_p8 + local_r11 * 1)) goto loc_00313BDF;
loc_00313AE7:
    if (0 == (*(uint32_t *)(v_stack_p40 + 0xC))) goto loc_00313B57;
loc_00313AEE:
    if (1 == 0) goto loc_00313B68;
    Arg2 = (uint32_t)(0x400ULL);
    if ((1 - 1) <= 0x3FFULL) { Arg2 = 1; }
    Arg1 = (v_stack_p8) & (0xFFFFFFFFFFFFF000ULL);
    result = (uint32_t)((Arg2 - 1) & (0x3FFULL));
    result = (result) | (Arg1);
    *(uint64_t *)(v_stack_p40 + Arg4 * 8 + 0x28) = result;
    Arg4 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p40 + 0x1C))) + 1);
    Arg1 = (Arg2) << (12);
    local_rbx = (v_stack_p8) + (Arg1);
    *(uint32_t *)(v_stack_p40 + 0x1C) = Arg4;
    local_r14 = (1) - (Arg2);
    if (condition_is_equal) goto loc_00313AEE;
    if (Arg4 == (*(uint32_t *)(v_stack_p40 + 0xC))) goto loc_003138E5;
    goto loc_00313AEE;
loc_00313B4F:
    local_r14 = 0;
    goto loc_00313A89;
loc_00313B57:
    if (0 == 0) goto loc_00313BAA;
    if ((*(uint8_t *)(v_stack_p40 + 0x19)) == 0) goto loc_00313C5E;
loc_00313B68:
    goto loc_00313A91;
loc_00313B77:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p40 + 0x10)))) & (4)) != 0) goto loc_003138E5;
    if (local_rbx < (v_stack_p8 + local_r11 * 1)) goto loc_003138E5;
    if (local_rbx > Arg4) goto loc_003138E5;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p40 + 0x10))) | (4));
    *(uint32_t *)(v_stack_p40 + 0x10) = (uint32_t)(Arg1);
    goto loc_003138E5;
loc_00313BAA:
    if ((*(uint8_t *)(v_stack_p40 + 0x19)) != 0) goto loc_00313B68;
    result = qsort(v_stack_p40 + 40, Arg4, 8, v_rip + 3677391);
    result = MiCompressTbFlushList(v_stack_p40, Arg4, 8, v_rip + 3677391);
    goto loc_003138E8;
loc_00313BDF:
    Arg1 = (uint32_t)((v_stack_p40) & (0x3FFULL));
    if (((uint32_t)(v_stack_p30) + Arg1 * 1) > 0x3FFULL) goto loc_00313AE7;
    if (((uint32_t)(v_stack_p30) + Arg1 * 1) <= Arg1) goto loc_00313AE7;
    result = (result) - (local_r11);
    result = (result) ^ (result + (uint32_t)(v_stack_p30) * 1);
    result = (result) & (0xFFFFFFFFFFFFFC00ULL);
    result = (result) ^ (result + (uint32_t)(v_stack_p30) * 1);
    *(uint64_t *)(v_stack_p40 + Arg4 - 0x1 + 0x5 * 8) = result;
    goto loc_00313A91;
loc_00313C29:
    Arg1 = 0;
    goto loc_003137EF;
loc_00313C36:
    Arg1 = 0;
    goto loc_00313A21;
loc_00313C40:
    result = (Arg1 + 9) ^ (Arg1 + 9 + (uint32_t)(v_stack_p30) * 1);
    result = (result) & (0xFFFFFFFFFFFFFC00ULL);
    result = (result) ^ (Arg1 + 9 + (uint32_t)(v_stack_p30) * 1);
    *(uint64_t *)(v_stack_p40 + Arg4 - 0x1 + 0x5 * 8 + 0x28) = result;
    goto loc_00313B68;
loc_00313C5E:
    *(uint8_t *)(v_stack_p40 + 0x19) = 1;
    goto loc_00313B68;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xB8` | `32` | `R` |
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00313730&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
