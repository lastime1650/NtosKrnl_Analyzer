# DifZwQueryInstallUILanguageWrapper

- RVA: `0x00647D60`–`0x00647EBD` (길이 `349` bytes)
- VA: `0x0000000140647D60`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060130`
- 디코드: `94`개 명령, `349/349` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00647D8D` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00647DB5` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00647DE3` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00647E0A` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00647E23` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00647E2B` → [ZwQueryInstallUILanguage](../6A/ZwQueryInstallUILanguage_function_006AFC70.md) (function, `0x006AFC70`)
- `0x00647E58` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00647E7F` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00647E98` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00647DC7` → RVA `0x00F048B8` (`.data`; read)
- `0x00647DD0` → RVA `0x00F04980` (`.data`; read)
- `0x00647DDC` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00647D60  4C 8B DC                        mov r11, rsp
00647D63  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00647D67  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
00647D6B  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
00647D6F  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
00647D73  41 56                           push r14
00647D75  48 83 EC 40                     sub rsp, 0x40
00647D79  33 C0                           xor eax, eax
00647D7B  0F 57 C0                        xorps xmm0, xmm0
00647D7E  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
00647D83  48 8B E9                        mov rbp, rcx
00647D86  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
00647D8A  8D 48 2A                        lea ecx, [rax + 0x2a]
00647D8D  E8 A2 DC E4 FF                  call 0x140495a34
00647D92  48 8B F0                        mov rsi, rax
00647D95  48 85 C0                        test rax, rax
00647D98  0F 84 8A 00 00 00               je 0x140647e28
00647D9E  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00647DA1  A8 18                           test al, 0x18
00647DA3  74 0C                           je 0x140647db1
00647DA5  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00647DAA  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00647DAF  EB 0E                           jmp 0x140647dbf
00647DB1  A8 04                           test al, 4
00647DB3  74 0A                           je 0x140647dbf
00647DB5  E8 4E BE E8 FF                  call 0x1404d3c08
00647DBA  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00647DBF  40 32 FF                        xor dil, dil
00647DC2  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
00647DC7  40 38 3D EA CA 8B 00            cmp byte ptr [rip + 0x8bcaea], dil
00647DCE  75 0C                           jne 0x140647ddc
00647DD0  F7 05 A6 CB 8B 00 00 08 00 00   test dword ptr [rip + 0x8bcba6], 0x800
00647DDA  74 13                           je 0x140647def
00647DDC  48 8D 0D 9D C0 8B 00            lea rcx, [rip + 0x8bc09d]
00647DE3  E8 38 E8 BC FF                  call 0x140216620
00647DE8  40 8A F8                        mov dil, al
00647DEB  84 C0                           test al, al
00647DED  74 39                           je 0x140647e28
00647DEF  4C 8D 76 20                     lea r14, [rsi + 0x20]
00647DF3  49 8B 1E                        mov rbx, qword ptr [r14]
00647DF6  EB 1A                           jmp 0x140647e12
00647DF8  48 8D 43 F0                     lea rax, [rbx - 0x10]
00647DFC  48 85 C0                        test rax, rax
00647DFF  74 0E                           je 0x140647e0f
00647E01  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00647E05  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00647E0A  E8 C1 2C 07 00                  call 0x1406baad0
00647E0F  48 8B 1B                        mov rbx, qword ptr [rbx]
00647E12  49 3B DE                        cmp rbx, r14
00647E15  75 E1                           jne 0x140647df8
00647E17  40 84 FF                        test dil, dil
00647E1A  74 0C                           je 0x140647e28
00647E1C  48 8D 0D 5D C0 8B 00            lea rcx, [rip + 0x8bc05d]
00647E23  E8 58 20 D0 FF                  call 0x140349e80
00647E28  48 8B CD                        mov rcx, rbp
00647E2B  E8 40 7E 06 00                  call 0x1406afc70
00647E30  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00647E34  48 85 F6                        test rsi, rsi
00647E37  74 64                           je 0x140647e9d
00647E39  40 32 FF                        xor dil, dil
00647E3C  40 38 3D 75 CA 8B 00            cmp byte ptr [rip + 0x8bca75], dil
00647E43  75 0C                           jne 0x140647e51
00647E45  F7 05 31 CB 8B 00 00 08 00 00   test dword ptr [rip + 0x8bcb31], 0x800
00647E4F  74 13                           je 0x140647e64
00647E51  48 8D 0D 28 C0 8B 00            lea rcx, [rip + 0x8bc028]
00647E58  E8 C3 E7 BC FF                  call 0x140216620
00647E5D  40 8A F8                        mov dil, al
00647E60  84 C0                           test al, al
00647E62  74 39                           je 0x140647e9d
00647E64  48 83 C6 30                     add rsi, 0x30
00647E68  48 8B 1E                        mov rbx, qword ptr [rsi]
00647E6B  EB 1A                           jmp 0x140647e87
00647E6D  48 8D 43 F0                     lea rax, [rbx - 0x10]
00647E71  48 85 C0                        test rax, rax
00647E74  74 0E                           je 0x140647e84
00647E76  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00647E7A  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00647E7F  E8 4C 2C 07 00                  call 0x1406baad0
00647E84  48 8B 1B                        mov rbx, qword ptr [rbx]
00647E87  48 3B DE                        cmp rbx, rsi
00647E8A  75 E1                           jne 0x140647e6d
00647E8C  40 84 FF                        test dil, dil
00647E8F  74 0C                           je 0x140647e9d
00647E91  48 8D 0D E8 BF 8B 00            lea rcx, [rip + 0x8bbfe8]
00647E98  E8 E3 1F D0 FF                  call 0x140349e80
00647E9D  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
00647EA1  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00647EA6  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
00647EAB  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
00647EB0  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
00647EB5  48 83 C4 40                     add rsp, 0x40
00647EB9  41 5E                           pop r14
00647EBB  C3                              ret
00647EBC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwQueryInstallUILanguageWrapper(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (64);
    result = 0;
    v_stack_m28 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 24) = 0;
    result = DifGetAPIThunkContextById(result + 42, a2, a3, a4);
    if (result == 0) goto loc_00647E28;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00647DB1;
    v_stack_m28 = v_stack_p0;
    goto loc_00647DBF;
