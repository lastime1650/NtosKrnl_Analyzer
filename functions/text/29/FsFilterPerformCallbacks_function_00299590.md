# FsFilterPerformCallbacks

- RVA: `0x00299590`–`0x00299892` (길이 `770` bytes)
- VA: `0x0000000140299590`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00067C1C`
- 디코드: `221`개 명령, `770/770` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x002997B8` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0029985C` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0029988C` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- [FsRtlReleaseFileForModWrite](FsRtlReleaseFileForModWrite_function_00299100.md) at `0x00299234`
- [FsRtlAcquireFileForModWriteEx](FsRtlAcquireFileForModWriteEx_function_00299E5C.md) at `0x00299FA7`
- [FsRtlReleaseFile](../../page/98/FsRtlReleaseFile_function_00985B70.md) at `0x00985C42`
- [FsRtlAcquireFileForCcFlushEx](../../page/9D/FsRtlAcquireFileForCcFlushEx_function_009D72F0.md) at `0x009D73DD`
- [FsRtlReleaseFileForCcFlush](../../page/9D/FsRtlReleaseFileForCcFlush_function_009D75A0.md) at `0x009D7671`
- [FsRtlQueryOpen](../../page/9D/FsRtlQueryOpen_function_009D85A4.md) at `0x009D865D`
- [FsRtlAcquireFileExclusiveCommon](../../page/9D/FsRtlAcquireFileExclusiveCommon_function_009D8E50.md) at `0x009D8F7E`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00299590  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
00299595  55                              push rbp
00299596  56                              push rsi
00299597  41 54                           push r12
00299599  41 55                           push r13
0029959B  41 57                           push r15
0029959D  48 83 EC 30                     sub rsp, 0x30
002995A1  48 8B 59 08                     mov rbx, qword ptr [rcx + 8]
002995A5  49 8B F1                        mov rsi, r9
002995A8  48 89 7C 24 60                  mov qword ptr [rsp + 0x60], rdi
002995AD  45 0F B6 E0                     movzx r12d, r8b
002995B1  4C 89 74 24 68                  mov qword ptr [rsp + 0x68], r14
002995B6  44 0F B6 FA                     movzx r15d, dl
002995BA  48 8B E9                        mov rbp, rcx
002995BD  41 C7 01 02 00 00 00            mov dword ptr [r9], 2
002995C4  41 BD FF FF 00 00               mov r13d, 0xffff
002995CA  48 85 DB                        test rbx, rbx
002995CD  0F 84 C1 00 00 00               je 0x140299694
002995D3  48 8B 83 38 01 00 00            mov rax, qword ptr [rbx + 0x138]
002995DA  45 33 C9                        xor r9d, r9d
002995DD  45 33 C0                        xor r8d, r8d
002995E0  4C 8B 70 30                     mov r14, qword ptr [rax + 0x30]
002995E4  48 89 5D 08                     mov qword ptr [rbp + 8], rbx
002995E8  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
002995EC  48 8B 48 30                     mov rcx, qword ptr [rax + 0x30]
002995F0  48 8B 51 30                     mov rdx, qword ptr [rcx + 0x30]
002995F4  48 85 D2                        test rdx, rdx
002995F7  74 7F                           je 0x140299678
002995F9  0F B6 45 04                     movzx eax, byte ptr [rbp + 4]
002995FD  3D FE 00 00 00                  cmp eax, 0xfe
00299602  74 46                           je 0x14029964a
00299604  3D FF 00 00 00                  cmp eax, 0xff
00299609  0F 84 E1 00 00 00               je 0x1402996f0
0029960F  2D F9 00 00 00                  sub eax, 0xf9
00299614  0F 84 D1 01 00 00               je 0x1402997eb
0029961A  83 E8 01                        sub eax, 1
0029961D  0F 84 F2 00 00 00               je 0x140299715
00299623  83 E8 01                        sub eax, 1
00299626  0F 85 0E 01 00 00               jne 0x14029973a
0029962C  8B 0A                           mov ecx, dword ptr [rdx]
0029962E  83 F9 30                        cmp ecx, 0x30
00299631  72 0C                           jb 0x14029963f
00299633  48 8B 42 28                     mov rax, qword ptr [rdx + 0x28]
00299637  48 85 C0                        test rax, rax
0029963A  74 03                           je 0x14029963f
0029963C  4C 8B C8                        mov r9, rax
0029963F  83 F9 38                        cmp ecx, 0x38
00299642  72 2A                           jb 0x14029966e
00299644  48 8B 42 30                     mov rax, qword ptr [rdx + 0x30]
00299648  EB 1C                           jmp 0x140299666
0029964A  8B 0A                           mov ecx, dword ptr [rdx]
0029964C  83 F9 20                        cmp ecx, 0x20
0029964F  72 0C                           jb 0x14029965d
00299651  48 8B 42 18                     mov rax, qword ptr [rdx + 0x18]
00299655  48 85 C0                        test rax, rax
00299658  74 03                           je 0x14029965d
0029965A  4C 8B C8                        mov r9, rax
0029965D  83 F9 28                        cmp ecx, 0x28
00299660  72 0C                           jb 0x14029966e
00299662  48 8B 42 20                     mov rax, qword ptr [rdx + 0x20]
00299666  48 85 C0                        test rax, rax
00299669  74 03                           je 0x14029966e
0029966B  4C 8B C0                        mov r8, rax
0029966E  4D 85 C9                        test r9, r9
00299671  75 40                           jne 0x1402996b3
00299673  4D 85 C0                        test r8, r8
00299676  75 44                           jne 0x1402996bc
00299678  48 8B 83 38 01 00 00            mov rax, qword ptr [rbx + 0x138]
0029967F  48 8B 58 30                     mov rbx, qword ptr [rax + 0x30]
00299683  4D 85 F6                        test r14, r14
00299686  0F 85 3E FF FF FF               jne 0x1402995ca
0029968C  83 26 FD                        and dword ptr [rsi], 0xfffffffd
0029968F  E9 36 FF FF FF                  jmp 0x1402995ca
00299694  33 C0                           xor eax, eax
00299696  4C 8B 74 24 68                  mov r14, qword ptr [rsp + 0x68]
0029969B  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
002996A0  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
002996A5  48 83 C4 30                     add rsp, 0x30
002996A9  41 5F                           pop r15
002996AB  41 5D                           pop r13
002996AD  41 5C                           pop r12
002996AF  5E                              pop rsi
002996B0  5D                              pop rbp
002996B1  C3                              ret
002996B2  CC                              int3
002996B3  4D 85 C0                        test r8, r8
002996B6  0F 84 29 01 00 00               je 0x1402997e5
002996BC  0F B7 45 4A                     movzx eax, word ptr [rbp + 0x4a]
002996C0  66 3B 45 48                     cmp ax, word ptr [rbp + 0x48]
002996C4  73 1A                           jae 0x1402996e0
002996C6  8B F8                           mov edi, eax
002996C8  66 FF C0                        inc ax
002996CB  48 C1 E7 05                     shl rdi, 5
002996CF  48 03 7D 50                     add rdi, qword ptr [rbp + 0x50]
002996D3  66 89 45 4A                     mov word ptr [rbp + 0x4a], ax
002996D7  48 85 FF                        test rdi, rdi
002996DA  0F 85 B2 00 00 00               jne 0x140299792
002996E0  45 84 FF                        test r15b, r15b
002996E3  0F 84 8F 01 00 00               je 0x140299878
002996E9  B8 9A 00 00 C0                  mov eax, 0xc000009a
002996EE  EB A6                           jmp 0x140299696
002996F0  8B 02                           mov eax, dword ptr [rdx]
002996F2  83 F8 10                        cmp eax, 0x10
002996F5  72 0C                           jb 0x140299703
002996F7  48 8B 4A 08                     mov rcx, qword ptr [rdx + 8]
002996FB  48 85 C9                        test rcx, rcx
002996FE  74 03                           je 0x140299703
00299700  4C 8B C9                        mov r9, rcx
00299703  83 F8 18                        cmp eax, 0x18
00299706  0F 82 62 FF FF FF               jb 0x14029966e
0029970C  48 8B 42 10                     mov rax, qword ptr [rdx + 0x10]
00299710  E9 51 FF FF FF                  jmp 0x140299666
00299715  8B 0A                           mov ecx, dword ptr [rdx]
00299717  83 F9 40                        cmp ecx, 0x40
0029971A  72 0C                           jb 0x140299728
0029971C  48 8B 42 38                     mov rax, qword ptr [rdx + 0x38]
00299720  48 85 C0                        test rax, rax
00299723  74 03                           je 0x140299728
00299725  4C 8B C8                        mov r9, rax
00299728  83 F9 48                        cmp ecx, 0x48
0029972B  0F 82 3D FF FF FF               jb 0x14029966e
00299731  48 8B 42 40                     mov rax, qword ptr [rdx + 0x40]
00299735  E9 2C FF FF FF                  jmp 0x140299666
0029973A  83 E8 01                        sub eax, 1
0029973D  74 2E                           je 0x14029976d
0029973F  83 F8 01                        cmp eax, 1
00299742  0F 85 30 FF FF FF               jne 0x140299678
00299748  8B 02                           mov eax, dword ptr [rdx]
0029974A  83 F8 50                        cmp eax, 0x50
0029974D  72 0C                           jb 0x14029975b
0029974F  48 8B 4A 48                     mov rcx, qword ptr [rdx + 0x48]
00299753  48 85 C9                        test rcx, rcx
00299756  74 03                           je 0x14029975b
00299758  4C 8B C9                        mov r9, rcx
0029975B  83 F8 58                        cmp eax, 0x58
0029975E  0F 82 0A FF FF FF               jb 0x14029966e
00299764  48 8B 42 50                     mov rax, qword ptr [rdx + 0x50]
00299768  E9 F9 FE FF FF                  jmp 0x140299666
0029976D  8B 0A                           mov ecx, dword ptr [rdx]
0029976F  83 F9 60                        cmp ecx, 0x60
00299772  72 0C                           jb 0x140299780
00299774  48 8B 42 58                     mov rax, qword ptr [rdx + 0x58]
00299778  48 85 C0                        test rax, rax
0029977B  74 03                           je 0x140299780
0029977D  4C 8B C8                        mov r9, rax
00299780  83 F9 68                        cmp ecx, 0x68
00299783  0F 82 E5 FE FF FF               jb 0x14029966e
00299789  48 8B 42 60                     mov rax, qword ptr [rdx + 0x60]
0029978D  E9 D4 FE FF FF                  jmp 0x140299666
00299792  48 89 1F                        mov qword ptr [rdi], rbx
00299795  48 8B 4D 10                     mov rcx, qword ptr [rbp + 0x10]
00299799  48 89 4F 08                     mov qword ptr [rdi + 8], rcx
0029979D  48 C7 47 10 00 00 00 00         mov qword ptr [rdi + 0x10], 0
002997A5  4C 89 47 18                     mov qword ptr [rdi + 0x18], r8
002997A9  4D 85 C9                        test r9, r9
002997AC  74 19                           je 0x1402997c7
002997AE  48 8D 57 10                     lea rdx, [rdi + 0x10]
002997B2  48 8B CD                        mov rcx, rbp
002997B5  49 8B C1                        mov rax, r9
002997B8  E8 13 13 42 00                  call 0x1406baad0
002997BD  85 C0                           test eax, eax
002997BF  0F 88 9D 00 00 00               js 0x140299862
002997C5  75 5D                           jne 0x140299824
002997C7  48 8B 45 08                     mov rax, qword ptr [rbp + 8]
002997CB  48 3B D8                        cmp rbx, rax
002997CE  75 40                           jne 0x140299810
002997D0  4D 85 F6                        test r14, r14
002997D3  74 62                           je 0x140299837
002997D5  48 8B 83 38 01 00 00            mov rax, qword ptr [rbx + 0x138]
002997DC  48 8B 58 30                     mov rbx, qword ptr [rax + 0x30]
002997E0  E9 E5 FD FF FF                  jmp 0x1402995ca
002997E5  33 FF                           xor edi, edi
002997E7  33 D2                           xor edx, edx
002997E9  EB C7                           jmp 0x1402997b2
002997EB  8B 0A                           mov ecx, dword ptr [rdx]
002997ED  83 F9 70                        cmp ecx, 0x70
002997F0  72 0C                           jb 0x1402997fe
002997F2  48 8B 42 68                     mov rax, qword ptr [rdx + 0x68]
002997F6  48 85 C0                        test rax, rax
002997F9  74 03                           je 0x1402997fe
002997FB  4C 8B C8                        mov r9, rax
002997FE  83 F9 78                        cmp ecx, 0x78
00299801  0F 82 67 FE FF FF               jb 0x14029966e
00299807  48 8B 42 70                     mov rax, qword ptr [rdx + 0x70]
0029980B  E9 56 FE FF FF                  jmp 0x140299666
00299810  83 4D 40 04                     or dword ptr [rbp + 0x40], 4
00299814  48 8B D8                        mov rbx, rax
00299817  E9 AE FD FF FF                  jmp 0x1402995ca
0029981C  45 84 E4                        test r12b, r12b
0029981F  74 22                           je 0x140299843
00299821  83 0E 01                        or dword ptr [rsi], 1
00299824  48 85 FF                        test rdi, rdi
00299827  0F 84 69 FE FF FF               je 0x140299696
0029982D  66 44 01 6D 4A                  add word ptr [rbp + 0x4a], r13w
00299832  E9 5F FE FF FF                  jmp 0x140299696
00299837  48 85 FF                        test rdi, rdi
0029983A  74 99                           je 0x1402997d5
0029983C  66 44 01 6D 4A                  add word ptr [rbp + 0x4a], r13w
00299841  EB 92                           jmp 0x1402997d5
00299843  45 33 C0                        xor r8d, r8d
00299846  48 63 D0                        movsxd rdx, eax
00299849  41 B9 B8 03 00 00               mov r9d, 0x3b8
0029984F  48 C7 44 24 20 00 00 00 00      mov qword ptr [rsp + 0x20], 0
00299858  41 8D 48 22                     lea ecx, [r8 + 0x22]
0029985C  E8 FF 3D 26 00                  call 0x1404fd660
00299861  CC                              int3
00299862  45 84 FF                        test r15b, r15b
00299865  74 07                           je 0x14029986e
00299867  4D 85 F6                        test r14, r14
0029986A  75 B8                           jne 0x140299824
0029986C  EB AE                           jmp 0x14029981c
0029986E  4D 85 F6                        test r14, r14
00299871  74 A9                           je 0x14029981c
00299873  E9 4F FF FF FF                  jmp 0x1402997c7
00299878  33 D2                           xor edx, edx
0029987A  48 C7 44 24 20 00 00 00 00      mov qword ptr [rsp + 0x20], 0
00299883  45 33 C9                        xor r9d, r9d
00299886  45 33 C0                        xor r8d, r8d
00299889  8D 4A 22                        lea ecx, [rdx + 0x22]
0029988C  E8 CF 3D 26 00                  call 0x1404fd660
00299891  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FsFilterPerformCallbacks(__int64 a1, unsigned __int8 a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (48);
    v_stack_p8 = v_rdi;
    v_stack_p10 = v_r14;
    *(unsigned int *)(a4) = 2;
loc_002995CA:
    if (*(unsigned __int64 *)(a1 + 8) == 0) goto loc_00299694;
    a4 = 0;
    a3 = 0;
    *(unsigned __int64 *)(a1 + 8) = *(unsigned __int64 *)(a1 + 8);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 8) + 48) + 48) == 0) goto loc_00299678;
    if (((unsigned int)(*(unsigned __int8 *)(a1 + 4))) == 254) goto loc_0029964A;
    if (((unsigned int)(*(unsigned __int8 *)(a1 + 4))) == 255) goto loc_002996F0;
    result = (unsigned int)((*(unsigned __int8 *)(a1 + 4)) - (249));
    if (condition_is_equal) goto loc_002997EB;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00299715;
    result = (unsigned int)((result) - (1));
    if (condition_is_not_equal) goto loc_0029973A;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 8) + 48) + 48))))) < 48) goto loc_0029963F;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 8) + 48) + 48) + 40) != 0) {
        a4 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 8) + 48) + 48) + 40);
    }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 8) + 48) + 48))))) < 56) goto loc_0029966E;
    goto loc_00299666;
