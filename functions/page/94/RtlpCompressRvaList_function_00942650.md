# RtlpCompressRvaList

- RVA: `0x00942650`–`0x00942A65` (길이 `1,045` bytes)
- VA: `0x0000000140942650`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000903D8`
- 디코드: `258`개 명령, `1,045/1,045` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **6**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x009426AB` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x009426D3` → [RtlpSetRvaListRvaStateBits](RtlpSetRvaListRvaStateBits_function_00942DD0.md) (function, `0x00942DD0`)
- `0x009427E2` → [MiQueryFlagsForRvaEntry](MiQueryFlagsForRvaEntry_function_00942CC0.md) (function, `0x00942CC0`)
- `0x00942879` → [MiImageGetRawRvaState](MiImageGetRawRvaState_function_00942D60.md) (function, `0x00942D60`)
- `0x00942A38` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00942A59` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [RtlCreateRvaList](RtlCreateRvaList_function_00942490.md) at `0x009424E7`
- [RtlCreateRvaList](RtlCreateRvaList_function_00942490.md) at `0x009425F2`

### Static image references
- `0x009426E8` → RVA `0x0099FB70` (`MiImageCfgRvaIteratorNext`; read)
- `0x009426EF` → RVA `0x00012D10` (`.rdata`; read)
- `0x009426FB` → RVA `0x00942A70` (`MiImageRvaRawEnumNext`; read)
- `0x00942A04` → RVA `0x00E2D828` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x009426AB` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00942A38` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00942A59` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00942650  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
00942655  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
0094265A  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
0094265F  53                              push rbx
00942660  55                              push rbp
00942661  56                              push rsi
00942662  57                              push rdi
00942663  41 54                           push r12
00942665  41 55                           push r13
00942667  41 56                           push r14
00942669  41 57                           push r15
0094266B  48 81 EC 88 00 00 00            sub rsp, 0x88
00942672  48 8B BC 24 F0 00 00 00         mov rdi, qword ptr [rsp + 0xf0]
0094267A  48 8D 44 24 58                  lea rax, [rsp + 0x58]
0094267F  45 33 FF                        xor r15d, r15d
00942682  48 8B F2                        mov rsi, rdx
00942685  4C 8B F1                        mov r14, rcx
00942688  44 89 7C 24 58                  mov dword ptr [rsp + 0x58], r15d
0094268D  48 85 FF                        test rdi, rdi
00942690  48 8B CE                        mov rcx, rsi
00942693  41 8B DF                        mov ebx, r15d
00942696  4C 8B E7                        mov r12, rdi
00942699  49 0F 44 C7                     cmove rax, r15
0094269D  45 8B EF                        mov r13d, r15d
009426A0  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
009426A5  48 8B D0                        mov rdx, rax
009426A8  49 8B C0                        mov rax, r8
009426AB  E8 20 84 D7 FF                  call 0x1406baad0
009426B0  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
009426B4  8B E8                           mov ebp, eax
009426B6  85 C0                           test eax, eax
009426B8  0F 84 67 03 00 00               je 0x140942a25
009426BE  48 85 FF                        test rdi, rdi
009426C1  74 15                           je 0x1409426d8
009426C3  44 8B 44 24 58                  mov r8d, dword ptr [rsp + 0x58]
009426C8  4C 8D 67 04                     lea r12, [rdi + 4]
009426CC  33 D2                           xor edx, edx
009426CE  89 07                           mov dword ptr [rdi], eax
009426D0  49 8B CE                        mov rcx, r14
009426D3  E8 F8 06 00 00                  call 0x140942dd0
009426D8  41 BD 04 00 00 00               mov r13d, 4
009426DE  C7 44 24 50 01 00 00 00         mov dword ptr [rsp + 0x50], 1
009426E6  8B FD                           mov edi, ebp
009426E8  4C 8D 1D 81 D4 05 00            lea r11, [rip + 0x5d481]
009426EF  48 8D 15 1A 06 6D FF            lea rdx, [rip - 0x92f9e6]
009426F6  44 89 6C 24 5C                  mov dword ptr [rsp + 0x5c], r13d
009426FB  4C 8D 05 6E 03 00 00            lea r8, [rip + 0x36e]
00942702  3B EF                           cmp ebp, edi
00942704  0F 85 01 02 00 00               jne 0x14094290b
0094270A  48 8B 84 24 E8 00 00 00         mov rax, qword ptr [rsp + 0xe8]
00942712  8B DF                           mov ebx, edi
00942714  89 5C 24 68                     mov dword ptr [rsp + 0x68], ebx
00942718  49 3B C0                        cmp rax, r8
0094271B  0F 85 30 03 00 00               jne 0x140942a51
00942721  4C 8B 94 24 D8 00 00 00         mov r10, qword ptr [rsp + 0xd8]
00942729  41 83 BA 38 01 00 00 00         cmp dword ptr [r10 + 0x138], 0
00942731  0F 84 7C 02 00 00               je 0x1409429b3
00942737  41 83 BA 90 00 00 00 00         cmp dword ptr [r10 + 0x90], 0
0094273F  4D 8D B2 98 00 00 00            lea r14, [r10 + 0x98]
00942746  41 8B FF                        mov edi, r15d
00942749  41 8B F7                        mov esi, r15d
0094274C  0F 86 14 01 00 00               jbe 0x140942866
00942752  49 8D 5E 20                     lea rbx, [r14 + 0x20]
00942756  33 ED                           xor ebp, ebp
00942758  48 8B 43 F0                     mov rax, qword ptr [rbx - 0x10]
0094275C  48 85 C0                        test rax, rax
0094275F  0F 84 DA 00 00 00               je 0x14094283f
00942765  45 8B 3E                        mov r15d, dword ptr [r14]
00942768  45 3B BA 38 01 00 00            cmp r15d, dword ptr [r10 + 0x138]
0094276F  0F 85 BA 00 00 00               jne 0x14094282f
00942775  49 3B C3                        cmp rax, r11
00942778  0F 85 AF 02 00 00               jne 0x140942a2d
0094277E  44 8B 2B                        mov r13d, dword ptr [rbx]
00942781  44 8B FD                        mov r15d, ebp
00942784  40 88 AC 24 E0 00 00 00         mov byte ptr [rsp + 0xe0], bpl
0094278C  44 8B CD                        mov r9d, ebp
0094278F  89 6C 24 54                     mov dword ptr [rsp + 0x54], ebp
00942793  45 85 ED                        test r13d, r13d
00942796  0F 84 90 00 00 00               je 0x14094282c
0094279C  48 8B 4B F8                     mov rcx, qword ptr [rbx - 8]
009427A0  41 8B 52 54                     mov edx, dword ptr [r10 + 0x54]
009427A4  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
009427A9  89 54 24 64                     mov dword ptr [rsp + 0x64], edx
009427AD  45 85 ED                        test r13d, r13d
009427B0  74 64                           je 0x140942816
009427B2  48 8D 43 E4                     lea rax, [rbx - 0x1c]
009427B6  4C 8D 84 24 E0 00 00 00         lea r8, [rsp + 0xe0]
009427BE  4C 89 44 24 40                  mov qword ptr [rsp + 0x40], r8
009427C3  4C 8D 44 24 54                  lea r8, [rsp + 0x54]
009427C8  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
009427CD  41 8B 42 24                     mov eax, dword ptr [r10 + 0x24]
009427D1  48 89 6C 24 30                  mov qword ptr [rsp + 0x30], rbp
009427D6  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
009427DA  41 8B 42 20                     mov eax, dword ptr [r10 + 0x20]
009427DE  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
009427E2  E8 D9 04 00 00                  call 0x140942cc0
009427E7  85 C0                           test eax, eax
009427E9  0F 88 15 02 00 00               js 0x140942a04
009427EF  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
009427F4  41 FF CD                        dec r13d
009427F7  8B 54 24 64                     mov edx, dword ptr [rsp + 0x64]
009427FB  48 03 CA                        add rcx, rdx
009427FE  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
00942803  40 38 AC 24 E0 00 00 00         cmp byte ptr [rsp + 0xe0], bpl
0094280B  0F 85 02 02 00 00               jne 0x140942a13
00942811  44 8B 7C 24 54                  mov r15d, dword ptr [rsp + 0x54]
00942816  44 89 2B                        mov dword ptr [rbx], r13d
00942819  48 89 4B F8                     mov qword ptr [rbx - 8], rcx
0094281D  4C 8B 94 24 D8 00 00 00         mov r10, qword ptr [rsp + 0xd8]
00942825  4C 8D 1D 44 D3 05 00            lea r11, [rip + 0x5d344]
0094282C  45 89 3E                        mov dword ptr [r14], r15d
0094282F  45 85 FF                        test r15d, r15d
00942832  74 0B                           je 0x14094283f
00942834  85 FF                           test edi, edi
00942836  0F 85 09 02 00 00               jne 0x140942a45
0094283C  41 8B FF                        mov edi, r15d
0094283F  FF C6                           inc esi
00942841  49 83 C6 28                     add r14, 0x28
00942845  48 83 C3 28                     add rbx, 0x28
00942849  41 3B B2 90 00 00 00            cmp esi, dword ptr [r10 + 0x90]
00942850  0F 82 02 FF FF FF               jb 0x140942758
00942856  8B 6C 24 60                     mov ebp, dword ptr [rsp + 0x60]
0094285A  45 33 FF                        xor r15d, r15d
0094285D  8B 5C 24 68                     mov ebx, dword ptr [rsp + 0x68]
00942861  44 8B 6C 24 5C                  mov r13d, dword ptr [rsp + 0x5c]
00942866  48 8B 74 24 78                  mov rsi, qword ptr [rsp + 0x78]
0094286B  48 85 F6                        test rsi, rsi
0094286E  74 18                           je 0x140942888
00942870  85 FF                           test edi, edi
00942872  74 14                           je 0x140942888
00942874  8B D7                           mov edx, edi
00942876  49 8B CA                        mov rcx, r10
00942879  E8 E2 04 00 00                  call 0x140942d60
0094287E  4C 8B 94 24 D8 00 00 00         mov r10, qword ptr [rsp + 0xd8]
00942886  89 06                           mov dword ptr [rsi], eax
00942888  48 8B B4 24 D8 00 00 00         mov rsi, qword ptr [rsp + 0xd8]
00942890  4C 8B B4 24 D0 00 00 00         mov r14, qword ptr [rsp + 0xd0]
00942898  41 89 BA 38 01 00 00            mov dword ptr [r10 + 0x138], edi
0094289F  85 FF                           test edi, edi
009428A1  0F 84 0C 01 00 00               je 0x1409429b3
009428A7  3B FB                           cmp edi, ebx
009428A9  0F 86 FE 00 00 00               jbe 0x1409429ad
009428AF  4D 85 E4                        test r12, r12
009428B2  74 45                           je 0x1409428f9
009428B4  8B 44 24 58                     mov eax, dword ptr [rsp + 0x58]
009428B8  89 84 24 E0 00 00 00            mov dword ptr [rsp + 0xe0], eax
009428BF  85 C0                           test eax, eax
009428C1  74 36                           je 0x1409428f9
009428C3  41 8B 46 08                     mov eax, dword ptr [r14 + 8]
009428C7  83 F8 01                        cmp eax, 1
009428CA  76 2D                           jbe 0x1409428f9
009428CC  0F AF 44 24 50                  imul eax, dword ptr [rsp + 0x50]
009428D1  41 8B D7                        mov edx, r15d
009428D4  44 8B C0                        mov r8d, eax
009428D7  48 8D 84 24 E0 00 00 00         lea rax, [rsp + 0xe0]
009428DF  0F A3 10                        bt dword ptr [rax], edx
009428E2  73 0D                           jae 0x1409428f1
009428E4  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
009428E8  8B CA                           mov ecx, edx
009428EA  49 03 C8                        add rcx, r8
009428ED  48 0F AB 08                     bts qword ptr [rax], rcx
009428F1  FF C2                           inc edx
009428F3  41 3B 56 08                     cmp edx, dword ptr [r14 + 8]
009428F7  72 DE                           jb 0x1409428d7
009428F9  FF 44 24 50                     inc dword ptr [rsp + 0x50]
009428FD  48 8D 15 0C 04 6D FF            lea rdx, [rip - 0x92fbf4]
00942904  4C 8D 1D 65 D2 05 00            lea r11, [rip + 0x5d265]
0094290B  44 8B CF                        mov r9d, edi
0094290E  41 8B CF                        mov ecx, r15d
00942911  44 2B CD                        sub r9d, ebp
00942914  4C 8D 05 55 01 00 00            lea r8, [rip + 0x155]
0094291B  83 F9 04                        cmp ecx, 4
0094291E  0F 83 DE FD FF FF               jae 0x140942702
00942924  8B C1                           mov eax, ecx
00942926  44 8B 04 82                     mov r8d, dword ptr [rdx + rax*4]
0094292A  45 3B C8                        cmp r9d, r8d
0094292D  73 04                           jae 0x140942933
0094292F  FF C1                           inc ecx
00942931  EB E1                           jmp 0x140942914
00942933  33 D2                           xor edx, edx
00942935  41 8B C1                        mov eax, r9d
00942938  41 F7 F0                        div r8d
0094293B  44 8B C8                        mov r9d, eax
0094293E  83 F8 3F                        cmp eax, 0x3f
00942941  0F 83 B2 00 00 00               jae 0x1409429f9
00942947  4D 85 E4                        test r12, r12
0094294A  74 10                           je 0x14094295c
0094294C  0F B6 C1                        movzx eax, cl
0094294F  C0 E0 06                        shl al, 6
00942952  41 0A C1                        or al, r9b
00942955  41 88 04 24                     mov byte ptr [r12], al
00942959  49 FF C4                        inc r12
0094295C  45 0F AF C1                     imul r8d, r9d
00942960  48 8D 15 A9 03 6D FF            lea rdx, [rip - 0x92fc57]
00942967  41 FF C5                        inc r13d
0094296A  44 89 6C 24 5C                  mov dword ptr [rsp + 0x5c], r13d
0094296F  41 03 E8                        add ebp, r8d
00942972  4C 8D 05 F7 00 00 00            lea r8, [rip + 0xf7]
00942979  89 6C 24 60                     mov dword ptr [rsp + 0x60], ebp
0094297D  3B EF                           cmp ebp, edi
0094297F  75 8A                           jne 0x14094290b
00942981  48 8D 15 88 03 6D FF            lea rdx, [rip - 0x92fc78]
00942988  4C 8D 05 E1 00 00 00            lea r8, [rip + 0xe1]
0094298F  83 F9 03                        cmp ecx, 3
00942992  0F 84 6A FD FF FF               je 0x140942702
00942998  4D 85 E4                        test r12, r12
0094299B  74 08                           je 0x1409429a5
0094299D  41 C6 04 24 C0                  mov byte ptr [r12], 0xc0
009429A2  49 FF C4                        inc r12
009429A5  41 FF C5                        inc r13d
009429A8  E9 42 FD FF FF                  jmp 0x1409426ef
009429AD  41 BF 7B 00 00 C0               mov r15d, 0xc000007b
009429B3  8B 5C 24 50                     mov ebx, dword ptr [rsp + 0x50]
009429B7  48 8B BC 24 F0 00 00 00         mov rdi, qword ptr [rsp + 0xf0]
009429BF  48 85 FF                        test rdi, rdi
009429C2  75 0E                           jne 0x1409429d2
009429C4  48 8B 8C 24 F8 00 00 00         mov rcx, qword ptr [rsp + 0xf8]
009429CC  41 8B D5                        mov edx, r13d
009429CF  48 89 11                        mov qword ptr [rcx], rdx
009429D2  48 8B 8C 24 00 01 00 00         mov rcx, qword ptr [rsp + 0x100]
009429DA  41 8B C7                        mov eax, r15d
009429DD  48 85 C9                        test rcx, rcx
009429E0  74 02                           je 0x1409429e4
009429E2  89 19                           mov dword ptr [rcx], ebx
009429E4  48 81 C4 88 00 00 00            add rsp, 0x88
009429EB  41 5F                           pop r15
009429ED  41 5E                           pop r14
009429EF  41 5D                           pop r13
009429F1  41 5C                           pop r12
009429F3  5F                              pop rdi
009429F4  5E                              pop rsi
009429F5  5D                              pop rbp
009429F6  5B                              pop rbx
009429F7  C3                              ret
009429F8  CC                              int3
009429F9  41 B9 3F 00 00 00               mov r9d, 0x3f
009429FF  E9 43 FF FF FF                  jmp 0x140942947
00942A04  C7 05 1A AE 4E 00 0E 00 00 00   mov dword ptr [rip + 0x4eae1a], 0xe
00942A0E  E9 0A FE FF FF                  jmp 0x14094281d
00942A13  44 8B 4C 24 54                  mov r9d, dword ptr [rsp + 0x54]
00942A18  4C 8B 94 24 D8 00 00 00         mov r10, qword ptr [rsp + 0xd8]
00942A20  E9 88 FD FF FF                  jmp 0x1409427ad
00942A25  41 BF 0D 00 00 C0               mov r15d, 0xc000000d
00942A2B  EB 92                           jmp 0x1409429bf
00942A2D  4C 8D 43 E4                     lea r8, [rbx - 0x1c]
00942A31  49 8B CA                        mov rcx, r10
00942A34  48 8D 53 F8                     lea rdx, [rbx - 8]
00942A38  E8 93 80 D7 FF                  call 0x1406baad0
00942A3D  44 8B F8                        mov r15d, eax
00942A40  E9 D8 FD FF FF                  jmp 0x14094281d
00942A45  41 3B FF                        cmp edi, r15d
00942A48  41 0F 43 FF                     cmovae edi, r15d
00942A4C  E9 EE FD FF FF                  jmp 0x14094283f
00942A51  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
00942A56  48 8B CE                        mov rcx, rsi
00942A59  E8 72 80 D7 FF                  call 0x1406baad0
00942A5E  8B F8                           mov edi, eax
00942A60  E9 3A FE FF FF                  jmp 0x14094289f
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpCompressRvaList(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m60;
    unsigned int v_stack_m64;
    unsigned int v_stack_m68;
    unsigned int v_stack_m6C;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m74;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned int v_stack_mA0;
    unsigned int v_stack_mA8;
    unsigned __int64 v_stack_p10;
    unsigned __int8 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p54;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_pD8;

    v_stack_p20 = a4;
    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (136);
    v_r15 = 0;
    v_stack_m70 = 0;
    result = v_stack_m70;
    if (a5 == 0) { result = 0; }
    v_stack_m50 = result;
    result = guard_dispatch_icall(a2, result, a3, a4);
    v_stack_m68 = (unsigned int)(result);
    if ((unsigned int)(result) == 0) goto loc_00942A25;
    v_r12 = a5;
    if (a5 != 0) {
        a3 = v_stack_m70;
        v_r12 = a5 + 4;
        a2 = 0;
        *(unsigned int *)(a5) = (unsigned int)(result);
        a1 = a1;
        result = RtlpSetRvaListRvaStateBits(a1, a2, a3, a4);
    }
    v_stack_m78 = 1;
loc_009426EF:
    v_stack_m6C = 4;
loc_00942702:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))))))) goto loc_0094290B;
    v_stack_m60 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))))));
    if (v_stack_p20 != (v_rip + 878)) goto loc_00942A51;
    if ((*(unsigned int *)(v_stack_p10 + 312)) == 0) goto loc_009429B3;
    if ((*(unsigned int *)(v_stack_p10 + 144)) <= 0) goto loc_00942866;
    v_rbp = 0;
loc_00942758:
    if (*(unsigned __int64 *)(v_stack_p10 + 152 + 32 - 16) == 0) goto loc_0094283F;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 152)))) != (*(unsigned int *)(v_stack_p10 + 312))) goto loc_0094282F;
    if ((*(unsigned __int64 *)(v_stack_p10 + 152 + 32 - 16)) != (v_rip + 382081)) goto loc_00942A2D;
    v_stack_p18 = 0;
    v_stack_m74 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 152 + 32))) == 0) goto loc_0094282C;
    v_stack_m58 = *(unsigned __int64 *)(v_stack_p10 + 152 + 32 - 8);
    v_stack_m64 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 84)));
loc_009427AD:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 152 + 32))) == 0) goto loc_00942816;
    v_stack_m88 = v_stack_p18;
    v_stack_m90 = v_stack_p10 + 152 + 32 - 28;
    v_stack_m98 = 0;
    v_stack_mA0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 36)));
    v_stack_mA8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 32)));
    result = MiQueryFlagsForRvaEntry(*(unsigned __int64 *)(v_stack_p10 + 152 + 32 - 8), (unsigned int)(*(unsigned int *)(v_stack_p10 + 84)), v_stack_m74, 0);
    if (sign_flag) goto loc_00942A04;
    v_r13 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p10 + 152 + 32))) - 1);
    a1 = (v_stack_m58) + ((unsigned int)(v_stack_m64));
    v_stack_m58 = a1;
    if (v_stack_p18 != 0) goto loc_00942A13;
loc_00942816:
    *(unsigned int *)(v_stack_p10 + 152 + 32) = (unsigned int)(v_r13);
    *(unsigned __int64 *)(v_stack_p10 + 152 + 32 - 8) = a1;
loc_0094281D:
loc_0094282C:
    *(unsigned int *)(v_stack_p10 + 152) = (unsigned int)((unsigned int)(v_stack_m74));
loc_0094282F:
    if ((unsigned int)((unsigned int)(v_stack_m74)) == 0) goto loc_0094283F;
    if (0 != 0) goto loc_00942A45;
loc_0094283F:
    v_rsi = (unsigned int)((0) + 1);
    v_r14 = (v_stack_p10 + 152) + (40);
    v_rbx = (v_stack_p10 + 152 + 32) + (40);
    if (((unsigned int)(v_rsi)) < (*(unsigned int *)(v_stack_p10 + 144))) goto loc_00942758;
    v_r15 = 0;
loc_00942866:
    if (v_stack_m50 == 0) goto loc_00942888;
    v_r10 = v_stack_p10;
    if ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m74)))) != 0) {
        a2 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m74))));
        a1 = v_stack_p10;
        result = MiImageGetRawRvaState(a1, a2, v_stack_m74, 0);
        v_r10 = v_stack_p10;
        *(unsigned int *)(v_stack_m50) = (unsigned int)(result);
    }
    *(unsigned int *)(v_r10 + 312) = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m74))));
loc_0094289F:
    if ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m74)))) == 0) goto loc_009429B3;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m74))))) <= ((unsigned int)((unsigned int)(v_stack_m60)))) goto loc_009429AD;
    if (v_r12 == 0) goto loc_009428F9;
    v_stack_p18 = (unsigned int)((unsigned int)(v_stack_m70));
    if ((unsigned int)((unsigned int)(v_stack_m70)) == 0) goto loc_009428F9;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 8)))) <= 1) goto loc_009428F9;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p8 + 8))) * (v_stack_m78));
loc_009428D7:
    result = v_stack_p18;
    if (!(condition_is_above_or_equal)) {
        result = *(unsigned __int64 *)(v_stack_p8 + 40);
        a1 = 0;
        a1 = (a1) + ((unsigned int)((unsigned int)(result)));
    }
    a2 = (unsigned int)((0) + 1);
    if (((unsigned int)(a2)) < (*(unsigned int *)(v_stack_p8 + 8))) goto loc_009428D7;
loc_009428F9:
loc_0094290B:
    a4 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m74)))))) - ((unsigned int)((unsigned int)(v_stack_m68))));
loc_00942914:
    if (0 >= 4) goto loc_00942702;
    if (((unsigned int)(a4)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 9632756 + 0 * 4))))) goto loc_00942933;
    a1 = (unsigned int)((0) + 1);
    goto loc_00942914;
loc_00942933:
    a2 = 0;
    if (((unsigned int)((unsigned int)((unsigned int)(a4)))) >= 63) goto loc_009429F9;
loc_00942947:
    result = (unsigned int)((unsigned int)(a4));
    if (v_r12 != 0) {
        result = (unsigned __int8)(a1);
        result = (unsigned __int8)((result) << (6));
        result = (unsigned __int8)((result) | ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a4)))))));
        *(unsigned __int8 *)(v_r12) = (unsigned __int8)(result);
        v_r12 = (v_r12) + 1;
    }
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip - 9632756 + 0 * 4))) * ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a4)))))));
    v_r13 = (unsigned int)(((unsigned int)(v_stack_m6C)) + 1);
    v_stack_m6C = (unsigned int)(v_r13);
    v_rbp = (unsigned int)(((unsigned int)(v_stack_m68)) + ((unsigned int)(a3)));
    v_stack_m68 = (unsigned int)(v_rbp);
    if (((unsigned int)(v_rbp)) != ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m74)))))) goto loc_0094290B;
    if (((unsigned int)(a1)) == 3) goto loc_00942702;
    if (v_r12 != 0) {
        *(unsigned __int8 *)(v_r12) = 192;
        v_r12 = (v_r12) + 1;
    }
    v_r13 = (unsigned int)((v_r13) + 1);
    goto loc_009426EF;
loc_009429AD:
loc_009429B3:
loc_009429BF:
    if (a5 == 0) {
        a1 = a6;
        a2 = (unsigned int)(v_r13);
        *(unsigned __int64 *)(a1) = a2;
    }
    if (a7 != 0) {
        *(unsigned int *)(a7) = (unsigned int)((unsigned int)(v_stack_m78));
    }
    v_rsp = (v_rsp) + (136);
    return (unsigned int)((unsigned int)((unsigned int)(0xC000007BULL)));
loc_009429F9:
    goto loc_00942947;
loc_00942A04:
    *(unsigned int *)(v_rip + 5156378) = 14;
    goto loc_0094281D;
loc_00942A13:
    goto loc_009427AD;
loc_00942A25:
    goto loc_009429BF;
loc_00942A2D:
    result = guard_dispatch_icall(v_stack_pD8, (unsigned int)(v_stack_m78) - 8, (unsigned int)(v_stack_m78) - 28, (unsigned int)(v_stack_p54));
    goto loc_0094281D;
loc_00942A45:
    if (((unsigned int)(a5)) >= ((unsigned int)((unsigned int)((unsigned int)(result))))) { a5 = (unsigned int)((unsigned int)((unsigned int)(result))); }
    goto loc_0094283F;
loc_00942A51:
    result = guard_dispatch_icall(v_stack_p10, v_stack_p78, (unsigned int)(v_stack_m78) - 28, (unsigned int)(v_stack_p54));
    goto loc_0094289F;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpCompressRvaList(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, void *Arg6, int64_t Arg7)
{
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m60;
    uint32_t v_stack_m64;
    uint32_t v_stack_m68;
    uint32_t v_stack_m6C;
    uint64_t v_stack_m70;
    uint32_t v_stack_m74;
    uint32_t v_stack_m78;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint32_t v_stack_mA0;
    uint32_t v_stack_mA8;
    uint64_t v_stack_p10;
    uint8_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p54;
    uint64_t v_stack_p78;
    uint64_t v_stack_p8;
    uint64_t v_stack_pD8;

    v_stack_p20 = Arg4;
    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (136);
    local_r15 = 0;
    v_stack_m70 = 0;
    result = v_stack_m70;
    if (Arg5 == 0) { result = 0; }
    v_stack_m50 = result;
    result = guard_dispatch_icall(Arg2, result, Arg3, Arg4);
    v_stack_m68 = (uint32_t)(result);
    if ((uint32_t)(result) == 0) goto loc_00942A25;
    local_r12 = Arg5;
    if (Arg5 != 0) {
        Arg3 = v_stack_m70;
        local_r12 = Arg5 + 4;
        Arg2 = 0;
        *(uint32_t *)(Arg5) = (uint32_t)(result);
        Arg1 = Arg1;
        result = RtlpSetRvaListRvaStateBits(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m78 = 1;
loc_009426EF:
    v_stack_m6C = 4;
loc_00942702:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))))))) goto loc_0094290B;
    v_stack_m60 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))))));
    if (v_stack_p20 != (v_rip + 878)) goto loc_00942A51;
    if ((*(uint32_t *)(v_stack_p10 + 0x138)) == 0) goto loc_009429B3;
    if ((*(uint32_t *)(v_stack_p10 + 0x90)) <= 0) goto loc_00942866;
    local_rbp = 0;
loc_00942758:
    if (*(uint64_t *)(v_stack_p10 + 0x98 + 0x20 - 0x10) == 0) goto loc_0094283F;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x98)))) != (*(uint32_t *)(v_stack_p10 + 0x138))) goto loc_0094282F;
    if ((*(uint64_t *)(v_stack_p10 + 0x98 + 0x20 - 0x10)) != (v_rip + 382081)) goto loc_00942A2D;
    v_stack_p18 = 0;
    v_stack_m74 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x98 + 0x20))) == 0) goto loc_0094282C;
    v_stack_m58 = *(uint64_t *)(v_stack_p10 + 0x98 + 0x20 - 0x8);
    v_stack_m64 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x54)));
loc_009427AD:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x98 + 0x20))) == 0) goto loc_00942816;
    v_stack_m88 = v_stack_p18;
    v_stack_m90 = v_stack_p10 + 152 + 32 - 28;
    v_stack_m98 = 0;
    v_stack_mA0 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x24)));
    v_stack_mA8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x20)));
    result = MiQueryFlagsForRvaEntry(*(uint64_t *)(v_stack_p10 + 0x98 + 0x20 - 0x8), (uint32_t)(*(uint32_t *)(v_stack_p10 + 0x54)), v_stack_m74, 0);
    if (sign_flag) goto loc_00942A04;
    local_r13 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x98 + 0x20))) - 1);
    Arg1 = (v_stack_m58) + ((uint32_t)(v_stack_m64));
    v_stack_m58 = Arg1;
    if (v_stack_p18 != 0) goto loc_00942A13;
loc_00942816:
    *(uint32_t *)(v_stack_p10 + 0x98 + 0x20) = (uint32_t)(local_r13);
    *(uint64_t *)(v_stack_p10 + 0x98 + 0x20 - 0x8) = Arg1;
loc_0094281D:
loc_0094282C:
    *(uint32_t *)(v_stack_p10 + 0x98) = (uint32_t)((uint32_t)(v_stack_m74));
loc_0094282F:
    if ((uint32_t)((uint32_t)(v_stack_m74)) == 0) goto loc_0094283F;
    if (0 != 0) goto loc_00942A45;
loc_0094283F:
    local_rsi = (uint32_t)((0) + 1);
    local_r14 = (v_stack_p10 + 152) + (40);
    local_rbx = (v_stack_p10 + 152 + 32) + (40);
    if (((uint32_t)(local_rsi)) < (*(uint32_t *)(v_stack_p10 + 0x90))) goto loc_00942758;
    local_r15 = 0;
loc_00942866:
    if (v_stack_m50 == 0) goto loc_00942888;
    local_r10 = v_stack_p10;
    if ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m74)))) != 0) {
        Arg2 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m74))));
        Arg1 = v_stack_p10;
        result = MiImageGetRawRvaState(Arg1, Arg2, v_stack_m74, 0);
        local_r10 = v_stack_p10;
        *(uint32_t *)(v_stack_m50) = (uint32_t)(result);
    }
    *(uint32_t *)(local_r10 + 0x138) = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m74))));
loc_0094289F:
    if ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m74)))) == 0) goto loc_009429B3;
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m74))))) <= ((uint32_t)((uint32_t)(v_stack_m60)))) goto loc_009429AD;
    if (local_r12 == 0) goto loc_009428F9;
    v_stack_p18 = (uint32_t)((uint32_t)(v_stack_m70));
    if ((uint32_t)((uint32_t)(v_stack_m70)) == 0) goto loc_009428F9;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x8)))) <= 1) goto loc_009428F9;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x8))) * (v_stack_m78));
loc_009428D7:
    result = v_stack_p18;
    if (!(condition_is_above_or_equal)) {
        result = *(uint64_t *)(v_stack_p8 + 0x28);
        Arg1 = 0;
        Arg1 = (Arg1) + ((uint32_t)((uint32_t)(result)));
    }
    Arg2 = (uint32_t)((0) + 1);
    if (((uint32_t)(Arg2)) < (*(uint32_t *)(v_stack_p8 + 0x8))) goto loc_009428D7;
loc_009428F9:
loc_0094290B:
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m74)))))) - ((uint32_t)((uint32_t)(v_stack_m68))));
loc_00942914:
    if (0 >= 4) goto loc_00942702;
    if (((uint32_t)(Arg4)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x92FBF4 + 0x0 * 4))))) goto loc_00942933;
    Arg1 = (uint32_t)((0) + 1);
    goto loc_00942914;
loc_00942933:
    Arg2 = 0;
    if (((uint32_t)((uint32_t)((uint32_t)(Arg4)))) >= 63) goto loc_009429F9;
loc_00942947:
    result = (uint32_t)((uint32_t)(Arg4));
    if (local_r12 != 0) {
        result = (uint8_t)(Arg1);
        result = (uint8_t)((result) << (6));
        result = (uint8_t)((result) | ((uint8_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg4)))))));
        *(uint8_t *)(local_r12) = (uint8_t)(result);
        local_r12 = (local_r12) + 1;
    }
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip - 0x92FBF4 + 0x0 * 4))) * ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg4)))))));
    local_r13 = (uint32_t)(((uint32_t)(v_stack_m6C)) + 1);
    v_stack_m6C = (uint32_t)(local_r13);
    local_rbp = (uint32_t)(((uint32_t)(v_stack_m68)) + ((uint32_t)(Arg3)));
    v_stack_m68 = (uint32_t)(local_rbp);
    if (((uint32_t)(local_rbp)) != ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m74)))))) goto loc_0094290B;
    if (((uint32_t)(Arg1)) == 3) goto loc_00942702;
    if (local_r12 != 0) {
        *(uint8_t *)(local_r12) = 192;
        local_r12 = (local_r12) + 1;
    }
    local_r13 = (uint32_t)((local_r13) + 1);
    goto loc_009426EF;
loc_009429AD:
loc_009429B3:
loc_009429BF:
    if (Arg5 == 0) {
        Arg1 = Arg6;
        Arg2 = (uint32_t)(local_r13);
        *(uint64_t *)(Arg1) = Arg2;
    }
    if (Arg7 != 0) {
        *(uint32_t *)(Arg7) = (uint32_t)((uint32_t)(v_stack_m78));
    }
    local_rsp = (local_rsp) + (136);
    return (uint32_t)((uint32_t)((uint32_t)(0xC000007BULL)));
loc_009429F9:
    goto loc_00942947;
loc_00942A04:
    *(uint32_t *)(v_rip + 0x4EAE1A) = 14;
    goto loc_0094281D;
loc_00942A13:
    goto loc_009427AD;
loc_00942A25:
    goto loc_009429BF;
loc_00942A2D:
    result = guard_dispatch_icall(v_stack_pD8, (uint32_t)(v_stack_m78) - 8, (uint32_t)(v_stack_m78) - 28, (uint32_t)(v_stack_p54));
    goto loc_0094281D;
loc_00942A45:
    if (((uint32_t)(Arg5)) >= ((uint32_t)((uint32_t)((uint32_t)(result))))) { Arg5 = (uint32_t)((uint32_t)((uint32_t)(result))); }
    goto loc_0094283F;
loc_00942A51:
    result = guard_dispatch_icall(v_stack_p10, v_stack_p78, (uint32_t)(v_stack_m78) - 28, (uint32_t)(v_stack_p54));
    goto loc_0094289F;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg6` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00942650&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
