# DifZwRemoveIoCompletionExWrapper

- RVA: `0x00648F90`–`0x00649135` (길이 `421` bytes)
- VA: `0x0000000140648F90`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BD780`
- 디코드: `120`개 명령, `421/421` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **10**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00648FC6` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00648FD0` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00648FF8` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00649042` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00649068` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00649081` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x006490A3` → [ZwRemoveIoCompletionEx](../6B/ZwRemoveIoCompletionEx_function_006B00D0.md) (function, `0x006B00D0`)
- `0x006490CF` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006490F5` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0064910E` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00649008` → RVA `0x00F048B8` (`.data`; read)
- `0x0064902F` → RVA `0x00F04980` (`.data`; read)
- `0x0064903B` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00648F90  48 8B C4                        mov rax, rsp
00648F93  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00648F97  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00648F9B  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00648F9F  48 89 48 08                     mov qword ptr [rax + 8], rcx
00648FA3  55                              push rbp
00648FA4  41 54                           push r12
00648FA6  41 55                           push r13
00648FA8  41 56                           push r14
00648FAA  41 57                           push r15
00648FAC  48 8B EC                        mov rbp, rsp
00648FAF  48 83 EC 70                     sub rsp, 0x70
00648FB3  4C 8B EA                        mov r13, rdx
00648FB6  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00648FBA  33 D2                           xor edx, edx
00648FBC  45 8B E0                        mov r12d, r8d
00648FBF  4D 8B F9                        mov r15, r9
00648FC2  44 8D 42 40                     lea r8d, [rdx + 0x40]
00648FC6  E8 75 DC 07 00                  call 0x1406c6c40
00648FCB  B9 1F 00 00 00                  mov ecx, 0x1f
00648FD0  E8 5F CA E4 FF                  call 0x140495a34
00648FD5  4C 8B F0                        mov r14, rax
00648FD8  48 85 C0                        test rax, rax
00648FDB  0F 84 A5 00 00 00               je 0x140649086
00648FE1  8B 48 0C                        mov ecx, dword ptr [rax + 0xc]
00648FE4  F6 C1 18                        test cl, 0x18
00648FE7  74 0A                           je 0x140648ff3
00648FE9  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
00648FED  48 89 4D C0                     mov qword ptr [rbp - 0x40], rcx
00648FF1  EB 0E                           jmp 0x140649001
00648FF3  F6 C1 04                        test cl, 4
00648FF6  74 09                           je 0x140649001
00648FF8  E8 0B AC E8 FF                  call 0x1404d3c08
00648FFD  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00649001  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
00649005  40 32 F6                        xor sil, sil
00649008  40 38 35 A9 B8 8B 00            cmp byte ptr [rip + 0x8bb8a9], sil
0064900F  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00649013  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
00649017  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0064901B  8A 45 58                        mov al, byte ptr [rbp + 0x58]
0064901E  88 45 C8                        mov byte ptr [rbp - 0x38], al
00649021  4C 89 6D E8                     mov qword ptr [rbp - 0x18], r13
00649025  44 89 65 E0                     mov dword ptr [rbp - 0x20], r12d
00649029  4C 89 7D D8                     mov qword ptr [rbp - 0x28], r15
0064902D  75 0C                           jne 0x14064903b
0064902F  F7 05 47 B9 8B 00 00 08 00 00   test dword ptr [rip + 0x8bb947], 0x800
00649039  74 13                           je 0x14064904e
0064903B  48 8D 0D 3E AE 8B 00            lea rcx, [rip + 0x8bae3e]
00649042  E8 D9 D5 BC FF                  call 0x140216620
00649047  40 8A F0                        mov sil, al
0064904A  84 C0                           test al, al
0064904C  74 38                           je 0x140649086
0064904E  49 8D 7E 20                     lea rdi, [r14 + 0x20]
00649052  48 8B 1F                        mov rbx, qword ptr [rdi]
00649055  EB 19                           jmp 0x140649070
00649057  48 8D 43 F0                     lea rax, [rbx - 0x10]
0064905B  48 85 C0                        test rax, rax
0064905E  74 0D                           je 0x14064906d
00649060  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00649064  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00649068  E8 63 1A 07 00                  call 0x1406baad0
0064906D  48 8B 1B                        mov rbx, qword ptr [rbx]
00649070  48 3B DF                        cmp rbx, rdi
00649073  75 E2                           jne 0x140649057
00649075  40 84 F6                        test sil, sil
00649078  74 0C                           je 0x140649086
0064907A  48 8D 0D FF AD 8B 00            lea rcx, [rip + 0x8badff]
00649081  E8 FA 0D D0 FF                  call 0x140349e80
00649086  8A 45 58                        mov al, byte ptr [rbp + 0x58]
00649089  4D 8B CF                        mov r9, r15
0064908C  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
00649090  45 8B C4                        mov r8d, r12d
00649093  88 44 24 28                     mov byte ptr [rsp + 0x28], al
00649097  49 8B D5                        mov rdx, r13
0064909A  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
0064909E  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
006490A3  E8 28 70 06 00                  call 0x1406b00d0
006490A8  89 45 F8                        mov dword ptr [rbp - 8], eax
006490AB  4D 85 F6                        test r14, r14
006490AE  74 63                           je 0x140649113
006490B0  40 32 FF                        xor dil, dil
006490B3  40 38 3D FE B7 8B 00            cmp byte ptr [rip + 0x8bb7fe], dil
006490BA  75 0C                           jne 0x1406490c8
006490BC  F7 05 BA B8 8B 00 00 08 00 00   test dword ptr [rip + 0x8bb8ba], 0x800
006490C6  74 13                           je 0x1406490db
006490C8  48 8D 0D B1 AD 8B 00            lea rcx, [rip + 0x8badb1]
006490CF  E8 4C D5 BC FF                  call 0x140216620
006490D4  40 8A F8                        mov dil, al
006490D7  84 C0                           test al, al
006490D9  74 38                           je 0x140649113
006490DB  49 8D 76 30                     lea rsi, [r14 + 0x30]
006490DF  48 8B 1E                        mov rbx, qword ptr [rsi]
006490E2  EB 19                           jmp 0x1406490fd
006490E4  48 8D 43 F0                     lea rax, [rbx - 0x10]
006490E8  48 85 C0                        test rax, rax
006490EB  74 0D                           je 0x1406490fa
006490ED  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006490F1  48 8D 4D C0                     lea rcx, [rbp - 0x40]
006490F5  E8 D6 19 07 00                  call 0x1406baad0
006490FA  48 8B 1B                        mov rbx, qword ptr [rbx]
006490FD  48 3B DE                        cmp rbx, rsi
00649100  75 E2                           jne 0x1406490e4
00649102  40 84 FF                        test dil, dil
00649105  74 0C                           je 0x140649113
00649107  48 8D 0D 72 AD 8B 00            lea rcx, [rip + 0x8bad72]
0064910E  E8 6D 0D D0 FF                  call 0x140349e80
00649113  8B 45 F8                        mov eax, dword ptr [rbp - 8]
00649116  4C 8D 5C 24 70                  lea r11, [rsp + 0x70]
0064911B  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
0064911F  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00649123  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00649127  49 8B E3                        mov rsp, r11
0064912A  41 5F                           pop r15
0064912C  41 5E                           pop r14
0064912E  41 5D                           pop r13
00649130  41 5C                           pop r12
00649132  5D                              pop rbp
00649133  C3                              ret
00649134  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwRemoveIoCompletionExWrapper(__int64 a1, __int64 a2, int a3, __int64 a4, __int64 a5, unsigned __int8 a6)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned int v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int8 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int8 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (112);
    a2 = 0;
    result = memset(v_stack_m68, a2, a2 + 64, a4);
    result = DifGetAPIThunkContextById(31, a2, a2 + 64, a4);
    if (result == 0) goto loc_00649086;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00648FF3;
    v_stack_m68 = v_stack_p0;
    goto loc_00649001;
loc_00648FF3:
    if ((((unsigned __int8)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a2 + 64, a4);
        v_stack_m68 = result;
    }
    v_rsi = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m58 = a5;
    v_stack_m60 = a6;
    v_stack_m40 = 0;
    v_stack_m48 = (unsigned int)((unsigned int)(a3));
    v_stack_m50 = a4;
    if ((*(unsigned __int8 *)(v_rip + 9156777)) != 0) goto loc_0064903B;
    if (((*(unsigned int *)(v_rip + 9156935)) & (0x800ULL)) == 0) goto loc_0064904E;
loc_0064903B:
    result = ExAcquireRundownProtection(v_rip + 9154110, a2, a2 + 64, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00649086;
loc_0064904E:
    goto loc_00649070;
loc_00649057:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, a2, a2 + 64, a4);
    }
loc_00649070:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00649057;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9154047;
        result = ExReleaseRundownProtection(a1, a2, a2 + 64, a4);
    }
    v_stack_m70 = a6;
    v_stack_m78 = a5;
    result = ZwRemoveIoCompletionEx(v_stack_p8, 0, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    v_stack_m30 = (unsigned int)(result);
    if (result == 0) goto loc_00649113;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9156606)) != 0) goto loc_006490C8;
    if (((*(unsigned int *)(v_rip + 9156794)) & (0x800ULL)) == 0) goto loc_006490DB;
loc_006490C8:
    result = ExAcquireRundownProtection(v_rip + 9153969, 0, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00649113;
loc_006490DB:
    goto loc_006490FD;
loc_006490E4:
    result = *(unsigned __int64 *)(result + 48) - 16;
    if (*(unsigned __int64 *)(result + 48) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 48) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, 0, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    }
loc_006490FD:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 48))) != (result + 48)) goto loc_006490E4;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9153906;
        result = ExReleaseRundownProtection(a1, 0, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    }
    return (unsigned int)(v_stack_m30);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwRemoveIoCompletionExWrapper(int64_t Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4, int64_t Arg5, uint8_t Arg6)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint32_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint8_t v_stack_m60;
    uint64_t v_stack_m68;
    uint8_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_p0;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (112);
    Arg2 = 0;
    result = memset(v_stack_m68, Arg2, Arg2 + 64, Arg4);
    result = DifGetAPIThunkContextById(31, Arg2, Arg2 + 64, Arg4);
    if (result == 0) goto loc_00649086;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00648FF3;
    v_stack_m68 = v_stack_p0;
    goto loc_00649001;
loc_00648FF3:
    if ((((uint8_t)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg2 + 64, Arg4);
        v_stack_m68 = result;
    }
    local_rsi = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m58 = Arg5;
    v_stack_m60 = Arg6;
    v_stack_m40 = 0;
    v_stack_m48 = (uint32_t)((uint32_t)(Arg3));
    v_stack_m50 = Arg4;
    if ((*(uint8_t *)(v_rip + 0x8BB8A9)) != 0) goto loc_0064903B;
    if (((*(uint32_t *)(v_rip + 0x8BB947)) & (0x800ULL)) == 0) goto loc_0064904E;
loc_0064903B:
    result = ExAcquireRundownProtection(v_rip + 9154110, Arg2, Arg2 + 64, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00649086;
loc_0064904E:
    goto loc_00649070;
loc_00649057:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, Arg2, Arg2 + 64, Arg4);
    }
loc_00649070:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00649057;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9154047;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg2 + 64, Arg4);
    }
    v_stack_m70 = Arg6;
    v_stack_m78 = Arg5;
    result = ZwRemoveIoCompletionEx(v_stack_p8, 0, (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    v_stack_m30 = (uint32_t)(result);
    if (result == 0) goto loc_00649113;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8BB7FE)) != 0) goto loc_006490C8;
    if (((*(uint32_t *)(v_rip + 0x8BB8BA)) & (0x800ULL)) == 0) goto loc_006490DB;
loc_006490C8:
    result = ExAcquireRundownProtection(v_rip + 9153969, 0, (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    if ((uint8_t)(result) == 0) goto loc_00649113;
loc_006490DB:
    goto loc_006490FD;
loc_006490E4:
    result = *(uint64_t *)(result + 0x30) - 16;
    if (*(uint64_t *)(result + 0x30) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x30) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, 0, (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    }
loc_006490FD:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x30))) != (result + 48)) goto loc_006490E4;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9153906;
        result = ExReleaseRundownProtection(Arg1, 0, (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    }
    return (uint32_t)(v_stack_m30);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00648F90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00648F90[BB_00648F90]
  bb_00648FE1[BB_00648FE1]
  bb_00648FE9[BB_00648FE9]
  bb_00648FF3[BB_00648FF3]
  bb_00648FF8[BB_00648FF8]
  bb_00649001[BB_00649001]
  bb_0064902F[BB_0064902F]
  bb_0064903B[BB_0064903B]
  bb_0064904E[BB_0064904E]
  bb_00649057[BB_00649057]
  bb_00649060[BB_00649060]
  bb_0064906D[BB_0064906D]
  bb_00649070[BB_00649070]
  bb_00649075[BB_00649075]
  bb_0064907A[BB_0064907A]
  bb_00649086[BB_00649086]
  bb_006490B0[BB_006490B0]
  bb_006490BC[BB_006490BC]
  bb_006490C8[BB_006490C8]
  bb_006490DB[BB_006490DB]
  bb_006490E4[BB_006490E4]
  bb_006490ED[BB_006490ED]
  bb_006490FA[BB_006490FA]
  bb_006490FD[BB_006490FD]
  bb_00649102[BB_00649102]
  bb_00649107[BB_00649107]
  bb_00649113[BB_00649113]
  bb_00649134[BB_00649134]
  bb_00648F90 -->|branch| bb_00649086
  bb_00648F90 -->|fallthrough| bb_00648FE1
  bb_00648FE1 -->|branch| bb_00648FF3
  bb_00648FE1 -->|fallthrough| bb_00648FE9
  bb_00648FE9 -->|branch| bb_00649001
  bb_00648FF3 -->|branch| bb_00649001
  bb_00648FF3 -->|fallthrough| bb_00648FF8
  bb_00648FF8 -->|flow| bb_00649001
  bb_00649001 -->|branch| bb_0064903B
  bb_00649001 -->|fallthrough| bb_0064902F
  bb_0064902F -->|branch| bb_0064904E
  bb_0064902F -->|fallthrough| bb_0064903B
  bb_0064903B -->|branch| bb_00649086
  bb_0064903B -->|fallthrough| bb_0064904E
  bb_0064904E -->|branch| bb_00649070
  bb_00649057 -->|branch| bb_0064906D
  bb_00649057 -->|fallthrough| bb_00649060
  bb_00649060 -->|flow| bb_0064906D
  bb_0064906D -->|flow| bb_00649070
  bb_00649070 -->|branch| bb_00649057
  bb_00649070 -->|fallthrough| bb_00649075
  bb_00649075 -->|branch| bb_00649086
  bb_00649075 -->|fallthrough| bb_0064907A
  bb_0064907A -->|flow| bb_00649086
  bb_00649086 -->|branch| bb_00649113
  bb_00649086 -->|fallthrough| bb_006490B0
  bb_006490B0 -->|branch| bb_006490C8
  bb_006490B0 -->|fallthrough| bb_006490BC
  bb_006490BC -->|branch| bb_006490DB
  bb_006490BC -->|fallthrough| bb_006490C8
  bb_006490C8 -->|branch| bb_00649113
  bb_006490C8 -->|fallthrough| bb_006490DB
  bb_006490DB -->|branch| bb_006490FD
  bb_006490E4 -->|branch| bb_006490FA
  bb_006490E4 -->|fallthrough| bb_006490ED
  bb_006490ED -->|flow| bb_006490FA
  bb_006490FA -->|flow| bb_006490FD
  bb_006490FD -->|branch| bb_006490E4
  bb_006490FD -->|fallthrough| bb_00649102
  bb_00649102 -->|branch| bb_00649113
  bb_00649102 -->|fallthrough| bb_00649107
  bb_00649107 -->|flow| bb_00649113
```