loc_0029964A:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 8) + 48) + 48))))) < 32) goto loc_0029965D;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 8) + 48) + 48) + 24) != 0) {
        a4 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 8) + 48) + 48) + 24);
    }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 8) + 48) + 48))))) < 40) goto loc_0029966E;
loc_00299666:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 8) + 48) + 48) + 32) != 0) {
        a3 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 8) + 48) + 48) + 32);
    }
    if (a4 != 0) goto loc_002996B3;
    if (a3 != 0) goto loc_002996BC;
loc_00299678:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 312) + 48) != 0) goto loc_002995CA;
    goto loc_002995CA;
loc_00299694:
    result = 0;
loc_00299696:
    v_rsp = (v_rsp) + (48);
    return result;
loc_002996B3:
    if (a3 == 0) goto loc_002997E5;
loc_002996BC:
    if (((unsigned __int16)(*(unsigned __int16 *)(a1 + 74))) >= (*(unsigned __int16 *)(a1 + 72))) goto loc_002996E0;
    result = (unsigned __int16)((*(unsigned __int16 *)(a1 + 74)) + 1);
    v_rdi = ((unsigned int)((unsigned int)(*(unsigned __int16 *)(a1 + 74)))) << (5);
    v_rdi = (v_rdi) + (*(unsigned __int64 *)(a1 + 80));
    *(unsigned __int16 *)(a1 + 74) = (unsigned __int16)(result);
    if (v_rdi != 0) goto loc_00299792;
