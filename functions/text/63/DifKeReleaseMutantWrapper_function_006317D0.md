# DifKeReleaseMutantWrapper

- RVA: `0x006317D0`–`0x00631951` (길이 `385` bytes)
- VA: `0x00000001406317D0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D2CBC`
- 디코드: `111`개 명령, `385/385` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0063180C` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00631832` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0063186E` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00631894` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006318AD` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x006318BF` → [KeReleaseMutant](../39/KeReleaseMutant_function_003967D0.md) (function, `0x003967D0`)
- `0x006318EB` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00631911` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063192A` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00631842` → RVA `0x00F048B8` (`.data`; read)
- `0x0063185B` → RVA `0x00F04980` (`.data`; read)
- `0x00631867` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006317D0  48 8B C4                        mov rax, rsp
006317D3  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
006317D7  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
006317DB  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
006317DF  48 89 48 08                     mov qword ptr [rax + 8], rcx
006317E3  55                              push rbp
006317E4  41 54                           push r12
006317E6  41 55                           push r13
006317E8  41 56                           push r14
006317EA  41 57                           push r15
006317EC  48 8B EC                        mov rbp, rsp
006317EF  48 83 EC 40                     sub rsp, 0x40
006317F3  0F 57 C0                        xorps xmm0, xmm0
006317F6  B9 05 01 00 00                  mov ecx, 0x105
006317FB  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
006317FF  45 8A F9                        mov r15b, r9b
00631802  45 8A E0                        mov r12b, r8b
00631805  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
00631809  44 8B EA                        mov r13d, edx
0063180C  E8 23 42 E6 FF                  call 0x140495a34
00631811  48 8B F0                        mov rsi, rax
00631814  48 85 C0                        test rax, rax
00631817  0F 84 95 00 00 00               je 0x1406318b2
0063181D  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00631820  A8 18                           test al, 0x18
00631822  74 0A                           je 0x14063182e
00631824  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
00631828  48 89 4D E0                     mov qword ptr [rbp - 0x20], rcx
0063182C  EB 0D                           jmp 0x14063183b
0063182E  A8 04                           test al, 4
00631830  74 09                           je 0x14063183b
00631832  E8 D1 23 EA FF                  call 0x1404d3c08
00631837  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
0063183B  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
0063183F  45 32 F6                        xor r14b, r14b
00631842  44 38 35 6F 30 8D 00            cmp byte ptr [rip + 0x8d306f], r14b
00631849  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0063184D  44 89 6D EC                     mov dword ptr [rbp - 0x14], r13d
00631851  44 88 65 E9                     mov byte ptr [rbp - 0x17], r12b
00631855  44 88 7D E8                     mov byte ptr [rbp - 0x18], r15b
00631859  75 0C                           jne 0x140631867
0063185B  F7 05 1B 31 8D 00 00 08 00 00   test dword ptr [rip + 0x8d311b], 0x800
00631865  74 13                           je 0x14063187a
00631867  48 8D 0D 12 26 8D 00            lea rcx, [rip + 0x8d2612]
0063186E  E8 AD 4D BE FF                  call 0x140216620
00631873  44 8A F0                        mov r14b, al
00631876  84 C0                           test al, al
00631878  74 38                           je 0x1406318b2
0063187A  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0063187E  48 8B 1F                        mov rbx, qword ptr [rdi]
00631881  EB 19                           jmp 0x14063189c
00631883  48 8D 43 F0                     lea rax, [rbx - 0x10]
00631887  48 85 C0                        test rax, rax
0063188A  74 0D                           je 0x140631899
0063188C  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00631890  48 8D 4D E0                     lea rcx, [rbp - 0x20]
00631894  E8 37 92 08 00                  call 0x1406baad0
00631899  48 8B 1B                        mov rbx, qword ptr [rbx]
0063189C  48 3B DF                        cmp rbx, rdi
0063189F  75 E2                           jne 0x140631883
006318A1  45 84 F6                        test r14b, r14b
006318A4  74 0C                           je 0x1406318b2
006318A6  48 8D 0D D3 25 8D 00            lea rcx, [rip + 0x8d25d3]
006318AD  E8 CE 85 D1 FF                  call 0x140349e80
006318B2  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
006318B6  45 8A CF                        mov r9b, r15b
006318B9  45 8A C4                        mov r8b, r12b
006318BC  41 8B D5                        mov edx, r13d
006318BF  E8 0C 4F D6 FF                  call 0x1403967d0
006318C4  89 45 F8                        mov dword ptr [rbp - 8], eax
006318C7  48 85 F6                        test rsi, rsi
006318CA  74 63                           je 0x14063192f
006318CC  40 32 FF                        xor dil, dil
006318CF  40 38 3D E2 2F 8D 00            cmp byte ptr [rip + 0x8d2fe2], dil
006318D6  75 0C                           jne 0x1406318e4
006318D8  F7 05 9E 30 8D 00 00 08 00 00   test dword ptr [rip + 0x8d309e], 0x800
006318E2  74 13                           je 0x1406318f7
006318E4  48 8D 0D 95 25 8D 00            lea rcx, [rip + 0x8d2595]
006318EB  E8 30 4D BE FF                  call 0x140216620
006318F0  40 8A F8                        mov dil, al
006318F3  84 C0                           test al, al
006318F5  74 38                           je 0x14063192f
006318F7  48 83 C6 30                     add rsi, 0x30
006318FB  48 8B 1E                        mov rbx, qword ptr [rsi]
006318FE  EB 19                           jmp 0x140631919
00631900  48 8D 43 F0                     lea rax, [rbx - 0x10]
00631904  48 85 C0                        test rax, rax
00631907  74 0D                           je 0x140631916
00631909  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063190D  48 8D 4D E0                     lea rcx, [rbp - 0x20]
00631911  E8 BA 91 08 00                  call 0x1406baad0
00631916  48 8B 1B                        mov rbx, qword ptr [rbx]
00631919  48 3B DE                        cmp rbx, rsi
0063191C  75 E2                           jne 0x140631900
0063191E  40 84 FF                        test dil, dil
00631921  74 0C                           je 0x14063192f
00631923  48 8D 0D 56 25 8D 00            lea rcx, [rip + 0x8d2556]
0063192A  E8 51 85 D1 FF                  call 0x140349e80
0063192F  8B 45 F8                        mov eax, dword ptr [rbp - 8]
00631932  4C 8D 5C 24 40                  lea r11, [rsp + 0x40]
00631937  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
0063193B  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
0063193F  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00631943  49 8B E3                        mov rsp, r11
00631946  41 5F                           pop r15
00631948  41 5E                           pop r14
0063194A  41 5D                           pop r13
0063194C  41 5C                           pop r12
0063194E  5D                              pop rbp
0063194F  C3                              ret
00631950  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifKeReleaseMutantWrapper(__int64 a1, int a2, unsigned __int8 a3, unsigned __int8 a4)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m3C;
    unsigned __int8 v_stack_m3F;
    unsigned __int8 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (64);
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    result = DifGetAPIThunkContextById(261, a2, a3, a4);
    if (result == 0) goto loc_006318B2;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0063182E;
    v_stack_m48 = v_stack_p0;
    goto loc_0063183B;
loc_0063182E:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m48 = result;
    }
    v_r14 = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m3C = (unsigned int)((unsigned int)(a2));
    v_stack_m3F = a3;
    v_stack_m40 = a4;
    if ((*(unsigned __int8 *)(v_rip + 9252975)) != 0) goto loc_00631867;
    if (((*(unsigned int *)(v_rip + 9253147)) & (0x800ULL)) == 0) goto loc_0063187A;
loc_00631867:
    result = ExAcquireRundownProtection(v_rip + 9250322, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006318B2;
loc_0063187A:
    goto loc_0063189C;
loc_00631883:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m48;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063189C:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00631883;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9250259;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = KeReleaseMutant(v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    v_stack_m30 = (unsigned int)(result);
    if (result == 0) goto loc_0063192F;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9252834)) != 0) goto loc_006318E4;
    if (((*(unsigned int *)(v_rip + 9253022)) & (0x800ULL)) == 0) goto loc_006318F7;
loc_006318E4:
    result = ExAcquireRundownProtection(v_rip + 9250197, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063192F;
loc_006318F7:
    v_rsi = (result) + (48);
    goto loc_00631919;
loc_00631900:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m48;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
loc_00631919:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00631900;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9250134;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
    return (unsigned int)(v_stack_m30);
}
```

