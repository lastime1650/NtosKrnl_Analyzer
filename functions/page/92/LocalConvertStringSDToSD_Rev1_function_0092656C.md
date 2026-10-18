# LocalConvertStringSDToSD_Rev1

- RVA: `0x0092656C`–`0x00926C39` (길이 `1,741` bytes)
- VA: `0x000000014092656C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008D518`
- 디코드: `473`개 명령, `1,741/1,741` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **23**; 고유 호출 대상: **8**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00926670` → [wcsnicmp](../../text/50/wcsnicmp_function_005001C0.md) (function, `0x005001C0`)
- `0x0092672B` → [wcsnicmp](../../text/50/wcsnicmp_function_005001C0.md) (function, `0x005001C0`)
- `0x0092678D` → [LocalGetAclForString](LocalGetAclForString_function_00927F30.md) (function, `0x00927F30`)
- `0x009267D2` → [LocalGetAclForString](LocalGetAclForString_function_00927F30.md) (function, `0x00927F30`)
- `0x00926805` → [PdcCloseEvent](../8D/PdcCloseEvent_function_008D2404.md) (function, `0x008D2404`)
- `0x00926813` → [PdcCloseEvent](../8D/PdcCloseEvent_function_008D2404.md) (function, `0x008D2404`)
- `0x0092681C` → [PdcCloseEvent](../8D/PdcCloseEvent_function_008D2404.md) (function, `0x008D2404`)
- `0x00926825` → [PdcCloseEvent](../8D/PdcCloseEvent_function_008D2404.md) (function, `0x008D2404`)
- `0x00926894` → [LookupSidInTable](LookupSidInTable_function_009293C0.md) (function, `0x009293C0`)
- `0x0092691E` → [LookupSidInTable](LookupSidInTable_function_009293C0.md) (function, `0x009293C0`)
- `0x0092696D` → [LocalpConvertStringSidToSid](../A1/LocalpConvertStringSidToSid_function_00A17490.md) (function, `0x00A17490`)
- `0x009269A7` → [LocalpConvertStringSidToSid](../A1/LocalpConvertStringSidToSid_function_00A17490.md) (function, `0x00A17490`)
- `0x009269D4` → [RtlNtStatusToDosError](RtlNtStatusToDosError_function_00926C40.md) (function, `0x00926C40`)
- `0x00926ACF` → [RtlMakeSelfRelativeSD](../A1/RtlMakeSelfRelativeSD_function_00A119D4.md) (function, `0x00A119D4`)
- `0x00926AE0` → [SddlpAlloc](SddlpAlloc_function_00925F88.md) (function, `0x00925F88`)
- `0x00926B02` → [RtlMakeSelfRelativeSD](../A1/RtlMakeSelfRelativeSD_function_00A119D4.md) (function, `0x00A119D4`)
- `0x00926B0D` → [RtlNtStatusToDosError](RtlNtStatusToDosError_function_00926C40.md) (function, `0x00926C40`)
- `0x00926B17` → [PdcCloseEvent](../8D/PdcCloseEvent_function_008D2404.md) (function, `0x008D2404`)
- `0x00926B6F` → [RtlNtStatusToDosError](RtlNtStatusToDosError_function_00926C40.md) (function, `0x00926C40`)
- `0x00926B91` → [RtlNtStatusToDosError](RtlNtStatusToDosError_function_00926C40.md) (function, `0x00926C40`)
- `0x00926BA7` → [RtlNtStatusToDosError](RtlNtStatusToDosError_function_00926C40.md) (function, `0x00926C40`)
- `0x00926BBF` → [RtlNtStatusToDosError](RtlNtStatusToDosError_function_00926C40.md) (function, `0x00926C40`)
- `0x00926BF7` → [RtlNtStatusToDosError](RtlNtStatusToDosError_function_00926C40.md) (function, `0x00926C40`)

### Direct callers
- [SeConvertStringSecurityDescriptorToSecurityDescriptor](../../text/48/SeConvertStringSecurityDescriptorToSecurityDescriptor_function_00480000.md) at `0x00480020`

### Static image references
- `0x009265F0` → RVA `0x00002B20` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00926670` → [wcsnicmp](../../text/50/wcsnicmp_function_005001C0.md) (`PAGE` → `.text`)
  - `0x0092672B` → [wcsnicmp](../../text/50/wcsnicmp_function_005001C0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0092656C  48 8B C4                        mov rax, rsp
0092656F  44 88 40 18                     mov byte ptr [rax + 0x18], r8b
00926573  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
00926577  48 89 48 08                     mov qword ptr [rax + 8], rcx
0092657B  55                              push rbp
0092657C  53                              push rbx
0092657D  56                              push rsi
0092657E  57                              push rdi
0092657F  41 54                           push r12
00926581  41 55                           push r13
00926583  41 56                           push r14
00926585  41 57                           push r15
00926587  48 8D 68 B1                     lea rbp, [rax - 0x4f]
0092658B  48 81 EC A8 00 00 00            sub rsp, 0xa8
00926592  33 D2                           xor edx, edx
00926594  49 8B D9                        mov rbx, r9
00926597  48 89 55 B7                     mov qword ptr [rbp - 0x49], rdx
0092659B  8B FA                           mov edi, edx
0092659D  48 89 55 BF                     mov qword ptr [rbp - 0x41], rdx
009265A1  44 8B E2                        mov r12d, edx
009265A4  48 89 55 CF                     mov qword ptr [rbp - 0x31], rdx
009265A8  44 8B FA                        mov r15d, edx
009265AB  48 89 55 D7                     mov qword ptr [rbp - 0x29], rdx
009265AF  44 8A EA                        mov r13b, dl
009265B2  48 89 55 A7                     mov qword ptr [rbp - 0x59], rdx
009265B6  44 8A F2                        mov r14b, dl
009265B9  88 55 67                        mov byte ptr [rbp + 0x67], dl
009265BC  89 55 B3                        mov dword ptr [rbp - 0x4d], edx
009265BF  88 55 5F                        mov byte ptr [rbp + 0x5f], dl
009265C2  88 55 57                        mov byte ptr [rbp + 0x57], dl
009265C5  66 89 55 AF                     mov word ptr [rbp - 0x51], dx
009265C9  66 89 55 6F                     mov word ptr [rbp + 0x6f], dx
009265CD  4D 85 C9                        test r9, r9
009265D0  0F 84 59 06 00 00               je 0x140926c2f
009265D6  48 39 55 77                     cmp qword ptr [rbp + 0x77], rdx
009265DA  0F 84 4F 06 00 00               je 0x140926c2f
009265E0  48 8B 45 7F                     mov rax, qword ptr [rbp + 0x7f]
009265E4  48 85 C0                        test rax, rax
009265E7  74 02                           je 0x1409265eb
009265E9  89 10                           mov dword ptr [rax], edx
009265EB  BE 57 00 00 00                  mov esi, 0x57
009265F0  4C 8D 0D 29 C5 6D FF            lea r9, [rip - 0x923ad7]
009265F7  B9 04 00 00 00                  mov ecx, 4
009265FC  48 85 DB                        test rbx, rbx
009265FF  0F 84 EF 01 00 00               je 0x1409267f4
00926605  0F B7 03                        movzx eax, word ptr [rbx]
00926608  66 85 C0                        test ax, ax
0092660B  0F 84 DB 01 00 00               je 0x1409267ec
00926611  66 83 F8 44                     cmp ax, 0x44
00926615  0F 85 93 00 00 00               jne 0x1409266ae
0092661B  66 83 7B 02 3A                  cmp word ptr [rbx + 2], 0x3a
00926620  0F 85 A5 03 00 00               jne 0x1409269cb
00926626  48 03 D9                        add rbx, rcx
00926629  48 39 55 CF                     cmp qword ptr [rbp - 0x31], rdx
0092662D  0F 85 98 03 00 00               jne 0x1409269cb
00926633  66 83 3B 28                     cmp word ptr [rbx], 0x28
00926637  0F 84 30 01 00 00               je 0x14092676d
0092663D  89 55 AF                        mov dword ptr [rbp - 0x51], edx
00926640  66 83 3B 20                     cmp word ptr [rbx], 0x20
00926644  0F 84 D6 05 00 00               je 0x140926c20
0092664A  8B FA                           mov edi, edx
0092664C  83 FF 06                        cmp edi, 6
0092664F  0F 83 14 01 00 00               jae 0x140926769
00926655  8B C7                           mov eax, edi
00926657  4C 8D 34 40                     lea r14, [rax + rax*2]
0092665B  43 8B 44 F1 10                  mov eax, dword ptr [r9 + r14*8 + 0x10]
00926660  A8 01                           test al, 1
00926662  74 1E                           je 0x140926682
00926664  47 8B 44 F1 08                  mov r8d, dword ptr [r9 + r14*8 + 8]
00926669  48 8B CB                        mov rcx, rbx
0092666C  4B 8B 14 F1                     mov rdx, qword ptr [r9 + r14*8]
00926670  E8 4B 9B BD FF                  call 0x1405001c0
00926675  33 D2                           xor edx, edx
00926677  4C 8D 0D A2 C4 6D FF            lea r9, [rip - 0x923b5e]
0092667E  85 C0                           test eax, eax
00926680  74 04                           je 0x140926686
00926682  FF C7                           inc edi
00926684  EB C6                           jmp 0x14092664c
00926686  8B 4D AF                        mov ecx, dword ptr [rbp - 0x51]
00926689  66 43 0B 4C F1 0C               or cx, word ptr [r9 + r14*8 + 0xc]
0092668F  43 8B 44 F1 08                  mov eax, dword ptr [r9 + r14*8 + 8]
00926694  89 4D AF                        mov dword ptr [rbp - 0x51], ecx
00926697  48 8D 1C 43                     lea rbx, [rbx + rax*2]
0092669B  48 85 DB                        test rbx, rbx
0092669E  74 AA                           je 0x14092664a
009266A0  66 83 3B 20                     cmp word ptr [rbx], 0x20
009266A4  75 A4                           jne 0x14092664a
009266A6  48 83 C3 02                     add rbx, 2
009266AA  75 F4                           jne 0x1409266a0
009266AC  EB 9C                           jmp 0x14092664a
009266AE  66 83 F8 47                     cmp ax, 0x47
009266B2  0F 84 0B 02 00 00               je 0x1409268c3
009266B8  66 83 F8 4F                     cmp ax, 0x4f
009266BC  0F 84 7F 01 00 00               je 0x140926841
009266C2  66 83 F8 20                     cmp ax, 0x20
009266C6  0F 84 77 02 00 00               je 0x140926943
009266CC  66 83 F8 53                     cmp ax, 0x53
009266D0  0F 85 F5 02 00 00               jne 0x1409269cb
009266D6  66 83 7B 02 3A                  cmp word ptr [rbx + 2], 0x3a
009266DB  0F 85 EA 02 00 00               jne 0x1409269cb
009266E1  48 03 D9                        add rbx, rcx
009266E4  48 39 55 D7                     cmp qword ptr [rbp - 0x29], rdx
009266E8  0F 85 DD 02 00 00               jne 0x1409269cb
009266EE  66 83 3B 28                     cmp word ptr [rbx], 0x28
009266F2  0F 84 BA 00 00 00               je 0x1409267b2
009266F8  89 55 6F                        mov dword ptr [rbp + 0x6f], edx
009266FB  66 83 3B 20                     cmp word ptr [rbx], 0x20
009266FF  0F 84 0C 05 00 00               je 0x140926c11
00926705  8B FA                           mov edi, edx
00926707  83 FF 06                        cmp edi, 6
0092670A  0F 83 9A 00 00 00               jae 0x1409267aa
00926710  8B C7                           mov eax, edi
00926712  4C 8D 34 40                     lea r14, [rax + rax*2]
00926716  43 8B 44 F1 10                  mov eax, dword ptr [r9 + r14*8 + 0x10]
0092671B  A8 02                           test al, 2
0092671D  74 1E                           je 0x14092673d
0092671F  47 8B 44 F1 08                  mov r8d, dword ptr [r9 + r14*8 + 8]
00926724  48 8B CB                        mov rcx, rbx
00926727  4B 8B 14 F1                     mov rdx, qword ptr [r9 + r14*8]
0092672B  E8 90 9A BD FF                  call 0x1405001c0
00926730  33 D2                           xor edx, edx
00926732  4C 8D 0D E7 C3 6D FF            lea r9, [rip - 0x923c19]
00926739  85 C0                           test eax, eax
0092673B  74 04                           je 0x140926741
0092673D  FF C7                           inc edi
0092673F  EB C6                           jmp 0x140926707
00926741  8B 4D 6F                        mov ecx, dword ptr [rbp + 0x6f]
00926744  66 43 0B 4C F1 0C               or cx, word ptr [r9 + r14*8 + 0xc]
0092674A  43 8B 44 F1 08                  mov eax, dword ptr [r9 + r14*8 + 8]
0092674F  89 4D 6F                        mov dword ptr [rbp + 0x6f], ecx
00926752  48 8D 1C 43                     lea rbx, [rbx + rax*2]
00926756  48 85 DB                        test rbx, rbx
00926759  74 AA                           je 0x140926705
0092675B  66 83 3B 20                     cmp word ptr [rbx], 0x20
0092675F  75 A4                           jne 0x140926705
00926761  48 83 C3 02                     add rbx, 2
00926765  75 F4                           jne 0x14092675b
00926767  EB 9C                           jmp 0x140926705
00926769  48 89 5D A7                     mov qword ptr [rbp - 0x59], rbx
0092676D  88 54 24 38                     mov byte ptr [rsp + 0x38], dl
00926771  4C 8D 4D A7                     lea r9, [rbp - 0x59]
00926775  48 89 54 24 30                  mov qword ptr [rsp + 0x30], rdx
0092677A  4C 8D 45 CF                     lea r8, [rbp - 0x31]
0092677E  48 89 54 24 28                  mov qword ptr [rsp + 0x28], rdx
00926783  48 8B CB                        mov rcx, rbx
00926786  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
0092678B  B2 01                           mov dl, 1
0092678D  E8 9E 17 00 00                  call 0x140927f30
00926792  33 D2                           xor edx, edx
00926794  8B F8                           mov edi, eax
00926796  85 C0                           test eax, eax
00926798  75 62                           jne 0x1409267fc
0092679A  48 8B 5D A7                     mov rbx, qword ptr [rbp - 0x59]
0092679E  41 B6 01                        mov r14b, 1
009267A1  44 88 75 5F                     mov byte ptr [rbp + 0x5f], r14b
009267A5  E9 46 FE FF FF                  jmp 0x1409265f0
009267AA  44 8A 75 5F                     mov r14b, byte ptr [rbp + 0x5f]
009267AE  48 89 5D A7                     mov qword ptr [rbp - 0x59], rbx
009267B2  88 54 24 38                     mov byte ptr [rsp + 0x38], dl
009267B6  4C 8D 4D A7                     lea r9, [rbp - 0x59]
009267BA  48 89 54 24 30                  mov qword ptr [rsp + 0x30], rdx
009267BF  4C 8D 45 D7                     lea r8, [rbp - 0x29]
009267C3  48 89 54 24 28                  mov qword ptr [rsp + 0x28], rdx
009267C8  48 8B CB                        mov rcx, rbx
009267CB  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
009267D0  33 D2                           xor edx, edx
009267D2  E8 59 17 00 00                  call 0x140927f30
009267D7  33 D2                           xor edx, edx
009267D9  8B F8                           mov edi, eax
009267DB  85 C0                           test eax, eax
009267DD  75 1D                           jne 0x1409267fc
009267DF  48 8B 5D A7                     mov rbx, qword ptr [rbp - 0x59]
009267E3  C6 45 57 01                     mov byte ptr [rbp + 0x57], 1
009267E7  E9 04 FE FF FF                  jmp 0x1409265f0
009267EC  48 8B DA                        mov rbx, rdx
009267EF  E9 08 FE FF FF                  jmp 0x1409265fc
009267F4  85 FF                           test edi, edi
009267F6  0F 84 13 02 00 00               je 0x140926a0f
009267FC  80 7D 67 01                     cmp byte ptr [rbp + 0x67], 1
00926800  75 08                           jne 0x14092680a
00926802  49 8B CC                        mov rcx, r12
00926805  E8 FA BB FA FF                  call 0x1408d2404
0092680A  41 80 FD 01                     cmp r13b, 1
0092680E  75 08                           jne 0x140926818
00926810  49 8B CF                        mov rcx, r15
00926813  E8 EC BB FA FF                  call 0x1408d2404
00926818  48 8B 4D CF                     mov rcx, qword ptr [rbp - 0x31]
0092681C  E8 E3 BB FA FF                  call 0x1408d2404
00926821  48 8B 4D D7                     mov rcx, qword ptr [rbp - 0x29]
00926825  E8 DA BB FA FF                  call 0x1408d2404
0092682A  8B C7                           mov eax, edi
0092682C  48 81 C4 A8 00 00 00            add rsp, 0xa8
00926833  41 5F                           pop r15
00926835  41 5E                           pop r14
00926837  41 5D                           pop r13
00926839  41 5C                           pop r12
0092683B  5F                              pop rdi
0092683C  5E                              pop rsi
0092683D  5B                              pop rbx
0092683E  5D                              pop rbp
0092683F  C3                              ret
00926840  CC                              int3
00926841  66 83 7B 02 3A                  cmp word ptr [rbx + 2], 0x3a
00926846  8B FE                           mov edi, esi
00926848  75 B2                           jne 0x1409267fc
0092684A  48 03 D9                        add rbx, rcx
0092684D  4D 85 E4                        test r12, r12
00926850  75 AA                           jne 0x1409267fc
00926852  48 89 55 C7                     mov qword ptr [rbp - 0x39], rdx
00926856  8B FA                           mov edi, edx
00926858  48 85 DB                        test rbx, rbx
0092685B  0F 84 6A 01 00 00               je 0x1409269cb
00926861  88 55 67                        mov byte ptr [rbp + 0x67], dl
00926864  66 39 13                        cmp word ptr [rbx], dx
00926867  0F 84 8E 01 00 00               je 0x1409269fb
0092686D  66 39 53 02                     cmp word ptr [rbx + 2], dx
00926871  0F 84 84 01 00 00               je 0x1409269fb
00926877  48 8D 43 04                     lea rax, [rbx + 4]
0092687B  45 33 C0                        xor r8d, r8d
0092687E  48 89 45 A7                     mov qword ptr [rbp - 0x59], rax
00926882  48 8B CB                        mov rcx, rbx
00926885  48 8D 45 C7                     lea rax, [rbp - 0x39]
00926889  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0092688E  88 54 24 28                     mov byte ptr [rsp + 0x28], dl
00926892  33 D2                           xor edx, edx
00926894  E8 27 2B 00 00                  call 0x1409293c0
00926899  33 D2                           xor edx, edx
0092689B  48 85 C0                        test rax, rax
0092689E  0F 84 A8 00 00 00               je 0x14092694c
009268A4  4C 8B 60 10                     mov r12, qword ptr [rax + 0x10]
009268A8  40 8A C7                        mov al, dil
009268AB  4C 89 65 B7                     mov qword ptr [rbp - 0x49], r12
009268AF  85 FF                           test edi, edi
009268B1  0F 85 45 FF FF FF               jne 0x1409267fc
009268B7  48 8B 5D A7                     mov rbx, qword ptr [rbp - 0x59]
009268BB  88 45 67                        mov byte ptr [rbp + 0x67], al
009268BE  E9 2D FD FF FF                  jmp 0x1409265f0
009268C3  66 83 7B 02 3A                  cmp word ptr [rbx + 2], 0x3a
009268C8  8B FE                           mov edi, esi
009268CA  0F 85 2C FF FF FF               jne 0x1409267fc
009268D0  48 03 D9                        add rbx, rcx
009268D3  4D 85 FF                        test r15, r15
009268D6  0F 85 20 FF FF FF               jne 0x1409267fc
009268DC  48 89 55 C7                     mov qword ptr [rbp - 0x39], rdx
009268E0  8B FA                           mov edi, edx
009268E2  48 85 DB                        test rbx, rbx
009268E5  0F 84 E0 00 00 00               je 0x1409269cb
009268EB  44 8A EA                        mov r13b, dl
009268EE  66 39 13                        cmp word ptr [rbx], dx
009268F1  0F 84 0E 01 00 00               je 0x140926a05
009268F7  66 39 53 02                     cmp word ptr [rbx + 2], dx
009268FB  0F 84 04 01 00 00               je 0x140926a05
00926901  48 8D 43 04                     lea rax, [rbx + 4]
00926905  45 33 C0                        xor r8d, r8d
00926908  48 89 45 A7                     mov qword ptr [rbp - 0x59], rax
0092690C  48 8B CB                        mov rcx, rbx
0092690F  48 8D 45 C7                     lea rax, [rbp - 0x39]
00926913  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00926918  88 54 24 28                     mov byte ptr [rsp + 0x28], dl
0092691C  33 D2                           xor edx, edx
0092691E  E8 9D 2A 00 00                  call 0x1409293c0
00926923  33 D2                           xor edx, edx
00926925  48 85 C0                        test rax, rax
00926928  74 61                           je 0x14092698b
0092692A  4C 8B 78 10                     mov r15, qword ptr [rax + 0x10]
0092692E  4C 89 7D BF                     mov qword ptr [rbp - 0x41], r15
00926932  85 FF                           test edi, edi
00926934  0F 85 C2 FE FF FF               jne 0x1409267fc
0092693A  48 8B 5D A7                     mov rbx, qword ptr [rbp - 0x59]
0092693E  E9 AD FC FF FF                  jmp 0x1409265f0
00926943  48 83 C3 02                     add rbx, 2
00926947  E9 B0 FC FF FF                  jmp 0x1409265fc
0092694C  4C 8B 65 C7                     mov r12, qword ptr [rbp - 0x39]
00926950  4D 85 E4                        test r12, r12
00926953  0F 85 94 00 00 00               jne 0x1409269ed
00926959  41 8D 44 24 04                  lea eax, [r12 + 4]
0092695E  48 8B CB                        mov rcx, rbx
00926961  48 29 45 A7                     sub qword ptr [rbp - 0x59], rax
00926965  4C 8D 45 A7                     lea r8, [rbp - 0x59]
00926969  48 8D 55 B7                     lea rdx, [rbp - 0x49]
0092696D  E8 1E 0B 0F 00                  call 0x140a17490
00926972  33 D2                           xor edx, edx
00926974  85 C0                           test eax, eax
00926976  78 5A                           js 0x1409269d2
00926978  4C 8B 65 B7                     mov r12, qword ptr [rbp - 0x49]
0092697C  4D 85 E4                        test r12, r12
0092697F  74 64                           je 0x1409269e5
00926981  B0 01                           mov al, 1
00926983  88 45 67                        mov byte ptr [rbp + 0x67], al
00926986  E9 24 FF FF FF                  jmp 0x1409268af
0092698B  4C 8B 7D C7                     mov r15, qword ptr [rbp - 0x39]
0092698F  4D 85 FF                        test r15, r15
00926992  75 5F                           jne 0x1409269f3
00926994  41 8D 47 04                     lea eax, [r15 + 4]
00926998  48 8B CB                        mov rcx, rbx
0092699B  48 29 45 A7                     sub qword ptr [rbp - 0x59], rax
0092699F  4C 8D 45 A7                     lea r8, [rbp - 0x59]
009269A3  48 8D 55 BF                     lea rdx, [rbp - 0x41]
009269A7  E8 E4 0A 0F 00                  call 0x140a17490
009269AC  33 D2                           xor edx, edx
009269AE  85 C0                           test eax, eax
009269B0  0F 88 3F 02 00 00               js 0x140926bf5
009269B6  4C 8B 7D BF                     mov r15, qword ptr [rbp - 0x41]
009269BA  4D 85 FF                        test r15, r15
009269BD  0F 84 6F FF FF FF               je 0x140926932
009269C3  41 B5 01                        mov r13b, 1
009269C6  E9 67 FF FF FF                  jmp 0x140926932
009269CB  8B FE                           mov edi, esi
009269CD  E9 2A FE FF FF                  jmp 0x1409267fc
009269D2  8B C8                           mov ecx, eax
009269D4  E8 67 02 00 00                  call 0x140926c40
009269D9  33 D2                           xor edx, edx
009269DB  8B F8                           mov edi, eax
009269DD  85 C0                           test eax, eax
009269DF  74 97                           je 0x140926978
009269E1  4C 8B 65 B7                     mov r12, qword ptr [rbp - 0x49]
009269E5  8A 45 67                        mov al, byte ptr [rbp + 0x67]
009269E8  E9 C2 FE FF FF                  jmp 0x1409268af
009269ED  4C 89 65 B7                     mov qword ptr [rbp - 0x49], r12
009269F1  EB 8E                           jmp 0x140926981
009269F3  41 B5 01                        mov r13b, 1
009269F6  E9 33 FF FF FF                  jmp 0x14092692e
009269FB  BF 34 05 00 00                  mov edi, 0x534
00926A00  E9 05 FE FF FF                  jmp 0x14092680a
00926A05  BF 34 05 00 00                  mov edi, 0x534
00926A0A  E9 ED FD FF FF                  jmp 0x1409267fc
00926A0F  33 C0                           xor eax, eax
00926A11  0F 57 C0                        xorps xmm0, xmm0
00926A14  0F 11 45 DF                     movups xmmword ptr [rbp - 0x21], xmm0
00926A18  0F B7 5D E1                     movzx ebx, word ptr [rbp - 0x1f]
00926A1C  BE 79 00 00 C0                  mov esi, 0xc0000079
00926A21  48 89 45 FF                     mov qword ptr [rbp - 1], rax
00926A25  8B 45 6F                        mov eax, dword ptr [rbp + 0x6f]
00926A28  66 0B D8                        or bx, ax
00926A2B  8B 45 AF                        mov eax, dword ptr [rbp - 0x51]
00926A2E  66 0B D8                        or bx, ax
00926A31  C6 45 DF 01                     mov byte ptr [rbp - 0x21], 1
00926A35  0F B7 C3                        movzx eax, bx
00926A38  66 89 5D E1                     mov word ptr [rbp - 0x1f], bx
00926A3C  0F 11 45 EF                     movups xmmword ptr [rbp - 0x11], xmm0
00926A40  4D 85 E4                        test r12, r12
00926A43  0F 85 8F 01 00 00               jne 0x140926bd8
00926A49  4D 85 FF                        test r15, r15
00926A4C  0F 85 01 01 00 00               jne 0x140926b53
00926A52  45 84 F6                        test r14b, r14b
00926A55  74 2B                           je 0x140926a82
00926A57  66 85 DB                        test bx, bx
00926A5A  0F 88 0D 01 00 00               js 0x140926b6d
00926A60  48 8B 45 CF                     mov rax, qword ptr [rbp - 0x31]
00926A64  66 83 CB 04                     or bx, 4
00926A68  48 85 C0                        test rax, rax
00926A6B  48 8B CA                        mov rcx, rdx
00926A6E  48 0F 45 C8                     cmovne rcx, rax
00926A72  B8 F7 FF 00 00                  mov eax, 0xfff7
00926A77  66 23 D8                        and bx, ax
00926A7A  48 89 4D FF                     mov qword ptr [rbp - 1], rcx
00926A7E  66 89 5D E1                     mov word ptr [rbp - 0x1f], bx
00926A82  38 55 57                        cmp byte ptr [rbp + 0x57], dl
00926A85  74 2B                           je 0x140926ab2
00926A87  66 85 DB                        test bx, bx
00926A8A  0F 88 FF 00 00 00               js 0x140926b8f
00926A90  48 8B 45 D7                     mov rax, qword ptr [rbp - 0x29]
00926A94  66 83 CB 10                     or bx, 0x10
00926A98  48 85 C0                        test rax, rax
00926A9B  48 8B CA                        mov rcx, rdx
00926A9E  48 0F 45 C8                     cmovne rcx, rax
00926AA2  B8 DF FF 00 00                  mov eax, 0xffdf
00926AA7  66 23 D8                        and bx, ax
00926AAA  48 89 4D F7                     mov qword ptr [rbp - 9], rcx
00926AAE  66 89 5D E1                     mov word ptr [rbp - 0x1f], bx
00926AB2  4C 8B 75 77                     mov r14, qword ptr [rbp + 0x77]
00926AB6  BE 00 80 00 00                  mov esi, 0x8000
00926ABB  49 8B 16                        mov rdx, qword ptr [r14]
00926ABE  66 85 DE                        test si, bx
00926AC1  0F 85 82 00 00 00               jne 0x140926b49
00926AC7  4C 8D 45 B3                     lea r8, [rbp - 0x4d]
00926ACB  48 8D 4D DF                     lea rcx, [rbp - 0x21]
00926ACF  E8 00 AF 0E 00                  call 0x140a119d4
00926AD4  3D 23 00 00 C0                  cmp eax, 0xc0000023
00926AD9  75 6E                           jne 0x140926b49
00926ADB  8B 4D B3                        mov ecx, dword ptr [rbp - 0x4d]
00926ADE  33 FF                           xor edi, edi
00926AE0  E8 A3 F4 FF FF                  call 0x140925f88
00926AE5  49 89 06                        mov qword ptr [r14], rax
00926AE8  48 85 C0                        test rax, rax
00926AEB  74 52                           je 0x140926b3f
00926AED  66 85 75 E1                     test word ptr [rbp - 0x1f], si
00926AF1  0F 85 8E 00 00 00               jne 0x140926b85
00926AF7  4C 8D 45 B3                     lea r8, [rbp - 0x4d]
00926AFB  48 8B D0                        mov rdx, rax
00926AFE  48 8D 4D DF                     lea rcx, [rbp - 0x21]
00926B02  E8 CD AE 0E 00                  call 0x140a119d4
00926B07  85 C0                           test eax, eax
00926B09  79 1D                           jns 0x140926b28
00926B0B  8B C8                           mov ecx, eax
00926B0D  E8 2E 01 00 00                  call 0x140926c40
00926B12  49 8B 0E                        mov rcx, qword ptr [r14]
00926B15  8B F8                           mov edi, eax
00926B17  E8 E8 B8 FA FF                  call 0x1408d2404
00926B1C  49 83 26 00                     and qword ptr [r14], 0
00926B20  85 FF                           test edi, edi
00926B22  0F 85 D4 FC FF FF               jne 0x1409267fc
00926B28  48 8B 4D 7F                     mov rcx, qword ptr [rbp + 0x7f]
00926B2C  48 85 C9                        test rcx, rcx
00926B2F  0F 84 C7 FC FF FF               je 0x1409267fc
00926B35  8B 45 B3                        mov eax, dword ptr [rbp - 0x4d]
00926B38  89 01                           mov dword ptr [rcx], eax
00926B3A  E9 BD FC FF FF                  jmp 0x1409267fc
00926B3F  BF 08 00 00 00                  mov edi, 8
00926B44  E9 B3 FC FF FF                  jmp 0x1409267fc
00926B49  BF 7A 00 00 00                  mov edi, 0x7a
00926B4E  E9 A9 FC FF FF                  jmp 0x1409267fc
00926B53  66 85 C0                        test ax, ax
00926B56  78 4D                           js 0x140926ba5
00926B58  B8 FD FF 00 00                  mov eax, 0xfffd
00926B5D  4C 89 7D EF                     mov qword ptr [rbp - 0x11], r15
00926B61  66 23 D8                        and bx, ax
00926B64  66 89 5D E1                     mov word ptr [rbp - 0x1f], bx
00926B68  E9 E5 FE FF FF                  jmp 0x140926a52
00926B6D  8B CE                           mov ecx, esi
00926B6F  E8 CC 00 00 00                  call 0x140926c40
00926B74  33 D2                           xor edx, edx
00926B76  8B F8                           mov edi, eax
00926B78  85 C0                           test eax, eax
00926B7A  0F 85 7C FC FF FF               jne 0x1409267fc
00926B80  E9 FD FE FF FF                  jmp 0x140926a82
00926B85  B8 E7 00 00 C0                  mov eax, 0xc00000e7
00926B8A  E9 7C FF FF FF                  jmp 0x140926b0b
00926B8F  8B CE                           mov ecx, esi
00926B91  E8 AA 00 00 00                  call 0x140926c40
00926B96  8B F8                           mov edi, eax
00926B98  85 C0                           test eax, eax
00926B9A  0F 84 12 FF FF FF               je 0x140926ab2
00926BA0  E9 57 FC FF FF                  jmp 0x1409267fc
00926BA5  8B CE                           mov ecx, esi
00926BA7  E8 94 00 00 00                  call 0x140926c40
00926BAC  33 D2                           xor edx, edx
00926BAE  8B F8                           mov edi, eax
00926BB0  85 C0                           test eax, eax
00926BB2  0F 84 9A FE FF FF               je 0x140926a52
00926BB8  E9 3F FC FF FF                  jmp 0x1409267fc
00926BBD  8B CE                           mov ecx, esi
00926BBF  E8 7C 00 00 00                  call 0x140926c40
00926BC4  8B F8                           mov edi, eax
00926BC6  33 D2                           xor edx, edx
00926BC8  0F B7 C3                        movzx eax, bx
00926BCB  85 FF                           test edi, edi
00926BCD  0F 85 29 FC FF FF               jne 0x1409267fc
00926BD3  E9 71 FE FF FF                  jmp 0x140926a49
00926BD8  66 85 DB                        test bx, bx
00926BDB  78 E0                           js 0x140926bbd
00926BDD  B8 FE FF 00 00                  mov eax, 0xfffe
00926BE2  4C 89 65 E7                     mov qword ptr [rbp - 0x19], r12
00926BE6  66 23 D8                        and bx, ax
00926BE9  66 89 5D E1                     mov word ptr [rbp - 0x1f], bx
00926BED  0F B7 C3                        movzx eax, bx
00926BF0  E9 54 FE FF FF                  jmp 0x140926a49
00926BF5  8B C8                           mov ecx, eax
00926BF7  E8 44 00 00 00                  call 0x140926c40
00926BFC  33 D2                           xor edx, edx
00926BFE  8B F8                           mov edi, eax
00926C00  85 C0                           test eax, eax
00926C02  0F 84 AE FD FF FF               je 0x1409269b6
00926C08  4C 8B 7D BF                     mov r15, qword ptr [rbp - 0x41]
00926C0C  E9 21 FD FF FF                  jmp 0x140926932
00926C11  48 83 C3 02                     add rbx, 2
00926C15  0F 85 E0 FA FF FF               jne 0x1409266fb
00926C1B  E9 E5 FA FF FF                  jmp 0x140926705
00926C20  48 83 C3 02                     add rbx, 2
00926C24  0F 85 16 FA FF FF               jne 0x140926640
00926C2A  E9 1B FA FF FF                  jmp 0x14092664a
00926C2F  B8 57 00 00 00                  mov eax, 0x57
00926C34  E9 F3 FB FF FF                  jmp 0x14092682c
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall LocalConvertStringSDToSD_Rev1(__int64 a1, __int64 a2, unsigned __int8 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int8 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int8 v_stack_p28;
    unsigned __int64 v_stack_p30;

    *(unsigned __int8 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (168);
    a2 = 0;
    *(unsigned __int64 *)(v_rsp - 79 - 73) = 0;
    *(unsigned __int64 *)(v_rsp - 79 - 65) = 0;
    *(unsigned __int64 *)(v_rsp - 79 - 49) = 0;
    *(unsigned __int64 *)(v_rsp - 79 - 41) = 0;
    *(unsigned __int64 *)(v_rsp - 79 - 89) = 0;
    *(unsigned __int8 *)(v_rsp - 79 + 103) = 0;
    *(unsigned int *)(v_rsp - 79 - 77) = 0;
    *(unsigned __int8 *)(v_rsp - 79 + 95) = 0;
    *(unsigned __int8 *)(v_rsp - 79 + 87) = 0;
    *(unsigned __int16 *)(v_rsp - 79 - 81) = 0;
    *(unsigned __int16 *)(v_rsp - 79 + 111) = 0;
    if (a4 == 0) goto loc_00926C2F;
    if ((*(unsigned __int64 *)(v_rsp - 79 + 119)) == 0) goto loc_00926C2F;
    if (*(unsigned __int64 *)(v_rsp - 79 + 127) != 0) {
        *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 79 + 127)) = 0;
    }
loc_009265F0:
loc_009265FC:
    if (a4 == 0) goto loc_009267F4;
    if ((unsigned __int16)(*(unsigned __int16 *)(a4)) == 0) goto loc_009267EC;
    if (((unsigned __int16)(*(unsigned __int16 *)(a4))) != 68) goto loc_009266AE;
    if ((*(unsigned __int16 *)(a4 + 2)) != 58) goto loc_009269CB;
    v_rbx = (a4) + (4);
    if ((*(unsigned __int64 *)(v_rsp - 79 - 49)) != 0) goto loc_009269CB;
    if ((*(unsigned __int16 *)(v_rbx)) == 40) goto loc_0092676D;
    *(unsigned int *)(v_rsp - 79 - 81) = 0;
loc_00926640:
    if ((*(unsigned __int16 *)(v_rbx)) == 32) goto loc_00926C20;
loc_0092664A:
loc_0092664C:
    if (0 >= 6) goto loc_00926769;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip - 9583319 + 0 + 0 * 2 * 8 + 16)))) & (1)) == 0) goto loc_00926682;
    result = wcsnicmp(v_rbx, *(unsigned __int64 *)(v_rip - 9583319 + 0 + 0 * 2 * 8), (unsigned int)(*(unsigned int *)(v_rip - 9583319 + 0 + 0 * 2 * 8 + 8)), v_rip - 9583319);
    a2 = 0;
    if ((unsigned int)(result) == 0) goto loc_00926686;