loc_002996E0:
    if (a2 == 0) goto loc_00299878;
    goto loc_00299696;
loc_002996F0:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 8) + 48) + 48))))) < 16) goto loc_00299703;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 8) + 48) + 48) + 8) != 0) {
        a4 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 8) + 48) + 48) + 8);
    }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 8) + 48) + 48))))) < 24) goto loc_0029966E;
    goto loc_00299666;
loc_00299715:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 8) + 48) + 48))))) < 64) goto loc_00299728;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 8) + 48) + 48) + 56) != 0) {
        a4 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 8) + 48) + 48) + 56);
    }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 8) + 48) + 48))))) < 72) goto loc_0029966E;
    goto loc_00299666;
loc_0029973A:
    result = (unsigned int)((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 8) + 48) + 48) + 64)) - (1));
    if (condition_is_equal) goto loc_0029976D;
    if (((unsigned int)(result)) != 1) goto loc_00299678;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 8) + 48) + 48))))) < 80) goto loc_0029975B;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 8) + 48) + 48) + 72) != 0) {
        a4 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 8) + 48) + 48) + 72);
    }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 8) + 48) + 48))))) < 88) goto loc_0029966E;
    goto loc_00299666;
loc_0029976D:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 8) + 48) + 48))))) < 96) goto loc_00299780;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 8) + 48) + 48) + 88) != 0) {
        a4 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 8) + 48) + 48) + 88);
    }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 8) + 48) + 48))))) < 104) goto loc_0029966E;
    goto loc_00299666;