## 5. (Beta) C Style

```c
int64_t DifKeReleaseMutantWrapper(int64_t Arg1, int32_t Arg2, uint8_t Arg3, uint8_t Arg4)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint32_t v_stack_m3C;
    uint8_t v_stack_m3F;
    uint8_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_p0;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (64);
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    result = DifGetAPIThunkContextById(261, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_006318B2;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0063182E;
    v_stack_m48 = v_stack_p0;
    goto loc_0063183B;
loc_0063182E:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m48 = result;
    }
    local_r14 = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m3C = (uint32_t)((uint32_t)(Arg2));
    v_stack_m3F = Arg3;
    v_stack_m40 = Arg4;
    if ((*(uint8_t *)(v_rip + 0x8D306F)) != 0) goto loc_00631867;
    if (((*(uint32_t *)(v_rip + 0x8D311B)) & (0x800ULL)) == 0) goto loc_0063187A;
loc_00631867:
    result = ExAcquireRundownProtection(v_rip + 9250322, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_006318B2;
loc_0063187A:
    goto loc_0063189C;
loc_00631883:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m48;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_0063189C:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00631883;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9250259;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    result = KeReleaseMutant(v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    v_stack_m30 = (uint32_t)(result);
    if (result == 0) goto loc_0063192F;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D2FE2)) != 0) goto loc_006318E4;
    if (((*(uint32_t *)(v_rip + 0x8D309E)) & (0x800ULL)) == 0) goto loc_006318F7;
loc_006318E4:
    result = ExAcquireRundownProtection(v_rip + 9250197, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0063192F;
loc_006318F7:
    local_rsi = (result) + (48);
    goto loc_00631919;
loc_00631900:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m48;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    }
loc_00631919:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00631900;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9250134;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    }
    return (uint32_t)(v_stack_m30);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006317D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006317D0[BB_006317D0]
  bb_0063181D[BB_0063181D]
  bb_00631824[BB_00631824]
  bb_0063182E[BB_0063182E]
  bb_00631832[BB_00631832]
  bb_0063183B[BB_0063183B]
  bb_0063185B[BB_0063185B]
  bb_00631867[BB_00631867]
  bb_0063187A[BB_0063187A]
  bb_00631883[BB_00631883]
  bb_0063188C[BB_0063188C]
  bb_00631899[BB_00631899]
  bb_0063189C[BB_0063189C]
  bb_006318A1[BB_006318A1]
  bb_006318A6[BB_006318A6]
  bb_006318B2[BB_006318B2]
  bb_006318CC[BB_006318CC]
  bb_006318D8[BB_006318D8]
  bb_006318E4[BB_006318E4]
  bb_006318F7[BB_006318F7]
  bb_00631900[BB_00631900]
  bb_00631909[BB_00631909]
  bb_00631916[BB_00631916]
  bb_00631919[BB_00631919]
  bb_0063191E[BB_0063191E]
  bb_00631923[BB_00631923]
  bb_0063192F[BB_0063192F]
  bb_00631950[BB_00631950]
  bb_006317D0 -->|branch| bb_006318B2
  bb_006317D0 -->|fallthrough| bb_0063181D
  bb_0063181D -->|branch| bb_0063182E
  bb_0063181D -->|fallthrough| bb_00631824
  bb_00631824 -->|branch| bb_0063183B
  bb_0063182E -->|branch| bb_0063183B
  bb_0063182E -->|fallthrough| bb_00631832
  bb_00631832 -->|flow| bb_0063183B
  bb_0063183B -->|branch| bb_00631867
  bb_0063183B -->|fallthrough| bb_0063185B
  bb_0063185B -->|branch| bb_0063187A
  bb_0063185B -->|fallthrough| bb_00631867
  bb_00631867 -->|branch| bb_006318B2
  bb_00631867 -->|fallthrough| bb_0063187A
  bb_0063187A -->|branch| bb_0063189C
  bb_00631883 -->|branch| bb_00631899
  bb_00631883 -->|fallthrough| bb_0063188C
  bb_0063188C -->|flow| bb_00631899
  bb_00631899 -->|flow| bb_0063189C
  bb_0063189C -->|branch| bb_00631883
  bb_0063189C -->|fallthrough| bb_006318A1
  bb_006318A1 -->|branch| bb_006318B2
  bb_006318A1 -->|fallthrough| bb_006318A6
  bb_006318A6 -->|flow| bb_006318B2
  bb_006318B2 -->|branch| bb_0063192F
  bb_006318B2 -->|fallthrough| bb_006318CC
  bb_006318CC -->|branch| bb_006318E4
  bb_006318CC -->|fallthrough| bb_006318D8
  bb_006318D8 -->|branch| bb_006318F7
  bb_006318D8 -->|fallthrough| bb_006318E4
  bb_006318E4 -->|branch| bb_0063192F
  bb_006318E4 -->|fallthrough| bb_006318F7
  bb_006318F7 -->|branch| bb_00631919
  bb_00631900 -->|branch| bb_00631916
  bb_00631900 -->|fallthrough| bb_00631909
  bb_00631909 -->|flow| bb_00631916
  bb_00631916 -->|flow| bb_00631919
  bb_00631919 -->|branch| bb_00631900
  bb_00631919 -->|fallthrough| bb_0063191E
  bb_0063191E -->|branch| bb_0063192F
  bb_0063191E -->|fallthrough| bb_00631923
  bb_00631923 -->|flow| bb_0063192F
```
