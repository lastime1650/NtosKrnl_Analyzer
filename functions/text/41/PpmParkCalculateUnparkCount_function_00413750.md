# PpmParkCalculateUnparkCount

- RVA: `0x00413750`–`0x00413BF9` (길이 `1,193` bytes)
- VA: `0x0000000140413750`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009BFD4`
- 디코드: `269`개 명령, `1,193/1,193` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **8**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **9**

### Outgoing calls
- `0x004138B3` → [PpmHeteroIsMultiClassParkingEnabled](PpmHeteroIsMultiClassParkingEnabled_function_00414310.md) (function, `0x00414310`)
- `0x004138DB` → [PpmHeteroIsMultiClassParkingEnabled](PpmHeteroIsMultiClassParkingEnabled_function_00414310.md) (function, `0x00414310`)
- `0x00413966` → [PpmEventHgsCoresUnparkedCount](PpmEventHgsCoresUnparkedCount_function_0041432C.md) (function, `0x0041432C`)
- `0x0041396B` → [Feature_PpmParkEx__private_IsEnabledDeviceUsageNoInline](../4F/Feature_PpmParkEx__private_IsEnabledDeviceUsageNoInline_function_004F135C.md) (function, `0x004F135C`)
- `0x004139B5` → [PpmEventParkingCountSelection](PpmEventParkingCountSelection_function_00414388.md) (function, `0x00414388`)
- `0x004139E5` → [PpmEventParkingCountSelectionEx](../4F/PpmEventParkingCountSelectionEx_function_004F4188.md) (function, `0x004F4188`)
- `0x00413A19` → [PpmHeteroHgsCalculateContainmentCount](PpmHeteroHgsCalculateContainmentCount_function_004144E4.md) (function, `0x004144E4`)
- `0x00413B43` → [PpmHeteroIsMultiClassParkingEnabled](PpmHeteroIsMultiClassParkingEnabled_function_00414310.md) (function, `0x00414310`)

### Direct callers
- [PpmCheckComputeMultiClassHeteroResponse](PpmCheckComputeMultiClassHeteroResponse_function_00412534.md) at `0x00412989`
- [PpmCheckComputeMultiClassHeteroResponseEx](../4F/PpmCheckComputeMultiClassHeteroResponseEx_function_004F14A4.md) at `0x004F181B`
- [PpmCheckComputeHeteroResponseEx](../5D/PpmCheckComputeHeteroResponseEx_function_005DECA0.md) at `0x005DF561`
- [sub_006FA0AE](../6F/Unknown_function_006FA0AE.md) at `0x006FA435`

### Static image references
- `0x00413764` → RVA `0x00F083D0` (`.data`; read)
- `0x00413776` → RVA `0x00E08380` (`.data`; read)
- `0x0041377D` → RVA `0x00F0CE0C` (`.data`; read)
- `0x0041378B` → RVA `0x00F0B244` (`.data`; read)
- `0x004137D2` → RVA `0x00F083E0` (`.data`; read)
- `0x00413808` → RVA `0x00F083D8` (`.data`; read)
- `0x0041389F` → RVA `0x00F083A0` (`.data`; read)
- `0x00413952` → RVA `0x00FC6A86` (`ALMOSTRO`; read)
- `0x00413B18` → RVA `0x00F083A2` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00413750  40 53                           push rbx
00413752  55                              push rbp
00413753  56                              push rsi
00413754  57                              push rdi
00413755  41 54                           push r12
00413757  41 55                           push r13
00413759  41 56                           push r14
0041375B  41 57                           push r15
0041375D  48 83 EC 78                     sub rsp, 0x78
00413761  45 33 C0                        xor r8d, r8d
00413764  44 39 05 65 4C AF 00            cmp dword ptr [rip + 0xaf4c65], r8d
0041376B  44 89 44 24 60                  mov dword ptr [rsp + 0x60], r8d
00413770  45 8D 48 01                     lea r9d, [r8 + 1]
00413774  74 72                           je 0x1404137e8
00413776  48 8B 15 03 4C 9F 00            mov rdx, qword ptr [rip + 0x9f4c03]
0041377D  48 63 05 88 96 AF 00            movsxd rax, dword ptr [rip + 0xaf9688]
00413784  48 69 C8 E8 01 00 00            imul rcx, rax, 0x1e8
0041378B  83 3D B2 7A AF 00 05            cmp dword ptr [rip + 0xaf7ab2], 5
00413792  8A 84 11 B9 00 00 00            mov al, byte ptr [rcx + rdx + 0xb9]
00413799  44 8B A4 11 C0 00 00 00         mov r12d, dword ptr [rcx + rdx + 0xc0]
004137A1  44 8B AC 11 BC 00 00 00         mov r13d, dword ptr [rcx + rdx + 0xbc]
004137A9  88 84 24 C8 00 00 00            mov byte ptr [rsp + 0xc8], al
004137B0  8A 84 11 B8 00 00 00            mov al, byte ptr [rcx + rdx + 0xb8]
004137B7  8A 94 11 B6 00 00 00            mov dl, byte ptr [rcx + rdx + 0xb6]
004137BE  88 94 24 D0 00 00 00            mov byte ptr [rsp + 0xd0], dl
004137C5  88 84 24 C0 00 00 00            mov byte ptr [rsp + 0xc0], al
004137CC  0F 84 66 03 00 00               je 0x140413b38
004137D2  44 39 05 07 4C AF 00            cmp dword ptr [rip + 0xaf4c07], r8d
004137D9  45 0F B7 F0                     movzx r14d, r8w
004137DD  66 44 89 84 24 D8 00 00 00      mov word ptr [rsp + 0xd8], r8w
004137E6  75 15                           jne 0x1404137fd
004137E8  41 8A C1                        mov al, r9b
004137EB  48 83 C4 78                     add rsp, 0x78
004137EF  41 5F                           pop r15
004137F1  41 5E                           pop r14
004137F3  41 5D                           pop r13
004137F5  41 5C                           pop r12
004137F7  5F                              pop rdi
004137F8  5E                              pop rsi
004137F9  5D                              pop rbp
004137FA  5B                              pop rbx
004137FB  C3                              ret
004137FC  CC                              int3
004137FD  41 0F B7 C6                     movzx eax, r14w
00413801  48 69 D8 10 05 00 00            imul rbx, rax, 0x510
00413808  48 03 1D C9 4B AF 00            add rbx, qword ptr [rip + 0xaf4bc9]
0041380F  44 84 8B A0 04 00 00            test byte ptr [rbx + 0x4a0], r9b
00413816  75 61                           jne 0x140413879
00413818  44 01 0B                        add dword ptr [rbx], r9d
0041381B  41 8A F0                        mov sil, r8b
0041381E  8B 03                           mov eax, dword ptr [rbx]
00413820  44 38 43 0C                     cmp byte ptr [rbx + 0xc], r8b
00413824  76 53                           jbe 0x140413879
00413826  44 8B F0                        mov r14d, eax
00413829  40 0F B6 C6                     movzx eax, sil
0041382D  48 8D 3C 80                     lea rdi, [rax + rax*4]
00413831  40 8A C6                        mov al, sil
00413834  48 C1 E7 07                     shl rdi, 7
00413838  48 03 BB 08 05 00 00            add rdi, qword ptr [rbx + 0x508]
0041383F  F6 D8                           neg al
00413841  1B C9                           sbb ecx, ecx
00413843  44 0F B7 1F                     movzx r11d, word ptr [rdi]
00413847  83 E1 02                        and ecx, 2
0041384A  83 C1 02                        add ecx, 2
0041384D  44 89 44 24 60                  mov dword ptr [rsp + 0x60], r8d
00413852  84 8B A0 04 00 00               test byte ptr [rbx + 0x4a0], cl
00413858  0F 85 E5 02 00 00               jne 0x140413b43
0041385E  41 8A C0                        mov al, r8b
00413861  66 45 85 DB                     test r11w, r11w
00413865  75 34                           jne 0x14041389b
00413867  41 02 F1                        add sil, r9b
0041386A  40 3A 73 0C                     cmp sil, byte ptr [rbx + 0xc]
0041386E  72 B9                           jb 0x140413829
00413870  44 0F B7 B4 24 D8 00 00 00      movzx r14d, word ptr [rsp + 0xd8]
00413879  66 45 03 F1                     add r14w, r9w
0041387D  41 0F B7 CE                     movzx ecx, r14w
00413881  3B 0D 59 4B AF 00               cmp ecx, dword ptr [rip + 0xaf4b59]
00413887  66 44 89 B4 24 D8 00 00 00      mov word ptr [rsp + 0xd8], r14w
00413890  0F 83 52 FF FF FF               jae 0x1404137e8
00413896  E9 62 FF FF FF                  jmp 0x1404137fd
0041389B  84 C0                           test al, al
0041389D  75 C8                           jne 0x140413867
0041389F  40 8A 2D FA 4A AF 00            mov bpl, byte ptr [rip + 0xaf4afa]
004138A6  45 0F B7 D1                     movzx r10d, r9w
004138AA  40 84 ED                        test bpl, bpl
004138AD  0F 84 A5 02 00 00               je 0x140413b58
004138B3  E8 58 0A 00 00                  call 0x140414310
004138B8  84 C0                           test al, al
004138BA  0F 85 A5 02 00 00               jne 0x140413b65
004138C0  40 84 F6                        test sil, sil
004138C3  0F 84 5A 01 00 00               je 0x140413a23
004138C9  8A 8B 9A 04 00 00               mov cl, byte ptr [rbx + 0x49a]
004138CF  44 0F B7 8B 98 04 00 00         movzx r9d, word ptr [rbx + 0x498]
004138D7  45 0F B7 F9                     movzx r15d, r9w
004138DB  E8 30 0A 00 00                  call 0x140414310
004138E0  84 C0                           test al, al
004138E2  75 2B                           jne 0x14041390f
004138E4  B8 01 00 00 00                  mov eax, 1
004138E9  40 84 ED                        test bpl, bpl
004138EC  0F 85 90 02 00 00               jne 0x140413b82
004138F2  66 45 3B CB                     cmp r9w, r11w
004138F6  73 20                           jae 0x140413918
004138F8  3A CA                           cmp cl, dl
004138FA  76 1C                           jbe 0x140413918
004138FC  44 8B 44 24 60                  mov r8d, dword ptr [rsp + 0x60]
00413901  66 44 03 C8                     add r9w, ax
00413905  44 0B C0                        or r8d, eax
00413908  44 89 44 24 60                  mov dword ptr [rsp + 0x60], r8d
0041390D  EB 0E                           jmp 0x14041391d
0041390F  44 38 83 A1 04 00 00            cmp byte ptr [rbx + 0x4a1], r8b
00413916  74 CC                           je 0x1404138e4
00413918  44 8B 44 24 60                  mov r8d, dword ptr [rsp + 0x60]
0041391D  0F B7 57 08                     movzx edx, word ptr [rdi + 8]
00413921  33 C0                           xor eax, eax
00413923  40 84 ED                        test bpl, bpl
00413926  0F 85 68 02 00 00               jne 0x140413b94
0041392C  66 41 3B D1                     cmp dx, r9w
00413930  0F 82 28 01 00 00               jb 0x140413a5e
00413936  0F 87 8B 01 00 00               ja 0x140413ac7
0041393C  66 41 3B D3                     cmp dx, r11w
00413940  72 04                           jb 0x140413946
00413942  41 0F B7 D3                     movzx edx, r11w
00413946  45 33 C0                        xor r8d, r8d
00413949  40 84 ED                        test bpl, bpl
0041394C  0F 85 85 02 00 00               jne 0x140413bd7
00413952  44 38 05 2D 31 BB 00            cmp byte ptr [rip + 0xbb312d], r8b
00413959  66 89 57 06                     mov word ptr [rdi + 6], dx
0041395D  0F 85 89 00 00 00               jne 0x1404139ec
00413963  48 8B CB                        mov rcx, rbx
00413966  E8 C1 09 00 00                  call 0x14041432c
0041396B  E8 EC D9 0D 00                  call 0x1404f135c
00413970  44 89 74 24 50                  mov dword ptr [rsp + 0x50], r14d
00413975  85 C0                           test eax, eax
00413977  8A 84 24 C0 00 00 00            mov al, byte ptr [rsp + 0xc0]
0041397E  40 8A CE                        mov cl, sil
00413981  44 89 6C 24 48                  mov dword ptr [rsp + 0x48], r13d
00413986  44 89 64 24 40                  mov dword ptr [rsp + 0x40], r12d
0041398B  88 44 24 38                     mov byte ptr [rsp + 0x38], al
0041398F  8A 84 24 C8 00 00 00            mov al, byte ptr [rsp + 0xc8]
00413996  88 44 24 30                     mov byte ptr [rsp + 0x30], al
0041399A  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
0041399E  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
004139A2  75 2B                           jne 0x1404139cf
004139A4  8A 07                           mov al, byte ptr [rdi]
004139A6  41 8A D7                        mov dl, r15b
004139A9  44 8A 4F 06                     mov r9b, byte ptr [rdi + 6]
004139AD  44 8A 47 08                     mov r8b, byte ptr [rdi + 8]
004139B1  88 44 24 20                     mov byte ptr [rsp + 0x20], al
004139B5  E8 CE 09 00 00                  call 0x140414388
004139BA  8A 94 24 D0 00 00 00            mov dl, byte ptr [rsp + 0xd0]
004139C1  41 B9 01 00 00 00               mov r9d, 1
004139C7  45 33 C0                        xor r8d, r8d
004139CA  E9 98 FE FF FF                  jmp 0x140413867
004139CF  0F B7 07                        movzx eax, word ptr [rdi]
004139D2  41 0F B7 D7                     movzx edx, r15w
004139D6  44 0F B7 4F 06                  movzx r9d, word ptr [rdi + 6]
004139DB  44 0F B7 47 08                  movzx r8d, word ptr [rdi + 8]
004139E0  66 89 44 24 20                  mov word ptr [rsp + 0x20], ax
004139E5  E8 9E 07 0E 00                  call 0x1404f4188
004139EA  EB CE                           jmp 0x1404139ba
004139EC  0F B7 83 F0 04 00 00            movzx eax, word ptr [rbx + 0x4f0]
004139F3  66 89 93 F4 04 00 00            mov word ptr [rbx + 0x4f4], dx
004139FA  66 3B D0                        cmp dx, ax
004139FD  0F 82 E6 01 00 00               jb 0x140413be9
00413A03  66 2B D0                        sub dx, ax
00413A06  66 89 93 F2 04 00 00            mov word ptr [rbx + 0x4f2], dx
00413A0D  45 0F B7 C1                     movzx r8d, r9w
00413A11  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
00413A16  48 8B CB                        mov rcx, rbx
00413A19  E8 C6 0A 00 00                  call 0x1404144e4
00413A1E  E9 40 FF FF FF                  jmp 0x140413963
00413A23  44 38 83 A1 04 00 00            cmp byte ptr [rbx + 0x4a1], r8b
00413A2A  0F 84 99 FE FF FF               je 0x1404138c9
00413A30  48 8B 8B 08 05 00 00            mov rcx, qword ptr [rbx + 0x508]
00413A37  0F B7 81 8A 02 00 00            movzx eax, word ptr [rcx + 0x28a]
00413A3E  66 39 81 86 02 00 00            cmp word ptr [rcx + 0x286], ax
00413A45  0F 82 7E FE FF FF               jb 0x1404138c9
00413A4B  44 0F B7 89 7A 02 00 00         movzx r9d, word ptr [rcx + 0x27a]
00413A53  8A 89 7C 02 00 00               mov cl, byte ptr [rcx + 0x27c]
00413A59  E9 79 FE FF FF                  jmp 0x1404138d7
00413A5E  66 41 3B D3                     cmp dx, r11w
00413A62  0F 83 DA FE FF FF               jae 0x140413942
00413A68  45 3B F4                        cmp r14d, r12d
00413A6B  0F 82 D5 FE FF FF               jb 0x140413946
00413A71  0F B6 8C 24 C8 00 00 00         movzx ecx, byte ptr [rsp + 0xc8]
00413A79  41 83 C8 04                     or r8d, 4
00413A7D  44 89 44 24 60                  mov dword ptr [rsp + 0x60], r8d
00413A82  89 03                           mov dword ptr [rbx], eax
00413A84  85 C9                           test ecx, ecx
00413A86  0F 84 42 01 00 00               je 0x140413bce
00413A8C  83 E9 01                        sub ecx, 1
00413A8F  0F 84 1E 01 00 00               je 0x140413bb3
00413A95  83 E9 01                        sub ecx, 1
00413A98  0F 84 A4 FE FF FF               je 0x140413942
00413A9E  83 F9 01                        cmp ecx, 1
00413AA1  0F 85 9F FE FF FF               jne 0x140413946
00413AA7  44 0F B7 83 9E 04 00 00         movzx r8d, word ptr [rbx + 0x49e]
00413AAF  0F B7 CA                        movzx ecx, dx
00413AB2  41 03 C8                        add ecx, r8d
00413AB5  41 3B CB                        cmp ecx, r11d
00413AB8  0F 83 84 FE FF FF               jae 0x140413942
00413ABE  66 41 03 D0                     add dx, r8w
00413AC2  E9 75 FE FF FF                  jmp 0x14041393c
00413AC7  66 41 3B D2                     cmp dx, r10w
00413ACB  0F 82 6B FE FF FF               jb 0x14041393c
00413AD1  45 3B F5                        cmp r14d, r13d
00413AD4  0F 82 62 FE FF FF               jb 0x14041393c
00413ADA  0F B6 8C 24 C0 00 00 00         movzx ecx, byte ptr [rsp + 0xc0]
00413AE2  41 83 C8 08                     or r8d, 8
00413AE6  44 89 44 24 60                  mov dword ptr [rsp + 0x60], r8d
00413AEB  89 03                           mov dword ptr [rbx], eax
00413AED  85 C9                           test ecx, ecx
00413AEF  0F 84 D9 00 00 00               je 0x140413bce
00413AF5  83 E9 01                        sub ecx, 1
00413AF8  0F 84 C7 00 00 00               je 0x140413bc5
00413AFE  83 E9 01                        sub ecx, 1
00413B01  0F 84 B5 00 00 00               je 0x140413bbc
00413B07  83 F9 01                        cmp ecx, 1
00413B0A  0F 85 2C FE FF FF               jne 0x14041393c
00413B10  44 0F B7 83 9E 04 00 00         movzx r8d, word ptr [rbx + 0x49e]
00413B18  44 0F B7 15 82 48 AF 00         movzx r10d, word ptr [rip + 0xaf4882]
00413B20  0F B7 C2                        movzx eax, dx
00413B23  43 8D 0C 10                     lea ecx, [r8 + r10]
00413B27  3B C1                           cmp eax, ecx
00413B29  0F 86 8D 00 00 00               jbe 0x140413bbc
00413B2F  66 41 2B D0                     sub dx, r8w
00413B33  E9 04 FE FF FF                  jmp 0x14041393c
00413B38  45 8B E8                        mov r13d, r8d
00413B3B  45 8B E0                        mov r12d, r8d
00413B3E  E9 8F FC FF FF                  jmp 0x1404137d2
00413B43  E8 C8 07 00 00                  call 0x140414310
00413B48  84 C0                           test al, al
00413B4A  41 8A C1                        mov al, r9b
00413B4D  0F 84 0E FD FF FF               je 0x140413861
00413B53  E9 06 FD FF FF                  jmp 0x14041385e
00413B58  44 0F B7 15 42 48 AF 00         movzx r10d, word ptr [rip + 0xaf4842]
00413B60  E9 4E FD FF FF                  jmp 0x1404138b3
00413B65  44 38 83 A1 04 00 00            cmp byte ptr [rbx + 0x4a1], r8b
00413B6C  0F 84 57 FD FF FF               je 0x1404138c9
00413B72  44 0F B7 4F 06                  movzx r9d, word ptr [rdi + 6]
00413B77  8A 8F 7C 02 00 00               mov cl, byte ptr [rdi + 0x27c]
00413B7D  E9 55 FD FF FF                  jmp 0x1404138d7
00413B82  66 39 05 19 48 AF 00            cmp word ptr [rip + 0xaf4819], ax
00413B89  0F 85 89 FD FF FF               jne 0x140413918
00413B8F  E9 5E FD FF FF                  jmp 0x1404138f2
00413B94  0F B7 0D 07 48 AF 00            movzx ecx, word ptr [rip + 0xaf4807]
00413B9B  8B C2                           mov eax, edx
00413B9D  33 D2                           xor edx, edx
00413B9F  41 83 C8 02                     or r8d, 2
00413BA3  F7 F1                           div ecx
00413BA5  44 89 44 24 60                  mov dword ptr [rsp + 0x60], r8d
00413BAA  8B D0                           mov edx, eax
00413BAC  33 C0                           xor eax, eax
00413BAE  E9 79 FD FF FF                  jmp 0x14041392c
00413BB3  66 41 03 D2                     add dx, r10w
00413BB7  E9 80 FD FF FF                  jmp 0x14041393c
00413BBC  41 0F B7 D2                     movzx edx, r10w
00413BC0  E9 77 FD FF FF                  jmp 0x14041393c
00413BC5  66 41 2B D2                     sub dx, r10w
00413BC9  E9 6E FD FF FF                  jmp 0x14041393c
00413BCE  41 0F B7 D1                     movzx edx, r9w
00413BD2  E9 65 FD FF FF                  jmp 0x14041393c
00413BD7  0F B7 05 C4 47 AF 00            movzx eax, word ptr [rip + 0xaf47c4]
00413BDE  0F B7 D2                        movzx edx, dx
00413BE1  0F AF D0                        imul edx, eax
00413BE4  E9 69 FD FF FF                  jmp 0x140413952
00413BE9  66 89 83 F4 04 00 00            mov word ptr [rbx + 0x4f4], ax
00413BF0  41 0F B7 D0                     movzx edx, r8w
00413BF4  E9 0D FE FF FF                  jmp 0x140413a06
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmParkCalculateUnparkCount(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m58;
    unsigned __int8 v_stack_p10;
    unsigned __int8 v_stack_p18;
    unsigned __int16 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned __int8 v_stack_p30;
    unsigned __int8 v_stack_p38;
    unsigned int v_stack_p40;
    unsigned int v_stack_p48;
    unsigned int v_stack_p50;
    unsigned int v_stack_p60;
    unsigned __int8 v_stack_p8;
    unsigned __int8 v_stack_pC0;
    unsigned __int8 v_stack_pC8;
    unsigned __int8 v_stack_pD0;
    unsigned __int16 v_stack_pD8;

    v_rsp = (v_rsp) - (120);
    a3 = 0;
    v_stack_m58 = 0;
    if ((*(unsigned int *)(v_rip + 11488357)) == 0) goto loc_004137E8;
    a1 = (a1) * ((int)(*(unsigned int *)(v_rip + 11507336)));
    v_stack_p10 = (unsigned __int8)(*(unsigned __int8 *)(a1 + *(unsigned __int64 *)(v_rip + 10439683) * 1 + 185));
    v_stack_p18 = (unsigned __int8)(*(unsigned __int8 *)(a1 + *(unsigned __int64 *)(v_rip + 10439683) * 1 + 182));
    v_stack_p8 = (unsigned __int8)(*(unsigned __int8 *)(a1 + *(unsigned __int64 *)(v_rip + 10439683) * 1 + 184));
    if ((*(unsigned int *)(v_rip + 11500210)) == 5) goto loc_00413B38;
loc_004137D2:
    v_stack_p20 = 0;
    if ((*(unsigned int *)(v_rip + 11488263)) != 0) goto loc_004137FD;
loc_004137E8:
    v_rsp = (v_rsp) + (120);
    return (unsigned __int8)(a3 + 1);
loc_004137FD:
    v_rbx = (v_rbx) * (0);
    v_rbx = (v_rbx) + (*(unsigned __int64 *)(v_rip + 11488201));
    if (((*(unsigned __int8 *)(v_rbx + 1184)) & ((unsigned __int8)(a3 + 1))) != 0) goto loc_00413879;
    if ((*(unsigned __int8 *)(v_rbx + 12)) <= 0) goto loc_00413879;
loc_00413829:
    v_rdi = (0 + 0 * 4) << (7);
    v_rdi = (v_rdi) + (*(unsigned __int64 *)(v_rbx + 1288));
    result = (unsigned __int8)(-(0));
    a1 = (unsigned int)((a1) & (2));
    a1 = (unsigned int)((a1) + (2));
    v_stack_p60 = 0;
    if (((*(unsigned __int8 *)(v_rbx + 1184)) & ((unsigned __int8)(a1))) != 0) goto loc_00413B43;
loc_0041385E:
loc_00413861:
    if ((unsigned __int16)(*(unsigned __int16 *)(v_rdi)) != 0) goto loc_0041389B;
loc_00413867:
    v_rsi = (unsigned __int8)((0) + ((unsigned __int8)(a3 + 1)));
    if (((unsigned __int8)(v_rsi)) < (*(unsigned __int8 *)(v_rbx + 12))) goto loc_00413829;
loc_00413879:
    v_r14 = (unsigned __int16)((v_stack_pD8) + ((unsigned __int16)(a3 + 1)));
    v_stack_pD8 = (unsigned __int16)(v_r14);
    if (((unsigned int)((unsigned __int16)(v_r14))) >= (*(unsigned int *)(v_rip + 11488089))) goto loc_004137E8;
    goto loc_004137FD;
loc_0041389B:
    if (0 != 0) goto loc_00413867;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 11487994)) == 0) goto loc_00413B58;
loc_004138B3:
    result = PpmHeteroIsMultiClassParkingEnabled((unsigned __int16)(v_r14), *(unsigned __int8 *)(a1 + *(unsigned __int64 *)(v_rip + 10439683) * 1 + 182), a3, a3 + 1);
    if ((unsigned __int8)(result) != 0) goto loc_00413B65;
    if ((unsigned __int8)(v_rsi) == 0) goto loc_00413A23;
loc_004138C9:
loc_004138D7:
    result = PpmHeteroIsMultiClassParkingEnabled(*(unsigned __int8 *)(v_rbx + 1178), *(unsigned __int8 *)(a1 + *(unsigned __int64 *)(v_rip + 10439683) * 1 + 182), a3, *(unsigned __int16 *)(v_rbx + 1176));
    if ((unsigned __int8)(result) != 0) goto loc_0041390F;
loc_004138E4:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 11487994)) != 0) goto loc_00413B82;
loc_004138F2:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rbx + 1176))) >= ((unsigned __int16)(*(unsigned __int16 *)(v_rdi)))) goto loc_00413918;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rbx + 1178))) <= ((unsigned __int8)(*(unsigned __int8 *)(a1 + *(unsigned __int64 *)(v_rip + 10439683) * 1 + 182)))) goto loc_00413918;
    a4 = (unsigned __int16)((*(unsigned __int16 *)(v_rbx + 1176)) + (1));
    a3 = (unsigned int)(((unsigned int)(v_stack_p60)) | (1));
    v_stack_p60 = a3;
    goto loc_0041391D;
loc_0041390F:
    if ((*(unsigned __int8 *)(v_rbx + 1185)) == ((unsigned __int8)(a3))) goto loc_004138E4;
loc_00413918:
loc_0041391D:
    result = 0;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 11487994)) != 0) goto loc_00413B94;
loc_0041392C:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rdi + 8))) < ((unsigned __int16)(a4))) goto loc_00413A5E;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rdi + 8))) > ((unsigned __int16)(a4))) goto loc_00413AC7;
loc_0041393C:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rdi + 8))) >= ((unsigned __int16)(*(unsigned __int16 *)(v_rdi)))) {
        a2 = (unsigned __int16)(*(unsigned __int16 *)(v_rdi));
    }
    a3 = 0;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 11487994)) != 0) goto loc_00413BD7;
loc_00413952:
    *(unsigned __int16 *)(v_rdi + 6) = (unsigned __int16)(a2);
    if ((*(unsigned __int8 *)(v_rip + 12267821)) != 0) goto loc_004139EC;
loc_00413963:
    result = PpmEventHgsCoresUnparkedCount(v_rbx, a2, a3, a4);
    result = Feature_PpmParkEx__private_IsEnabledDeviceUsageNoInline(v_rbx, a2, a3, a4);
    v_stack_p50 = (unsigned int)(v_r14);
    v_stack_p48 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + *(unsigned __int64 *)(v_rip + 10439683) * 1 + 188)));
    v_stack_p40 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + *(unsigned __int64 *)(v_rip + 10439683) * 1 + 192)));
    v_stack_p38 = (unsigned __int8)(v_stack_pC0);
    v_stack_p30 = (unsigned __int8)(v_stack_pC8);
    v_stack_p28 = (unsigned int)((unsigned int)(v_stack_p60));
    if ((unsigned int)(result) != 0) goto loc_004139CF;
    v_stack_p20 = (unsigned __int8)(*(unsigned __int8 *)(v_rdi));
    result = PpmEventParkingCountSelection((unsigned __int8)(v_rsi), (unsigned __int8)((unsigned __int16)(*(unsigned __int16 *)(v_rbx + 1176))), *(unsigned __int8 *)(v_rdi + 8), *(unsigned __int8 *)(v_rdi + 6));
loc_004139BA:
    a3 = 0;
    goto loc_00413867;
loc_004139CF:
    v_stack_p20 = (unsigned __int16)(*(unsigned __int16 *)(v_rdi));
    result = PpmEventParkingCountSelectionEx((unsigned __int8)(v_rsi), (unsigned __int16)((unsigned __int16)(*(unsigned __int16 *)(v_rbx + 1176))), *(unsigned __int16 *)(v_rdi + 8), *(unsigned __int16 *)(v_rdi + 6));
    goto loc_004139BA;
loc_004139EC:
    *(unsigned __int16 *)(v_rbx + 1268) = (unsigned __int16)((unsigned __int16)((unsigned __int16)(*(unsigned __int16 *)(v_rbx + 1176))));
    if (((unsigned __int16)((unsigned __int16)((unsigned __int16)(*(unsigned __int16 *)(v_rbx + 1176))))) < ((unsigned __int16)(*(unsigned __int16 *)(v_rbx + 1264)))) goto loc_00413BE9;
    a2 = (unsigned __int16)(((unsigned __int16)((unsigned __int16)(*(unsigned __int16 *)(v_rbx + 1176)))) - ((unsigned __int16)(*(unsigned __int16 *)(v_rbx + 1264))));
loc_00413A06:
    *(unsigned __int16 *)(v_rbx + 1266) = (unsigned __int16)(a2);
    result = PpmHeteroHgsCalculateContainmentCount(v_rbx, v_stack_p60, (unsigned __int16)(*(unsigned __int16 *)(v_rdi + 6)), *(unsigned __int16 *)(v_rdi + 6));
    goto loc_00413963;
loc_00413A23:
    if ((*(unsigned __int8 *)(v_rbx + 1185)) == ((unsigned __int8)((unsigned __int16)(*(unsigned __int16 *)(v_rdi + 6))))) goto loc_004138C9;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rbx + 1288) + 646)) < ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rbx + 1288) + 650)))) goto loc_004138C9;
    goto loc_004138D7;
loc_00413A5E:
    if (((unsigned __int16)(v_stack_p60)) >= ((unsigned __int16)(*(unsigned __int16 *)(v_rdi)))) goto loc_00413942;
    if (((unsigned int)(v_r14)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + *(unsigned __int64 *)(v_rip + 10439683) * 1 + 192))))) goto loc_00413946;
    a3 = (unsigned int)(((unsigned __int16)(*(unsigned __int16 *)(v_rdi + 6))) | (4));
    v_stack_p60 = a3;
    *(unsigned int *)(v_rbx) = (unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rbx + 1288) + 650));
    if ((unsigned int)(v_stack_pC8) == 0) goto loc_00413BCE;
    a1 = (unsigned int)((v_stack_pC8) - (1));
    if (condition_is_equal) goto loc_00413BB3;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00413942;
    if (((unsigned int)(a1)) != 1) goto loc_00413946;
    a1 = (unsigned int)(((unsigned __int16)(v_stack_p60)) + ((unsigned int)(*(unsigned __int16 *)(v_rbx + 1182))));
    if (((unsigned int)(a1)) >= ((unsigned int)(*(unsigned __int16 *)(v_rdi)))) goto loc_00413942;
    a2 = (unsigned __int16)((v_stack_p60) + ((unsigned __int16)(*(unsigned __int16 *)(v_rbx + 1182))));
    goto loc_0041393C;
loc_00413AC7:
    if (((unsigned __int16)(a2)) < ((unsigned __int16)((unsigned __int16)(a3 + 1)))) goto loc_0041393C;
    if (((unsigned int)(v_r14)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + *(unsigned __int64 *)(v_rip + 10439683) * 1 + 188))))) goto loc_0041393C;
    a3 = (unsigned int)((*(unsigned __int16 *)(v_rbx + 1182)) | (8));
    v_stack_p60 = a3;
    *(unsigned int *)(v_rbx) = (unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rbx + 1288) + 650));
    if ((unsigned int)(v_stack_pC0) == 0) goto loc_00413BCE;
    a1 = (unsigned int)((v_stack_pC0) - (1));
    if (condition_is_equal) goto loc_00413BC5;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00413BBC;
    if (((unsigned int)(a1)) != 1) goto loc_0041393C;
    if (((unsigned int)((unsigned __int16)(a2))) <= ((unsigned int)(*(unsigned __int16 *)(v_rbx + 1182) + *(unsigned __int16 *)(v_rip + 11487362) * 1))) goto loc_00413BBC;
    a2 = (unsigned __int16)((a2) - ((unsigned __int16)(*(unsigned __int16 *)(v_rbx + 1182))));
    goto loc_0041393C;
loc_00413B38:
    goto loc_004137D2;
loc_00413B43:
    result = PpmHeteroIsMultiClassParkingEnabled(*(unsigned __int16 *)(v_rbx + 1182) + *(unsigned __int16 *)(v_rip + 11487362) * 1, a2, *(unsigned __int16 *)(v_rbx + 1182), *(unsigned __int16 *)(*(unsigned __int64 *)(v_rbx + 1288) + 634));
    if ((unsigned __int8)(result) == 0) goto loc_00413861;
    goto loc_0041385E;
loc_00413B58:
    goto loc_004138B3;
loc_00413B65:
    if ((*(unsigned __int8 *)(v_rbx + 1185)) == ((unsigned __int8)(*(unsigned __int16 *)(v_rbx + 1182)))) goto loc_004138C9;
    goto loc_004138D7;
loc_00413B82:
    if ((*(unsigned __int16 *)(v_rip + 11487257)) != ((unsigned __int16)((unsigned __int8)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rbx + 1288) + 634))))) goto loc_00413918;
    goto loc_004138F2;
loc_00413B94:
    a2 = 0;
    a3 = (unsigned int)((*(unsigned __int16 *)(v_rbx + 1182)) | (2));
    v_stack_p60 = a3;
    result = 0;
    goto loc_0041392C;
loc_00413BB3:
    a2 = (unsigned __int16)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a2))))) + ((unsigned __int16)(*(unsigned __int16 *)(v_rip + 11487298))));
    goto loc_0041393C;
loc_00413BBC:
    goto loc_0041393C;
loc_00413BC5:
    a2 = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(v_rip + 11487298))) - ((unsigned __int16)(*(unsigned __int16 *)(v_rip + 11487298))));
    goto loc_0041393C;
loc_00413BCE:
    goto loc_0041393C;
loc_00413BD7:
    a2 = (unsigned int)(((unsigned __int16)((unsigned __int16)(*(unsigned __int16 *)(v_rdi + 6)))) * ((unsigned int)(*(unsigned __int16 *)(v_rip + 11487172))));
    goto loc_00413952;
loc_00413BE9:
    *(unsigned __int16 *)(v_rbx + 1268) = (unsigned __int16)(*(unsigned __int16 *)(v_rip + 11487172));
    goto loc_00413A06;
}
```