loc_00299792:
    *(unsigned __int64 *)(v_rdi) = v_stack_p18;
    *(unsigned __int64 *)(v_rdi + 8) = *(unsigned __int64 *)(a1 + 16);
    *(unsigned __int64 *)(v_rdi + 16) = 0;
    *(unsigned __int64 *)(v_rdi + 24) = a3;
    if (a4 == 0) goto loc_002997C7;
loc_002997B2:
    result = guard_dispatch_icall(a1, v_rdi + 16, a3, a4);
    if (sign_flag) goto loc_00299862;
    if ((unsigned int)(result) != 0) goto loc_00299824;
loc_002997C7:
    if (v_stack_p18 != (*(unsigned __int64 *)(a1 + 8))) goto loc_00299810;
    if (v_stack_p10 == 0) goto loc_00299837;
loc_002997D5:
    goto loc_002995CA;
loc_002997E5:
    v_rdi = 0;
    a2 = 0;
    goto loc_002997B2;
loc_002997EB:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2)))) < 112) goto loc_002997FE;
    if (*(unsigned __int64 *)(a2 + 104) != 0) {
        a4 = *(unsigned __int64 *)(a2 + 104);
    }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2)))) < 120) goto loc_0029966E;
    goto loc_00299666;
loc_00299810:
    goto loc_002995CA;