loc_00926682:
    v_rdi = (unsigned int)((0) + 1);
    goto loc_0092664C;
loc_00926686:
    a1 = (unsigned __int16)(((unsigned int)(*(unsigned int *)(v_rsp - 79 - 81))) | (*(unsigned __int16 *)(v_rip - 9583454 + 0 + 0 * 2 * 8 + 12)));
    *(unsigned int *)(v_rsp - 79 - 81) = (unsigned int)(a1);
    if (v_rbx + (unsigned int)(*(unsigned int *)(v_rip - 9583454 + 0 + 0 * 2 * 8 + 8)) * 2 == 0) goto loc_0092664A;
loc_009266A0:
    if ((*(unsigned __int16 *)(v_rbx + (unsigned int)(*(unsigned int *)(v_rip - 9583454 + 0 + 0 * 2 * 8 + 8)) * 2)) != 32) goto loc_0092664A;
    v_rbx = (v_rbx + (unsigned int)(*(unsigned int *)(v_rip - 9583454 + 0 + 0 * 2 * 8 + 8)) * 2) + (2);
    if (condition_is_not_equal) goto loc_009266A0;
    goto loc_0092664A;
loc_009266AE:
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(v_rip - 9583454 + 0 + 0 * 2 * 8 + 8)))) == 71) goto loc_009268C3;
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(v_rip - 9583454 + 0 + 0 * 2 * 8 + 8)))) == 79) goto loc_00926841;
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(v_rip - 9583454 + 0 + 0 * 2 * 8 + 8)))) == 32) goto loc_00926943;
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(v_rip - 9583454 + 0 + 0 * 2 * 8 + 8)))) != 83) goto loc_009269CB;
    if ((*(unsigned __int16 *)(v_rbx + 2)) != 58) goto loc_009269CB;
    v_rbx = (v_rbx) + (a1);
    if ((*(unsigned __int64 *)(v_rsp - 79 - 41)) != 0) goto loc_009269CB;
    if ((*(unsigned __int16 *)(v_rbx)) == 40) goto loc_009267B2;
    *(unsigned int *)(v_rsp - 79 + 111) = 0;