## 5. (Beta) C Style

```c
int64_t PpmParkCalculateUnparkCount(void *Arg1, int64_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m58;
    uint8_t v_stack_p10;
    uint8_t v_stack_p18;
    uint16_t v_stack_p20;
    uint32_t v_stack_p28;
    uint8_t v_stack_p30;
    uint8_t v_stack_p38;
    uint32_t v_stack_p40;
    uint32_t v_stack_p48;
    uint32_t v_stack_p50;
    uint32_t v_stack_p60;
    uint8_t v_stack_p8;
    uint8_t v_stack_pC0;
    uint8_t v_stack_pC8;
    uint8_t v_stack_pD0;
    uint16_t v_stack_pD8;

    local_rsp = (local_rsp) - (120);
    Arg3 = 0;
    v_stack_m58 = 0;
    if ((*(uint32_t *)(v_rip + 0xAF4C65)) == 0) goto loc_004137E8;
    Arg1 = (Arg1) * ((int32_t)(*(uint32_t *)(v_rip + 0xAF9688)));
    v_stack_p10 = (uint8_t)(*(uint8_t *)(arg1 + *(uint64_t *)(v_rip + 0x9F4C03) * 1 + 0xB9));
    v_stack_p18 = (uint8_t)(*(uint8_t *)(arg1 + *(uint64_t *)(v_rip + 0x9F4C03) * 1 + 0xB6));
    v_stack_p8 = (uint8_t)(*(uint8_t *)(arg1 + *(uint64_t *)(v_rip + 0x9F4C03) * 1 + 0xB8));
    if ((*(uint32_t *)(v_rip + 0xAF7AB2)) == 5) goto loc_00413B38;
loc_004137D2:
    v_stack_p20 = 0;
    if ((*(uint32_t *)(v_rip + 0xAF4C07)) != 0) goto loc_004137FD;
loc_004137E8:
    local_rsp = (local_rsp) + (120);
    return (uint8_t)(Arg3 + 1);
loc_004137FD:
    local_rbx = (local_rbx) * (0);
    local_rbx = (local_rbx) + (*(uint64_t *)(v_rip + 0xAF4BC9));
    if (((*(uint8_t *)(local_rbx + 0x4A0)) & ((uint8_t)(Arg3 + 1))) != 0) goto loc_00413879;
    if ((*(uint8_t *)(local_rbx + 0xC)) <= 0) goto loc_00413879;
loc_00413829:
    local_rdi = (0 + 0 * 4) << (7);
    local_rdi = (local_rdi) + (*(uint64_t *)(local_rbx + 0x508));
    result = (uint8_t)(-(0));
    Arg1 = (uint32_t)((Arg1) & (2));
    Arg1 = (uint32_t)((Arg1) + (2));
    v_stack_p60 = 0;
    if (((*(uint8_t *)(local_rbx + 0x4A0)) & ((uint8_t)(Arg1))) != 0) goto loc_00413B43;
loc_0041385E:
loc_00413861:
    if ((uint16_t)(*(uint16_t *)(local_rdi)) != 0) goto loc_0041389B;
loc_00413867:
    local_rsi = (uint8_t)((0) + ((uint8_t)(Arg3 + 1)));
    if (((uint8_t)(local_rsi)) < (*(uint8_t *)(local_rbx + 0xC))) goto loc_00413829;
loc_00413879:
    local_r14 = (uint16_t)((v_stack_pD8) + ((uint16_t)(Arg3 + 1)));
    v_stack_pD8 = (uint16_t)(local_r14);
    if (((uint32_t)((uint16_t)(local_r14))) >= (*(uint32_t *)(v_rip + 0xAF4B59))) goto loc_004137E8;
    goto loc_004137FD;
loc_0041389B:
    if (0 != 0) goto loc_00413867;
    if ((uint8_t)(*(uint8_t *)(v_rip + 0xAF4AFA)) == 0) goto loc_00413B58;
loc_004138B3:
    result = PpmHeteroIsMultiClassParkingEnabled((uint16_t)(local_r14), *(uint8_t *)(arg1 + *(uint64_t *)(v_rip + 0x9F4C03) * 1 + 0xB6), Arg3, Arg3 + 1);
    if ((uint8_t)(result) != 0) goto loc_00413B65;
    if ((uint8_t)(local_rsi) == 0) goto loc_00413A23;
loc_004138C9:
loc_004138D7:
    result = PpmHeteroIsMultiClassParkingEnabled(*(uint8_t *)(local_rbx + 0x49A), *(uint8_t *)(arg1 + *(uint64_t *)(v_rip + 0x9F4C03) * 1 + 0xB6), Arg3, *(uint16_t *)(local_rbx + 0x498));
    if ((uint8_t)(result) != 0) goto loc_0041390F;
loc_004138E4:
    if ((uint8_t)(*(uint8_t *)(v_rip + 0xAF4AFA)) != 0) goto loc_00413B82;
loc_004138F2:
    if (((uint16_t)(*(uint16_t *)(local_rbx + 0x498))) >= ((uint16_t)(*(uint16_t *)(local_rdi)))) goto loc_00413918;
    if (((uint8_t)(*(uint8_t *)(local_rbx + 0x49A))) <= ((uint8_t)(*(uint8_t *)(arg1 + *(uint64_t *)(v_rip + 0x9F4C03) * 1 + 0xB6)))) goto loc_00413918;
    a4 = (uint16_t)((*(uint16_t *)(local_rbx + 0x498)) + (1));
    Arg3 = (uint32_t)(((uint32_t)(v_stack_p60)) | (1));
    v_stack_p60 = Arg3;
    goto loc_0041391D;
loc_0041390F:
    if ((*(uint8_t *)(local_rbx + 0x4A1)) == ((uint8_t)(Arg3))) goto loc_004138E4;
loc_00413918:
loc_0041391D:
    result = 0;
    if ((uint8_t)(*(uint8_t *)(v_rip + 0xAF4AFA)) != 0) goto loc_00413B94;
loc_0041392C:
    if (((uint16_t)(*(uint16_t *)(local_rdi + 0x8))) < ((uint16_t)(a4))) goto loc_00413A5E;
    if (((uint16_t)(*(uint16_t *)(local_rdi + 0x8))) > ((uint16_t)(a4))) goto loc_00413AC7;
loc_0041393C:
    if (((uint16_t)(*(uint16_t *)(local_rdi + 0x8))) >= ((uint16_t)(*(uint16_t *)(local_rdi)))) {
        Arg2 = (uint16_t)(*(uint16_t *)(local_rdi));
    }
    Arg3 = 0;
    if ((uint8_t)(*(uint8_t *)(v_rip + 0xAF4AFA)) != 0) goto loc_00413BD7;
loc_00413952:
    *(uint16_t *)(local_rdi + 0x6) = (uint16_t)(Arg2);
    if ((*(uint8_t *)(v_rip + 0xBB312D)) != 0) goto loc_004139EC;
loc_00413963:
    result = PpmEventHgsCoresUnparkedCount(local_rbx, Arg2, Arg3, a4);
    result = Feature_PpmParkEx__private_IsEnabledDeviceUsageNoInline(local_rbx, Arg2, Arg3, a4);
    v_stack_p50 = (uint32_t)(local_r14);
    v_stack_p48 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + *(uint64_t *)(v_rip + 0x9F4C03) * 1 + 0xBC)));
    v_stack_p40 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + *(uint64_t *)(v_rip + 0x9F4C03) * 1 + 0xC0)));
    v_stack_p38 = (uint8_t)(v_stack_pC0);
    v_stack_p30 = (uint8_t)(v_stack_pC8);
    v_stack_p28 = (uint32_t)((uint32_t)(v_stack_p60));
    if ((uint32_t)(result) != 0) goto loc_004139CF;
    v_stack_p20 = (uint8_t)(*(uint8_t *)(local_rdi));
    result = PpmEventParkingCountSelection((uint8_t)(local_rsi), (uint8_t)((uint16_t)(*(uint16_t *)(local_rbx + 0x498))), *(uint8_t *)(local_rdi + 0x8), *(uint8_t *)(local_rdi + 0x6));
loc_004139BA:
    Arg3 = 0;
    goto loc_00413867;
loc_004139CF:
    v_stack_p20 = (uint16_t)(*(uint16_t *)(local_rdi));
    result = PpmEventParkingCountSelectionEx((uint8_t)(local_rsi), (uint16_t)((uint16_t)(*(uint16_t *)(local_rbx + 0x498))), *(uint16_t *)(local_rdi + 0x8), *(uint16_t *)(local_rdi + 0x6));
    goto loc_004139BA;
loc_004139EC:
    *(uint16_t *)(local_rbx + 0x4F4) = (uint16_t)((uint16_t)((uint16_t)(*(uint16_t *)(local_rbx + 0x498))));
    if (((uint16_t)((uint16_t)((uint16_t)(*(uint16_t *)(local_rbx + 0x498))))) < ((uint16_t)(*(uint16_t *)(local_rbx + 0x4F0)))) goto loc_00413BE9;
    Arg2 = (uint16_t)(((uint16_t)((uint16_t)(*(uint16_t *)(local_rbx + 0x498)))) - ((uint16_t)(*(uint16_t *)(local_rbx + 0x4F0))));
loc_00413A06:
    *(uint16_t *)(local_rbx + 0x4F2) = (uint16_t)(Arg2);
    result = PpmHeteroHgsCalculateContainmentCount(local_rbx, v_stack_p60, (uint16_t)(*(uint16_t *)(local_rdi + 0x6)), *(uint16_t *)(local_rdi + 0x6));
    goto loc_00413963;
loc_00413A23:
    if ((*(uint8_t *)(local_rbx + 0x4A1)) == ((uint8_t)((uint16_t)(*(uint16_t *)(local_rdi + 0x6))))) goto loc_004138C9;
    if ((*(uint16_t *)(*(uint64_t *)(local_rbx + 0x508) + 0x286)) < ((uint16_t)(*(uint16_t *)(*(uint64_t *)(local_rbx + 0x508) + 0x28A)))) goto loc_004138C9;
    goto loc_004138D7;
loc_00413A5E:
    if (((uint16_t)(v_stack_p60)) >= ((uint16_t)(*(uint16_t *)(local_rdi)))) goto loc_00413942;
    if (((uint32_t)(local_r14)) < ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + *(uint64_t *)(v_rip + 0x9F4C03) * 1 + 0xC0))))) goto loc_00413946;
    Arg3 = (uint32_t)(((uint16_t)(*(uint16_t *)(local_rdi + 0x6))) | (4));
    v_stack_p60 = Arg3;
    *(uint32_t *)(local_rbx) = (uint32_t)(*(uint16_t *)(*(uint64_t *)(local_rbx + 0x508) + 0x28A));
    if ((uint32_t)(v_stack_pC8) == 0) goto loc_00413BCE;
    Arg1 = (uint32_t)((v_stack_pC8) - (1));
    if (condition_is_equal) goto loc_00413BB3;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00413942;
    if (((uint32_t)(Arg1)) != 1) goto loc_00413946;
    Arg1 = (uint32_t)(((uint16_t)(v_stack_p60)) + ((uint32_t)(*(uint16_t *)(local_rbx + 0x49E))));
    if (((uint32_t)(Arg1)) >= ((uint32_t)(*(uint16_t *)(local_rdi)))) goto loc_00413942;
    Arg2 = (uint16_t)((v_stack_p60) + ((uint16_t)(*(uint16_t *)(local_rbx + 0x49E))));
    goto loc_0041393C;
loc_00413AC7:
    if (((uint16_t)(Arg2)) < ((uint16_t)((uint16_t)(Arg3 + 1)))) goto loc_0041393C;
    if (((uint32_t)(local_r14)) < ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + *(uint64_t *)(v_rip + 0x9F4C03) * 1 + 0xBC))))) goto loc_0041393C;
    Arg3 = (uint32_t)((*(uint16_t *)(local_rbx + 0x49E)) | (8));
    v_stack_p60 = Arg3;
    *(uint32_t *)(local_rbx) = (uint32_t)(*(uint16_t *)(*(uint64_t *)(local_rbx + 0x508) + 0x28A));
    if ((uint32_t)(v_stack_pC0) == 0) goto loc_00413BCE;
    Arg1 = (uint32_t)((v_stack_pC0) - (1));
    if (condition_is_equal) goto loc_00413BC5;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00413BBC;
    if (((uint32_t)(Arg1)) != 1) goto loc_0041393C;
    if (((uint32_t)((uint16_t)(Arg2))) <= ((uint32_t)(*(uint16_t *)(local_rbx + 0x49E) + *(uint16_t *)(v_rip + 0xAF4882) * 1))) goto loc_00413BBC;
    Arg2 = (uint16_t)((Arg2) - ((uint16_t)(*(uint16_t *)(local_rbx + 0x49E))));
    goto loc_0041393C;
loc_00413B38:
    goto loc_004137D2;
loc_00413B43:
    result = PpmHeteroIsMultiClassParkingEnabled(*(uint16_t *)(local_rbx + 0x49E) + *(uint16_t *)(v_rip + 0xAF4882) * 1, Arg2, *(uint16_t *)(local_rbx + 0x49E), *(uint16_t *)(*(uint64_t *)(local_rbx + 0x508) + 0x27A));
    if ((uint8_t)(result) == 0) goto loc_00413861;
    goto loc_0041385E;
loc_00413B58:
    goto loc_004138B3;
loc_00413B65:
    if ((*(uint8_t *)(local_rbx + 0x4A1)) == ((uint8_t)(*(uint16_t *)(local_rbx + 0x49E)))) goto loc_004138C9;
    goto loc_004138D7;
loc_00413B82:
    if ((*(uint16_t *)(v_rip + 0xAF4819)) != ((uint16_t)((uint8_t)(*(uint16_t *)(*(uint64_t *)(local_rbx + 0x508) + 0x27A))))) goto loc_00413918;
    goto loc_004138F2;
loc_00413B94:
    Arg2 = 0;
    Arg3 = (uint32_t)((*(uint16_t *)(local_rbx + 0x49E)) | (2));
    v_stack_p60 = Arg3;
    result = 0;
    goto loc_0041392C;
loc_00413BB3:
    Arg2 = (uint16_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg2))))) + ((uint16_t)(*(uint16_t *)(v_rip + 0xAF4842))));
    goto loc_0041393C;
loc_00413BBC:
    goto loc_0041393C;
loc_00413BC5:
    Arg2 = (uint16_t)(((uint16_t)(*(uint16_t *)(v_rip + 0xAF4842))) - ((uint16_t)(*(uint16_t *)(v_rip + 0xAF4842))));
    goto loc_0041393C;
loc_00413BCE:
    goto loc_0041393C;
loc_00413BD7:
    Arg2 = (uint32_t)(((uint16_t)((uint16_t)(*(uint16_t *)(local_rdi + 0x6)))) * ((uint32_t)(*(uint16_t *)(v_rip + 0xAF47C4))));
    goto loc_00413952;
loc_00413BE9:
    *(uint16_t *)(local_rbx + 0x4F4) = (uint16_t)(*(uint16_t *)(v_rip + 0xAF47C4));
    goto loc_00413A06;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xB6 + rdx*1` | `8` | `R` |
| `Arg1` | `+ 0xB8 + rdx*1` | `8` | `R` |
| `Arg1` | `+ 0xB9 + rdx*1` | `8` | `R` |
| `Arg1` | `+ 0xBC + rdx*1` | `32` | `R` |
| `Arg1` | `+ 0xC0 + rdx*1` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00413750&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