loc_0029981C:
    if ((unsigned __int8)((unsigned __int8)(a3)) == 0) goto loc_00299843;
loc_00299824:
    if (0 == 0) goto loc_00299696;
    goto loc_00299696;
loc_00299837:
    if (0 == 0) goto loc_002997D5;
    goto loc_002997D5;
loc_00299843:
    a3 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(a3 + 34, (int)((unsigned int)(*(unsigned __int64 *)(a2 + 112))), a3, 952);
loc_00299862:
    if (0 == 0) goto loc_0029986E;
    if (v_stack_p10 != 0) goto loc_00299824;
    goto loc_0029981C;
loc_0029986E:
    if (v_stack_p10 == 0) goto loc_0029981C;
    goto loc_002997C7;
loc_00299878:
    a2 = 0;
    v_stack_p20 = 0;
    a4 = 0;
    a3 = 0;
    result = KeBugCheckEx(a2 + 34, a2, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t FsFilterPerformCallbacks(void *Arg1, uint8_t Arg2, int32_t Arg3, void *Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (48);
    v_stack_p8 = local_rdi;
    v_stack_p10 = local_r14;
    *(uint32_t *)(arg4) = 2;
loc_002995CA:
    if (*(uint64_t *)(arg1 + 0x8) == 0) goto loc_00299694;
    Arg4 = 0;
    Arg3 = 0;
    *(uint64_t *)(arg1 + 0x8) = *(uint64_t *)(arg1 + 0x8);
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x8) + 0x30) + 0x30) == 0) goto loc_00299678;
    if (((uint32_t)(*(uint8_t *)(arg1 + 0x4))) == 254) goto loc_0029964A;
    if (((uint32_t)(*(uint8_t *)(arg1 + 0x4))) == 255) goto loc_002996F0;
    result = (uint32_t)((*(uint8_t *)(arg1 + 0x4)) - (249));
    if (condition_is_equal) goto loc_002997EB;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00299715;
    result = (uint32_t)((result) - (1));
    if (condition_is_not_equal) goto loc_0029973A;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x8) + 0x30) + 0x30))))) < 48) goto loc_0029963F;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x8) + 0x30) + 0x30) + 0x28) != 0) {
        Arg4 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x8) + 0x30) + 0x30) + 0x28);
    }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x8) + 0x30) + 0x30))))) < 56) goto loc_0029966E;
    goto loc_00299666;