loc_009266FB:
    if ((*(unsigned __int16 *)(v_rbx)) == 32) goto loc_00926C11;
loc_00926705:
loc_00926707:
    if (0 >= 6) goto loc_009267AA;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip - 9583454 + 0 + 0 * 2 * 8 + 16)))) & (2)) == 0) goto loc_0092673D;
    result = wcsnicmp(v_rbx, *(unsigned __int64 *)(v_rip - 9583454 + 0 + 0 * 2 * 8), (unsigned int)(*(unsigned int *)(v_rip - 9583454 + 0 + 0 * 2 * 8 + 8)), v_rip - 9583454);
    a2 = 0;
    if ((unsigned int)(result) == 0) goto loc_00926741;
loc_0092673D:
    v_rdi = (unsigned int)((0) + 1);
    goto loc_00926707;
loc_00926741:
    a1 = (unsigned __int16)(((unsigned int)(*(unsigned int *)(v_rsp - 79 + 111))) | (*(unsigned __int16 *)(v_rip - 9583641 + 0 + 0 * 2 * 8 + 12)));
    *(unsigned int *)(v_rsp - 79 + 111) = (unsigned int)(a1);
    if (v_rbx + (unsigned int)(*(unsigned int *)(v_rip - 9583641 + 0 + 0 * 2 * 8 + 8)) * 2 == 0) goto loc_00926705;
