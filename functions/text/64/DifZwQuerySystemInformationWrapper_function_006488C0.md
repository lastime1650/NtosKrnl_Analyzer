# DifZwQuerySystemInformationWrapper

- RVA: `0x006488C0`–`0x00648A43` (길이 `387` bytes)
- VA: `0x00000001406488C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BCEF0`
- 디코드: `113`개 명령, `387/387` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x006488FF` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00648927` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00648961` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00648987` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006489A0` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x006489B1` → [ZwQuerySystemInformation](../6A/ZwQuerySystemInformation_function_006AD790.md) (function, `0x006AD790`)
- `0x006489DD` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00648A03` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00648A1C` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00648936` → RVA `0x00F048B8` (`.data`; read)
- `0x0064894E` → RVA `0x00F04980` (`.data`; read)
- `0x0064895A` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006488C0  48 8B C4                        mov rax, rsp
006488C3  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
006488C7  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
006488CB  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
006488CF  89 48 08                        mov dword ptr [rax + 8], ecx
006488D2  55                              push rbp
006488D3  41 54                           push r12
006488D5  41 55                           push r13
006488D7  41 56                           push r14
006488D9  41 57                           push r15
006488DB  48 8B EC                        mov rbp, rsp
006488DE  48 83 EC 50                     sub rsp, 0x50
006488E2  33 C0                           xor eax, eax
006488E4  0F 57 C0                        xorps xmm0, xmm0
006488E7  4D 8B F9                        mov r15, r9
006488EA  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
006488EE  45 8B E0                        mov r12d, r8d
006488F1  4C 8B EA                        mov r13, rdx
006488F4  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
006488F8  8D 48 23                        lea ecx, [rax + 0x23]
006488FB  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
006488FF  E8 30 D1 E4 FF                  call 0x140495a34
00648904  4C 8B F0                        mov r14, rax
00648907  48 85 C0                        test rax, rax
0064890A  0F 84 95 00 00 00               je 0x1406489a5
00648910  8B 48 0C                        mov ecx, dword ptr [rax + 0xc]
00648913  F6 C1 18                        test cl, 0x18
00648916  74 0A                           je 0x140648922
00648918  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0064891C  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
00648920  EB 0E                           jmp 0x140648930
00648922  F6 C1 04                        test cl, 4
00648925  74 09                           je 0x140648930
00648927  E8 DC B2 E8 FF                  call 0x1404d3c08
0064892C  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
00648930  8B 45 30                        mov eax, dword ptr [rbp + 0x30]
00648933  40 32 F6                        xor sil, sil
00648936  40 38 35 7B BF 8B 00            cmp byte ptr [rip + 0x8bbf7b], sil
0064893D  89 45 F0                        mov dword ptr [rbp - 0x10], eax
00648940  4C 89 6D E8                     mov qword ptr [rbp - 0x18], r13
00648944  44 89 65 E0                     mov dword ptr [rbp - 0x20], r12d
00648948  4C 89 7D D8                     mov qword ptr [rbp - 0x28], r15
0064894C  75 0C                           jne 0x14064895a
0064894E  F7 05 28 C0 8B 00 00 08 00 00   test dword ptr [rip + 0x8bc028], 0x800
00648958  74 13                           je 0x14064896d
0064895A  48 8D 0D 1F B5 8B 00            lea rcx, [rip + 0x8bb51f]
00648961  E8 BA DC BC FF                  call 0x140216620
00648966  40 8A F0                        mov sil, al
00648969  84 C0                           test al, al
0064896B  74 38                           je 0x1406489a5
0064896D  49 8D 7E 20                     lea rdi, [r14 + 0x20]
00648971  48 8B 1F                        mov rbx, qword ptr [rdi]
00648974  EB 19                           jmp 0x14064898f
00648976  48 8D 43 F0                     lea rax, [rbx - 0x10]
0064897A  48 85 C0                        test rax, rax
0064897D  74 0D                           je 0x14064898c
0064897F  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00648983  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00648987  E8 44 21 07 00                  call 0x1406baad0
0064898C  48 8B 1B                        mov rbx, qword ptr [rbx]
0064898F  48 3B DF                        cmp rbx, rdi
00648992  75 E2                           jne 0x140648976
00648994  40 84 F6                        test sil, sil
00648997  74 0C                           je 0x1406489a5
00648999  48 8D 0D E0 B4 8B 00            lea rcx, [rip + 0x8bb4e0]
006489A0  E8 DB 14 D0 FF                  call 0x140349e80
006489A5  8B 4D 30                        mov ecx, dword ptr [rbp + 0x30]
006489A8  4D 8B CF                        mov r9, r15
006489AB  45 8B C4                        mov r8d, r12d
006489AE  49 8B D5                        mov rdx, r13
006489B1  E8 DA 4D 06 00                  call 0x1406ad790
006489B6  89 45 F4                        mov dword ptr [rbp - 0xc], eax
006489B9  4D 85 F6                        test r14, r14
006489BC  74 63                           je 0x140648a21
006489BE  40 32 FF                        xor dil, dil
006489C1  40 38 3D F0 BE 8B 00            cmp byte ptr [rip + 0x8bbef0], dil
006489C8  75 0C                           jne 0x1406489d6
006489CA  F7 05 AC BF 8B 00 00 08 00 00   test dword ptr [rip + 0x8bbfac], 0x800
006489D4  74 13                           je 0x1406489e9
006489D6  48 8D 0D A3 B4 8B 00            lea rcx, [rip + 0x8bb4a3]
006489DD  E8 3E DC BC FF                  call 0x140216620
006489E2  40 8A F8                        mov dil, al
006489E5  84 C0                           test al, al
006489E7  74 38                           je 0x140648a21
006489E9  49 8D 76 30                     lea rsi, [r14 + 0x30]
006489ED  48 8B 1E                        mov rbx, qword ptr [rsi]
006489F0  EB 19                           jmp 0x140648a0b
006489F2  48 8D 43 F0                     lea rax, [rbx - 0x10]
006489F6  48 85 C0                        test rax, rax
006489F9  74 0D                           je 0x140648a08
006489FB  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006489FF  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00648A03  E8 C8 20 07 00                  call 0x1406baad0
00648A08  48 8B 1B                        mov rbx, qword ptr [rbx]
00648A0B  48 3B DE                        cmp rbx, rsi
00648A0E  75 E2                           jne 0x1406489f2
00648A10  40 84 FF                        test dil, dil
00648A13  74 0C                           je 0x140648a21
00648A15  48 8D 0D 64 B4 8B 00            lea rcx, [rip + 0x8bb464]
00648A1C  E8 5F 14 D0 FF                  call 0x140349e80
00648A21  8B 45 F4                        mov eax, dword ptr [rbp - 0xc]
00648A24  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
00648A29  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00648A2D  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00648A31  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00648A35  49 8B E3                        mov rsp, r11
00648A38  41 5F                           pop r15
00648A3A  41 5E                           pop r14
00648A3C  41 5D                           pop r13
00648A3E  41 5C                           pop r12
00648A40  5D                              pop rbp
00648A41  C3                              ret
00648A42  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwQuerySystemInformationWrapper(int a1, __int64 a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m34;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p0;
    unsigned int v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    *(unsigned int *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (80);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(result + 35, a2, a3, a4);
    if (result == 0) goto loc_006489A5;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00648922;
    v_stack_m58 = v_stack_p0;
    goto loc_00648930;
loc_00648922:
    if ((((unsigned __int8)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_rsi = 0;
    v_stack_m38 = (unsigned int)((unsigned int)(v_stack_p8));
    v_stack_m40 = a2;
    v_stack_m48 = (unsigned int)((unsigned int)(a3));
    v_stack_m50 = a4;
    if ((*(unsigned __int8 *)(v_rip + 9158523)) != 0) goto loc_0064895A;
    if (((*(unsigned int *)(v_rip + 9158696)) & (0x800ULL)) == 0) goto loc_0064896D;
loc_0064895A:
    result = ExAcquireRundownProtection(v_rip + 9155871, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006489A5;
loc_0064896D:
    goto loc_0064898F;
loc_00648976:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0064898F:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00648976;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9155808;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ZwQuerySystemInformation((unsigned int)(v_stack_p8), a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    v_stack_m34 = (unsigned int)(result);
    if (result == 0) goto loc_00648A21;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9158384)) != 0) goto loc_006489D6;
    if (((*(unsigned int *)(v_rip + 9158572)) & (0x800ULL)) == 0) goto loc_006489E9;
loc_006489D6:
    result = ExAcquireRundownProtection(v_rip + 9155747, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00648A21;
loc_006489E9:
    goto loc_00648A0B;
loc_006489F2:
    result = *(unsigned __int64 *)(result + 48) - 16;
    if (*(unsigned __int64 *)(result + 48) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 48) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    }
loc_00648A0B:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 48))) != (result + 48)) goto loc_006489F2;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9155684;
        result = ExReleaseRundownProtection(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    }
    return (unsigned int)(v_stack_m34);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwQuerySystemInformationWrapper(int32_t Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint32_t v_stack_m34;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_p0;
    uint32_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    *(uint32_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (80);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(result + 35, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_006489A5;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00648922;
    v_stack_m58 = v_stack_p0;
    goto loc_00648930;
loc_00648922:
    if ((((uint8_t)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m58 = result;
    }
    local_rsi = 0;
    v_stack_m38 = (uint32_t)((uint32_t)(v_stack_p8));
    v_stack_m40 = Arg2;
    v_stack_m48 = (uint32_t)((uint32_t)(Arg3));
    v_stack_m50 = Arg4;
    if ((*(uint8_t *)(v_rip + 0x8BBF7B)) != 0) goto loc_0064895A;
    if (((*(uint32_t *)(v_rip + 0x8BC028)) & (0x800ULL)) == 0) goto loc_0064896D;
loc_0064895A:
    result = ExAcquireRundownProtection(v_rip + 9155871, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_006489A5;
loc_0064896D:
    goto loc_0064898F;
loc_00648976:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_0064898F:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00648976;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9155808;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    result = ZwQuerySystemInformation((uint32_t)(v_stack_p8), Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    v_stack_m34 = (uint32_t)(result);
    if (result == 0) goto loc_00648A21;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8BBEF0)) != 0) goto loc_006489D6;
    if (((*(uint32_t *)(v_rip + 0x8BBFAC)) & (0x800ULL)) == 0) goto loc_006489E9;
loc_006489D6:
    result = ExAcquireRundownProtection(v_rip + 9155747, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    if ((uint8_t)(result) == 0) goto loc_00648A21;
loc_006489E9:
    goto loc_00648A0B;
loc_006489F2:
    result = *(uint64_t *)(result + 0x30) - 16;
    if (*(uint64_t *)(result + 0x30) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x30) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    }
loc_00648A0B:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x30))) != (result + 48)) goto loc_006489F2;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9155684;
        result = ExReleaseRundownProtection(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    }
    return (uint32_t)(v_stack_m34);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006488C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006488C0[BB_006488C0]
  bb_00648910[BB_00648910]
  bb_00648918[BB_00648918]
  bb_00648922[BB_00648922]
  bb_00648927[BB_00648927]
  bb_00648930[BB_00648930]
  bb_0064894E[BB_0064894E]
  bb_0064895A[BB_0064895A]
  bb_0064896D[BB_0064896D]
  bb_00648976[BB_00648976]
  bb_0064897F[BB_0064897F]
  bb_0064898C[BB_0064898C]
  bb_0064898F[BB_0064898F]
  bb_00648994[BB_00648994]
  bb_00648999[BB_00648999]
  bb_006489A5[BB_006489A5]
  bb_006489BE[BB_006489BE]
  bb_006489CA[BB_006489CA]
  bb_006489D6[BB_006489D6]
  bb_006489E9[BB_006489E9]
  bb_006489F2[BB_006489F2]
  bb_006489FB[BB_006489FB]
  bb_00648A08[BB_00648A08]
  bb_00648A0B[BB_00648A0B]
  bb_00648A10[BB_00648A10]
  bb_00648A15[BB_00648A15]
  bb_00648A21[BB_00648A21]
  bb_00648A42[BB_00648A42]
  bb_006488C0 -->|branch| bb_006489A5
  bb_006488C0 -->|fallthrough| bb_00648910
  bb_00648910 -->|branch| bb_00648922
  bb_00648910 -->|fallthrough| bb_00648918
  bb_00648918 -->|branch| bb_00648930
  bb_00648922 -->|branch| bb_00648930
  bb_00648922 -->|fallthrough| bb_00648927
  bb_00648927 -->|flow| bb_00648930
  bb_00648930 -->|branch| bb_0064895A
  bb_00648930 -->|fallthrough| bb_0064894E
  bb_0064894E -->|branch| bb_0064896D
  bb_0064894E -->|fallthrough| bb_0064895A
  bb_0064895A -->|branch| bb_006489A5
  bb_0064895A -->|fallthrough| bb_0064896D
  bb_0064896D -->|branch| bb_0064898F
  bb_00648976 -->|branch| bb_0064898C
  bb_00648976 -->|fallthrough| bb_0064897F
  bb_0064897F -->|flow| bb_0064898C
  bb_0064898C -->|flow| bb_0064898F
  bb_0064898F -->|branch| bb_00648976
  bb_0064898F -->|fallthrough| bb_00648994
  bb_00648994 -->|branch| bb_006489A5
  bb_00648994 -->|fallthrough| bb_00648999
  bb_00648999 -->|flow| bb_006489A5
  bb_006489A5 -->|branch| bb_00648A21
  bb_006489A5 -->|fallthrough| bb_006489BE
  bb_006489BE -->|branch| bb_006489D6
  bb_006489BE -->|fallthrough| bb_006489CA
  bb_006489CA -->|branch| bb_006489E9
  bb_006489CA -->|fallthrough| bb_006489D6
  bb_006489D6 -->|branch| bb_00648A21
  bb_006489D6 -->|fallthrough| bb_006489E9
  bb_006489E9 -->|branch| bb_00648A0B
  bb_006489F2 -->|branch| bb_00648A08
  bb_006489F2 -->|fallthrough| bb_006489FB
  bb_006489FB -->|flow| bb_00648A08
  bb_00648A08 -->|flow| bb_00648A0B
  bb_00648A0B -->|branch| bb_006489F2
  bb_00648A0B -->|fallthrough| bb_00648A10
  bb_00648A10 -->|branch| bb_00648A21
  bb_00648A10 -->|fallthrough| bb_00648A15
  bb_00648A15 -->|flow| bb_00648A21
```
