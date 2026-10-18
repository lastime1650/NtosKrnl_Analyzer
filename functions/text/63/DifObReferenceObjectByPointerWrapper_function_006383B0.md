# DifObReferenceObjectByPointerWrapper

- RVA: `0x006383B0`–`0x0063853D` (길이 `397` bytes)
- VA: `0x00000001406383B0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D2BBC`
- 디코드: `113`개 명령, `397/397` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x006383F0` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00638416` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00638452` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00638478` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00638491` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x006384AB` → [ObReferenceObjectByPointerWithTag](../41/ObReferenceObjectByPointerWithTag_function_00419870.md) (function, `0x00419870`)
- `0x006384D7` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006384FD` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00638516` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00638426` → RVA `0x00F048B8` (`.data`; read)
- `0x0063843F` → RVA `0x00F04980` (`.data`; read)
- `0x0063844B` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006383B0  48 8B C4                        mov rax, rsp
006383B3  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
006383B7  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
006383BB  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
006383BF  48 89 48 08                     mov qword ptr [rax + 8], rcx
006383C3  55                              push rbp
006383C4  41 54                           push r12
006383C6  41 55                           push r13
006383C8  41 56                           push r14
006383CA  41 57                           push r15
006383CC  48 8B EC                        mov rbp, rsp
006383CF  48 83 EC 60                     sub rsp, 0x60
006383D3  0F 57 C0                        xorps xmm0, xmm0
006383D6  B9 C9 00 00 00                  mov ecx, 0xc9
006383DB  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
006383DF  45 8A F9                        mov r15b, r9b
006383E2  4D 8B E0                        mov r12, r8
006383E5  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
006383E9  44 8B EA                        mov r13d, edx
006383EC  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
006383F0  E8 3F D6 E5 FF                  call 0x140495a34
006383F5  48 8B F0                        mov rsi, rax
006383F8  48 85 C0                        test rax, rax
006383FB  0F 84 95 00 00 00               je 0x140638496
00638401  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00638404  A8 18                           test al, 0x18
00638406  74 0A                           je 0x140638412
00638408  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0063840C  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
00638410  EB 0D                           jmp 0x14063841f
00638412  A8 04                           test al, 4
00638414  74 09                           je 0x14063841f
00638416  E8 ED B7 E9 FF                  call 0x1404d3c08
0063841B  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0063841F  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
00638423  45 32 F6                        xor r14b, r14b
00638426  44 38 35 8B C4 8C 00            cmp byte ptr [rip + 0x8cc48b], r14b
0063842D  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00638431  44 89 6D E8                     mov dword ptr [rbp - 0x18], r13d
00638435  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
00638439  44 88 7D D8                     mov byte ptr [rbp - 0x28], r15b
0063843D  75 0C                           jne 0x14063844b
0063843F  F7 05 37 C5 8C 00 00 08 00 00   test dword ptr [rip + 0x8cc537], 0x800
00638449  74 13                           je 0x14063845e
0063844B  48 8D 0D 2E BA 8C 00            lea rcx, [rip + 0x8cba2e]
00638452  E8 C9 E1 BD FF                  call 0x140216620
00638457  44 8A F0                        mov r14b, al
0063845A  84 C0                           test al, al
0063845C  74 38                           je 0x140638496
0063845E  48 8D 7E 20                     lea rdi, [rsi + 0x20]
00638462  48 8B 1F                        mov rbx, qword ptr [rdi]
00638465  EB 19                           jmp 0x140638480
00638467  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063846B  48 85 C0                        test rax, rax
0063846E  74 0D                           je 0x14063847d
00638470  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00638474  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00638478  E8 53 26 08 00                  call 0x1406baad0
0063847D  48 8B 1B                        mov rbx, qword ptr [rbx]
00638480  48 3B DF                        cmp rbx, rdi
00638483  75 E2                           jne 0x140638467
00638485  45 84 F6                        test r14b, r14b
00638488  74 0C                           je 0x140638496
0063848A  48 8D 0D EF B9 8C 00            lea rcx, [rip + 0x8cb9ef]
00638491  E8 EA 19 D1 FF                  call 0x140349e80
00638496  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
0063849A  45 8A CF                        mov r9b, r15b
0063849D  4D 8B C4                        mov r8, r12
006384A0  C7 44 24 20 44 66 6C 74         mov dword ptr [rsp + 0x20], 0x746c6644
006384A8  41 8B D5                        mov edx, r13d
006384AB  E8 C0 13 DE FF                  call 0x140419870
006384B0  89 45 F8                        mov dword ptr [rbp - 8], eax
006384B3  48 85 F6                        test rsi, rsi
006384B6  74 63                           je 0x14063851b
006384B8  40 32 FF                        xor dil, dil
006384BB  40 38 3D F6 C3 8C 00            cmp byte ptr [rip + 0x8cc3f6], dil
006384C2  75 0C                           jne 0x1406384d0
006384C4  F7 05 B2 C4 8C 00 00 08 00 00   test dword ptr [rip + 0x8cc4b2], 0x800
006384CE  74 13                           je 0x1406384e3
006384D0  48 8D 0D A9 B9 8C 00            lea rcx, [rip + 0x8cb9a9]
006384D7  E8 44 E1 BD FF                  call 0x140216620
006384DC  40 8A F8                        mov dil, al
006384DF  84 C0                           test al, al
006384E1  74 38                           je 0x14063851b
006384E3  48 83 C6 30                     add rsi, 0x30
006384E7  48 8B 1E                        mov rbx, qword ptr [rsi]
006384EA  EB 19                           jmp 0x140638505
006384EC  48 8D 43 F0                     lea rax, [rbx - 0x10]
006384F0  48 85 C0                        test rax, rax
006384F3  74 0D                           je 0x140638502
006384F5  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006384F9  48 8D 4D D0                     lea rcx, [rbp - 0x30]
006384FD  E8 CE 25 08 00                  call 0x1406baad0
00638502  48 8B 1B                        mov rbx, qword ptr [rbx]
00638505  48 3B DE                        cmp rbx, rsi
00638508  75 E2                           jne 0x1406384ec
0063850A  40 84 FF                        test dil, dil
0063850D  74 0C                           je 0x14063851b
0063850F  48 8D 0D 6A B9 8C 00            lea rcx, [rip + 0x8cb96a]
00638516  E8 65 19 D1 FF                  call 0x140349e80
0063851B  8B 45 F8                        mov eax, dword ptr [rbp - 8]
0063851E  4C 8D 5C 24 60                  lea r11, [rsp + 0x60]
00638523  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00638527  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
0063852B  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
0063852F  49 8B E3                        mov rsp, r11
00638532  41 5F                           pop r15
00638534  41 5E                           pop r14
00638536  41 5D                           pop r13
00638538  41 5C                           pop r12
0063853A  5D                              pop rbp
0063853B  C3                              ret
0063853C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifObReferenceObjectByPointerWrapper(__int64 a1, int a2, __int64 a3, unsigned __int8 a4)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int8 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (96);
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    result = DifGetAPIThunkContextById(201, a2, a3, a4);
    if (result == 0) goto loc_00638496;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00638412;
    v_stack_m58 = v_stack_p0;
    goto loc_0063841F;
loc_00638412:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m40 = (unsigned int)((unsigned int)(a2));
    v_stack_m48 = a3;
    v_stack_m50 = a4;
    if ((*(unsigned __int8 *)(v_rip + 9225355)) != 0) goto loc_0063844B;
    if (((*(unsigned int *)(v_rip + 9225527)) & (0x800ULL)) == 0) goto loc_0063845E;
loc_0063844B:
    result = ExAcquireRundownProtection(v_rip + 9222702, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00638496;
loc_0063845E:
    goto loc_00638480;
loc_00638467:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00638480:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00638467;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9222639;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_stack_m68 = 0x746C6644ULL;
    result = ObReferenceObjectByPointerWithTag(v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    v_stack_m30 = (unsigned int)(result);
    if (result == 0) goto loc_0063851B;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9225206)) != 0) goto loc_006384D0;
    if (((*(unsigned int *)(v_rip + 9225394)) & (0x800ULL)) == 0) goto loc_006384E3;
loc_006384D0:
    result = ExAcquireRundownProtection(v_rip + 9222569, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063851B;
loc_006384E3:
    v_rsi = (result) + (48);
    goto loc_00638505;
loc_006384EC:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
loc_00638505:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_006384EC;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9222506;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
    return (unsigned int)(v_stack_m30);
}
```