loc_0092675B:
    if ((*(unsigned __int16 *)(v_rbx + (unsigned int)(*(unsigned int *)(v_rip - 9583641 + 0 + 0 * 2 * 8 + 8)) * 2)) != 32) goto loc_00926705;
    v_rbx = (v_rbx + (unsigned int)(*(unsigned int *)(v_rip - 9583641 + 0 + 0 * 2 * 8 + 8)) * 2) + (2);
    if (condition_is_not_equal) goto loc_0092675B;
    goto loc_00926705;
loc_00926769:
    *(unsigned __int64 *)(v_rsp - 79 - 89) = v_rbx;
loc_0092676D:
    v_stack_mB0 = 0;
    v_stack_mB8 = 0;
    v_stack_mC0 = 0;
    v_stack_mC8 = 0;
    result = LocalGetAclForString(v_rbx, 1, v_rsp - 79 - 49, v_rsp - 79 - 89);
    a2 = 0;
    if ((unsigned int)(result) != 0) goto loc_009267FC;
    *(unsigned __int8 *)(v_rsp - 79 + 95) = 1;
    goto loc_009265F0;
loc_009267AA:
    *(unsigned __int64 *)(v_rsp - 79 - 89) = *(unsigned __int64 *)(v_rsp - 79 - 89);