loc_0029964A:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x8) + 0x30) + 0x30))))) < 32) goto loc_0029965D;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x8) + 0x30) + 0x30) + 0x18) != 0) {
        Arg4 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x8) + 0x30) + 0x30) + 0x18);
    }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x8) + 0x30) + 0x30))))) < 40) goto loc_0029966E;
loc_00299666:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x8) + 0x30) + 0x30) + 0x20) != 0) {
        Arg3 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x8) + 0x30) + 0x30) + 0x20);
    }
    if (Arg4 != NULL) goto loc_002996B3;
    if (Arg3 != 0) goto loc_002996BC;
loc_00299678:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x138) + 0x30) != 0) goto loc_002995CA;
    goto loc_002995CA;
loc_00299694:
    result = 0;
loc_00299696:
    local_rsp = (local_rsp) + (48);
    return result;
loc_002996B3:
    if (Arg3 == 0) goto loc_002997E5;
loc_002996BC:
    if (((uint16_t)(*(uint16_t *)(arg1 + 0x4A))) >= (*(uint16_t *)(arg1 + 0x48))) goto loc_002996E0;
    result = (uint16_t)((*(uint16_t *)(arg1 + 0x4A)) + 1);
    local_rdi = ((uint32_t)((uint32_t)(*(uint16_t *)(arg1 + 0x4A)))) << (5);
    local_rdi = (local_rdi) + (*(uint64_t *)(arg1 + 0x50));
    *(uint16_t *)(arg1 + 0x4A) = (uint16_t)(result);
    if (local_rdi != 0) goto loc_00299792;
loc_002996E0:
    if (Arg2 == 0) goto loc_00299878;
    goto loc_00299696;
loc_002996F0:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x8) + 0x30) + 0x30))))) < 16) goto loc_00299703;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x8) + 0x30) + 0x30) + 0x8) != 0) {
        Arg4 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x8) + 0x30) + 0x30) + 0x8);
    }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x8) + 0x30) + 0x30))))) < 24) goto loc_0029966E;
    goto loc_00299666;
