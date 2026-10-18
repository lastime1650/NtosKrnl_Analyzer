# DifZwCreateDirectoryObjectWrapper

- RVA: `0x0063F450`–`0x0063F5C5` (길이 `373` bytes)
- VA: `0x000000014063F450`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A9A64`
- 디코드: `108`개 명령, `373/373` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0063F48C` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0063F4B2` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0063F4E6` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063F50C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063F525` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0063F533` → [ZwCreateDirectoryObject](../6A/ZwCreateDirectoryObject_function_006AE650.md) (function, `0x006AE650`)
- `0x0063F55F` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063F585` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063F59E` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0063F4C2` → RVA `0x00F048B8` (`.data`; read)
- `0x0063F4D3` → RVA `0x00F04980` (`.data`; read)
- `0x0063F4DF` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0063F450  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0063F455  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
0063F45A  48 89 7C 24 18                  mov qword ptr [rsp + 0x18], rdi
0063F45F  55                              push rbp
0063F460  41 54                           push r12
0063F462  41 55                           push r13
0063F464  41 56                           push r14
0063F466  41 57                           push r15
0063F468  48 8B EC                        mov rbp, rsp
0063F46B  48 83 EC 50                     sub rsp, 0x50
0063F46F  33 C0                           xor eax, eax
0063F471  0F 57 C0                        xorps xmm0, xmm0
0063F474  4C 8B E9                        mov r13, rcx
0063F477  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0063F47B  4D 8B F8                        mov r15, r8
0063F47E  44 8B E2                        mov r12d, edx
0063F481  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0063F485  8D 48 7F                        lea ecx, [rax + 0x7f]
0063F488  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
0063F48C  E8 A3 65 E5 FF                  call 0x140495a34
0063F491  48 8B F0                        mov rsi, rax
0063F494  48 85 C0                        test rax, rax
0063F497  0F 84 8D 00 00 00               je 0x14063f52a
0063F49D  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0063F4A0  A8 18                           test al, 0x18
0063F4A2  74 0A                           je 0x14063f4ae
0063F4A4  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0063F4A8  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
0063F4AC  EB 0D                           jmp 0x14063f4bb
0063F4AE  A8 04                           test al, 4
0063F4B0  74 09                           je 0x14063f4bb
0063F4B2  E8 51 47 E9 FF                  call 0x1404d3c08
0063F4B7  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0063F4BB  45 32 F6                        xor r14b, r14b
0063F4BE  4C 89 6D E8                     mov qword ptr [rbp - 0x18], r13
0063F4C2  44 38 35 EF 53 8C 00            cmp byte ptr [rip + 0x8c53ef], r14b
0063F4C9  44 89 65 E0                     mov dword ptr [rbp - 0x20], r12d
0063F4CD  4C 89 7D D8                     mov qword ptr [rbp - 0x28], r15
0063F4D1  75 0C                           jne 0x14063f4df
0063F4D3  F7 05 A3 54 8C 00 00 08 00 00   test dword ptr [rip + 0x8c54a3], 0x800
0063F4DD  74 13                           je 0x14063f4f2
0063F4DF  48 8D 0D 9A 49 8C 00            lea rcx, [rip + 0x8c499a]
0063F4E6  E8 35 71 BD FF                  call 0x140216620
0063F4EB  44 8A F0                        mov r14b, al
0063F4EE  84 C0                           test al, al
0063F4F0  74 38                           je 0x14063f52a
0063F4F2  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0063F4F6  48 8B 1F                        mov rbx, qword ptr [rdi]
0063F4F9  EB 19                           jmp 0x14063f514
0063F4FB  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063F4FF  48 85 C0                        test rax, rax
0063F502  74 0D                           je 0x14063f511
0063F504  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063F508  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0063F50C  E8 BF B5 07 00                  call 0x1406baad0
0063F511  48 8B 1B                        mov rbx, qword ptr [rbx]
0063F514  48 3B DF                        cmp rbx, rdi
0063F517  75 E2                           jne 0x14063f4fb
0063F519  45 84 F6                        test r14b, r14b
0063F51C  74 0C                           je 0x14063f52a
0063F51E  48 8D 0D 5B 49 8C 00            lea rcx, [rip + 0x8c495b]
0063F525  E8 56 A9 D0 FF                  call 0x140349e80
0063F52A  4D 8B C7                        mov r8, r15
0063F52D  41 8B D4                        mov edx, r12d
0063F530  49 8B CD                        mov rcx, r13
0063F533  E8 18 F1 06 00                  call 0x1406ae650
0063F538  89 45 F0                        mov dword ptr [rbp - 0x10], eax
0063F53B  48 85 F6                        test rsi, rsi
0063F53E  74 63                           je 0x14063f5a3
0063F540  40 32 FF                        xor dil, dil
0063F543  40 38 3D 6E 53 8C 00            cmp byte ptr [rip + 0x8c536e], dil
0063F54A  75 0C                           jne 0x14063f558
0063F54C  F7 05 2A 54 8C 00 00 08 00 00   test dword ptr [rip + 0x8c542a], 0x800
0063F556  74 13                           je 0x14063f56b
0063F558  48 8D 0D 21 49 8C 00            lea rcx, [rip + 0x8c4921]
0063F55F  E8 BC 70 BD FF                  call 0x140216620
0063F564  40 8A F8                        mov dil, al
0063F567  84 C0                           test al, al
0063F569  74 38                           je 0x14063f5a3
0063F56B  48 83 C6 30                     add rsi, 0x30
0063F56F  48 8B 1E                        mov rbx, qword ptr [rsi]
0063F572  EB 19                           jmp 0x14063f58d
0063F574  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063F578  48 85 C0                        test rax, rax
0063F57B  74 0D                           je 0x14063f58a
0063F57D  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063F581  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0063F585  E8 46 B5 07 00                  call 0x1406baad0
0063F58A  48 8B 1B                        mov rbx, qword ptr [rbx]
0063F58D  48 3B DE                        cmp rbx, rsi
0063F590  75 E2                           jne 0x14063f574
0063F592  40 84 FF                        test dil, dil
0063F595  74 0C                           je 0x14063f5a3
0063F597  48 8D 0D E2 48 8C 00            lea rcx, [rip + 0x8c48e2]
0063F59E  E8 DD A8 D0 FF                  call 0x140349e80
0063F5A3  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
0063F5A6  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
0063F5AB  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
0063F5AF  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
0063F5B3  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
0063F5B7  49 8B E3                        mov rsp, r11
0063F5BA  41 5F                           pop r15
0063F5BC  41 5E                           pop r14
0063F5BE  41 5D                           pop r13
0063F5C0  41 5C                           pop r12
0063F5C2  5D                              pop rbp
0063F5C3  C3                              ret
0063F5C4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwCreateDirectoryObjectWrapper(__int64 a1, int a2, __int64 a3)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_stack_p18 = v_rdi;
    v_rsp = (v_rsp) - (80);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(result + 127, a2, a3, a4);
    if (result == 0) goto loc_0063F52A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0063F4AE;
    v_stack_m58 = v_stack_p0;
    goto loc_0063F4BB;
loc_0063F4AE:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m40 = a1;
    v_stack_m48 = (unsigned int)((unsigned int)(a2));
    v_stack_m50 = a3;
    if ((*(unsigned __int8 *)(v_rip + 9196527)) != 0) goto loc_0063F4DF;
    if (((*(unsigned int *)(v_rip + 9196707)) & (0x800ULL)) == 0) goto loc_0063F4F2;
loc_0063F4DF:
    result = ExAcquireRundownProtection(v_rip + 9193882, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063F52A;
loc_0063F4F2:
    goto loc_0063F514;
loc_0063F4FB:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063F514:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0063F4FB;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9193819;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ZwCreateDirectoryObject(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    v_stack_m38 = (unsigned int)(result);
    if (result == 0) goto loc_0063F5A3;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9196398)) != 0) goto loc_0063F558;
    if (((*(unsigned int *)(v_rip + 9196586)) & (0x800ULL)) == 0) goto loc_0063F56B;
loc_0063F558:
    result = ExAcquireRundownProtection(v_rip + 9193761, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063F5A3;
loc_0063F56B:
    v_rsi = (result) + (48);
    goto loc_0063F58D;
loc_0063F574:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
loc_0063F58D:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0063F574;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9193698;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
    return (unsigned int)(v_stack_m38);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwCreateDirectoryObjectWrapper(int64_t Arg1, int32_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    v_stack_p18 = local_rdi;
    local_rsp = (local_rsp) - (80);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(result + 127, Arg2, Arg3, a4);
    if (result == 0) goto loc_0063F52A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0063F4AE;
    v_stack_m58 = v_stack_p0;
    goto loc_0063F4BB;
loc_0063F4AE:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, a4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m40 = Arg1;
    v_stack_m48 = (uint32_t)((uint32_t)(Arg2));
    v_stack_m50 = Arg3;
    if ((*(uint8_t *)(v_rip + 0x8C53EF)) != 0) goto loc_0063F4DF;
    if (((*(uint32_t *)(v_rip + 0x8C54A3)) & (0x800ULL)) == 0) goto loc_0063F4F2;
loc_0063F4DF:
    result = ExAcquireRundownProtection(v_rip + 9193882, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0063F52A;
loc_0063F4F2:
    goto loc_0063F514;
loc_0063F4FB:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_0063F514:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0063F4FB;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9193819;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    result = ZwCreateDirectoryObject(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    v_stack_m38 = (uint32_t)(result);
    if (result == 0) goto loc_0063F5A3;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8C536E)) != 0) goto loc_0063F558;
    if (((*(uint32_t *)(v_rip + 0x8C542A)) & (0x800ULL)) == 0) goto loc_0063F56B;
loc_0063F558:
    result = ExAcquireRundownProtection(v_rip + 9193761, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0063F5A3;
loc_0063F56B:
    local_rsi = (result) + (48);
    goto loc_0063F58D;
loc_0063F574:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    }
loc_0063F58D:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0063F574;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9193698;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    }
    return (uint32_t)(v_stack_m38);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0063F450&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0063F450[BB_0063F450]
  bb_0063F49D[BB_0063F49D]
  bb_0063F4A4[BB_0063F4A4]
  bb_0063F4AE[BB_0063F4AE]
  bb_0063F4B2[BB_0063F4B2]
  bb_0063F4BB[BB_0063F4BB]
  bb_0063F4D3[BB_0063F4D3]
  bb_0063F4DF[BB_0063F4DF]
  bb_0063F4F2[BB_0063F4F2]
  bb_0063F4FB[BB_0063F4FB]
  bb_0063F504[BB_0063F504]
  bb_0063F511[BB_0063F511]
  bb_0063F514[BB_0063F514]
  bb_0063F519[BB_0063F519]
  bb_0063F51E[BB_0063F51E]
  bb_0063F52A[BB_0063F52A]
  bb_0063F540[BB_0063F540]
  bb_0063F54C[BB_0063F54C]
  bb_0063F558[BB_0063F558]
  bb_0063F56B[BB_0063F56B]
  bb_0063F574[BB_0063F574]
  bb_0063F57D[BB_0063F57D]
  bb_0063F58A[BB_0063F58A]
  bb_0063F58D[BB_0063F58D]
  bb_0063F592[BB_0063F592]
  bb_0063F597[BB_0063F597]
  bb_0063F5A3[BB_0063F5A3]
  bb_0063F5C4[BB_0063F5C4]
  bb_0063F450 -->|branch| bb_0063F52A
  bb_0063F450 -->|fallthrough| bb_0063F49D
  bb_0063F49D -->|branch| bb_0063F4AE
  bb_0063F49D -->|fallthrough| bb_0063F4A4
  bb_0063F4A4 -->|branch| bb_0063F4BB
  bb_0063F4AE -->|branch| bb_0063F4BB
  bb_0063F4AE -->|fallthrough| bb_0063F4B2
  bb_0063F4B2 -->|flow| bb_0063F4BB
  bb_0063F4BB -->|branch| bb_0063F4DF
  bb_0063F4BB -->|fallthrough| bb_0063F4D3
  bb_0063F4D3 -->|branch| bb_0063F4F2
  bb_0063F4D3 -->|fallthrough| bb_0063F4DF
  bb_0063F4DF -->|branch| bb_0063F52A
  bb_0063F4DF -->|fallthrough| bb_0063F4F2
  bb_0063F4F2 -->|branch| bb_0063F514
  bb_0063F4FB -->|branch| bb_0063F511
  bb_0063F4FB -->|fallthrough| bb_0063F504
  bb_0063F504 -->|flow| bb_0063F511
  bb_0063F511 -->|flow| bb_0063F514
  bb_0063F514 -->|branch| bb_0063F4FB
  bb_0063F514 -->|fallthrough| bb_0063F519
  bb_0063F519 -->|branch| bb_0063F52A
  bb_0063F519 -->|fallthrough| bb_0063F51E
  bb_0063F51E -->|flow| bb_0063F52A
  bb_0063F52A -->|branch| bb_0063F5A3
  bb_0063F52A -->|fallthrough| bb_0063F540
  bb_0063F540 -->|branch| bb_0063F558
  bb_0063F540 -->|fallthrough| bb_0063F54C
  bb_0063F54C -->|branch| bb_0063F56B
  bb_0063F54C -->|fallthrough| bb_0063F558
  bb_0063F558 -->|branch| bb_0063F5A3
  bb_0063F558 -->|fallthrough| bb_0063F56B
  bb_0063F56B -->|branch| bb_0063F58D
  bb_0063F574 -->|branch| bb_0063F58A
  bb_0063F574 -->|fallthrough| bb_0063F57D
  bb_0063F57D -->|flow| bb_0063F58A
  bb_0063F58A -->|flow| bb_0063F58D
  bb_0063F58D -->|branch| bb_0063F574
  bb_0063F58D -->|fallthrough| bb_0063F592
  bb_0063F592 -->|branch| bb_0063F5A3
  bb_0063F592 -->|fallthrough| bb_0063F597
  bb_0063F597 -->|flow| bb_0063F5A3
```