loc_009267B2:
    v_stack_mB0 = 0;
    v_stack_mB8 = 0;
    v_stack_mC0 = 0;
    v_stack_mC8 = 0;
    a2 = 0;
    result = LocalGetAclForString(*(unsigned __int64 *)(v_rsp - 79 - 89), a2, v_rsp - 79 - 41, v_rsp - 79 - 89);
    a2 = 0;
    if ((unsigned int)(result) != 0) goto loc_009267FC;
    *(unsigned __int8 *)(v_rsp - 79 + 87) = 1;
    goto loc_009265F0;
loc_009267EC:
    goto loc_009265FC;
loc_009267F4:
    if ((unsigned int)((unsigned int)((unsigned int)(result))) == 0) goto loc_00926A0F;
loc_009267FC:
    if ((*(unsigned __int8 *)(v_rsp - 79 + 103)) == 1) {
        a1 = 0;
        result = PdcCloseEvent(a1, a2, v_rsp - 79 - 41, v_rsp - 79 - 89);
    }
    if (0 == 1) {
        a1 = 0;
        result = PdcCloseEvent(a1, a2, v_rsp - 79 - 41, v_rsp - 79 - 89);
    }
    result = PdcCloseEvent(*(unsigned __int64 *)(v_rsp - 79 - 49), a2, v_rsp - 79 - 41, v_rsp - 79 - 89);
    result = PdcCloseEvent(*(unsigned __int64 *)(v_rsp - 79 - 41), a2, v_rsp - 79 - 41, v_rsp - 79 - 89);
loc_0092682C:
    v_rsp = (v_rsp) + (168);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_00926841:
    if ((*(unsigned __int16 *)(0 + 2)) != 58) goto loc_009267FC;
    v_rbx = (0) + (*(unsigned __int64 *)(v_rsp - 79 - 41));
    if (0 != 0) goto loc_009267FC;
    *(unsigned __int64 *)(v_rsp - 79 - 57) = 0;
    if (v_rbx == 0) goto loc_009269CB;
    *(unsigned __int8 *)(v_rsp - 79 + 103) = 0;
    if ((*(unsigned __int16 *)(v_rbx)) == 0) goto loc_009269FB;
    if ((*(unsigned __int16 *)(v_rbx + 2)) == 0) goto loc_009269FB;
    a3 = 0;
    *(unsigned __int64 *)(v_rsp - 79 - 89) = v_rbx + 4;
    v_stack_p30 = v_rsp - 79 - 57;
    v_stack_p28 = 0;
    a2 = 0;
    result = LookupSidInTable(v_rbx, a2, a3, v_rsp - 79 - 89);
    a2 = 0;
    if (result == 0) goto loc_0092694C;
    *(unsigned __int64 *)(v_rsp - 79 - 73) = *(unsigned __int64 *)(result + 16);
loc_009268AF:
    if (0 != 0) goto loc_009267FC;
    *(unsigned __int8 *)(v_rsp - 79 + 103) = 0;
    goto loc_009265F0;
loc_009268C3:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 79 - 89) + 2)) != 58) goto loc_009267FC;
    v_rbx = (*(unsigned __int64 *)(v_rsp - 79 - 89)) + (v_rbx);
    if (0 != 0) goto loc_009267FC;
    *(unsigned __int64 *)(v_rsp - 79 - 57) = 0;
    if (v_rbx == 0) goto loc_009269CB;
    if ((*(unsigned __int16 *)(v_rbx)) == 0) goto loc_00926A05;
    if ((*(unsigned __int16 *)(v_rbx + 2)) == 0) goto loc_00926A05;
    a3 = 0;
    *(unsigned __int64 *)(v_rsp - 79 - 89) = v_rbx + 4;
    v_stack_p30 = v_rsp - 79 - 57;
    v_stack_p28 = 0;
    a2 = 0;
    result = LookupSidInTable(v_rbx, a2, a3, v_rsp - 79 - 89);
    a2 = 0;
    if (result == 0) goto loc_0092698B;
loc_0092692E:
    *(unsigned __int64 *)(v_rsp - 79 - 65) = *(unsigned __int64 *)(result + 16);
loc_00926932:
    if (0 != 0) goto loc_009267FC;
    goto loc_009265F0;
loc_00926943:
    v_rbx = (*(unsigned __int64 *)(v_rsp - 79 - 89)) + (2);
    goto loc_009265FC;
loc_0092694C:
    if (*(unsigned __int64 *)(v_rsp - 79 - 57) != 0) goto loc_009269ED;
    result = LocalpConvertStringSidToSid(v_rbx, v_rsp - 79 - 73, v_rsp - 79 - 89, v_rsp - 79 - 89);
    a2 = 0;
    if (sign_flag) goto loc_009269D2;
loc_00926978:
    if (*(unsigned __int64 *)(v_rsp - 79 - 73) == 0) goto loc_009269E5;
loc_00926981:
    *(unsigned __int8 *)(v_rsp - 79 + 103) = 1;
    goto loc_009268AF;
loc_0092698B:
    if (*(unsigned __int64 *)(v_rsp - 79 - 57) != 0) goto loc_009269F3;
    result = LocalpConvertStringSidToSid(v_rbx, v_rsp - 79 - 65, v_rsp - 79 - 89, v_rsp - 79 - 89);
    a2 = 0;
    if (sign_flag) goto loc_00926BF5;
loc_009269B6:
    if (*(unsigned __int64 *)(v_rsp - 79 - 65) == 0) goto loc_00926932;
    goto loc_00926932;
loc_009269CB:
    goto loc_009267FC;
loc_009269D2:
    result = RtlNtStatusToDosError((unsigned int)((unsigned int)(result)), a2, v_rsp - 79 - 89, v_rsp - 79 - 89);
    a2 = 0;
    if ((unsigned int)(result) == 0) goto loc_00926978;
loc_009269E5:
    goto loc_009268AF;
loc_009269ED:
    *(unsigned __int64 *)(v_rsp - 79 - 73) = *(unsigned __int64 *)(v_rsp - 79 - 73);
    goto loc_00926981;
loc_009269F3:
    goto loc_0092692E;
loc_009269FB:
    goto loc_0092680A;
loc_00926A05:
    goto loc_009267FC;