loc_00647DB1:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    v_rdi = 0;
    v_stack_m20 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9161450)) != 0) goto loc_00647DDC;
    if (((*(unsigned int *)(v_rip + 9161638)) & (0x800ULL)) == 0) goto loc_00647DEF;
loc_00647DDC:
    result = ExAcquireRundownProtection(v_rip + 9158813, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00647E28;
loc_00647DEF:
    goto loc_00647E12;
loc_00647DF8:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00647E12:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00647DF8;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9158749;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ZwQueryInstallUILanguage(a1, a2, a3, a4);
    v_stack_m18 = (unsigned int)(result);
    if (result == 0) goto loc_00647E9D;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9161333)) != 0) goto loc_00647E51;
    if (((*(unsigned int *)(v_rip + 9161521)) & (0x800ULL)) == 0) goto loc_00647E64;
loc_00647E51:
    result = ExAcquireRundownProtection(v_rip + 9158696, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00647E9D;
loc_00647E64:
    v_rsi = (result) + (48);
    goto loc_00647E87;
loc_00647E6D:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00647E87:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00647E6D;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9158632;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return (unsigned int)(v_stack_m18);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwQueryInstallUILanguageWrapper(int64_t Arg1)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (64);
    result = 0;
    v_stack_m28 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x18) = 0;
    result = DifGetAPIThunkContextById(result + 42, a2, a3, a4);
    if (result == 0) goto loc_00647E28;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00647DB1;
    v_stack_m28 = v_stack_p0;
    goto loc_00647DBF;
loc_00647DB1:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    local_rdi = 0;
    v_stack_m20 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8BCAEA)) != 0) goto loc_00647DDC;
    if (((*(uint32_t *)(v_rip + 0x8BCBA6)) & (0x800ULL)) == 0) goto loc_00647DEF;
loc_00647DDC:
    result = ExAcquireRundownProtection(v_rip + 9158813, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00647E28;
loc_00647DEF:
    goto loc_00647E12;
loc_00647DF8:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_00647E12:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00647DF8;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9158749;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = ZwQueryInstallUILanguage(Arg1, a2, a3, a4);
    v_stack_m18 = (uint32_t)(result);
    if (result == 0) goto loc_00647E9D;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8BCA75)) != 0) goto loc_00647E51;
    if (((*(uint32_t *)(v_rip + 0x8BCB31)) & (0x800ULL)) == 0) goto loc_00647E64;