loc_00299715:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x8) + 0x30) + 0x30))))) < 64) goto loc_00299728;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x8) + 0x30) + 0x30) + 0x38) != 0) {
        Arg4 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x8) + 0x30) + 0x30) + 0x38);
    }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x8) + 0x30) + 0x30))))) < 72) goto loc_0029966E;
    goto loc_00299666;
loc_0029973A:
    result = (uint32_t)((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x8) + 0x30) + 0x30) + 0x40)) - (1));
    if (condition_is_equal) goto loc_0029976D;
    if (((uint32_t)(result)) != 1) goto loc_00299678;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x8) + 0x30) + 0x30))))) < 80) goto loc_0029975B;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x8) + 0x30) + 0x30) + 0x48) != 0) {
        Arg4 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x8) + 0x30) + 0x30) + 0x48);
    }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x8) + 0x30) + 0x30))))) < 88) goto loc_0029966E;
    goto loc_00299666;
loc_0029976D:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x8) + 0x30) + 0x30))))) < 96) goto loc_00299780;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x8) + 0x30) + 0x30) + 0x58) != 0) {
        Arg4 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x8) + 0x30) + 0x30) + 0x58);
    }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x8) + 0x30) + 0x30))))) < 104) goto loc_0029966E;
    goto loc_00299666;
loc_00299792:
    *(uint64_t *)(local_rdi) = v_stack_p18;
    *(uint64_t *)(local_rdi + 0x8) = *(uint64_t *)(arg1 + 0x10);
    *(uint64_t *)(local_rdi + 0x10) = 0;
    *(uint64_t *)(local_rdi + 0x18) = Arg3;
    if (Arg4 == NULL) goto loc_002997C7;
loc_002997B2:
    result = guard_dispatch_icall(Arg1, local_rdi + 16, Arg3, Arg4);
    if (sign_flag) goto loc_00299862;
    if ((uint32_t)(result) != 0) goto loc_00299824;
loc_002997C7:
    if (v_stack_p18 != (*(uint64_t *)(arg1 + 0x8))) goto loc_00299810;
    if (v_stack_p10 == 0) goto loc_00299837;
loc_002997D5:
    goto loc_002995CA;
loc_002997E5:
    local_rdi = 0;
    Arg2 = 0;
    goto loc_002997B2;
loc_002997EB:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg2)))) < 112) goto loc_002997FE;
    if (*(uint64_t *)(Arg2 + 0x68) != 0) {
        Arg4 = *(uint64_t *)(Arg2 + 0x68);
    }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg2)))) < 120) goto loc_0029966E;
    goto loc_00299666;
loc_00299810:
    goto loc_002995CA;
loc_0029981C:
    if ((uint8_t)((uint8_t)(Arg3)) == 0) goto loc_00299843;
loc_00299824:
    if (0 == 0) goto loc_00299696;
    goto loc_00299696;
loc_00299837:
    if (0 == 0) goto loc_002997D5;
    goto loc_002997D5;
loc_00299843:
    Arg3 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(Arg3 + 34, (int32_t)((uint32_t)(*(uint64_t *)(Arg2 + 0x70))), Arg3, 952);
loc_00299862:
    if (0 == 0) goto loc_0029986E;
    if (v_stack_p10 != 0) goto loc_00299824;
    goto loc_0029981C;
loc_0029986E:
    if (v_stack_p10 == 0) goto loc_0029981C;
    goto loc_002997C7;
loc_00299878:
    Arg2 = 0;
    v_stack_p20 = 0;
    Arg4 = 0;
    Arg3 = 0;
    result = KeBugCheckEx(Arg2 + 34, Arg2, Arg3, Arg4);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x4` | `8` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x40` | `32` | `R/W` |
| `Arg1` | `+ 0x48` | `16` | `R` |
| `Arg1` | `+ 0x4A` | `16` | `R` |
| `Arg1` | `+ 0x4A` | `16` | `R/W` |
| `Arg1` | `+ 0x4A` | `16` | `W` |
| `Arg1` | `+ 0x50` | `64` | `R` |
| `Arg4` | `+ 0x0` | `32` | `R/W` |
| `Arg4` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00299590&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