## 5. (Beta) C Style

```c
int64_t DifObReferenceObjectByPointerWrapper(int64_t Arg1, int32_t Arg2, int64_t Arg3, uint8_t Arg4)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint32_t v_stack_m40;
    uint64_t v_stack_m48;
    uint8_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m68;
    uint64_t v_stack_p0;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (96);
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    result = DifGetAPIThunkContextById(201, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_00638496;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00638412;
    v_stack_m58 = v_stack_p0;
    goto loc_0063841F;
loc_00638412:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m40 = (uint32_t)((uint32_t)(Arg2));
    v_stack_m48 = Arg3;
    v_stack_m50 = Arg4;
    if ((*(uint8_t *)(v_rip + 0x8CC48B)) != 0) goto loc_0063844B;
    if (((*(uint32_t *)(v_rip + 0x8CC537)) & (0x800ULL)) == 0) goto loc_0063845E;
loc_0063844B:
    result = ExAcquireRundownProtection(v_rip + 9222702, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00638496;
loc_0063845E:
    goto loc_00638480;
loc_00638467:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_00638480:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00638467;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9222639;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m68 = 0x746C6644ULL;
    result = ObReferenceObjectByPointerWithTag(v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    v_stack_m30 = (uint32_t)(result);
    if (result == 0) goto loc_0063851B;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8CC3F6)) != 0) goto loc_006384D0;
    if (((*(uint32_t *)(v_rip + 0x8CC4B2)) & (0x800ULL)) == 0) goto loc_006384E3;
loc_006384D0:
    result = ExAcquireRundownProtection(v_rip + 9222569, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0063851B;
loc_006384E3:
    local_rsi = (result) + (48);
    goto loc_00638505;
loc_006384EC:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    }
loc_00638505:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_006384EC;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9222506;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    }
    return (uint32_t)(v_stack_m30);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006383B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006383B0[BB_006383B0]
  bb_00638401[BB_00638401]
  bb_00638408[BB_00638408]
  bb_00638412[BB_00638412]
  bb_00638416[BB_00638416]
  bb_0063841F[BB_0063841F]
  bb_0063843F[BB_0063843F]
  bb_0063844B[BB_0063844B]
  bb_0063845E[BB_0063845E]
  bb_00638467[BB_00638467]
  bb_00638470[BB_00638470]
  bb_0063847D[BB_0063847D]
  bb_00638480[BB_00638480]
  bb_00638485[BB_00638485]
  bb_0063848A[BB_0063848A]
  bb_00638496[BB_00638496]
  bb_006384B8[BB_006384B8]
  bb_006384C4[BB_006384C4]
  bb_006384D0[BB_006384D0]
  bb_006384E3[BB_006384E3]
  bb_006384EC[BB_006384EC]
  bb_006384F5[BB_006384F5]
  bb_00638502[BB_00638502]
  bb_00638505[BB_00638505]
  bb_0063850A[BB_0063850A]
  bb_0063850F[BB_0063850F]
  bb_0063851B[BB_0063851B]
  bb_0063853C[BB_0063853C]
  bb_006383B0 -->|branch| bb_00638496
  bb_006383B0 -->|fallthrough| bb_00638401
  bb_00638401 -->|branch| bb_00638412
  bb_00638401 -->|fallthrough| bb_00638408
  bb_00638408 -->|branch| bb_0063841F
  bb_00638412 -->|branch| bb_0063841F
  bb_00638412 -->|fallthrough| bb_00638416
  bb_00638416 -->|flow| bb_0063841F
  bb_0063841F -->|branch| bb_0063844B
  bb_0063841F -->|fallthrough| bb_0063843F
  bb_0063843F -->|branch| bb_0063845E
  bb_0063843F -->|fallthrough| bb_0063844B
  bb_0063844B -->|branch| bb_00638496
  bb_0063844B -->|fallthrough| bb_0063845E
  bb_0063845E -->|branch| bb_00638480
  bb_00638467 -->|branch| bb_0063847D
  bb_00638467 -->|fallthrough| bb_00638470
  bb_00638470 -->|flow| bb_0063847D
  bb_0063847D -->|flow| bb_00638480
  bb_00638480 -->|branch| bb_00638467
  bb_00638480 -->|fallthrough| bb_00638485
  bb_00638485 -->|branch| bb_00638496
  bb_00638485 -->|fallthrough| bb_0063848A
  bb_0063848A -->|flow| bb_00638496
  bb_00638496 -->|branch| bb_0063851B
  bb_00638496 -->|fallthrough| bb_006384B8
  bb_006384B8 -->|branch| bb_006384D0
  bb_006384B8 -->|fallthrough| bb_006384C4
  bb_006384C4 -->|branch| bb_006384E3
  bb_006384C4 -->|fallthrough| bb_006384D0
  bb_006384D0 -->|branch| bb_0063851B
  bb_006384D0 -->|fallthrough| bb_006384E3
  bb_006384E3 -->|branch| bb_00638505
  bb_006384EC -->|branch| bb_00638502
  bb_006384EC -->|fallthrough| bb_006384F5
  bb_006384F5 -->|flow| bb_00638502
  bb_00638502 -->|flow| bb_00638505
  bb_00638505 -->|branch| bb_006384EC
  bb_00638505 -->|fallthrough| bb_0063850A
  bb_0063850A -->|branch| bb_0063851B
  bb_0063850A -->|fallthrough| bb_0063850F
  bb_0063850F -->|flow| bb_0063851B
```