loc_00647E51:
    result = ExAcquireRundownProtection(v_rip + 9158696, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00647E9D;
loc_00647E64:
    local_rsi = (result) + (48);
    goto loc_00647E87;
loc_00647E6D:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_00647E87:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00647E6D;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9158632;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return (uint32_t)(v_stack_m18);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00647D60&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00647D60[BB_00647D60]
  bb_00647D9E[BB_00647D9E]
  bb_00647DA5[BB_00647DA5]
  bb_00647DB1[BB_00647DB1]
  bb_00647DB5[BB_00647DB5]
  bb_00647DBF[BB_00647DBF]
  bb_00647DD0[BB_00647DD0]
  bb_00647DDC[BB_00647DDC]
  bb_00647DEF[BB_00647DEF]
  bb_00647DF8[BB_00647DF8]
  bb_00647E01[BB_00647E01]
  bb_00647E0F[BB_00647E0F]
  bb_00647E12[BB_00647E12]
  bb_00647E17[BB_00647E17]
  bb_00647E1C[BB_00647E1C]
  bb_00647E28[BB_00647E28]
  bb_00647E39[BB_00647E39]
  bb_00647E45[BB_00647E45]
  bb_00647E51[BB_00647E51]
  bb_00647E64[BB_00647E64]
  bb_00647E6D[BB_00647E6D]
  bb_00647E76[BB_00647E76]
  bb_00647E84[BB_00647E84]
  bb_00647E87[BB_00647E87]
  bb_00647E8C[BB_00647E8C]
  bb_00647E91[BB_00647E91]
  bb_00647E9D[BB_00647E9D]
  bb_00647EBC[BB_00647EBC]
  bb_00647D60 -->|branch| bb_00647E28
  bb_00647D60 -->|fallthrough| bb_00647D9E
  bb_00647D9E -->|branch| bb_00647DB1
  bb_00647D9E -->|fallthrough| bb_00647DA5
  bb_00647DA5 -->|branch| bb_00647DBF
  bb_00647DB1 -->|branch| bb_00647DBF
  bb_00647DB1 -->|fallthrough| bb_00647DB5
  bb_00647DB5 -->|flow| bb_00647DBF
  bb_00647DBF -->|branch| bb_00647DDC
  bb_00647DBF -->|fallthrough| bb_00647DD0
  bb_00647DD0 -->|branch| bb_00647DEF
  bb_00647DD0 -->|fallthrough| bb_00647DDC
  bb_00647DDC -->|branch| bb_00647E28
  bb_00647DDC -->|fallthrough| bb_00647DEF
  bb_00647DEF -->|branch| bb_00647E12
  bb_00647DF8 -->|branch| bb_00647E0F
  bb_00647DF8 -->|fallthrough| bb_00647E01
  bb_00647E01 -->|flow| bb_00647E0F
  bb_00647E0F -->|flow| bb_00647E12
  bb_00647E12 -->|branch| bb_00647DF8
  bb_00647E12 -->|fallthrough| bb_00647E17
  bb_00647E17 -->|branch| bb_00647E28
  bb_00647E17 -->|fallthrough| bb_00647E1C
  bb_00647E1C -->|flow| bb_00647E28
  bb_00647E28 -->|branch| bb_00647E9D
  bb_00647E28 -->|fallthrough| bb_00647E39
  bb_00647E39 -->|branch| bb_00647E51
  bb_00647E39 -->|fallthrough| bb_00647E45
  bb_00647E45 -->|branch| bb_00647E64
  bb_00647E45 -->|fallthrough| bb_00647E51
  bb_00647E51 -->|branch| bb_00647E9D
  bb_00647E51 -->|fallthrough| bb_00647E64
  bb_00647E64 -->|branch| bb_00647E87
  bb_00647E6D -->|branch| bb_00647E84
  bb_00647E6D -->|fallthrough| bb_00647E76
  bb_00647E76 -->|flow| bb_00647E84
  bb_00647E84 -->|flow| bb_00647E87
  bb_00647E87 -->|branch| bb_00647E6D
  bb_00647E87 -->|fallthrough| bb_00647E8C
  bb_00647E8C -->|branch| bb_00647E9D
  bb_00647E8C -->|fallthrough| bb_00647E91
  bb_00647E91 -->|flow| bb_00647E9D
```