loc_00926A0F:
    result = 0;
    *(unsigned __int64 *)(v_rsp - 79 - 33) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 79 - 1) = 0;
    v_rbx = (unsigned __int16)((*(unsigned __int16 *)(v_rsp - 79 - 31)) | ((unsigned __int16)((unsigned int)(*(unsigned int *)(v_rsp - 79 + 111)))));
    v_rbx = (unsigned __int16)((v_rbx) | ((unsigned __int16)((unsigned int)(*(unsigned int *)(v_rsp - 79 - 81)))));
    *(unsigned __int8 *)(v_rsp - 79 - 33) = 1;
    *(unsigned __int16 *)(v_rsp - 79 - 31) = (unsigned __int16)(v_rbx);
    *(unsigned __int64 *)(v_rsp - 79 - 17) = v_xmm0;
    if (*(unsigned __int64 *)(v_rsp - 79 - 73) != 0) goto loc_00926BD8;
loc_00926A49:
    if (*(unsigned __int64 *)(v_rsp - 79 - 65) != 0) goto loc_00926B53;
loc_00926A52:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rsp - 79 + 95)) == 0) goto loc_00926A82;
    if (sign_flag) goto loc_00926B6D;
    v_rbx = (unsigned __int16)((v_rbx) | (4));
    a1 = 0;
    if (*(unsigned __int64 *)(v_rsp - 79 - 49) != 0) { a1 = *(unsigned __int64 *)(v_rsp - 79 - 49); }
    v_rbx = (unsigned __int16)((v_rbx) & ((unsigned __int16)((unsigned int)(0xFFF7ULL))));
    *(unsigned __int64 *)(v_rsp - 79 - 1) = a1;
    *(unsigned __int16 *)(v_rsp - 79 - 31) = (unsigned __int16)(v_rbx);
loc_00926A82:
    if ((*(unsigned __int8 *)(v_rsp - 79 + 87)) == 0) goto loc_00926AB2;
    if (sign_flag) goto loc_00926B8F;
    v_rbx = (unsigned __int16)((v_rbx) | (16));
    a1 = 0;
    if (*(unsigned __int64 *)(v_rsp - 79 - 41) != 0) { a1 = *(unsigned __int64 *)(v_rsp - 79 - 41); }
    v_rbx = (unsigned __int16)((v_rbx) & ((unsigned __int16)((unsigned int)(0xFFDFULL))));
    *(unsigned __int64 *)(v_rsp - 79 - 9) = a1;
    *(unsigned __int16 *)(v_rsp - 79 - 31) = (unsigned __int16)(v_rbx);
loc_00926AB2:
    if ((((unsigned __int16)((unsigned int)(0x8000ULL))) & ((unsigned __int16)(v_rbx))) != 0) goto loc_00926B49;
    result = RtlMakeSelfRelativeSD(v_rsp - 79 - 33, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 79 + 119)), v_rsp - 79 - 77, v_rsp - 79 - 89);
    if (((unsigned int)(result)) != 0xC0000023ULL) goto loc_00926B49;
    v_rdi = 0;
    result = SddlpAlloc((unsigned int)(*(unsigned int *)(v_rsp - 79 - 77)), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 79 + 119)), v_rsp - 79 - 77, v_rsp - 79 - 89);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 79 + 119)) = result;
    if (result == 0) goto loc_00926B3F;
    if (((*(unsigned __int16 *)(v_rsp - 79 - 31)) & ((unsigned __int16)((unsigned int)(0x8000ULL)))) != 0) goto loc_00926B85;
    result = RtlMakeSelfRelativeSD(v_rsp - 79 - 33, result, v_rsp - 79 - 77, v_rsp - 79 - 89);
    if (!sign_flag) goto loc_00926B28;
loc_00926B0B:
    result = RtlNtStatusToDosError((unsigned int)((unsigned int)(result)), result, v_rsp - 79 - 77, v_rsp - 79 - 89);
    result = PdcCloseEvent(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 79 + 119)), result, v_rsp - 79 - 77, v_rsp - 79 - 89);
    if ((unsigned int)((unsigned int)((unsigned int)(result))) != 0) goto loc_009267FC;
loc_00926B28:
    if (*(unsigned __int64 *)(v_rsp - 79 + 127) == 0) goto loc_009267FC;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 79 + 127)) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 - 77)));
    goto loc_009267FC;
loc_00926B3F:
    goto loc_009267FC;
loc_00926B49:
    goto loc_009267FC;
loc_00926B53:
    if (sign_flag) goto loc_00926BA5;
    *(unsigned __int64 *)(v_rsp - 79 - 17) = *(unsigned __int64 *)(v_rsp - 79 - 65);
    v_rbx = (unsigned __int16)((v_rbx) & ((unsigned __int16)((unsigned int)(0xFFFDULL))));
    *(unsigned __int16 *)(v_rsp - 79 - 31) = (unsigned __int16)(v_rbx);
    goto loc_00926A52;
loc_00926B6D:
    result = RtlNtStatusToDosError((unsigned int)((unsigned int)((unsigned int)(0x8000ULL))), result, v_rsp - 79 - 77, v_rsp - 79 - 89);
    a2 = 0;
    if ((unsigned int)(result) != 0) goto loc_009267FC;
    goto loc_00926A82;
loc_00926B85:
    goto loc_00926B0B;
loc_00926B8F:
    result = RtlNtStatusToDosError((unsigned int)((unsigned int)((unsigned int)(0x8000ULL))), a2, v_rsp - 79 - 77, v_rsp - 79 - 89);
    if ((unsigned int)(result) == 0) goto loc_00926AB2;
    goto loc_009267FC;
loc_00926BA5:
    result = RtlNtStatusToDosError((unsigned int)((unsigned int)((unsigned int)(0x8000ULL))), a2, v_rsp - 79 - 77, v_rsp - 79 - 89);
    a2 = 0;
    if ((unsigned int)(result) == 0) goto loc_00926A52;
    goto loc_009267FC;
loc_00926BBD:
    result = RtlNtStatusToDosError((unsigned int)((unsigned int)((unsigned int)(0x8000ULL))), a2, v_rsp - 79 - 77, v_rsp - 79 - 89);
    a2 = 0;
    if ((unsigned int)((unsigned int)((unsigned int)(result))) != 0) goto loc_009267FC;
    goto loc_00926A49;
loc_00926BD8:
    if (sign_flag) goto loc_00926BBD;
    *(unsigned __int64 *)(v_rsp - 79 - 25) = *(unsigned __int64 *)(v_rsp - 79 - 73);
    v_rbx = (unsigned __int16)((v_rbx) & ((unsigned __int16)((unsigned int)(0xFFFEULL))));
    *(unsigned __int16 *)(v_rsp - 79 - 31) = (unsigned __int16)(v_rbx);
    goto loc_00926A49;
loc_00926BF5:
    result = RtlNtStatusToDosError((unsigned int)((unsigned int)((unsigned __int16)(v_rbx))), a2, v_rsp - 79 - 77, v_rsp - 79 - 89);
    a2 = 0;
    if ((unsigned int)(result) == 0) goto loc_009269B6;
    goto loc_00926932;
loc_00926C11:
    v_rbx = (v_rbx) + (2);
    if (condition_is_not_equal) goto loc_009266FB;
    goto loc_00926705;
loc_00926C20:
    v_rbx = (v_rbx) + (2);
    if (condition_is_not_equal) goto loc_00926640;
    goto loc_0092664A;
loc_00926C2F:
    goto loc_0092682C;
}
```

## 5. (Beta) C Style

```c
int64_t LocalConvertStringSDToSD_Rev1(int64_t Arg1, int64_t Arg2, uint8_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint8_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint8_t v_stack_p28;
    uint64_t v_stack_p30;

    *(uint8_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (168);
    Arg2 = 0;
    *(uint64_t *)(local_rsp - 0x4F - 0x49) = 0;
    *(uint64_t *)(local_rsp - 0x4F - 0x41) = 0;
    *(uint64_t *)(local_rsp - 0x4F - 0x31) = 0;
    *(uint64_t *)(local_rsp - 0x4F - 0x29) = 0;
    *(uint64_t *)(local_rsp - 0x4F - 0x59) = 0;
    *(uint8_t *)(local_rsp - 0x4F + 0x67) = 0;
    *(uint32_t *)(local_rsp - 0x4F - 0x4D) = 0;
    *(uint8_t *)(local_rsp - 0x4F + 0x5F) = 0;
    *(uint8_t *)(local_rsp - 0x4F + 0x57) = 0;
    *(uint16_t *)(local_rsp - 0x4F - 0x51) = 0;
    *(uint16_t *)(local_rsp - 0x4F + 0x6F) = 0;
    if (Arg4 == 0) goto loc_00926C2F;
    if ((*(uint64_t *)(local_rsp - 0x4F + 0x77)) == 0) goto loc_00926C2F;
    if (*(uint64_t *)(local_rsp - 0x4F + 0x7F) != 0) {
        *(uint32_t *)(*(uint64_t *)(local_rsp - 0x4F + 0x7F)) = 0;
    }
loc_009265F0:
loc_009265FC:
    if (Arg4 == 0) goto loc_009267F4;
    if ((uint16_t)(*(uint16_t *)(Arg4)) == 0) goto loc_009267EC;
    if (((uint16_t)(*(uint16_t *)(Arg4))) != 68) goto loc_009266AE;
    if ((*(uint16_t *)(Arg4 + 0x2)) != 58) goto loc_009269CB;
    local_rbx = (Arg4) + (4);
    if ((*(uint64_t *)(local_rsp - 0x4F - 0x31)) != 0) goto loc_009269CB;
    if ((*(uint16_t *)(local_rbx)) == 40) goto loc_0092676D;
    *(uint32_t *)(local_rsp - 0x4F - 0x51) = 0;
loc_00926640:
    if ((*(uint16_t *)(local_rbx)) == 32) goto loc_00926C20;
loc_0092664A:
loc_0092664C:
    if (0 >= 6) goto loc_00926769;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip - 0x923AD7 + 0x0 + 0x0 * 2 * 8 + 0x10)))) & (1)) == 0) goto loc_00926682;
    result = wcsnicmp(local_rbx, *(uint64_t *)(v_rip - 0x923AD7 + 0x0 + 0x0 * 2 * 8), (uint32_t)(*(uint32_t *)(v_rip - 0x923AD7 + 0x0 + 0x0 * 2 * 8 + 0x8)), v_rip - 9583319);
    Arg2 = 0;
    if ((uint32_t)(result) == 0) goto loc_00926686;
loc_00926682:
    local_rdi = (uint32_t)((0) + 1);
    goto loc_0092664C;
loc_00926686:
    Arg1 = (uint16_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x51))) | (*(uint16_t *)(v_rip - 0x923B5E + 0x0 + 0x0 * 2 * 8 + 0xC)));
    *(uint32_t *)(local_rsp - 0x4F - 0x51) = (uint32_t)(Arg1);
    if (local_rbx + (uint32_t)(*(uint32_t *)(v_rip - 0x923B5E + 0x0 + 0x0 * 2 * 8 + 0x8)) * 2 == 0) goto loc_0092664A;
loc_009266A0:
    if ((*(uint16_t *)(local_rbx + (uint32_t)(*(uint32_t *)(v_rip - 0x923B5E + 0x0 + 0x0 * 2 * 8 + 0x8)) * 2)) != 32) goto loc_0092664A;
    local_rbx = (local_rbx + (uint32_t)(*(uint32_t *)(v_rip - 0x923B5E + 0x0 + 0x0 * 2 * 8 + 0x8)) * 2) + (2);
    if (condition_is_not_equal) goto loc_009266A0;
    goto loc_0092664A;
loc_009266AE:
    if (((uint16_t)((uint32_t)(*(uint32_t *)(v_rip - 0x923B5E + 0x0 + 0x0 * 2 * 8 + 0x8)))) == 71) goto loc_009268C3;
    if (((uint16_t)((uint32_t)(*(uint32_t *)(v_rip - 0x923B5E + 0x0 + 0x0 * 2 * 8 + 0x8)))) == 79) goto loc_00926841;
    if (((uint16_t)((uint32_t)(*(uint32_t *)(v_rip - 0x923B5E + 0x0 + 0x0 * 2 * 8 + 0x8)))) == 32) goto loc_00926943;
    if (((uint16_t)((uint32_t)(*(uint32_t *)(v_rip - 0x923B5E + 0x0 + 0x0 * 2 * 8 + 0x8)))) != 83) goto loc_009269CB;
    if ((*(uint16_t *)(local_rbx + 0x2)) != 58) goto loc_009269CB;
    local_rbx = (local_rbx) + (Arg1);
    if ((*(uint64_t *)(local_rsp - 0x4F - 0x29)) != 0) goto loc_009269CB;
    if ((*(uint16_t *)(local_rbx)) == 40) goto loc_009267B2;
    *(uint32_t *)(local_rsp - 0x4F + 0x6F) = 0;
loc_009266FB:
    if ((*(uint16_t *)(local_rbx)) == 32) goto loc_00926C11;
loc_00926705:
loc_00926707:
    if (0 >= 6) goto loc_009267AA;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip - 0x923B5E + 0x0 + 0x0 * 2 * 8 + 0x10)))) & (2)) == 0) goto loc_0092673D;
    result = wcsnicmp(local_rbx, *(uint64_t *)(v_rip - 0x923B5E + 0x0 + 0x0 * 2 * 8), (uint32_t)(*(uint32_t *)(v_rip - 0x923B5E + 0x0 + 0x0 * 2 * 8 + 0x8)), v_rip - 9583454);
    Arg2 = 0;
    if ((uint32_t)(result) == 0) goto loc_00926741;
loc_0092673D:
    local_rdi = (uint32_t)((0) + 1);
    goto loc_00926707;
loc_00926741:
    Arg1 = (uint16_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x4F + 0x6F))) | (*(uint16_t *)(v_rip - 0x923C19 + 0x0 + 0x0 * 2 * 8 + 0xC)));
    *(uint32_t *)(local_rsp - 0x4F + 0x6F) = (uint32_t)(Arg1);
    if (local_rbx + (uint32_t)(*(uint32_t *)(v_rip - 0x923C19 + 0x0 + 0x0 * 2 * 8 + 0x8)) * 2 == 0) goto loc_00926705;
loc_0092675B:
    if ((*(uint16_t *)(local_rbx + (uint32_t)(*(uint32_t *)(v_rip - 0x923C19 + 0x0 + 0x0 * 2 * 8 + 0x8)) * 2)) != 32) goto loc_00926705;
    local_rbx = (local_rbx + (uint32_t)(*(uint32_t *)(v_rip - 0x923C19 + 0x0 + 0x0 * 2 * 8 + 0x8)) * 2) + (2);
    if (condition_is_not_equal) goto loc_0092675B;
    goto loc_00926705;
loc_00926769:
    *(uint64_t *)(local_rsp - 0x4F - 0x59) = local_rbx;
loc_0092676D:
    v_stack_mB0 = 0;
    v_stack_mB8 = 0;
    v_stack_mC0 = 0;
    v_stack_mC8 = 0;
    result = LocalGetAclForString(local_rbx, 1, local_rsp - 79 - 49, local_rsp - 79 - 89);
    Arg2 = 0;
    if ((uint32_t)(result) != 0) goto loc_009267FC;
    *(uint8_t *)(local_rsp - 0x4F + 0x5F) = 1;
    goto loc_009265F0;
loc_009267AA:
    *(uint64_t *)(local_rsp - 0x4F - 0x59) = *(uint64_t *)(local_rsp - 0x4F - 0x59);
loc_009267B2:
    v_stack_mB0 = 0;
    v_stack_mB8 = 0;
    v_stack_mC0 = 0;
    v_stack_mC8 = 0;
    Arg2 = 0;
    result = LocalGetAclForString(*(uint64_t *)(local_rsp - 0x4F - 0x59), Arg2, local_rsp - 79 - 41, local_rsp - 79 - 89);
    Arg2 = 0;
    if ((uint32_t)(result) != 0) goto loc_009267FC;
    *(uint8_t *)(local_rsp - 0x4F + 0x57) = 1;
    goto loc_009265F0;
loc_009267EC:
    goto loc_009265FC;
loc_009267F4:
    if ((uint32_t)((uint32_t)((uint32_t)(result))) == 0) goto loc_00926A0F;
loc_009267FC:
    if ((*(uint8_t *)(local_rsp - 0x4F + 0x67)) == 1) {
        Arg1 = 0;
        result = PdcCloseEvent(Arg1, Arg2, local_rsp - 79 - 41, local_rsp - 79 - 89);
    }
    if (0 == 1) {
        Arg1 = 0;
        result = PdcCloseEvent(Arg1, Arg2, local_rsp - 79 - 41, local_rsp - 79 - 89);
    }
    result = PdcCloseEvent(*(uint64_t *)(local_rsp - 0x4F - 0x31), Arg2, local_rsp - 79 - 41, local_rsp - 79 - 89);
    result = PdcCloseEvent(*(uint64_t *)(local_rsp - 0x4F - 0x29), Arg2, local_rsp - 79 - 41, local_rsp - 79 - 89);
loc_0092682C:
    local_rsp = (local_rsp) + (168);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_00926841:
    if ((*(uint16_t *)(0 + 0x2)) != 58) goto loc_009267FC;
    local_rbx = (0) + (*(uint64_t *)(local_rsp - 0x4F - 0x29));
    if (0 != 0) goto loc_009267FC;
    *(uint64_t *)(local_rsp - 0x4F - 0x39) = 0;
    if (local_rbx == 0) goto loc_009269CB;
    *(uint8_t *)(local_rsp - 0x4F + 0x67) = 0;
    if ((*(uint16_t *)(local_rbx)) == 0) goto loc_009269FB;
    if ((*(uint16_t *)(local_rbx + 0x2)) == 0) goto loc_009269FB;
    Arg3 = 0;
    *(uint64_t *)(local_rsp - 0x4F - 0x59) = local_rbx + 4;
    v_stack_p30 = local_rsp - 79 - 57;
    v_stack_p28 = 0;
    Arg2 = 0;
    result = LookupSidInTable(local_rbx, Arg2, Arg3, local_rsp - 79 - 89);
    Arg2 = 0;
    if (result == 0) goto loc_0092694C;
    *(uint64_t *)(local_rsp - 0x4F - 0x49) = *(uint64_t *)(result + 0x10);
loc_009268AF:
    if (0 != 0) goto loc_009267FC;
    *(uint8_t *)(local_rsp - 0x4F + 0x67) = 0;
    goto loc_009265F0;
loc_009268C3:
    if ((*(uint16_t *)(*(uint64_t *)(local_rsp - 0x4F - 0x59) + 0x2)) != 58) goto loc_009267FC;
    local_rbx = (*(uint64_t *)(local_rsp - 0x4F - 0x59)) + (local_rbx);
    if (0 != 0) goto loc_009267FC;
    *(uint64_t *)(local_rsp - 0x4F - 0x39) = 0;
    if (local_rbx == 0) goto loc_009269CB;
    if ((*(uint16_t *)(local_rbx)) == 0) goto loc_00926A05;
    if ((*(uint16_t *)(local_rbx + 0x2)) == 0) goto loc_00926A05;
    Arg3 = 0;
    *(uint64_t *)(local_rsp - 0x4F - 0x59) = local_rbx + 4;
    v_stack_p30 = local_rsp - 79 - 57;
    v_stack_p28 = 0;
    Arg2 = 0;
    result = LookupSidInTable(local_rbx, Arg2, Arg3, local_rsp - 79 - 89);
    Arg2 = 0;
    if (result == 0) goto loc_0092698B;
loc_0092692E:
    *(uint64_t *)(local_rsp - 0x4F - 0x41) = *(uint64_t *)(result + 0x10);
loc_00926932:
    if (0 != 0) goto loc_009267FC;
    goto loc_009265F0;
loc_00926943:
    local_rbx = (*(uint64_t *)(local_rsp - 0x4F - 0x59)) + (2);
    goto loc_009265FC;
loc_0092694C:
    if (*(uint64_t *)(local_rsp - 0x4F - 0x39) != 0) goto loc_009269ED;
    result = LocalpConvertStringSidToSid(local_rbx, local_rsp - 79 - 73, local_rsp - 79 - 89, local_rsp - 79 - 89);
    Arg2 = 0;
    if (sign_flag) goto loc_009269D2;
loc_00926978:
    if (*(uint64_t *)(local_rsp - 0x4F - 0x49) == 0) goto loc_009269E5;
loc_00926981:
    *(uint8_t *)(local_rsp - 0x4F + 0x67) = 1;
    goto loc_009268AF;
loc_0092698B:
    if (*(uint64_t *)(local_rsp - 0x4F - 0x39) != 0) goto loc_009269F3;
    result = LocalpConvertStringSidToSid(local_rbx, local_rsp - 79 - 65, local_rsp - 79 - 89, local_rsp - 79 - 89);
    Arg2 = 0;
    if (sign_flag) goto loc_00926BF5;
loc_009269B6:
    if (*(uint64_t *)(local_rsp - 0x4F - 0x41) == 0) goto loc_00926932;
    goto loc_00926932;
loc_009269CB:
    goto loc_009267FC;
loc_009269D2:
    result = RtlNtStatusToDosError((uint32_t)((uint32_t)(result)), Arg2, local_rsp - 79 - 89, local_rsp - 79 - 89);
    Arg2 = 0;
    if ((uint32_t)(result) == 0) goto loc_00926978;
loc_009269E5:
    goto loc_009268AF;
loc_009269ED:
    *(uint64_t *)(local_rsp - 0x4F - 0x49) = *(uint64_t *)(local_rsp - 0x4F - 0x49);
    goto loc_00926981;
loc_009269F3:
    goto loc_0092692E;
loc_009269FB:
    goto loc_0092680A;
loc_00926A05:
    goto loc_009267FC;
loc_00926A0F:
    result = 0;
    *(uint64_t *)(local_rsp - 0x4F - 0x21) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x4F - 0x1) = 0;
    local_rbx = (uint16_t)((*(uint16_t *)(local_rsp - 0x4F - 0x1F)) | ((uint16_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F + 0x6F)))));
    local_rbx = (uint16_t)((local_rbx) | ((uint16_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x51)))));
    *(uint8_t *)(local_rsp - 0x4F - 0x21) = 1;
    *(uint16_t *)(local_rsp - 0x4F - 0x1F) = (uint16_t)(local_rbx);
    *(uint64_t *)(local_rsp - 0x4F - 0x11) = v_xmm0;
    if (*(uint64_t *)(local_rsp - 0x4F - 0x49) != 0) goto loc_00926BD8;
loc_00926A49:
    if (*(uint64_t *)(local_rsp - 0x4F - 0x41) != 0) goto loc_00926B53;
loc_00926A52:
    if ((uint8_t)(*(uint8_t *)(local_rsp - 0x4F + 0x5F)) == 0) goto loc_00926A82;
    if (sign_flag) goto loc_00926B6D;
    local_rbx = (uint16_t)((local_rbx) | (4));
    Arg1 = 0;
    if (*(uint64_t *)(local_rsp - 0x4F - 0x31) != 0) { Arg1 = *(uint64_t *)(local_rsp - 0x4F - 0x31); }
    local_rbx = (uint16_t)((local_rbx) & ((uint16_t)((uint32_t)(0xFFF7ULL))));
    *(uint64_t *)(local_rsp - 0x4F - 0x1) = Arg1;
    *(uint16_t *)(local_rsp - 0x4F - 0x1F) = (uint16_t)(local_rbx);
loc_00926A82:
    if ((*(uint8_t *)(local_rsp - 0x4F + 0x57)) == 0) goto loc_00926AB2;
    if (sign_flag) goto loc_00926B8F;
    local_rbx = (uint16_t)((local_rbx) | (16));
    Arg1 = 0;
    if (*(uint64_t *)(local_rsp - 0x4F - 0x29) != 0) { Arg1 = *(uint64_t *)(local_rsp - 0x4F - 0x29); }
    local_rbx = (uint16_t)((local_rbx) & ((uint16_t)((uint32_t)(0xFFDFULL))));
    *(uint64_t *)(local_rsp - 0x4F - 0x9) = Arg1;
    *(uint16_t *)(local_rsp - 0x4F - 0x1F) = (uint16_t)(local_rbx);
loc_00926AB2:
    if ((((uint16_t)((uint32_t)(0x8000ULL))) & ((uint16_t)(local_rbx))) != 0) goto loc_00926B49;
    result = RtlMakeSelfRelativeSD(local_rsp - 79 - 33, *(uint64_t *)(*(uint64_t *)(local_rsp - 0x4F + 0x77)), local_rsp - 79 - 77, local_rsp - 79 - 89);
    if (((uint32_t)(result)) != 0xC0000023ULL) goto loc_00926B49;
    local_rdi = 0;
    result = SddlpAlloc((uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x4D)), *(uint64_t *)(*(uint64_t *)(local_rsp - 0x4F + 0x77)), local_rsp - 79 - 77, local_rsp - 79 - 89);
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x4F + 0x77)) = result;
    if (result == 0) goto loc_00926B3F;
    if (((*(uint16_t *)(local_rsp - 0x4F - 0x1F)) & ((uint16_t)((uint32_t)(0x8000ULL)))) != 0) goto loc_00926B85;
    result = RtlMakeSelfRelativeSD(local_rsp - 79 - 33, result, local_rsp - 79 - 77, local_rsp - 79 - 89);
    if (!sign_flag) goto loc_00926B28;
loc_00926B0B:
    result = RtlNtStatusToDosError((uint32_t)((uint32_t)(result)), result, local_rsp - 79 - 77, local_rsp - 79 - 89);
    result = PdcCloseEvent(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x4F + 0x77)), result, local_rsp - 79 - 77, local_rsp - 79 - 89);
    if ((uint32_t)((uint32_t)((uint32_t)(result))) != 0) goto loc_009267FC;
loc_00926B28:
    if (*(uint64_t *)(local_rsp - 0x4F + 0x7F) == 0) goto loc_009267FC;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x4F + 0x7F)) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x4D)));
    goto loc_009267FC;
loc_00926B3F:
    goto loc_009267FC;
loc_00926B49:
    goto loc_009267FC;
loc_00926B53:
    if (sign_flag) goto loc_00926BA5;
    *(uint64_t *)(local_rsp - 0x4F - 0x11) = *(uint64_t *)(local_rsp - 0x4F - 0x41);
    local_rbx = (uint16_t)((local_rbx) & ((uint16_t)((uint32_t)(0xFFFDULL))));
    *(uint16_t *)(local_rsp - 0x4F - 0x1F) = (uint16_t)(local_rbx);
    goto loc_00926A52;
loc_00926B6D:
    result = RtlNtStatusToDosError((uint32_t)((uint32_t)((uint32_t)(0x8000ULL))), result, local_rsp - 79 - 77, local_rsp - 79 - 89);
    Arg2 = 0;
    if ((uint32_t)(result) != 0) goto loc_009267FC;
    goto loc_00926A82;
loc_00926B85:
    goto loc_00926B0B;
loc_00926B8F:
    result = RtlNtStatusToDosError((uint32_t)((uint32_t)((uint32_t)(0x8000ULL))), Arg2, local_rsp - 79 - 77, local_rsp - 79 - 89);
    if ((uint32_t)(result) == 0) goto loc_00926AB2;
    goto loc_009267FC;
loc_00926BA5:
    result = RtlNtStatusToDosError((uint32_t)((uint32_t)((uint32_t)(0x8000ULL))), Arg2, local_rsp - 79 - 77, local_rsp - 79 - 89);
    Arg2 = 0;
    if ((uint32_t)(result) == 0) goto loc_00926A52;
    goto loc_009267FC;
loc_00926BBD:
    result = RtlNtStatusToDosError((uint32_t)((uint32_t)((uint32_t)(0x8000ULL))), Arg2, local_rsp - 79 - 77, local_rsp - 79 - 89);
    Arg2 = 0;
    if ((uint32_t)((uint32_t)((uint32_t)(result))) != 0) goto loc_009267FC;
    goto loc_00926A49;
loc_00926BD8:
    if (sign_flag) goto loc_00926BBD;
    *(uint64_t *)(local_rsp - 0x4F - 0x19) = *(uint64_t *)(local_rsp - 0x4F - 0x49);
    local_rbx = (uint16_t)((local_rbx) & ((uint16_t)((uint32_t)(0xFFFEULL))));
    *(uint16_t *)(local_rsp - 0x4F - 0x1F) = (uint16_t)(local_rbx);
    goto loc_00926A49;
loc_00926BF5:
    result = RtlNtStatusToDosError((uint32_t)((uint32_t)((uint16_t)(local_rbx))), Arg2, local_rsp - 79 - 77, local_rsp - 79 - 89);
    Arg2 = 0;
    if ((uint32_t)(result) == 0) goto loc_009269B6;
    goto loc_00926932;
loc_00926C11:
    local_rbx = (local_rbx) + (2);
    if (condition_is_not_equal) goto loc_009266FB;
    goto loc_00926705;
loc_00926C20:
    local_rbx = (local_rbx) + (2);
    if (condition_is_not_equal) goto loc_00926640;
    goto loc_0092664A;
loc_00926C2F:
    goto loc_0092682C;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0092656C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
